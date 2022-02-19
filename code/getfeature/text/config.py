width = 1080
height = 1920
real_height = 1920
real_height_nostatus = 1920

parallel = False
threads = 5


MERGE_NEIGHBOUR = False                 #？
REMOVE_SINGLE_CHILD_CONTAINER = True    #删去冗余的container
only_double_containers = True           #接上一条，对于两个container嵌套，可选不删
REMOVE_SMALL_LEAF = True                #删去无子节点，长或宽小于10的
MERGE_IMAGE_AND_TEXT_LEAF = True        #？
REMOVE_EMPTY_CONTAINER = True           #删去冗余的container
REMOVE_NEST_CLICK = True                #不对重叠的多个记录click？
KEEP_ONLY_FOREGROUND = True             #只保留最上层
KEEP_ONLY_FOREGROUND_H = True           #只保留最上层
FRAME_LAYOUT_CHILD = True               #？
REMOVE_OVERLAPPING = True               #去除重叠的组件
REMOVE_BOTSLIDE_BACKGROUND = True       #？
REMOVE_ALPHA_OVERLAY = True             #？
MERGE_WEBVIEW_LABEL = False
CONVERT_WEBVIEW_CLASS = True            #将webview的类名转化
REMOVE_OUT_OF_SCREEN = True             #去掉bounds在屏幕外的组件
REMOVE_OVERLAP_OLD = True               #去除重叠的组件

ocr_resolution = 2073600

classify_use_bound = False
SCREEN_SCORE_BOUND = 10