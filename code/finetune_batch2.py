# -*- coding: utf-8
import sys

import numpy as np
import argparse

import torch
import random
import torch.nn.functional as F
from sklearn import neighbors
from sklearn.metrics import classification_report
from model_batch import PredictionGGNN
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.neural_network import MLPClassifier
from torch_geometric.data import Data
import argparse
import logging
import os
import time

from torch_geometric.nn import GCN
from torch_geometric.nn import GraphSAGE
from torch_geometric.nn import GAT
from torch_geometric.nn import GIN



logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def train(graph, model, optimizer):
    model.train()

    optimizer.zero_grad()  # 清空上一步的残余更新参数值（必有）

    # print(graph.y)
    # print(graph.x.shape)
    train_logits = model.forward(graph.x, graph.edge_index)
    train_loss = F.cross_entropy(train_logits, graph.y)

    train_acc = torch.sum(train_logits.argmax(dim=1) == graph.y)
    train_acc = train_acc.item() / graph.x.shape[0]

    train_loss.backward()  # 误差反向传播, 计算参数更新值
    optimizer.step()  # 将参数更新值施加到 net 的 parameters 上

    return train_loss, train_acc


def test(graph, model):
    model.eval()

    with torch.no_grad():
        test_logits = model.forward(graph.x, graph.edge_index)
        test_loss = F.cross_entropy(test_logits, graph.y)

        test_acc = torch.sum(test_logits.argmax(dim=1) == graph.y)
        test_acc = test_acc.item() / graph.x.shape[0]
        print(test_acc)

        # 保存预测的结果
        a = torch.softmax(test_logits, dim=1)
        b = test_logits.argmax(dim=1)


        y_predict = test_logits.argmax(dim=1).cpu().numpy()  # GPU tensor 转CPU tensor
        y_true = graph["y"].cpu().numpy()

        print(classification_report(y_true, y_predict))

    return test_loss, test_acc


def train_test(args, epochs, train_graph, val_graph, test_graph, model, optimizer,filename):

    print("start training...")

    # file_name = str(time.time()) + "/"
    # os.mkdir(file_name)
    file_name = filename
    max_acc = 0
    max_epoch = 0

    for epoch in range(1, epochs + 1):
        train_loss, train_acc = train(train_graph, model, optimizer)
        val_loss, val_acc = test(val_graph, model)
        test_loss, test_acc = test(test_graph, model)



        print("Epoch {:05d} | ".format(epoch) +
              "Train Accuracy: {:.4f} | Train Loss: {:.4f} | ".format(
                  train_acc, train_loss.item()) +
              "Val Accuracy: {:.4f} | Val loss: {:.4f} | ".format(
                  val_acc, val_loss.item()) +
              "Test Accuracy: {:.4f} | Test loss: {:.4f}".format(
                  test_acc, test_loss.item()))

        if epoch % 5 == 0:
            if max_acc < test_acc:
                if os.path.exists(file_name + str(max_epoch) + "-model.pth"):
                    os.remove(file_name + str(max_epoch) + "-model.pth")  # 删除保存的旧的结果
                max_acc = test_acc
                max_epoch = epoch
                torch.save(model.state_dict(), file_name + str(epoch) + "-model.pth")

            with open(file_name + "result", "a+") as f:
                f.writelines("epoch: " + str(epoch) +
                             "  val_acc: " + str(round(val_acc, 4)) +
                             "  val_loss:  " + str(round(val_loss.item(), 4)) +
                             "  test_acc: " + str(round(test_acc, 4)) +
                             "  test_loss: " + str(round(test_loss.item(), 4)) +
                             "\n")
                if epoch == args.epochs:
                    f.writelines("maxEpoch: " + str(max_epoch) + "  test_acc: " + str(round(max_acc, 4)) + "\n")

    print("maxEpoch: " + str(max_epoch) + "  test_acc: " + str(round(max_acc, 4)))


def main(epochs, lr, num_layer, emb_dim,seed,split):
    parser = argparse.ArgumentParser(description='PyTorch implementation of predict tasks')
    parser.add_argument('--epochs', type=int, default=200,  # 预训练方法运行200轮
                        help='number of epochs to train (default: 200)')
    parser.add_argument('--device', type=int, default=1,
                        help='which gpu to use if any (default: 1)')
    parser.add_argument('--lr', type=float, default=0.001,  # 0.0001非常差，0.1也不太行，0.001和0.01差不多，学习率越小，loss往往越小
                        help='learning rate (default: 0.001)')
    parser.add_argument('--decay', type=float, default=0,  # L2 norm coefficient，L2正则化系数 1e-05 （原来是0）
                        help='weight decay (default: 0)')
    parser.add_argument('--num_layer', type=int, default=5,  # 子图的层数为5 【对应了 K】
                        help='number of GNN message passing layers (default: 5).')
    parser.add_argument('--emb_dim', type=int, default=1000,  # 1000的维度
                        help='embedding dimensions (default: 300)')
    parser.add_argument('--pretrain', type=bool, default=False,  # 是否预训练
                        help='pretrain or not (default: False)')
    parser.add_argument('--seed', type=int, default=0, help="Seed for running experiments.")

    args = parser.parse_args()

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")

    train_data = torch.load("train.pt")
    val_data = torch.load("val.pt")
    test_data = torch.load("test.pt")

    train_graph = train_data["graph"].to(device)  # 读取训练集的图，并且加载到服务器
    train_graph['y'] = torch.tensor(train_graph['y'], dtype=torch.long)
    val_graph = val_data["graph"].to(device)
    val_graph['y'] = torch.tensor(val_graph['y'], dtype=torch.long)
    test_graph = test_data["graph"].to(device)
    test_graph['y'] = torch.tensor(test_graph['y'], dtype=torch.long)

    # 定义模型， 并将模型加载到GPU
    model = PredictionGGNN(in_feats=emb_dim, out_feats=args.emb_dim, n_steps=num_layer, aggregate_type="mean", num_cls=16).to(device)

    if args.pretrain:
        model.from_pretrained("2pretrain.pth")

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=args.decay)

    # 训练模型
    filebase = './pthggnn/ggnn_'
    filename = filebase + str(split)+'_'+str(seed)+'_'
    train_test(args, epochs ,train_graph, val_graph, test_graph, model, optimizer,filename)


def knn(k=1):
    train_data = torch.load("train.pt")
    test_data = torch.load("test.pt")

    train_graph = train_data["graph"]
    test_graph = test_data["graph"]

    neigh = neighbors.KNeighborsClassifier(n_neighbors=k, algorithm='auto', weights='distance')
    neigh.fit(train_graph.x, train_graph.y)
    print(neigh.predict(test_graph.x))

    prediction = neigh.predict(test_graph.x)
    print(classification_report(test_graph.y.numpy(), prediction))

    predict = neigh.predict_proba(test_graph.x)

    y_true = torch.zeros((test_graph.y.shape[0], 16))

    for i in range(test_graph.y.shape[0]):
        y_true[i][test_graph.y[i].item()] = 1

    print(y_true)
    print(y_true.shape)
    print(predict)
    print(predict.shape)

    print(roc_auc_score(y_true.numpy(), predict, average="weighted"))


def mlp(layer_size,seed):
    clas = MLPClassifier(hidden_layer_sizes=layer_size, max_iter=2000,
                         early_stopping=False, random_state=seed,
                         solver='adam')
    train_data = torch.load("train.pt")
    test_data = torch.load("test.pt")
    val_data = torch.load('val.pt')
    train_keys = train_data['graph']['x']
    train_lbls = train_data['graph']['y']

    clas.fit(train_keys, train_lbls)
    test_keys = test_data['graph']['x']
    test_lbls = test_data['graph']['y']

    val_keys = val_data['graph']['x']
    val_lbls = val_data['graph']['y']

    valpred = clas.predict(val_keys)
    testpred = clas.predict(test_keys)

    testpred = torch.from_numpy(testpred)
    valpred = torch.from_numpy(valpred)

    val_acc = torch.sum(valpred == val_lbls)
    val_acc = val_acc.item() / valpred.shape[0]

    test_acc = torch.sum(testpred == test_lbls)
    test_acc = test_acc.item() / testpred.shape[0]

    y_predict = testpred  # GPU tensor 转CPU tensor
    y_true = test_lbls
    print(classification_report(y_true, y_predict))

    print("MLP RESULT | " +
          "Val Accuracy: {:.4f}| ".format(
              val_acc) +
          "Test Accuracy: {:.4f}".format(
              test_acc))


def combine(app_id_list=[0, 1, 2], name="test.pt", featuretype ='vgg16', filename='textfeature1.pt'):
    data = torch.load("total.pt")
    if featuretype == 'tfidf':
        try:
            nodefeature = torch.load(filename)
        except IOError:
            print("no filename ", filename)
            return

    elif featuretype == 'vgg16':
        nodefeature = []
    else:
        print("featuretype error")
        return

    start_index = {}
    app_len = {}
    node_nums = 0
    all_x = 1
    all_y = 1
    all_edge_index = 1

    for app_id in app_id_list:
        app = data[app_id]
        if start_index == {}:
            if featuretype != 'vgg16':
                temp = torch.from_numpy(nodefeature[app_id])
                temp = temp.to(torch.float32)
                all_x = temp
            else:
                all_x = app.x
            all_edge_index = app.edge_index
            all_y = app.y
        else:
            if featuretype != 'vgg16':
                temp = torch.from_numpy(nodefeature[app_id])
                temp = temp.to(torch.float32)
                all_x = torch.cat((all_x, temp), dim=0)
            else:
                all_x = torch.cat((all_x, app.x), dim=0)
            all_y = torch.cat((all_y, app.y), dim=0)
            all_edge_index = torch.cat((all_edge_index, app.edge_index + node_nums), 1)

        start_index[app_id] = node_nums
        app_len[app_id] = app.num_nodes
        node_nums += app.num_nodes

    g = Data(x=all_x, edge_index=all_edge_index, y=all_y)

    data = dict()
    data['graph'] = g
    data['start_index'] = start_index
    data['app_len'] = app_len
    torch.save(data, name)

    return all_x.shape[1]


def split_batch(test_list=[], val_list=[], featuretype='tfidf', filename='textfeature.pt'):

    test_list = test_list
    val_list = val_list
    train_list = []

    for i in range(30):
        if i not in test_list and i not in val_list:
            train_list.append(i)

    combine(test_list, "test.pt", featuretype, filename)
    combine(val_list, "val.pt", featuretype, filename)
    size = combine(train_list, "train.pt", featuretype, filename)
    return size


def main_gcn(epochs, lr, num_layer, emb_dim,hidden_channel,seed,dropout,split,pthpath):
    parser = argparse.ArgumentParser(description='PyTorch implementation of predict tasks')
    parser.add_argument('--epochs', type=int, default=200,  # 预训练方法运行200轮
                        help='number of epochs to train (default: 200)')
    parser.add_argument('--device', type=int, default=1,
                        help='which gpu to use if any (default: 1)')
    parser.add_argument('--lr', type=float, default=0.001,  # 0.0001非常差，0.1也不太行，0.001和0.01差不多，学习率越小，loss往往越小
                        help='learning rate (default: 0.001)')
    parser.add_argument('--decay', type=float, default=0,  # L2 norm coefficient，L2正则化系数 1e-05 （原来是0）
                        help='weight decay (default: 0)')
    parser.add_argument('--num_layer', type=int, default=5,  # 子图的层数为5 【对应了 K】
                        help='number of GNN message passing layers (default: 5).')
    parser.add_argument('--emb_dim', type=int, default=1000,  # 1000的维度
                        help='embedding dimensions (default: 300)')
    parser.add_argument('--pretrain', type=bool, default=False,  # 是否预训练
                        help='pretrain or not (default: False)')
    parser.add_argument('--seed', type=int, default=0, help="Seed for running experiments.")

    args = parser.parse_args()

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")

    train_data = torch.load("train.pt")
    val_data = torch.load("val.pt")
    test_data = torch.load("test.pt")

    train_graph = train_data["graph"].to(device)  # 读取训练集的图，并且加载到服务器
    train_graph['y'] = torch.tensor(train_graph['y'], dtype=torch.long)
    val_graph = val_data["graph"].to(device)
    val_graph['y'] = torch.tensor(val_graph['y'], dtype=torch.long)
    test_graph = test_data["graph"].to(device)
    test_graph['y'] = torch.tensor(test_graph['y'], dtype=torch.long)

    # 定义模型， 并将模型加载到GPU
    model = GCN(in_channels=emb_dim,hidden_channels=hidden_channel,num_layers=num_layer,out_channels=16,dropout=dropout).to(device)

    if args.pretrain:
        model.from_pretrained("2pretrain.pth")

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=args.decay)

    filebase = pthpath
    filename = filebase + str(split)+'_'+str(seed)+'_'
    train_test(args, epochs ,train_graph, val_graph, test_graph, model, optimizer,filename)


def main_sage(epochs, lr, num_layer, emb_dim,hidden_channel,seed,dropout,split,pthpath):
    parser = argparse.ArgumentParser(description='PyTorch implementation of predict tasks')
    parser.add_argument('--epochs', type=int, default=200,  # 预训练方法运行200轮
                        help='number of epochs to train (default: 200)')
    parser.add_argument('--device', type=int, default=1,
                        help='which gpu to use if any (default: 1)')
    parser.add_argument('--lr', type=float, default=0.001,  # 0.0001非常差，0.1也不太行，0.001和0.01差不多，学习率越小，loss往往越小
                        help='learning rate (default: 0.001)')
    parser.add_argument('--decay', type=float, default=0,  # L2 norm coefficient，L2正则化系数 1e-05 （原来是0）
                        help='weight decay (default: 0)')
    parser.add_argument('--num_layer', type=int, default=5,  # 子图的层数为5 【对应了 K】
                        help='number of GNN message passing layers (default: 5).')
    parser.add_argument('--emb_dim', type=int, default=1000,  # 1000的维度
                        help='embedding dimensions (default: 300)')
    parser.add_argument('--pretrain', type=bool, default=False,  # 是否预训练
                        help='pretrain or not (default: False)')
    parser.add_argument('--seed', type=int, default=0, help="Seed for running experiments.")

    args = parser.parse_args()

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")

    train_data = torch.load("train.pt")
    val_data = torch.load("val.pt")
    test_data = torch.load("test.pt")

    train_graph = train_data["graph"].to(device)  # 读取训练集的图，并且加载到服务器
    train_graph['y'] = torch.tensor(train_graph['y'], dtype=torch.long)
    val_graph = val_data["graph"].to(device)
    val_graph['y'] = torch.tensor(val_graph['y'], dtype=torch.long)
    test_graph = test_data["graph"].to(device)
    test_graph['y'] = torch.tensor(test_graph['y'], dtype=torch.long)

    # 定义模型， 并将模型加载到GPU
    model = GraphSAGE(in_channels=emb_dim,hidden_channels=hidden_channel,num_layers=num_layer,out_channels=16,dropout=dropout).to(device)

    if args.pretrain:
        model.from_pretrained("2pretrain.pth")

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=args.decay)

    # 训练模型
    filebase = pthpath
    filename = filebase + str(split)+'_'+str(seed)+'_'
    train_test(args, epochs ,train_graph, val_graph, test_graph, model, optimizer,filename)


def main_gat(epochs, lr, num_layer, emb_dim,hidden_channel,seed,dropout,split,pthpath):
    parser = argparse.ArgumentParser(description='PyTorch implementation of predict tasks')
    parser.add_argument('--epochs', type=int, default=200,  # 预训练方法运行200轮
                        help='number of epochs to train (default: 200)')
    parser.add_argument('--device', type=int, default=1,
                        help='which gpu to use if any (default: 1)')
    parser.add_argument('--lr', type=float, default=0.001,  # 0.0001非常差，0.1也不太行，0.001和0.01差不多，学习率越小，loss往往越小
                        help='learning rate (default: 0.001)')
    parser.add_argument('--decay', type=float, default=0,  # L2 norm coefficient，L2正则化系数 1e-05 （原来是0）
                        help='weight decay (default: 0)')
    parser.add_argument('--num_layer', type=int, default=5,  # 子图的层数为5 【对应了 K】
                        help='number of GNN message passing layers (default: 5).')
    parser.add_argument('--emb_dim', type=int, default=1000,  # 1000的维度
                        help='embedding dimensions (default: 300)')
    parser.add_argument('--pretrain', type=bool, default=False,  # 是否预训练
                        help='pretrain or not (default: False)')
    parser.add_argument('--seed', type=int, default=0, help="Seed for running experiments.")

    args = parser.parse_args()

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")

    train_data = torch.load("train.pt")
    val_data = torch.load("val.pt")
    test_data = torch.load("test.pt")

    train_graph = train_data["graph"].to(device)  # 读取训练集的图，并且加载到服务器
    train_graph['y'] = torch.tensor(train_graph['y'], dtype=torch.long)
    val_graph = val_data["graph"].to(device)
    val_graph['y'] = torch.tensor(val_graph['y'], dtype=torch.long)
    test_graph = test_data["graph"].to(device)
    test_graph['y'] = torch.tensor(test_graph['y'], dtype=torch.long)

    model = GAT(in_channels=emb_dim,hidden_channels=hidden_channel,num_layers=num_layer,out_channels=16,dropout=dropout).to(device)

    if args.pretrain:
        model.from_pretrained("2pretrain.pth")

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=args.decay)

    # 训练模型
    filebase = pthpath
    filename = filebase + str(split)+'_'+str(seed)+'_'
    train_test(args, epochs ,train_graph, val_graph, test_graph, model, optimizer,filename)


def main_gin(epochs, lr, num_layer, emb_dim,hidden_channel,seed,dropout,split,pthpath):
    parser = argparse.ArgumentParser(description='PyTorch implementation of predict tasks')
    parser.add_argument('--epochs', type=int, default=200,  # 预训练方法运行200轮
                        help='number of epochs to train (default: 200)')
    parser.add_argument('--device', type=int, default=1,
                        help='which gpu to use if any (default: 1)')
    parser.add_argument('--lr', type=float, default=0.001,  # 0.0001非常差，0.1也不太行，0.001和0.01差不多，学习率越小，loss往往越小
                        help='learning rate (default: 0.001)')
    parser.add_argument('--decay', type=float, default=0,  # L2 norm coefficient，L2正则化系数 1e-05 （原来是0）
                        help='weight decay (default: 0)')
    parser.add_argument('--num_layer', type=int, default=5,  # 子图的层数为5 【对应了 K】
                        help='number of GNN message passing layers (default: 5).')
    parser.add_argument('--emb_dim', type=int, default=1000,  # 1000的维度
                        help='embedding dimensions (default: 300)')
    parser.add_argument('--pretrain', type=bool, default=False,  # 是否预训练
                        help='pretrain or not (default: False)')
    parser.add_argument('--seed', type=int, default=0, help="Seed for running experiments.")

    args = parser.parse_args()

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")

    train_data = torch.load("train.pt")
    val_data = torch.load("val.pt")
    test_data = torch.load("test.pt")

    train_graph = train_data["graph"].to(device)  # 读取训练集的图，并且加载到服务器
    train_graph['y'] = torch.tensor(train_graph['y'], dtype=torch.long)
    val_graph = val_data["graph"].to(device)
    val_graph['y'] = torch.tensor(val_graph['y'], dtype=torch.long)
    test_graph = test_data["graph"].to(device)
    test_graph['y'] = torch.tensor(test_graph['y'], dtype=torch.long)

    # 定义模型， 并将模型加载到GPU
    model = GIN(in_channels=emb_dim,hidden_channels=hidden_channel,num_layers=num_layer,out_channels=16,dropout=dropout).to(device)

    if args.pretrain:
        model.from_pretrained("2pretrain.pth")

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=args.decay)

    # 训练模型
    filebase = pthpath
    filename = filebase + str(split)+'_'+str(seed)+'_'
    train_test(args, epochs ,train_graph, val_graph, test_graph, model, optimizer,filename)



if __name__ == "__main__":
    split_test_1 = [1, 10, 18]
    split_val_1 = [11, 14, 27]
    split_test_2 = [3, 8, 25]
    split_val_2 = [4, 9, 22]
    split_test_3 = [0, 4, 7]
    split_val_3 = [3, 11, 27]
    split_test_4 = [7, 10, 24]
    split_val_4 = [16, 17, 25]
    split_test_5 = [21, 22, 24]
    split_val_5 = [1, 14, 18]

    split_test_dic = {1: split_test_1, 2: split_test_2, 3: split_test_3, 4: split_test_4, 5: split_test_5}
    split_val_dic = {1: split_val_1, 2: split_val_2, 3: split_val_3, 4: split_val_4, 5: split_val_5}

    epochs_list = [200]
    lr_list = [0.01]
    num_layer_list = [4]

    mlp_layer_list = [(60,)]

    for i in range(0,6):
        logger.warning("start split" + str(i))

        test_list = split_test_dic[i]
        val_list = split_val_dic[i]

        feature_file_base = './textfeature'
        feature_file_name = feature_file_base + str(i) + '.pt'
        emb_dim = split_batch(test_list=test_list, val_list=val_list, featuretype='tfidf', filename=feature_file_name)
        filebase = './result/ggnn/ggnn_'+str(i)+'_'
        for epocho in epochs_list:
            for lr in lr_list:
                for num_layer in num_layer_list:
                    for seed in range(0,11):
                        for roundtime in range(0,11):
                            logger.warning("start ggnn" + str(epocho) + str(lr) + str(num_layer))
                            filename = filebase + str(epocho) + '_' + str(lr) + '_' + str(num_layer)+ '_' + str(roundtime)+ '_' + str(seed) + '.txt'
                            with open(filename, 'w+') as file:
                                sys.stdout = file
                                print('ggnn')
                                print('epoch = ' + str(epocho))
                                print('lr = ' + str(lr))
                                print('num_layer = ' + str(num_layer))
                                print('seed = ' + str(seed))
                                main(epochs=epocho, lr=lr, num_layer=num_layer, emb_dim=emb_dim,seed=seed,split=i)
        
        for layer_size in mlp_layer_list:
            for seed in range(0,11):
                logger.warning("start mlp")
                logger.warning(layer_size)
                filebase = './result/mlp/mlp_'+str(i)+'_'
                filename = str(layer_size[0]) + '_' + str(len(layer_size)) + '_' + str(seed) + '.txt'
                filename = filebase + filename
                with open(filename, 'w+') as file:
                    sys.stdout = file
                    print('mlp')
                    print('layer_size')
                    print(layer_size)
                    print(seed)
                    mlp(layer_size,seed)

        gcn_drop = 0.2
        gcn_hidden_list = [100]
        gcn_epochs_list = [200]
        gcn_lr_list = [0.01]
        gcn_num_layer_list = [1]
        gcn_pth = './pthgcn/gcn_'
        filebase = './result/gcn/gcn_'+str(i)+'_'
        for epocho in gcn_epochs_list:
            for lr in gcn_lr_list:
                for num_layer in gcn_num_layer_list:
                    for gcn_hidden in gcn_hidden_list:
                        for seed in range(0,11):
                            logger.warning("start gcn" + str(epocho) + str(lr) + str(num_layer))
                            filename = filebase + str(epocho) + '_'+ str(gcn_hidden) + '_'+ str(gcn_drop) + '_' + str(lr) + '_' + str(num_layer)+ '_' + str(seed) + '.txt'
                            with open(filename, 'w+') as file:
                                sys.stdout = file
                                print('gcn')
                                print('epoch = ' + str(epocho))
                                print('hidden = ' + str(gcn_hidden))
                                print('drop = ' + str(gcn_drop))
                                print('lr = ' + str(lr))
                                print('num_layer = ' + str(num_layer))
                                print('seed = ' + str(seed))
                                main_gcn(epochs=epocho, lr=lr, num_layer=num_layer, emb_dim=emb_dim,
                                seed=seed,split=i,dropout=gcn_drop,hidden_channel=gcn_hidden,pthpath=gcn_pth)


        sage_drop = 0.2
        sage_hidden_list = [200]
        sage_epochs_list = [200]
        sage_lr_list = [0.01]
        sage_num_layer_list = [2]
        sage_pth = './pthsage/sage_'
        filebase = './result/sage/sage_' + str(i) + '_'
        for epocho in sage_epochs_list:
            for lr in sage_lr_list:
                for num_layer in sage_num_layer_list:
                    for sage_hidden in sage_hidden_list:
                        for seed in range(0, 11):
                            logger.warning("start sage" + str(epocho) + str(lr) + str(num_layer))
                            filename = filebase + str(epocho) + '_' + str(sage_hidden) + '_' + str(sage_drop) + '_' + str(
                                lr) + '_' + str(num_layer)+ '_' + str(seed) + '.txt'
                            with open(filename, 'w+') as file:
                                sys.stdout = file
                                print('sage')
                                print('epoch = ' + str(epocho))
                                print('hidden = ' + str(sage_hidden))
                                print('drop = ' + str(sage_drop))
                                print('lr = ' + str(lr))
                                print('num_layer = ' + str(num_layer))
                                print('seed = ' + str(seed))
                                main_sage(epochs=epocho, lr=lr, num_layer=num_layer, emb_dim=emb_dim, seed=seed, split=i,
                                         dropout=sage_drop, hidden_channel=sage_hidden,pthpath=sage_pth)

        gat_drop = 0.2
        gat_hidden_list = [200]
        gat_epochs_list = [200]
        gat_lr_list = [0.01]
        gat_num_layer_list = [1]
        gat_pth = './pthgat/gat_'
        filebase = './result/gat/gat_' + str(i) + '_'
        for epocho in gat_epochs_list:
            for lr in gat_lr_list:
                for num_layer in gat_num_layer_list:
                    for gat_hidden in gat_hidden_list:
                        for seed in range(0, 11):
                            logger.warning("start gat" + str(epocho) + str(lr) + str(num_layer))
                            filename = filebase + str(epocho) + '_' + str(gat_hidden) + '_' + str(gat_drop) + '_' + str(
                                lr) + '_' + str(num_layer) + '_' + str(seed) + '.txt'
                            with open(filename, 'w+') as file:
                                sys.stdout = file
                                print('gat')
                                print('epoch = ' + str(epocho))
                                print('hidden = ' + str(gat_hidden))
                                print('drop = ' + str(gat_drop))
                                print('lr = ' + str(lr))
                                print('num_layer = ' + str(num_layer))
                                print('seed = ' + str(seed))
                                main_gat(epochs=epocho, lr=lr, num_layer=num_layer, emb_dim=emb_dim, seed=seed, split=i,
                                          dropout=gat_drop, hidden_channel=gat_hidden, pthpath=gat_pth)

        gin_drop = 0.2
        gin_hidden_list = [200]
        gin_epochs_list = [200]
        gin_lr_list = [0.01]
        gin_num_layer_list = [1]
        gin_pth = './pthgin/gin_'
        filebase = './result/gin/gin_' + str(i) + '_'
        for epocho in gin_epochs_list:
            for lr in gin_lr_list:
                for num_layer in gin_num_layer_list:
                    for gin_hidden in gin_hidden_list:
                        for seed in range(0, 11):
                            logger.warning("start gin" + str(epocho) + str(lr) + str(num_layer))
                            filename = filebase + str(epocho) + '_' + str(gin_hidden) + '_' + str(gin_drop) + '_' + str(
                                lr) + '_' + str(num_layer) + '_' + str(seed) + '.txt'
                            with open(filename, 'w+') as file:
                                sys.stdout = file
                                print('gin')
                                print('epoch = ' + str(epocho))
                                print('hidden = ' + str(gin_hidden))
                                print('drop = ' + str(gin_drop))
                                print('lr = ' + str(lr))
                                print('num_layer = ' + str(num_layer))
                                print('seed = ' + str(seed))
                                main_gin(epochs=epocho, lr=lr, num_layer=num_layer, emb_dim=emb_dim, seed=seed, split=i,
                                         dropout=gin_drop, hidden_channel=gin_hidden, pthpath=gin_pth)

