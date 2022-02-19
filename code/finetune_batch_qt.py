import sys

import numpy as np
import argparse

import torch
import random
import torch.nn.functional as F
from sklearn import neighbors
from sklearn.metrics import classification_report
from model_batch import PredictionGGNN
from model import PixelGGNN
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.neural_network import MLPClassifier
from torch_geometric.data import Data
import argparse
import logging

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def train_test(args, epochs, train_graph, val_graph, test_graph, model, optimizer):
    print("start training...")
    model.train()

    for epoch in range(1, epochs + 1):
        optimizer.zero_grad()  # 清空上一步的残余更新参数值（必有）
        logits = model.forward(train_graph.x, train_graph.edge_index)
        train_loss = F.cross_entropy(logits, train_graph["y"])

        train_acc = torch.sum(logits.argmax(dim=1) == train_graph["y"])
        train_acc = train_acc.item() / train_graph.x.shape[0]


        # 计算验证集和测试集的loss和acc
        val_logits = model.forward(val_graph.x, val_graph.edge_index)
        val_loss = F.cross_entropy(val_logits, val_graph["y"])
        val_acc = torch.sum(val_logits.argmax(dim=1) == val_graph["y"])
        val_acc = val_acc.item() / val_graph.x.shape[0]

        test_logits = model.forward(test_graph.x, test_graph.edge_index)
        test_loss = F.cross_entropy(test_logits, test_graph["y"])
        test_acc = torch.sum(test_logits.argmax(dim=1) == test_graph["y"])
        test_acc = test_acc.item() / test_graph.x.shape[0]

        y_predict = test_logits.argmax(dim=1).cpu().numpy()  # GPU tensor 转CPU tensor
        y_true = test_graph["y"].cpu().numpy()
        print(classification_report(y_true, y_predict))

        # 转化为概率
        auc_test_logits = F.softmax(test_logits, dim=1)
        auc_y_predict = auc_test_logits.detach().cpu().numpy()

        auc_y_true = test_graph.y.cpu().numpy()  # (nums,1)
       
        print("Epoch {:05d} | ".format(epoch) +
              "Train Accuracy: {:.4f} | Train Loss: {:.4f} | ".format(
                  train_acc, train_loss.item()) +
              "Val Accuracy: {:.4f} | Val loss: {:.4f} | ".format(
                  val_acc, val_loss.item()) +
              "Test Accuracy: {:.4f} | Test loss: {:.4f}".format(
                  test_acc, test_loss.item()))

        train_loss.backward()  # 误差反向传播, 计算参数更新值（必有）
        optimizer.step()  # 将参数更新值施加到 net 的 parameters 上（必有）




def main(epochs, lr, num_layer, emb_dim,seed):
    parser = argparse.ArgumentParser(description='PyTorch implementation of predict tasks')
    # parser.add_argument('--epochs', type=int, default=300,  # 预训练方法运行200轮
    #                     help='number of epochs to train (default: 200)')
    parser.add_argument('--device', type=int, default=1,
                        help='which gpu to use if any (default: 1)')
    # parser.add_argument('--lr', type=float, default=0.01,  # 0.0001非常差，0.1也不太行，0.001和0.01差不多，学习率越小，loss往往越小
    #                     help='learning rate (default: 0.001)')
    parser.add_argument('--decay', type=float, default=0,  # L2 norm coefficient，L2正则化系数 1e-05 （原来是0）
                        help='weight decay (default: 0)')
    # parser.add_argument('--num_layer', type=int, default=3,  # 子图的层数为5 【对应了 K】
    #                     help='number of GNN message passing layers (default: 5).')
    parser.add_argument('--emb_dim', type=int, default=1000,  # 1000的维度
                        help='embedding dimensions (default: 300)')
    parser.add_argument('--pretrain', type=bool, default=False,  # 是否预训练
                        help='pretrain or not (default: False)')

    args = parser.parse_args()

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")

    train_data = torch.load("train2.pt")
    val_data = torch.load("val2.pt")
    test_data = torch.load("test2.pt")

    train_graph = train_data["graph"].to(device)  # 读取训练集的图，并且加载到服务器
    train_graph['y'] = torch.tensor(train_graph['y'],dtype=torch.long)
    val_graph = val_data["graph"].to(device)
    val_graph['y'] = torch.tensor(val_graph['y'],dtype=torch.long)
    test_graph = test_data["graph"].to(device)
    test_graph['y'] = torch.tensor(test_graph['y'],dtype=torch.long)

    # 定义模型， 并将模型加载到GPU
    model = PredictionGGNN(in_feats=21400, out_feats=args.emb_dim, n_steps=num_layer, aggregate_type="mean", num_cls=16).to(device)

    if args.pretrain:
        model.from_pretrained("2pretrain.pth")

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=args.decay)

    # 训练模型
    train_test(args, epochs, train_graph, val_graph, test_graph, model, optimizer)


def knn(k=1):
    train_data = torch.load("train2.pt")
    test_data = torch.load("test2.pt")

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
    train_data = torch.load("train2.pt")
    test_data = torch.load("test2.pt")
    val_data = torch.load('val2.pt')
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

    combine(test_list, "test2.pt", featuretype, filename)
    combine(val_list, "val2.pt", featuretype, filename)
    size = combine(train_list, "train2.pt", featuretype, filename)
    return size


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

    epochs_list = [300]
    lr_list = [0.001]
    num_layer_list = [2]

    mlp_layer_list = [(400,)]

    for i in range(0,6):
        logger.warning("start split" + str(i))

        test_list = split_test_dic[i]
        val_list = split_val_dic[i]

        feature_file_name = './newfeature/newqt_feature.pt'

        emb_dim = split_batch(test_list=test_list, val_list=val_list, featuretype='tfidf', filename=feature_file_name)

        filebase = './newsplit5/ggnnqt/ggnn_'+str(i)+'_'
        for epoch in epochs_list:
            for lr in lr_list:
                for num_layer in num_layer_list:
                    for seed in range(0,11):
                        logger.warning("start ggnn" + str(epoch) + str(lr) + str(num_layer))
                        filename = filebase + str(epoch) + '_' + str(lr) + '_' + str(num_layer)+ '_' + str(seed) + '.txt'
                        with open(filename, 'w+') as file:
                            sys.stdout = file
                            print('ggnn')
                            print('epoch = ' + str(epoch))
                            print('lr = ' + str(lr))
                            print('num_layer = ' + str(num_layer))
                            main(epochs=epoch, lr=lr, num_layer=num_layer, emb_dim=emb_dim,seed=seed)

        for layer_size in mlp_layer_list:
            for seed in range(0, 11):
                logger.warning("start mlp")
                logger.warning(layer_size)
                filebase = './newsplit5/mlpqt/mlp_'+str(i)+'_'
                filename = str(layer_size[0]) + '_' + str(len(layer_size)) + '_' + str(seed) + '.txt'
                filename = filebase + filename
                with open(filename, 'w+') as file:
                    sys.stdout = file
                    print('mlp')
                    print('layer_size')
                    print(layer_size)
                    mlp(layer_size,seed)
