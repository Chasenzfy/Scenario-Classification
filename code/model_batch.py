from torch import nn
import numpy as np
from torch_geometric.typing import Adj, OptTensor
from torch_geometric.nn.inits import uniform

import torch
from torch import Tensor
from torch.nn import Parameter as Param
from torch_sparse import SparseTensor, matmul
from torch_geometric.nn.conv import MessagePassing


class GGNNConv(MessagePassing):
    r"""The gated graph convolution operator from the `"Gated Graph Sequence
    Neural Networks" <https://arxiv.org/abs/1511.05493>`_ paper

    .. math::
        \mathbf{h}_i^{(0)} &= \mathbf{x}_i \, \Vert \, \mathbf{0}

        \mathbf{m}_i^{(l+1)} &= \sum_{j \in \mathcal{N}(i)} e_{j,i} \cdot
        \mathbf{\Theta} \cdot \mathbf{h}_j^{(l)}

        \mathbf{h}_i^{(l+1)} &= \textrm{GRU} (\mathbf{m}_i^{(l+1)},
        \mathbf{h}_i^{(l)})

    up to representation :math:`\mathbf{h}_i^{(L)}`.
    The number of input channels of :math:`\mathbf{x}_i` needs to be less or
    equal than :obj:`out_channels`.
    :math:`e_{j,i}` denotes the edge weight from source node :obj:`j` to target
    node :obj:`i` (default: :obj:`1`)

    Args:
        out_channels (int): Size of each input sample.
        num_layers (int): The sequence length :math:`L`.
        aggr (string, optional): The aggregation scheme to use
            (:obj:`"add"`, :obj:`"mean"`, :obj:`"max"`).
            (default: :obj:`"add"`)
        bias (bool, optional): If set to :obj:`False`, the layer will not learn
            an additive bias. (default: :obj:`True`)
        **kwargs (optional): Additional arguments of
            :class:`torch_geometric.nn.conv.MessagePassing`.
    """

    def __init__(self, out_channels: int, num_layers: int, aggr: str = 'add',
                 bias: bool = True, **kwargs):
        super(GGNNConv, self).__init__(aggr=aggr, **kwargs)

        self.out_channels = out_channels
        self.num_layers = num_layers

        self.weight = Param(Tensor(num_layers, out_channels, out_channels))
        # 这里权重是用了一个可以训练的向量进行计算，dgl中是一个linear
        self.rnn = torch.nn.GRUCell(out_channels, out_channels, bias=bias)

        self.reset_parameters()

    def reset_parameters(self):
        uniform(self.out_channels, self.weight)
        self.rnn.reset_parameters()

    def forward(self, x: Tensor, edge_index: Adj,
                edge_weight: OptTensor = None) -> Tensor:
        """"""
        if x.size(-1) > self.out_channels:
            raise ValueError('The number of input channels is not allowed to '
                             'be larger than the number of output channels')

        if x.size(-1) < self.out_channels:
            zero = x.new_zeros(x.size(0), self.out_channels - x.size(-1))
            x = torch.cat([x, zero], dim=1)

        for i in range(self.num_layers):
            m = torch.matmul(x, self.weight[i])
            # propagate_type: (x: Tensor, edge_weight: OptTensor)
            m = self.propagate(edge_index, x=m, edge_weight=edge_weight,
                               size=None)
            x = self.rnn(m, x)

        return x

    def message(self, x_j: Tensor, edge_weight: OptTensor):
        return x_j if edge_weight is None else edge_weight.view(-1, 1) * x_j

    def message_and_aggregate(self, adj_t: SparseTensor, x: Tensor) -> Tensor:
        return matmul(adj_t, x, reduce=self.aggr)

    def __repr__(self):
        return '{}({}, num_layers={})'.format(self.__class__.__name__,
                                              self.out_channels,
                                              self.num_layers)


class PretrainGGNN(nn.Module):
    # 预训练模型，不带线性层。
    def __init__(self,
                 out_feats,  # 输出的维度
                 n_steps,  # 相当于T，也就是循环的次数，模型层数
                 aggregate_type):  # 聚合邻居信息的方式，"mean"， "add"，"max"
        super(PretrainGGNN, self).__init__()

        self.out_feats = out_feats
        self.ggnn = GGNNConv(out_channels=out_feats, num_layers=n_steps, aggr=aggregate_type)

    def forward(self, x, edge_index):
        out = self.ggnn(x, edge_index)  # 得到ggnn层的输出，是gru的隐藏层的输出，大小是 节点数目*out_feats
        return out


class PredictionGGNN(nn.Module):
    def __init__(self,
                 in_feats,
                 out_feats,  # 输出的维度
                 n_steps,  # 相当于T，也就是循环的次数
                 aggregate_type,  # 聚合邻居信息的方式，"mean"， "add"，"max"
                 num_cls):  # 分类的数目
        super(PredictionGGNN, self).__init__()

        self.out_feats = out_feats

        self.output_layer = nn.Linear(in_feats, 200)
        self.ggnn = PretrainGGNN(out_feats=200, n_steps=n_steps, aggregate_type=aggregate_type)

        self.sig = nn.Sigmoid()
        self.drop = nn.Dropout(p=0.2)
        self.relu = nn.ReLU()
        self.output_layer2 = nn.Linear(200, num_cls)

    def from_pretrained(self, model_file):
        self.ggnn.load_state_dict(torch.load(model_file, map_location=lambda storage, loc: storage))
        # 在GPU上训练的模型加载到CPU上

    def forward(self, x, edge_index):
        out = self.output_layer(x)
        out = self.ggnn(out, edge_index)  # 得到ggnn层的输出，是gru的隐藏层的输出，大小是 节点数目*out_feats

        out = self.sig(out)
        out = self.drop(out)

        logits = self.output_layer2(out)

        return logits

class PredictionGGNN_CLASS(nn.Module):
    def __init__(self,
                 in_feats,
                 out_feats,  # 输出的维度
                 n_steps,  # 相当于T，也就是循环的次数
                 aggregate_type,  # 聚合邻居信息的方式，"mean"， "add"，"max"
                 num_cls):  # 分类的数目
        super(PredictionGGNN_CLASS, self).__init__()

        self.out_feats = out_feats

        self.output_layer = nn.Linear(16, 16)
        self.ggnn = PretrainGGNN(out_feats=16, n_steps=n_steps, aggregate_type=aggregate_type)

        self.sig = nn.Sigmoid()
        self.drop = nn.Dropout(p=0.2)
        self.relu = nn.ReLU()
        self.output_layer2 = nn.Linear(16, num_cls)


    def from_pretrained(self, model_file):
        self.ggnn.load_state_dict(torch.load(model_file, map_location=lambda storage, loc: storage))
        # 在GPU上训练的模型加载到CPU上

    def forward(self, x, edge_index):
        out = self.output_layer(x)
        out = self.ggnn(out, edge_index)  # 得到ggnn层的输出，是gru的隐藏层的输出，大小是 节点数目*out_feats

        out = self.sig(out)
        out = self.drop(out)

        logits = self.output_layer2(out)


        return logits


if __name__ == "__main__":
    torch.manual_seed(0)
    np.random.seed(0)

    feat = torch.ones(6, 10)
    edge_index = torch.tensor([[0, 1, 2, 3, 2, 5], [1, 2, 3, 4, 0, 3]])

    model = PredictionGGNN(out_feats=1000, n_steps=5, aggregate_type="mean", num_cls=16)
    model.from_pretrained("pretrain.pth")

    print(model.forward(feat, edge_index))
