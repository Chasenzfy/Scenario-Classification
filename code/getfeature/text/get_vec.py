from sklearn.feature_extraction.text import TfidfVectorizer
#, HashingVectorizer, CountVectorizer
#from sklearn.pipeline import make_pipeline
#from sklearn.preprocessing import Normalizer
#from sklearn.model_selection import KFold
from sklearn.svm import LinearSVC, SVC # noqa
from sklearn.neural_network import MLPClassifier
#from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier # noqa
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier # noqa
#from sklearn.externals import joblib
import joblib
from sklearn.decomposition import PCA
import sklearn
import numpy
import scipy
import torch


from tesserocr import PyTessBaseAPI, RIL
from sklearn.preprocessing import StandardScaler

import glob
import os
#import random
import re
#from functools import reduce
import xml.etree.ElementTree as ET
import subprocess
import multiprocessing
import functools
import logging
import argparse
import pickle
import random

import config
import perfmon
import analyze
import tags as taginfo
import util
import hidden

DATADIR = "../guis-news"

check_train = True
detail_report = False
missing_warn = False
report_exact = True
show_feature = False

use_rep = False
use_num = False
only_good_pt = True
use_fake_ocr = False
use_pca = False
nopt = False
use_treeinfo = True
use_rootinfo = False
use_scaler = False
use_titleinfo = True

random_state = 0
max_depth = 100
min_samples_leaf = 6
n_estimators = 58
n_components = 1000

if config.parallel:
    thread_count = config.threads
else:
    thread_count = 1
if use_num:
    basic_re = re.compile("[A-Za-z0-9]+")
else:
    basic_re = re.compile("[A-Za-z]+")

word_re = re.compile("[A-Z0-9]?[a-z0-9]+|[A-Z0-9]")
alpha_re = re.compile('[a-zA-z]+')

if use_rep:
    REP_COUNT = {'signin': 5, 'register': 5, 'main': 1, 'checkout': 1, 'addredit': 5,
                 'cardedit': 5, 'filter': 2, 'sort': 2, 'account': 5, 'setting': 5,
                 'address': 3, 'payment': 3, 'search': 5, 'cart': 1, 'detail': 1,
                 'searchret': 1, 'menu': 3, 'cat': 5, 'welcome': 5, 'orders': 5,
                 'about': 5, 'terms': 5, 'help': 5, 'notif': 5, 'contact': 5}
else:
    REP_COUNT = {}


bound_re = re.compile("\[(\d+),(\d+)\]\[(\d+),(\d+)\]")
SCR_SIZE = config.width * config.real_height
#SCR_SIZE = 1080*1920
VEC_WIDTH = 10


def vectorize(pts, tree_vec, act_vec, img_vec, title_vec):
    trees = []
    acts = []
    imgs = []
    titles = []
    extras = []
    for datapt in pts:
        trees.append(datapt['tree'])
        acts.append(datapt['act'])
        imgs.append(datapt['img'])
        titles.append(datapt['title'])
        extras.append(datapt['vec'])

    tree_vecs = tree_vec.transform(trees)
    act_vecs = act_vec.transform(acts)
    img_vecs = img_vec.transform(imgs)
    if use_titleinfo:
        title_vecs = title_vec.transform(titles)
    else:
        title_vecs = None
    extra_vecs = numpy.vstack(extras)
    x = scipy.sparse.hstack((tree_vecs, act_vecs, img_vecs, extra_vecs, title_vecs)) # C

    #x = scipy.sparse.hstack((tree_vecs, act_vecs, img_vecs, extra_vecs, title_vecs)) # C
    #x = scipy.sparse.hstack((tree_vecs, act_vecs, img_vecs, extra_vecs))
    #x = scipy.sparse.hstack((tree_vecs, img_vecs, title_vecs, extra_vecs)) # CASE B
    #x = scipy.sparse.hstack((tree_vecs, img_vecs, act_vecs))
    #x = scipy.sparse.hstack((tree_vecs, act_vecs))
    #x = scipy.sparse.hstack((tree_vecs, img_vecs))
    #x = scipy.sparse.hstack((tree_vecs, extra_vecs)) # CASE A
    #x = img_vecs
    #x = tree_vecs
    #x = act_vecs
#    if not parallel:
#        print("test shape: %d %d" % x.shape)
    x = x.toarray()

    return (x, tree_vecs, act_vecs, img_vecs, title_vecs)


def vectorize_test(pts, tree_vec, act_vec, img_vec, title_vec, scaler):
    vec = vectorize(pts, tree_vec, act_vec, img_vec, title_vec)[0]
    if use_scaler:
        return scaler.transform(vec)
    else:
        return vec


def vectorize_train(pts):
    trees = []
    acts = []
    imgs = []
    titles = []
    extras = []

    for datapt in pts:
        trees.append(datapt['tree'])
        acts.append(datapt['act'])
        imgs.append(datapt['img'])
        titles.append(datapt['title'])
        extras.append(datapt['vec'])
    
    # treefile = open('./tfidfwords/tree.txt','w+',encoding='utf-8')
    # actfile = open('./tfidfwords/act.txt','w+',encoding='utf-8')
    # imgfile = open('./tfidfwords/img.txt','w+',encoding='utf-8')
    # titlefile = open('./tfidfwords/title.txt','w+',encoding='utf-8')

    # print("tree")
    # for word in trees:
    #     treefile.write(word+'\n')
    # print("act")
    # for word in acts:
    #     actfile.write(word+'\n')
    # print("imgs")
    # for word in imgs:
    #     imgfile.write(word+'\n')
    # print("titles")
    # for word in titles:
    #     titlefile.write(word+'\n')

    tree_vectorizer = TfidfVectorizer(
        max_df=0.5, max_features=8192, min_df=0.01, stop_words='english', use_idf=True,
        ngram_range=(1, 1))
    #tree_vectorizer = CountVectorizer(max_df=0.5, max_features=8192, min_df=0.01,
    #stop_words='english', ngram_range=(1, 1))
    tree_vectorizer.fit(trees)
    act_vectorizer = TfidfVectorizer(
        max_df=1.0, max_features=8192, min_df=0.0, stop_words='english', use_idf=True,
        ngram_range=(1, 1))
    #act_vectorizer =  CountVectorizer(stop_words='english')
    act_vectorizer.fit(acts)
    img_vectorizer = TfidfVectorizer(
        max_df=0.5, max_features=8192, min_df=0.01, stop_words='english', use_idf=True,
        ngram_range=(1, 2))
    #img_vectorizer =  CountVectorizer()
    img_vectorizer.fit(imgs)
    if use_titleinfo:
        title_vectorizer = TfidfVectorizer(max_df=0.5, max_features=8192, min_df=0.01,
                                           stop_words='english', use_idf=True,
                                           ngram_range=(1, 2))
        title_vectorizer.fit(titles)
    else:
        title_vectorizer = None

    (x, tree_vecs, act_vecs, img_vecs, title_vecs) = vectorize(
        pts, tree_vectorizer, act_vectorizer, img_vectorizer, title_vectorizer)

    if use_scaler:
        scaler = StandardScaler()
        x = scaler.fit_transform(x)
    else:
        scaler = None
    #x = scipy.sparse.hstack((tree_vecs, img_vecs, extra_vecs))
    #x = tree_vecs
    #x = scipy.sparse.hstack((tree_vecs, act_vecs))
    #x = act_vecs

#    if not parallel:
#        print("tree cnt: %d %d" % tree_vecs.shape)
#        print("act  cnt: %d %d" % act_vecs.shape)
#        print("img  cnt: %d %d" % img_vecs.shape)
#        print("merged: %d %d" % x.shape)

    #x = x.toarray()

    mydict = [''] * (tree_vecs.shape[1] + act_vecs.shape[1] + img_vecs.shape[1])
    # for item in tree_vectorizer.vocabulary_:
    #     mydict[tree_vectorizer.vocabulary_[item]] = item
    # for item in act_vectorizer.vocabulary_:
    #     mydict[act_vectorizer.vocabulary_[item] + tree_vecs.shape[1]] = 'ACT' + item
    # for item in img_vectorizer.vocabulary_:
    #     mydict[img_vectorizer.vocabulary_[item] + tree_vecs.shape[1] + act_vecs.shape[1]
    #            ] = 'IMG' + item

    return (x, mydict, tree_vectorizer, act_vectorizer, img_vectorizer, title_vectorizer,
            scaler)

    
def sortbytag(x):
    return int(x['tag'])


def settrainpts(testapps,appdict):
    #传入测试app的列表，传出train的词集,test另行获得
    trainpts = []
    for appid in appdict:
        if appid not in testapps:
            trainpts.extend(appdict[appid])
    return trainpts


def get_featurept_bylist(testapps,savefile):
    #testapps = [1, 4, 9, 10, 17, 18]
    appdict = torch.load('dictdata.pt')
    features = {}

    trainpts = settrainpts(testapps, appdict)

    (train_keys, mydict, tree_vec, act_vec, img_vec, title_vec,
     scaler) = vectorize_train(trainpts)
    if use_pca:
        pca = PCA(n_components=n_components)
        train_keys = pca.fit_transform(train_keys)

    for app in appdict:
        test_pt = appdict[app]
        test_pt.sort(key=sortbytag)
        # for pt in test_pt:
        #     print(pt['file'])
        test_keys = vectorize_test(test_pt, tree_vec, act_vec, img_vec,
                                   title_vec, scaler)
        if use_pca:
            test_keys = pca.transform(test_keys)
        # print(app)
        # print(test_keys)
        print(test_keys.shape)
        features[app - 1] = test_keys
    #torch.save(features, 'appflowfeature2.pt')
    torch.save(features, savefile)

if __name__ == "__main__":
    # data = torch.load('./retotal.pt')
    # # print(data)
    # # print(len(data))
    # appdict = {}
    # appids = set()
    # for screen in data:
    #     appid = screen['app']
    #     appid = int(appid)
    #     if appid in appids:
    #         appdict[appid].append(screen)
    #     else:
    #         appids.add(appid)
    #         newlst = []
    #         appdict[appid] = newlst
    #         appdict[appid].append(screen)
    # print(appdict)
    # torch.save(appdict,'dictdata.pt')
    # #从乱序保存改为字典保存，每个app一个list

    #1
    # test_list = [11, 14, 27]
    # val_list = [1, 10, 18]

    #2
    # test_list = [4, 9, 18]
    # val_list = [1, 10, 17]



    # split_test_1 = [1, 10, 18]
    # split_val_1 = [11, 14, 27]
    # split_test_2 = [3, 8, 25]
    # split_val_2 = [4, 9, 22]
    # split_test_3 = [3, 11, 27]
    # split_val_3 = [0, 4, 7]
    # split_test_4 = [7, 10, 24]
    # split_val_4 = [16, 17, 25]
    # split_test_5 = [21, 22, 24]
    # split_val_5 = [1, 14, 18]

    # 2488
    # testapps = [1,10,11,14,18,27]
    # 2514
    # testapps = [3,4,8,9,22,25]
    # 2561
    testapps = [0,3,4,7,11,27]
    # 2523
    # testapps = [7,10,16,17,24,25]
    # 2366
    # testapps = [1,14,18,21,22,24]
    # testapps = [0]
    appdict = torch.load('dictdata.pt')
    features = {}
    
    trainpts = settrainpts(testapps,appdict)
    
    (train_keys, mydict, tree_vec, act_vec, img_vec, title_vec,
     scaler) = vectorize_train(trainpts)
    if use_pca:
            pca = PCA(n_components=n_components)
            train_keys = pca.fit_transform(train_keys)
    
    
    for app in appdict:
        test_pt = appdict[app]
        test_pt.sort(key=sortbytag)
        for pt in test_pt:
            print(pt['file'])
        test_keys = vectorize_test(test_pt, tree_vec, act_vec, img_vec,
                                   title_vec, scaler)
        if use_pca:
            test_keys = pca.transform(test_keys)
        print(app)
        print(test_keys)
        print(test_keys.shape)
        features[app-1] = test_keys
    torch.save(features,'appflowfeature3.pt')






    # for i in range(0,30):
    #     print(i)
    #     temp_applist = []
    #     temp_applist.append(i)
    #     print(temp_applist)
    #     filebase = './tfidf_features/'
    #     filename = 'tfidf_features'
    #     for app in temp_applist:
    #         filename += '_'
    #         filename += str(app)
    #     filename += '.pt'
    #     filename = filebase + filename
    #     print(filename)
    #     get_featurept_bylist(temp_applist, filename)
    # 每个app作为测试集，生成一个pt


    # get_featurept_bylist([1,10,11,14,18,27], './tfidf_features/tfidf_features_part1.pt')

    # get_featurept_bylist([1,4,9,10,17,18], './tfidf_features/tfidf_features_part2.pt')