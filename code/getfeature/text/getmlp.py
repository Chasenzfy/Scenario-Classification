from pickle import TRUE
from numpy import TooHardError
import torch
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from torch.autograd.grad_mode import F
import config

random_state = 0
n_components = 1000

use_pca = False
use_rep = False


def prepare_clas():
    if use_rep:
        class_weight = None
    else:
        class_weight = 'balanced'  # noqa
    # clas = SVC(verbose=False, decision_function_shape='ovr', kernel="rbf",
    #           class_weight=class_weight, C=1000)
    # clas = LinearSVC(verbose=False, C=1, class_weight=class_weight)
    clas = MLPClassifier(hidden_layer_sizes=(40,), max_iter=2000,
                         early_stopping=False, random_state=random_state,
                         solver='adam')
    # clas = GaussianNB()
    # clas = MultinomialNB()
    # clas = DecisionTreeClassifier(max_depth=100, random_state=random_state,
    #                              min_impurity_split=1e-7, min_samples_leaf=10)
    # clas = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(
    # max_depth=max_depth, random_state=random_state, min_impurity_split=1e-7,
    # min_samples_leaf=min_samples_leaf), random_state=random_state,
    # n_estimators=n_estimators)
    # clas = RandomForestClassifier() #n_estimators=50, random_state=random_state)
    return clas


# def combine(app_id_list=[0, 1, 2], name="test.pt", featuretype='vgg16'):
#     data = torch.load("total.pt")
#     if featuretype == 'tfidf1':
#         nodefeature = torch.load('appflowfeature1.pt')
#     elif featuretype == 'tfidf2':
#         nodefeature = torch.load('appflowfeature2.pt')
#     else:
#         nodefeature = []
#     start_index = {}
#     app_len = {}
#     node_nums = 0
#     all_x = 1
#     all_y = 1
#     all_edge_index = 1
#
#     for app_id in app_id_list:
#         app = data[app_id]
#         print(app_id)
#         print(app)
#         if start_index == {}:
#             if featuretype != 'vgg16':
#                 temp = torch.from_numpy(nodefeature[app_id])
#                 temp = temp.to(torch.float32)
#                 all_x = temp
#             else:
#                 all_x = app.x
#             all_edge_index = app.edge_index
#             all_y = app.y
#         else:
#             if featuretype != 'vgg16':
#                 temp = torch.from_numpy(nodefeature[app_id])
#                 temp = temp.to(torch.float32)
#                 all_x = torch.cat((all_x, temp), dim=0)
#             else:
#                 all_x = torch.cat((all_x, app.x), dim=0)
#             all_y = torch.cat((all_y, app.y), dim=0)
#             all_edge_index = torch.cat((all_edge_index, app.edge_index + node_nums), 1)
#
#         start_index[app_id] = node_nums
#         app_len[app_id] = app.num_nodes
#         node_nums += app.num_nodes
#
#         print(app.x.shape)
#         print(app.edge_index.shape)
#         print(app.y.shape)
#         print(all_x.shape)
#         print(all_edge_index.shape)
#         print(all_y.shape)


def combine(applst, features, data):
    first = True
    all_x = 1
    all_y = 1

    for app_id in applst:
        app = data[app_id]
        print(app_id)
        print(app)
        if first:
            all_x = torch.from_numpy(features[app_id])
            all_y = app.y
            first = False
        else:
            all_x = torch.cat((all_x, torch.from_numpy(features[app_id])), dim=0)
            all_y = torch.cat((all_y, app.y), dim=0)
        print(features[app_id].shape)
        print(app.y.shape)
        print(all_x.shape)
        print(all_y.shape)

    return (all_x, all_y)


if __name__ == "__main__":
    # # 1
    test_list = [11, 14, 27]
    val_list = [1, 10, 18]

    #2
    # test_list = [4, 9, 18]
    # val_list = [1, 10, 17]

    features = torch.load('appflowfeature1.pt')
    totaldata = torch.load('total.pt')

    train_list = []
    for i in range(30):
        if i not in test_list and i not in val_list:
            train_list.append(i)

    print(train_list)

    (train_keys, train_lbls) = combine(train_list, features, totaldata)

    clas = prepare_clas()
    if use_pca:
        pca = PCA(n_components=n_components)
        train_keys = pca.fit_transform(train_keys)
    #print(train_lbls)
    print("mlp fit")
    clas.fit(train_keys, train_lbls)
    classes = clas.classes_

    print("test")
    (test_keys,test_lbls) = combine(test_list, features, totaldata)
    if use_pca:
        test_keys = pca.transform(test_keys)
    try:
        scores = clas.decision_function(test_keys)[0]
        if config.classify_use_bound:
            score = config.SCREEN_SCORE_BOUND
        else:
            score = -1000
        testpred = 'NONE'
        print(scores)
        for i in range(len(classes)):
            if scores[i] > score:
                score = scores[i]
                testpred = classes[i]
    except:
        testpred = clas.predict(test_keys)

    print(testpred)
    print(testpred.shape)

    print("val")
    (val_keys, val_lbls) = combine(val_list, features, totaldata)
    if use_pca:
        val_keys = pca.transform(val_keys)
    try:
        scores = clas.decision_function(val_keys)[0]
        if config.classify_use_bound:
            score = config.SCREEN_SCORE_BOUND
        else:
            score = -1000
        valpred = 'NONE'
        print(scores)
        for i in range(len(classes)):
            if scores[i] > score:
                score = scores[i]
                valpred = classes[i]
    except:
        valpred = clas.predict(val_keys)

    print(valpred)
    print(valpred.shape)

    testpred = torch.from_numpy(testpred)
    valpred = torch.from_numpy(valpred)

    val_acc = torch.sum(valpred == val_lbls)
    print(val_acc)
    val_acc = val_acc.item() / valpred.shape[0]
    test_acc = torch.sum(testpred == test_lbls)
    print(test_acc)
    test_acc = test_acc.item() / testpred.shape[0]



    print("MLP RESULT | "+
          "Val Accuracy: {:.4f}| ".format(
              val_acc) +
          "Test Accuracy: {:.4f}".format(
              test_acc))