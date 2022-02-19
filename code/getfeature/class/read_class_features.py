import os
import numpy as np
import xml.etree.ElementTree as ET
import torch

screen_x = 1080
screen_y = 1920
edit_widget = ['android.widget.EditText']
image_widget = ['android.widget.Image','android.widget.ImageButton','android.widget.ImageView']
draw_widget = ['android.support.v4.widget.DrawerLayout']


def get_site(node):
    topbound = screen_y *0.2
    buttombound = screen_y * 0.8
    bounds = node.get('bounds')
    y_right_down = int(bounds.split(',')[2].split(']')[0])
    y_left_up = int(bounds.split(',')[1].split(']')[0])
    result = -1
    if(y_right_down < topbound):
        result = 0 #top
    elif(y_left_up > buttombound):
        result = 2 #button
    else:
        result = 1 #mid
    return result


def get_clickable(nodelst):
    num_top = 0
    num_mid = 0
    num_but = 0
    for node in nodelst:
        site = get_site(node)
        clickable = node.get('clickable')
        if clickable == 'true' and site == 0:
            num_top += 1
        elif clickable == 'true' and site == 1:
            num_mid += 1
        elif clickable == 'true' and site == 2:
            num_but += 1
    return (num_top,num_mid,num_but)


def get_swipeable(nodelst):
    num = 0
    for node in nodelst:
        scrollable = node.get('scrollable')
        if scrollable == 'true':
            num += 1
    return num


def get_edit(nodelst):
    num_top = 0
    num_mid = 0
    num_but = 0
    for node in nodelst:
        site = get_site(node)
        classname = node.get('class')
        if classname in edit_widget and site == 0:
            num_top += 1
        elif classname in edit_widget and site == 1:
            num_mid += 1
        elif classname in edit_widget and site == 2:
            num_but += 1
    return (num_top,num_mid,num_but)


def get_longclick(nodelst):
    num = 0
    for node in nodelst:
        longclick = node.get('long-clickable')
        if longclick == 'true':
            num += 1
    return num


def get_focus(nodelst):
    num_top = 0
    num_mid = 0
    num_but = 0
    for node in nodelst:
        site = get_site(node)
        focusable = node.get('focusable')
        if focusable == 'true' and site == 0:
            num_top += 1
        elif focusable == 'true' and site == 1:
            num_mid += 1
        elif focusable == 'true' and site == 2:
            num_but += 1
    return (num_top,num_mid,num_but)


def get_image(nodelst):
    num = 0
    for node in nodelst:
        site = get_site(node)
        classname = node.get('class')
        if classname in image_widget:
            num += 1
    return num


def get_passw(nodelst):
    num = 0
    for node in nodelst:
        password = node.get('password')
        if password == 'true':
            num += 1
    return num


def get_check(nodelst):
    num = 0
    for node in nodelst:
        checkable = node.get('checkable')
        if checkable == 'true':
            num += 1
    return num


def get_drawer(nodelst):
    num = 0
    for node in nodelst:
        site = get_site(node)
        classname = node.get('class')
        if classname in draw_widget:
            num += 1
    return num


def read_class(xml):
    vector = []

    tree = ET.fromstring(xml)
    print(tree)
    nodelst = []
    nodelst = preorder_traverse(nodelst, tree)

    click = get_clickable(nodelst)
    vector.append(click[0])
    vector.append(click[1])
    vector.append(click[2])

    swipe = get_swipeable(nodelst)
    vector.append(swipe)

    edit = get_edit(nodelst)
    vector.append(edit[0])
    vector.append(edit[1])
    vector.append(edit[2])

    longclick = get_longclick(nodelst)
    vector.append(longclick)

    focus = get_focus(nodelst)
    vector.append(focus[0])
    vector.append(focus[1])
    vector.append(focus[2])

    image = get_image(nodelst)
    vector.append(image)

    passw = get_passw(nodelst)
    vector.append(passw)

    check = get_check(nodelst)
    vector.append(check)

    drawer = get_drawer(nodelst)
    vector.append(drawer)

    vector.append(len(nodelst))

    print(vector)
    return vector


def preorder_traverse(nodelst, node):
    if 'hierarchy' != node.tag:
        nodelst.append(node)
    for child in node:
        nodelst = preorder_traverse(nodelst, child)
    return nodelst

if __name__ == '__main__':
    print('class features')
    totalpath = '../total'
    applist = os.listdir(totalpath)
    resultdic = {}
    if '.DS_Store' in applist:
        applist.remove('.DS_Store')
    for app in applist:
        newpath = os.path.join(totalpath,app)
        xmlpath = os.path.join(newpath, 'xml')
        appid = int(app.split('-')[0]) - 1
        print(xmlpath)
        xmllist = os.listdir(xmlpath)
        result = ""
        if '.DS_Store' in xmllist:
            xmllist.remove('.DS_Store')
        for i in range(len(xmllist)):
            filename = str(i) + '.xml'
            filepath = os.path.join(xmlpath,filename)
            # print(filepath)
            with open(filepath,'r',encoding='utf-8') as xmlfile:
                xml = xmlfile.read()
                print(filepath)
                # print(xml)
                vector = read_class(xml)
                vector = np.array(vector)
                vector = np.expand_dims(vector, axis=0)
                print(vector)
                print(vector.shape)
                if result == "":
                    result = vector
                else:
                    result = np.concatenate((result,vector),axis=0)
                print(result.shape)
        resultdic[appid] = result
    torch.save(resultdic,'class_feature.pt')