# -*- coding:utf8 -*-

import time
from appium import webdriver
import File


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.alphainventor.filemanager'
desired_caps['appActivity'] = '.activity.MainActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(20)

file = File.File(driver, screen_path, xml_path, jump_pairs, activity_info)

# 点击进入Main Storage
file.my_enter_main_storage()

# test1 主界面的文件浏览
file.file_browse_0(move_list=[3, 2, -1, 3, -1, -1, 6, -1, 7, -1, 8, -1, 1, -1, 10, -1])

# test2 主界面的新建文件夹 0-13-10
# 点击menu
file.menu_13(pre_num=0)
# 新建文件夹失败
file.new_folder_10(new_type=1, name="111", is_success=False)
# 点击menu
file.menu_13(pre_num=0)
# 新建文件夹失败
file.new_folder_10(new_type=2, name='111', is_success=False)

# test 3 主界面的文件搜索 0-3
# 文件搜索，点击取消文件搜索
file.search_3()
# 搜索1
file.search_3(text='1', result_index=1)
# 123
file.search_3(text='123', result_index=1)
# 搜wein
file.search_3(text='weixin')
# 搜索test1
file.search_3(text='weixin')
# 搜索 D
file.search_3(text='D', result_index=1)


# test 4 主界面的多文件 长按选中删除0-1-7，进行压缩0-1-13-2
# 长按选中：对主界面7个长按选中，然后取消，相当于没有选中[1-9]
file.long_click_1(sum=6)

# 长按选中两项
file.long_click_1(sum=8, select_list=[8, 9, 8, 8])
# 测试删除
file.delete_file_7(is_delete=True, is_success=False)

# 长按选中两项
file.long_click_1(sum=7, select_list=[9, 8])
# 点击menu
file.menu_13(pre_num=1)
# 压缩取消
file.compress_2()

# 长按选中两项
file.long_click_1(sum=7, select_list=[9, 8])
# 点击rename
file.rename_12(name='r1', name2='r2')


temp_list = [[10, 9, 7], [9, 8, 7, 6], [10, 9], [9, 5], [9, 7]]
for i in range(len(temp_list)):
    # 长按选中3项
    file.long_click_1(sum=7, select_list=temp_list[i])
    # 测试删除
    file.delete_file_7(is_delete=True, is_success=False)

    # 长按选中3项
    file.long_click_1(sum=7, select_list=temp_list[i])
    # 点击menu
    file.menu_13(pre_num=1)
    # 压缩取消
    file.compress_2(name='fail'+str(i), is_success=False)

    # 长按选中3项
    file.long_click_1(sum=7, select_list=temp_list[i])
    # 点击menu
    file.menu_13(pre_num=1)
    # 查看属性
    file.properties_browse_11(index=2)

    # 长按选中3项
    file.long_click_1(sum=7, select_list=temp_list[i])
    # 点击rename
    file.rename_12(name='rename_fail'+str(i), name2='r2'+str(i))

# test 5 主界面的单文件 长按选中删除0-1-7，查看属性0-1-13-11，重命名 0-1-13-12
# 长按选中第10个文件夹
file.long_click_1(sum=7, select_list=[10, 9, 9])
# 点击menu
file.menu_13(pre_num=1)
# 查看属性
file.properties_browse_11(index=2)

# 长按选中第10个文件夹
file.long_click_1(sum=7, select_list=[10])
# 测试删除
file.delete_file_7(is_delete=False, is_success=False)

# 长按选中第10个文件夹
file.long_click_1(sum=7, select_list=[10])
# 重命名
file.rename_12()

# test 7 主界面 对5个文件夹 每个文件夹长按选中，分别查看属性、删除、重命名、失败压缩、待粘贴（copy to和move to）、添加bookmark
temp_list = [[1], [2], [3], [4], [5]]
for i in range(len(temp_list)):
    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    file.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    file.properties_browse_11(index=2)

    # 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 7 删除失败
    file.delete_file_7(is_delete=False, is_success=False)

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 重命名
    file.rename_12()

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    file.menu_13(pre_num=1)
    # 压缩取消
    file.compress_2()

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    file.menu_13(pre_num=1)
    # 添加bookmark
    file.bookmarks_15(pre_num=1)

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 4 copy
    file.to_paste_4(pre_num=1, is_paste=False, move_list=[])

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 4 cut
    file.to_paste_4(pre_num=2, is_paste=False, move_list=[temp_list[i][0], -1])


# 7、测试的剪切和移动
# 1 长按选中
file.long_click_1(sum=8, select_list=[9, 2])
# 4 copy
file.to_paste_4(pre_num=1, is_paste=False, move_list=[9, -1, 8, -1, 7, -1, 6, -1])
# 1 长按选中
file.long_click_1(sum=8, select_list=[3, 2])
# 4 cut
file.to_paste_4(pre_num=2, is_paste=False, move_list=[4, -1, 3, 2, -1, 3, -1, -1])


# test 8 测试音乐播放
# 进入文件夹123中，进行测试
file.file_browse_0(move_list=[1])

# 1 长按选中
file.long_click_1(sum=8, select_list=[4])
# 4 copy
file.to_paste_4(pre_num=1, is_paste=True, move_list=[])

# 1 长按选中
file.long_click_1(sum=8, select_list=[4])
# 重命名
file.rename_12(name='test1.mp3')

# 测试音乐播放
file.play_songs_5(song_location=4, index=1, pause_time=2)
file.play_songs_5(song_location=4, index=1, pause_time=5)
file.play_songs_5(song_location=5, index=1, pause_time=3)
file.play_songs_5(song_location=4, index=2, left_num=2, right_num=2, equalizer=True)
file.play_songs_5(song_location=5, index=2, left_num=3, right_num=4, equalizer=False)

# test 9 新建文件,并且测试文本编辑
# 点击menu
file.menu_13(pre_num=0)
# 新建文件txt
file.new_folder_10(new_type=2, name='temp2.txt', is_success=True)

# 对txt进行编辑
file.text_edit_9(text_index=3, is_clear=False, text_input="add1", save_index=1)
file.text_edit_9(text_index=3, is_clear=False, text_input="add2", save_index=2)
file.text_edit_9(text_index=3, is_clear=False, text_input="add3", save_index=2)
file.text_edit_9(text_index=3, is_clear=True, text_input="add4", save_index=1)

file.text_edit_9(text_index=4, is_clear=False, text_input="add1", save_index=2)
file.text_edit_9(text_index=4, is_clear=True, text_input="add2", save_index=1)
file.text_edit_9(text_index=4, is_clear=True, text_input="add3", save_index=1)


# test 10 新建文件夹
# 点击menu
file.menu_13(pre_num=0)
# 新建文件夹
file.new_folder_10(new_type=1, name='1', is_success=True)
# 点击menu
file.menu_13(pre_num=0)
# 新建文件夹
file.new_folder_10(new_type=1, name='2', is_success=True)

# 进入文件夹2，新建5个文件夹
file.file_browse_0(move_list=[2])
for i in range(5):
    file.menu_13(pre_num=0)
    file.new_folder_10(new_type=1, name="newfolder"+str(i), is_success=True)

# 回到文件夹123下
file.file_browse_0(move_list=[-1])

# test 11 在123文件夹下测试搜索
#文件搜索，点击取消文件搜索
file.search_3()
# 搜索1
file.search_3(text='1', result_index=1)
# jpg
file.search_3(text='jpg')
# t
file.search_3(text='t')
# temp
file.search_3(text='new')
# txt
file.search_3(text='txt')

# test 12 在123文件夹下测试 查看属性、重命名、删除
temp_list = [[3], [4], [5], [6], [7]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    file.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    file.properties_browse_11(index=1)

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    file.menu_13(pre_num=1)
    # 压缩取消
    file.compress_2()

    # 1 长按选中
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    file.menu_13(pre_num=1)
    # 添加bookmark
    file.bookmarks_15(pre_num=1)

# test 12 在文件夹2下测试 重命名
file.file_browse_0([2])

for i in range(5):
    # 1 长按选中：第一个123
    select_list = list()
    select_list.append(i+1)
    file.long_click_1(sum=8, select_list=select_list)
    # 12 重命名
    file.rename_12(name="n"+str(i))

# 返回上一个目录
file.file_browse_0([-1])
# test 13 测试剪切 到文件夹2的文件夹4中
# 1 长按选中
file.long_click_1(sum=8, select_list=[6])
# 4 待粘贴：点击cut
file.to_paste_4(pre_num=2, is_paste=True, move_list=[1, -1, 2, 1, -1, 3, -1, 4])
# 返回上一个目录
file.file_browse_0([-1, -1])

# test 14 压缩 1.jpg
# 1 长按选中：1.jpg
file.long_click_1(sum=8, select_list=[3])
# 13 menu
file.menu_13(pre_num=1)
# 2 压缩compress1
file.compress_2(is_success=True, name="compress1")


# test 17 解压缩 compress1.zip
# 1 长按选中
file.long_click_1(sum=8, select_list=[5])
# 13 menu
file.menu_13(pre_num=1)
# 2 解压失败
file.decompress_8(index=1)
# 1 长按选中
file.long_click_1(sum=8, select_list=[5])
# 13 menu
file.menu_13(pre_num=1)
# 2 解压成功
file.decompress_8(index=2)

# 1 长按选中
file.long_click_1(sum=8, select_list=[6])
# 13 menu
file.menu_13(pre_num=1)
# 2 解压成功第二个文件下的第5个文件夹
file.decompress_8(index=3, is_success=True, decopress_list=[3, 3, -1, -1, 1, 3, -1, 2, 1, -1, 3, -1, 5])

# test 18 压缩 1.png 1.jpg
# 1 长按选中：
file.long_click_1(sum=8, select_list=[4, 5])
# 13 menu
file.menu_13(pre_num=1)
# 2 压缩
file.compress_2(is_success=True, name='compress2')


# test 19 解压
# 1 长按选中
file.long_click_1(sum=8, select_list=[7])
# 13 menu
file.menu_13(pre_num=1)
# 2 解压成功
file.decompress_8(index=3, is_success=True, decopress_list=[2, -1, 7, -1, 6, -1, 1, 2, 5, -1, 3, -1, 4, -1, -1, 3, -1, 1])

# 删除 文件夹1, 2, 3, 6，7
# 1 长按选中 test2.gz
file.long_click_1(sum=8, select_list=[1, 2, 3, 6, 7])
# 7 删除
file.delete_file_7(is_delete=False, is_success=True)

# bookmarks: 前7个bookmark都重命名，然后删除
for i in range(7):
    file.sidebar_6()
    file.bookmarks_15(pre_num=2, bookmark_index=1, name='b'+str(i), is_remove=True)

file.sidebar_6()
file.bookmarks_15(pre_num=2, bookmark_index=1, is_remove=False)

# 设置
file.settings_14(built_list=[1, 2, 3, 2, 3, 1], storage_list=[1, 2, 4, 5, 6, 7, 3], advanced_list=[2, 3, 3, 2, 4, 4])

# 最后一定要加入保存最后一个状态的图片的代码
file.get_screen_info()


