# -*- coding:utf8 -*-

import time
from appium import webdriver
import FX


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'nextapp.fx'
desired_caps['appActivity'] = '.ui.ExplorerActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(20)

fx = FX.FX(driver, screen_path, xml_path, jump_pairs, activity_info)


# 点击进入Main Storage
fx.my_enter_main_storage()

# test1 主界面的文件浏览
fx.file_browse_0(move_list=[2, -1, 3, 1, -1, 2, -1, 3, -1, -1, 10, -1, 11, -1, 1, 1, -1, 3, -1, -1])

# test2 主界面的新建文件夹 0-13-10 (大概有7个界面）
# 点击menu
fx.menu_13(pre_num=0)
# 新建文件夹失败
fx.new_folder_10(new_type=1)
# 点击menu
fx.menu_13(pre_num=0)
# 新建文件夹失败
fx.new_folder_10(new_type=2, type_list=[5, 4, 3, 2, 1, 2, 3, 4])

# test 3 主界面的文件搜索 0-3
# 文件搜索，点击取消文件搜索
fx.search_3()

# 搜索111
fx.search_3(text='111', include_system_file=True, close_location=True)
# 先搜索文件夹中的1，然后搜索test【搜索的是Folder】
fx.search_3(text='1', include_system_file=True, close_location=False, kind_index=2, new_text='test')
# 搜1，然后搜索2,搜索的是image
fx.search_3(text='1', include_system_file=False, close_location=False, kind_index=6, new_text='2')
# 搜索weixin, 然后搜索 test1，搜索类型是ALL
fx.search_3(text='weixin', include_system_file=True, close_location=False, kind_index=1, new_text='test1')

# test 4 主界面的多文件 长按选中删除0-1-7，进行压缩0-1-13-2
# 长按选中：对主界面7个长按选中，然后取消，相当于没有选中
fx.long_click_1(sum=5)

# 长按选中两项
fx.long_click_1(sum=7, select_list=[9, 10])
# 测试删除
fx.delete_file_7(is_success=False)

# 长按选中两项
fx.long_click_1(sum=7, select_list=[9, 10])
# 点击menu
fx.menu_13(pre_num=1)
# 压缩取消
fx.compress_2(is_success=False)

# 长按选中3项
fx.long_click_1(sum=7, select_list=[10, 9, 11])
# 测试删除
fx.delete_file_7(is_success=False)

# 长按选中3项
fx.long_click_1(sum=7, select_list=[10, 9, 11])
# 点击menu
fx.menu_13(pre_num=1)
# 压缩取消
fx.compress_2(is_success=False)

# 长按选中3项
fx.long_click_1(sum=7, select_list=[9, 1, 2, 4])
# 测试删除
fx.delete_file_7(is_success=False)

# 长按选中4
fx.long_click_1(sum=7, select_list=[9, 1, 2, 4])
# 点击menu
fx.menu_13(pre_num=1)
# 压缩取消
fx.compress_2(is_success=False)

# test 5 主界面的单文件 长按选中删除0-1-7，查看属性0-1-13-11，重命名 0-1-13-12
# 长按选中第10个文件夹
fx.long_click_1(sum=7, select_list=[9, 10, 9])
# 点击menu
fx.menu_13(pre_num=1)
# 查看属性
fx.properties_browse_11(index=3)

# 长按选中第10个文件夹
fx.long_click_1(sum=7, select_list=[10])
# 测试删除
fx.delete_file_7(is_success=False)

# 长按选中第10个文件夹
fx.long_click_1(sum=7, select_list=[10])
# 点击menu
fx.menu_13(pre_num=1)
# 重命名
fx.rename_12()

# test 7 主界面 对7个文件夹 每个文件夹长按选中，分别查看属性、删除、重命名、失败压缩、待粘贴（copy to和move to）、添加bookmark
temp_list = [[1], [3], [4], [7], [8], [5], [9]]
for i in range(len(temp_list)):
    # 1 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    fx.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    fx.properties_browse_11(index=3)

    # 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 7 删除失败
    fx.delete_file_7(is_success=False)

    # 1 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    fx.menu_13(pre_num=1)
    # 重命名
    fx.rename_12()

    # 1 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    fx.menu_13(pre_num=1)
    # 压缩取消
    fx.compress_2(is_success=False)

    # 1 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    fx.menu_13(pre_num=1)
    # 添加bookmark
    fx.bookmarks_15(pre_num=1, bookmark_name='bookmark'+str(i), icon_index=i+1, icon_label='icon'+str(i), location_index=1)

    # 1 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 4 copy
    fx.to_paste_4(pre_num=1, is_paste=False, move_list=[])

    # 1 长按选中
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 4 cut
    fx.to_paste_4(pre_num=2, is_paste=False, move_list=[temp_list[i][0], -1])


# 7、测试的剪切和移动
# 1 长按选中
fx.long_click_1(sum=8, select_list=[3, 10, 2, 4, 5])
# 4 copy
fx.to_paste_4(pre_num=1, is_paste=False, move_list=[7, -1, 3, 1, -1, 2, -1, 3, -1, -1, 1, 1, -1, -1])
# 1 长按选中
fx.long_click_1(sum=8, select_list=[3, 2])
# 4 cut
fx.to_paste_4(pre_num=2, is_paste=False, move_list=[1, 2, -1, 3, -1, -1])


# test 8 测试音乐播放
# 进入文件夹123中，进行测试
fx.file_browse_0(move_list=[1])

# 测试音乐播放
fx.play_songs_5(song_location=7, index=1, pause_time=2)
fx.play_songs_5(song_location=7, index=1, pause_time=10)

fx.play_songs_5(song_location=7, index=2)


# test 9 新建文件,并且测试文本编辑
# 点击menu
fx.menu_13(pre_num=0)
# 新建文件txt
fx.new_folder_10(new_type=2, name='temp', type_list=[1, 3, 4, 2])

# 对txt进行编辑
fx.text_edit_9(text_index=7, text_input='abcdef', colors=[8, 5, 2, 4, 6, 7, 3])

# test 10 新建文件夹
# 点击menu
fx.menu_13(pre_num=0)
# 新建文件夹
fx.new_folder_10(new_type=1, name='3')
# 进入文件夹test1，新建5个文件夹
fx.file_browse_0(move_list=[4])
for i in range(5):
    fx.menu_13(pre_num=0)
    fx.new_folder_10(new_type=1, name="newfolder"+str(i))
# 回到文件夹123下
fx.file_browse_0(move_list=[-1])

# test 11 在123文件夹下测试搜索
# 搜索2
# 先搜索文件夹中的te，然后搜索1
fx.search_3(text='te', include_system_file=True, close_location=False, kind_index=2, new_text='1')
# 搜mp3，然后搜索mp4
fx.search_3(text='mp3', include_system_file=False, close_location=False, kind_index=7, new_text='mp4')
# 搜索1, 然后搜索 png
fx.search_3(text='1', include_system_file=True, close_location=False, kind_index=1, new_text='png')

# test 12 在123文件夹下测试 查看属性、重命名、删除
temp_list = [[5], [6], [8]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    fx.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    if i == 0:
        fx.properties_browse_11(index=3)
    elif i == 1:
        fx.properties_browse_11(index=1)
    else:
        fx.properties_browse_11(index=2)

    # 1 长按选中：第一个123
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 7 删除失败
    fx.delete_file_7(is_success=False)

    # 1 长按选中：第一个123
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    fx.menu_13(pre_num=1)
    # 12 重命名
    fx.rename_12()

# test 12 在123文件夹下测试 重命名
temp_list = [[1], [1], [1], [1], [1]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    fx.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    fx.menu_13(pre_num=1)
    # 12 重命名
    fx.rename_12(name="zzzzzzzz"+str(i))

# test 13 添加bookmaks
# 点击menu
fx.menu_13(pre_num=0)
# 添加bookmark
fx.bookmarks_15(pre_num=2, group_name='g1', bookmark_name='b1', icon_index=10, icon_label='b1', location_index=3)

# test 13 测试剪切png 到文件夹2 中
# 1 长按选中：第7个png
fx.long_click_1(sum=8, select_list=[7])
# 4 待粘贴：点击cut
fx.to_paste_4(pre_num=2, is_paste=True, move_list=[1, -1, 2])
# 返回上一个目录
fx.file_browse_0([-1])

# test 14 压缩 1.jpg
# 1 长按选中：1.jpg
fx.long_click_1(sum=8, select_list=[6])
# 13 menu
fx.menu_13(pre_num=1)
# 2 压缩1.jpg.zip
fx.compress_2(is_success=True, compress_type=[3, 2, 1], password=None)


# test 17 解压缩 1.jpg.zip
# 1 长按选中
fx.long_click_1(sum=8, select_list=[7])
# 13 menu
fx.menu_13(pre_num=1)
# 2 解压失败
fx.decompress_8(is_success=False)
# 1 长按选中
fx.long_click_1(sum=8, select_list=[7])
# 13 menu
fx.menu_13(pre_num=1)
# 2 解压到zzzzz2 成功
fx.decompress_8(is_success=True, decopress_list=[2, -1, -1, 1, 3])

# test 18 压缩 1.png temp.txt
# 1 长按选中：
fx.long_click_1(sum=8, select_list=[6, 8])
# 13 menu
fx.menu_13(pre_num=1)
# 2 压缩
fx.compress_2(is_success=True, compress_type=[2, 5, 3], password=None)


# test 19 解压 Archive.tar.gz
# 1 长按选中
fx.long_click_1(sum=8, select_list=[8])
# 13 menu
fx.menu_13(pre_num=1)
# 2 解压成功在第4个文件夹下的文件夹3
fx.decompress_8(is_success=True, decopress_list=[3, -1, 5, -1, 1, -1, 4, 5, -1, 2, -1, 3])


# test 20 压缩 1.jpg
# 1 长按选中：1.jpg
fx.long_click_1(sum=8, select_list=[6])
# 13 menu
fx.menu_13(pre_num=1)
# 2 压缩1.jpg.tar.bz2
fx.compress_2(is_success=True, compress_type=[4], password=None)

# test 19 解压 1.jpg.tar.bz2
# 1 长按选中 1.jpg.tar.bz2
fx.long_click_1(sum=8, select_list=[7])
# 13 menu
fx.menu_13(pre_num=1)
# 2 解压成功在zzzzzz1
fx.decompress_8(is_success=True, decopress_list=[-1, 1, 3, -1, 2])

# 删除 文件夹1, 2, 3, 4, 5，7，8, 9
# 1 长按选中 test2.gz
fx.long_click_1(sum=8, select_list=[1, 2, 3, 4, 5, 7, 8, 9])

# 7 删除
fx.delete_file_7(is_success=True)


# 设置
fx.sidebar_6()
fx.settings_14(style_list=[10, 7, 6, 1, 2], dynamic_material=[4, 2, 1], shape=[3, 4, 1], file_checkbox=[1, 2])


# 最后一定要加入保存最后一个状态的图片的代码
fx.get_screen_info()


