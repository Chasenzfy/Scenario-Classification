# -*- coding:utf8 -*-

import time
from appium import webdriver
import ES


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.estrongs.android.pop'
desired_caps['appActivity'] = '.app.openscreenad.NewSplashActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(20)

es = ES.ES(driver, screen_path, xml_path, jump_pairs, activity_info)
'''
# 点击进入Internal Storage
es.my_enter_internal()
# test1 主界面的文件浏览
es.file_browse_0(move_list=[1, 1, -1, 2, -1, 3, -1, -1, 8, -1, 11, -1, 3, 1, -1, 3, -1, -1])

# test2 主界面的新建文件夹 0-13-10 (大概有4个界面）
# 点击menu
es.menu_13(pre_num=0)
# 新建folder失败
es.new_folder_10(new_type=1)
# 点击menu
es.menu_13(pre_num=0)
# 新建word失败
es.new_folder_10(new_type=2)
# 点击menu
es.menu_13(pre_num=0)
# 新建file失败
es.new_folder_10(new_type=5)


# test 4 主界面的文件搜索 0-3
# 文件搜索，点击取消文件搜索
es.search_3()
# 搜索1
es.search_3(text="1", menu_list=[1, 2])
# A
es.search_3(text='A', menu_list=[3, 4])
# 搜1.
es.search_3(text="1.", menu_list=[1, 5])


# test 4 主界面的多文件 长按选中删除0-1-7，进行压缩0-1-13-2
# 长按选中：对主界面7个长按选中，然后取消，相当于没有选中[1-9]
es.long_click_1(sum=5)

# 长按选中两项
es.long_click_1(sum=8, select_list=[7, 8, 7, 8, 7])
# 测试删除
es.delete_file_7(is_delete=True, is_success=False)

# 长按选中两项
es.long_click_1(sum=7, select_list=[8, 7])
# 点击menu
es.menu_13(pre_num=1)
# 压缩取消
es.compress_2()

# 长按选中两项
es.long_click_1(sum=7, select_list=[9, 8])
# 点击rename,取消重命名
es.rename_12(rename_num=2, name='r1', is_success=False, prefix='r2')


temp_list = [[2, 3, 4], [2, 4, 5], [3, 4], [3, 6], [2, 4]]
for i in range(len(temp_list)):
    # 长按选中3项
    es.long_click_1(sum=7, select_list=temp_list[i])
    # 测试删除
    es.delete_file_7(is_delete=True, is_success=False)

    # 点击menu
    es.menu_13(pre_num=1)
    # 查看属性
    es.properties_browse_11(select_nums=2)

    # rename
    es.rename_12(rename_num=2, name='fail'+str(i), is_success=False, start_number=str(i))

# test 7 主界面 对5个文件夹 每个文件夹长按选中，分别查看属性、删除、重命名、失败压缩、待粘贴（copy to和move to）、添加bookmark
temp_list = [[1, 2, 2], [2], [3], [4], [5]]
for i in range(len(temp_list)):
    # 1 长按选中
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    es.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    es.properties_browse_11(select_nums=2)

    # 删除失败
    es.delete_file_7(is_delete=True, is_success=False)

    # 13 menu
    es.menu_13(pre_num=1)
    # 压缩取消
    es.compress_2()

    # 1 长按选中
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 重命名
    es.rename_12(rename_num=1, name='name-test'+str(i), is_success=False)

    # 1 长按选中
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    es.menu_13(pre_num=1)
    # 添加bookmark
    es.bookmarks_15(pre_num=1, name="bookmarks"+str(i))

    # 1 长按选中
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 4 copy
    es.to_paste_4(pre_num=1, is_paste=False, move_list=[])

    # 1 长按选中
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 4 cut
    es.to_paste_4(pre_num=2, is_paste=False, move_list=[temp_list[i][0], -1])



# 7、测试的剪切和移动
# 1 长按选中
es.long_click_1(sum=8, select_list=[2, 7, 9, 4])
# 4 copy
es.to_paste_4(pre_num=1, is_paste=False, move_list=[1, 2, -1, 3, -1, -1, 3, 1, -1, 2, -1, -1, 1])

# test 8 测试音乐播放
# 进入文件夹123中，进行测试
es.file_browse_0(move_list=[-1, 1])

# 测试音乐播放
es.play_songs_5(song_index=6, playlist_name="playlist1", new_name='new1')
es.play_songs_5(song_index=7, playlist_name="playlist2", new_name='new2')


# test 9 新建文件,并且测试文本编辑
# 点击menu
es.menu_13(pre_num=0)
# 新建文件
es.new_folder_10(new_type=5, name='file1')

# 对txt进行编辑
es.text_edit_9(text_index=6, is_clear=False, start=2, text_input='first input', is_undo=True, save_index=1, new_text="add first")

# 再次进行编辑
es.text_edit_9(text_index=6, is_clear=False, start=3, text_input='second input', is_undo=True, save_index=2, line_num=4, new_text="add second")
# 再次编辑
es.text_edit_9(text_index=6, is_clear=True, start=1, text_input='third input', is_undo=False, save_index=1)
# 再次编辑
es.text_edit_9(text_index=6, is_clear=True, start=2, text_input='forth input', is_undo=True, save_index=2, new_text="add forth")


# test 10 新建文件夹
# 点击menu
es.menu_13(pre_num=0)
# 新建文件夹
es.new_folder_10(new_type=1, name='t1')
# 点击menu
es.menu_13(pre_num=0)
# 新建文件夹
es.new_folder_10(new_type=1, name='t2')
# 点击menu
es.menu_13(pre_num=0)
# 新建文件夹
es.new_folder_10(new_type=1, name='t3')

# 进入文件夹t1，新建5个文件夹
es.file_browse_0(move_list=[1])
for i in range(5):
    es.menu_13(pre_num=0)
    es.new_folder_10(new_type=1, name="newfolder"+str(i))

# 回到文件夹123下的第二个文件夹t2下， 新建5个文件
es.file_browse_0(move_list=[-1, 2])
for i in range(5):
    es.menu_13(pre_num=0)
    es.new_folder_10(new_type=i+1, name="new"+str(i))

# 在该文件夹下测试搜索
es.search_3()
es.search_3(text="new", menu_list=[2, 3, 5])

# 回到文件夹123下
es.file_browse_0([-1])

# test 11 在123文件夹下测试搜索
# 文件搜索，点击取消文件搜索
es.search_3()
# 搜索1
es.search_3(text="t", menu_list=[1, 2, 5])
# A
es.search_3(text='v', menu_list=[1, 2, 5])
# 搜1.
es.search_3(text="1.", menu_list=[2, 3])


# test 10 新建文件夹
# 点击menu
es.menu_13(pre_num=0)
# 新建文件夹
es.new_folder_10(new_type=1, name='t4')
# 点击menu
es.menu_13(pre_num=0)
# 新建文件夹
es.new_folder_10(new_type=1, name='t5')
# 点击menu
es.menu_13(pre_num=0)
# 新建文件夹
es.new_folder_10(new_type=1, name='t6')

# test 12 在123文件夹下测试 查看属性、重命名、删除
temp_list = [[12], [7], [8], [9], [10]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    es.menu_13(pre_num=1)
    # 11 查看属性
    es.properties_browse_11(select_nums=1)

    # 点击menu
    es.menu_13(pre_num=1)
    # 压缩取消
    es.compress_2()

    # 1 长按选中
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 点击menu
    es.menu_13(pre_num=1)
    # 添加bookmark
    es.bookmarks_15(pre_num=1, name="bookmark"+str(i))

# test 12 在文件夹1下测试 重命名
es.file_browse_0([1])

for i in range(5):
    es.long_click_1(sum=8, select_list=[1])
    # 12 重命名
    es.rename_12(rename_num=1, name="z"+str(i), is_success=True)

# 返回上一个目录
es.file_browse_0([-1])

# 重命名t1, t2为 rename
es.long_click_1(sum=8, select_list=[1, 2])
# 重命名
es.rename_12(rename_num=2, name="rename", is_success=True, start_number="1")


# 对t3，t4, t5, t6查看属性和删除
# temp_list = [[3], [4], [3], [3]]
temp_list = [[3], [3], [3], [3]]
for i in range(len(temp_list)):
    es.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    es.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    es.properties_browse_11(select_nums=2)

    # 删除
    es.delete_file_7(is_delete=True, is_success=True)


# test 13 测试拷贝 到文件夹2的文件夹new0中
# 1 长按选中
es.long_click_1(sum=8, select_list=[3])
# 4 待粘贴：点击copy
es.to_paste_4(pre_num=1, is_paste=True, move_list=[-1, 15, 1, 1, -1, -1, 3, -1, -1, 1, 2, 1])
# 返回上一个目录
es.file_browse_0([-1, -1])

# 1 长按选中
es.long_click_1(sum=8, select_list=[4])
# 点击menu
es.menu_13(pre_num=1)
# 4 待粘贴：点击copy to rename1中的z0
es.to_paste_4(pre_num=4, is_paste=True, move_list=[-1, 2, 3, 1, -1, 2, -1, -1, 1, 1, 1])


# 长按
es.long_click_1(sum=4)

# test 14 压缩 1.jpg
# 1 长按选中：1.jpg
es.long_click_1(sum=8, select_list=[3])
# 13 menu
es.menu_13(pre_num=1)
# 2 压缩compress1.zip, 然后失败
es.compress_2(name="compress1", compress_type=1, compress_level=[1, 2, 3, 4], password="111", is_success=False)


# test 14 压缩 1.jpg
# 1 长按选中：1.jpg
es.long_click_1(sum=8, select_list=[3])
# 13 menu
es.menu_13(pre_num=1)
# 2 压缩compress1.7z, 然后成功
es.compress_2(name="compress1", compress_type=2, password="123", is_success=True)
'''

# test 14 压缩 1.png
# 1 长按选中：1.png
es.long_click_1(sum=8, select_list=[4])
# 13 menu
es.menu_13(pre_num=1)
# 2 压缩compress2.zip, 然后成功
es.compress_2(name="compress2", compress_type=1, compress_level=[1, 3], is_success=True)

# test 14 压缩 file1
# 1 长按选中：file1
es.long_click_1(sum=8, select_list=[7])
# 13 menu
es.menu_13(pre_num=1)
# 2 压缩compress2.zip, 然后成功
es.compress_2(name="compress3", compress_type=3, is_success=True)


# test 17 解压缩 compress1.7z
# 1 长按选中
es.long_click_1(sum=8, select_list=[5])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压失败
es.decompress_8(is_success=False)

# 1 长按选中
es.long_click_1(sum=8, select_list=[5])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压成功
es.decompress_8(is_success=True, index=1, encoding_list=[10, 8, 6, 4, 2, 1], password='123')


# 1 长按选中 compress2.zip
es.long_click_1(sum=8, select_list=[7])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压失败
es.decompress_8(is_success=False)

# 1 长按选中 compress2.zip
es.long_click_1(sum=8, select_list=[7])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压成功第二个文件下的第3个文件夹
es.decompress_8(is_success=True, index=2, path_list=[3, 1, -1, -1, 1, 1, -1, 2, 1, -1, 2, -1, 3], encoding_list=[3, 1])

# 1 长按选中 compress3.zip
es.long_click_1(sum=8, select_list=[8])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压失败
es.decompress_8(is_success=False)


# 1 长按选中 compress3.zip
es.long_click_1(sum=8, select_list=[8])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压成功
es.decompress_8(is_success=True, index=1, encoding_list=[9, 7, 6, 5, 3, 4, 1])


# 1 长按选中 compress2.zip
es.long_click_1(sum=8, select_list=[8])
# 13 menu
es.menu_13(pre_num=1)
# 2 解压成功
es.decompress_8(is_success=True, index=1, encoding_list=[2, 1])


# 删除 文件夹1, 2, 3, 4, 5,
# 1 长按选中 test2.gz
es.long_click_1(sum=8, select_list=[1, 2, 3, 4, 5])
# 7 删除
es.delete_file_7(is_delete=False, is_success=True)

# 删除 文件夹3,4,5,6
# 1 长按选中 test2.gz
es.long_click_1(sum=8, select_list=[3, 4, 5, 6])
# 7 删除
es.delete_file_7(is_delete=False, is_success=True)

# 新建三个文件夹
for i in range(3):
    es.menu_13(pre_num=0)
    es.new_folder_10(new_type=1, name='t'+str(i+1))
# bookmarks:
for i in range(2):
    es.sidebar_6()
    es.bookmarks_15(pre_num=2, name='name'+str(i), path='path'+str(i))

es.sidebar_6()
# 设置
es.settings_14(display_list=[1, 2, 3, 5, 7, 8, 1, 3, 5, 7, 8, 2], notification_list=[3, 2, 2, 3, 1, 1, 4, 4, 5, 1, 5, 1])
# 最后一定要加入保存最后一个状态的图片的代码
es.get_screen_info()


