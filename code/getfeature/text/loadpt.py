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
#from src.util import print_tree
import tags as taginfo
import util
import hidden

DATADIR = "../retotal"

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
VEC_WIDTH = 10


def to_float(boolval):
    return 1.0 if boolval else 0.0


def preprocess_vec(tree):
    ret = numpy.zeros([VEC_WIDTH], numpy.float64)
    if tree is None:
        return ret
    #ret[0] = len(tree) / 100

    if use_treeinfo:
        treeinfo = analyze.collect_treeinfo(tree)
        #ret[1] = 1.0 if treeinfo['listlike'] else 0.0
        ret[2] = len(treeinfo['dupid']) / len(tree)
        ret[3] = len(treeinfo['itemlike']) / len(tree)

    if use_rootinfo:
        rootid = min(tree)
        ret[4] = to_float(tree[rootid]['x'] != 0)
        ret[5] = to_float(tree[rootid]['y'] != 0)
        ret[6] = to_float(tree[rootid]['x'] != 0 and
                          tree[rootid]['x'] + tree[rootid]['width'] < config.width)
        ret[7] = to_float(tree[rootid]['y'] != 0 and
                          tree[rootid]['y'] + tree[rootid]['height'] < config.real_height)

    return ret


def addseg(segs, value, regex=word_re):
    segs.append(value)
    segs.append('\n')
    #parts = regex.findall(value)
    #segs.extend(parts)


def addseg2(segs, kw, value, regex=word_re):
    if value.upper() == value:
        value = value.lower()
    for part in regex.findall(value):
        segs.append(kw + part)
    segs.append('\n')


def addngram(segs, val, regex=word_re, ngram=2):
    parts = regex.findall(val)
    for i in range(len(parts) - 1):
        addseg(segs, parts[i] + parts[i + 1])


def process_tree(tree):
    segs = []
    first_tv = True

    for nodeid in tree:
        node = tree[nodeid]

        if 'visible' in node and node['visible'] == 'hidden':
            continue

        clz = node['class']
        rid = node['id']
        text = node['text'][:30]
        desc = node['desc'][:30]
        ocr = node['ocr']

        addseg(segs, clz)
        addseg(segs, rid)
        addseg(segs, text)
        addseg(segs, desc)
        addseg(segs, ocr)
        addngram(segs, text)
        addngram(segs, desc)
        if node['password']:
            addseg2(segs, "ISPASSWORD", rid)
            addseg2(segs, "ISPASSWORD", clz)
        #if node['scroll']:
        #    addseg2(segs, "SCROLLABLE", rid)
        #    addseg2(segs, "SCROLLABLE", clz)
        #if node['checkable']:
        #    addseg2(segs, "CLICK", rid)
        #    addseg2(segs, "CLICK", clz)

        x = node['x']
        y = node['y']
        width = node['width']
        height = node['height']
        size = width * height
        if size < SCR_SIZE:
            if size > 0.5 * SCR_SIZE:
                segs.append("XXL" + clz)
                addseg2(segs, "XXL", rid)
            elif size > 0.05 * SCR_SIZE:
                segs.append("BIG" + clz)
                addseg2(segs, "BIG", rid)
        if width > 0.6 * config.width:
            segs.append("WIDE" + clz)
            addseg2(segs, "WIDE", rid)
        if height > 0.6 * config.height:
            segs.append("TALL" + clz)
            addseg2(segs, "TALL", rid)
        if y + height < 0.3 * config.height:
            segs.append("TOP" + clz)
            addseg2(segs, "TOP", rid)
        if y > 0.7 * config.height:
            segs.append("BOTTOM" + clz)
            addseg2(segs, "BOTTOM", rid)
        if x + width < 0.3 * config.width:
            segs.append("LEFT" + clz)
            addseg2(segs, "LEFT", rid)
        if x > 0.7 * config.width:
            segs.append("RIGHT" + clz)
            addseg2(segs, "RIGHT", rid)

        if clz == 'TextView' and first_tv:
            first_tv = False
            addseg2(segs, "TITLE", text)

    ret = ' '.join(segs)
    if show_feature:
        print(ret)
    return ret


def preprocess_txt(content):
    if '/' in content:
        content = content.split("/", 1)[1]
    pat = re.compile("[A-Z][a-z]+")
    return " ".join(pat.findall(content))


def preprocess_img(filename):
    ocrfile = filename.replace(".png", ".ocr")
    if os.path.exists(ocrfile):
        with open(ocrfile) as ocrf:
            ocrret = ocrf.read()
    else:
        #print("OCR %s" % filename)
        try:
            #"convert %s -density 420 -units pixelsperinch -define
            # png:compression-level=0 - | tesseract - stdout" % filename,
            ocrret = subprocess.check_output("tesseract %s stdout" % filename,
                                             shell=True, stderr=subprocess.PIPE
                                             ).decode("utf-8")
        except Exception as e:
            print(e)
            print(filename)
            print("err")
            ocrret = ''
        with open(ocrfile, 'w',encoding='utf-8') as ocrf:
            ocrf.write(ocrret)
    return ' '.join(basic_re.findall(ocrret))


def preprocess_title(filename):
    title = ''
    api = PyTessBaseAPI()
    api.SetImageFile(filename)
    boxes = api.GetComponentImages(RIL.TEXTLINE, True)
    for i, (im, box, _, _) in enumerate(boxes):
        api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
        ocrResult = api.GetUTF8Text()
        text = ' '.join(alpha_re.findall(ocrResult.strip()))
        if len(text) < 5:
            continue

        title = text
        break

    if title:
        #print("%s: %s", filename, title)
        print(filename, title)
    return title


@perfmon.op("screen", "prepare_point")
def prepare_point(actname,imgfile, tree=None):
    #if tree is None:
    #    treeinfo = preprocess(xmlsrc)
    #else:
    #print("tree")
    treeinfo = process_tree(tree)
    #print("txt")
    actinfo = preprocess_txt(actname)
    #print("img")
    imginfo = preprocess_img(imgfile)
    #print("vec")
    #imginfo = preprocess_img_fromocr(tree)
    vecinfo = preprocess_vec(tree)
    if use_titleinfo:
        titleinfo = preprocess_title(imgfile)
    else:
        titleinfo = ''
    return {'tree': treeinfo, 'act': actinfo, 'img': imginfo, 'vec': vecinfo,
            'title': titleinfo}
    # return {'tree': treeinfo, 'img': imginfo, 'vec': vecinfo,
    #         'title': titleinfo}


def process_input(filename):
    #print("processinput")
    print(filename)
    filebase = os.path.splitext(filename)[0]
    basename = os.path.basename(filename)
    pagename = basename.split(".")[0]
    if basename.count("_") == 1:
        (appname, scrname) = pagename.split("_")
    else:
        (appname, casename, scrname) = pagename.split("_")

    if scrname == 'cat1':
        scrname = "cat"
    elif scrname == 'cat':
        pass
    elif scrname.startswith('cat'):
        scrname = "cat2"
#    if scrname == "cat1":
#        continue
#    if scrname == "searchret":
#        scrname = "list"

    ptfile = filebase + '.pt'
    if os.path.exists(ptfile) and not nopt:
        ptf = open(ptfile, 'rb')
        unpickler = pickle.Unpickler(ptf)
        try:
            pt = unpickler.load()
            return (scrname, pt)
        except:
            pass
    ptf = open(ptfile, 'wb')
    pickler = pickle.Pickler(ptf)
    #with open(filename, 'r') as f:
    #    xmldata = f.read()
    tree = analyze.load_tree(filename)
    hidden.find_hidden_ocr(tree)
    hidden.mark_children_hidden_ocr(tree)


    if '.xml' in filename:
        actfile = filebase + '.txt'
        actname = open(actfile,encoding='utf-8').read()
#        tree = analyze.analyze([filename], show_progress=False)[0]
    elif '.hier' in filename:
        urlfile = filebase + '.url'
        actname = util.url_to_actname(open(urlfile,encoding='utf-8').read())
#        loaded = webdriver.load(filebase)
#        tree = analyze.analyze_items(loaded['items'])

    imgfile = filebase + '.png'
    # if config.use_postprocess:
    pt = prepare_point(actname, imgfile, tree)
    #pt = prepare_point(imgfile, tree)

    # else:
    #    pt = prepare_point(xmldata, open(actfile).read(), imgfile)
    pt['file'] = filename
    pt['app'] = appname
    pt['scr'] = appname
#            treeinfo = ' '.join([treeinfo, actinfo, imginfo])
    pickler.dump(pt)

    return (scrname, pt)


def collect_input(datadir, extrapath=None, extrascr=None):
    #print("Processing input")
    print("Processing input")
    dataset = {}

    pool = multiprocessing.Pool(processes=thread_count)
    filelist = glob.glob(os.path.join(datadir, "*.xml")) + \
        glob.glob(os.path.join(datadir, "*.hier"))
    for (scrname, pt) in pool.map(process_input, filelist):
        # print("scrname")
        if scrname is None:
            continue
        pt['extra'] = False
        for x in range(REP_COUNT.get(scrname, 1)):
            dataset[scrname] = dataset.get(scrname, []) + [pt]
    if extrapath is not None:
        filelist = glob.glob(os.path.join(extrapath, "*.xml")) + \
            glob.glob(os.path.join(extrapath, "*.hier"))
        #print("loading extra input from %s for %s", extrapath, extrascr)
        print("loading extra input from %s for %s", extrapath, extrascr)
        extrascr = extrascr.split(',')
        for (scrname, pt) in pool.map(process_input, filelist):
            if scrname is None or scrname not in extrascr:
                continue
            pt['extra'] = True
            for x in range(REP_COUNT.get(scrname, 1)):
                dataset[scrname] = dataset.get(scrname, []) + [pt]
    pool.close()

    return dataset


def load_datapts(datadir, appname=None, extrapath=None, extrascr=None):
    dataset = collect_input(datadir, extrapath, extrascr)
    #print(dataset)
    #print(dataset)


    # for screen in taginfo.tag['ignored_screens']:
    #     if screen in dataset:
    #         del dataset[screen]


    #dataset['other'] = dataset.pop('main') + dataset.pop('list')
    #del dataset['main']
    #del dataset['cat']
    #del dataset['cat1']
    #del dataset['cat3']
    #del dataset['list']
    #del dataset['register']
    #del dataset['paywith']

    apps = []
    tags = list(dataset.keys())
    tags.sort()

    datapts = []
    cnt_by_tag = {}
    for tag in tags:
        for obj in dataset[tag]:
            # ignore specific app's pts
            if appname is not None and obj['app'] == appname:
                continue
            obj['tag'] = tag
            datapts.append(obj)
            if not obj['extra']:
                apps.append(obj['app'])
        cnt_by_tag[tag] = len(dataset[tag])

    apps = sorted(set(apps))

    #datapts = sklearn.utils.shuffle(datapts, random_state=random_state)
    return (datapts, apps, tags, cnt_by_tag)



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    # run_evaluation()
    data_dir = '../retotal/'
    (datapts, apps, tags, cnt_by_tag) = load_datapts(data_dir)
    print(apps)
    print(tags)
    print(cnt_by_tag)
    torch.save(datapts,"retotal.pt")