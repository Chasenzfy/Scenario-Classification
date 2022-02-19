# -*- coding:utf8 -*-

import time
from appium import webdriver
import RSFile


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.rs.explorer.filemanager'
desired_caps['appActivity'] = 'com.edili.filemanager.MainActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(20)

rsfile = RSFile.RSFile(driver, screen_path, xml_path, jump_pairs, activity_info)
'''
# 点击进入Internal Storage
rsfile.my_enter_internal()
# test1 主界面的文件浏览
rsfile.file_browse_0(move_list=[1, -1, 2, -1, 5, 1, -1, 3, -1, -1, 3, 1, -1, 2, -1, -1])

# test2 设置 0-6-14
# 点击侧边栏
rsfile.sidebar_6()
# 设置
rsfile.settings_14()

# test3 主界面的新建文件夹 0-13-10 (大概有4个界面）
# 点击menu
rsfile.menu_13(pre_num=0)
# 新建文件夹失败
rsfile.new_folder_10(new_type=1)
# 点击menu
rsfile.menu_13(pre_num=0)
# 新建文件夹失败
rsfile.new_folder_10(new_type=2)

# test 4 主界面的文件搜索 0-3
# 文件搜索，点击取消文件搜索
rsfile.search_3()

# 搜索1
rsfile.search_3(text='1')
# 搜索123
rsfile.search_3(text='123')

# test 5 主界面的多文件 长按选中删除0-1-7，查看属性0-1-13-11，进行压缩0-1-13-2
# 长按选中：对主界面7个长按选中，然后取消，相当于没有选中
rsfile.long_click_1(sum=7)

# 长按选中两项，进行压缩
rsfile.long_click_1(sum=7, select_list=[2, 4])
# 测试删除
rsfile.delete_file_7(is_delete=True, is_success=False)

# 点击menu
rsfile.menu_13(pre_num=1)
# 查看属性
rsfile.properties_browse_11(select_nums=2)
# 点击menu
rsfile.menu_13(pre_num=1)
# 压缩取消
rsfile.compress_2()
# 长按选中3项，进行压缩
rsfile.long_click_1(sum=7, select_list=[2, 4, 6])
# 点击menu
rsfile.menu_13(pre_num=1)
# 查看属性
rsfile.properties_browse_11(select_nums=2)
# 点击menu
rsfile.menu_13(pre_num=1)
# zip压缩，但是最后取消压缩
rsfile.compress_2(name='compress', compress_type=1, compress_level=[1, 2, 4, 3], password='123', is_success=False)
# 长按选中3项，进行压缩
rsfile.long_click_1(sum=7, select_list=[2, 4, 6])
# 点击menu
rsfile.menu_13(pre_num=1)
# 7z压缩，但是最后取消压缩
rsfile.compress_2(name='compress', compress_type=2, password='123', is_success=False)

# test 6 主界面文件 测试删除0-1-7， 查看属性0-1-13-11，重命名 0-1-12
# 长按选中3项
rsfile.long_click_1(sum=7, select_list=[2, 4, 5])
# 测试删除
rsfile.delete_file_7(is_delete=True, is_success=False)

# 点击menu
rsfile.menu_13(pre_num=1)
# 查看属性
rsfile.properties_browse_11(select_nums=2)
# 以new name+number
rsfile.rename_12(rename_num=2, name='rename', is_success=False, start_number='1')
# 长按选中3项
rsfile.long_click_1(sum=7, select_list=[2, 4, 5])
# 以prefix + original
rsfile.rename_12(rename_num=2, name='rename', is_success=False, prefix='1')


# test 7 主界面 对5个文件夹 每个文件夹长按选中，分别查看属性、删除、待粘贴（copy to和move to）、重命名、失败压缩、添加bookmark
temp_list = [[3], [4], [5], [6], [7]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    rsfile.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    rsfile.properties_browse_11(select_nums=1)

    # 7 删除失败
    rsfile.delete_file_7(is_delete=True, is_success=False)

    print("开始了！")
    time.sleep(10)
    # 经常出现删除的时候，可能把长按选中的界面给取消，需要手动

    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 4 待粘贴 move to
    rsfile.to_paste_4(pre_num=3, is_paste=False, move_list=[3, 1, -1])

    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 4 待粘贴 copy to
    rsfile.to_paste_4(pre_num=4, is_paste=False, move_list=[3, 2, -1])

    # 12 重命名
    rsfile.rename_12(rename_num=1, name="rename"+str(i), is_success=False)

    # 1 长按选中：第一个123
    rsfile.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 2 失败压缩
    rsfile.compress_2()

    # 1 长按选中：第一个123
    rsfile.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 15 bookmarks
    rsfile.bookmarks_15(name="bookmarks"+str(i))

# 7、测试多项删除、查看属性
# 1 长按选中
rsfile.long_click_1(sum=8, select_list=[3, 4])
# 7 文件删除：0->1->7
rsfile.delete_file_7(is_delete=True, is_success=False)
# 13 menu
rsfile.menu_13(pre_num=1)
# 11 查看属性，0->1->13->11：查看文件123的属性
rsfile.properties_browse_11(select_nums=2)
# 4 待粘贴：点击copy
rsfile.to_paste_4(pre_num=1, is_paste=False, move_list=[3, 1, -1, 2, -1, -1])

# 1 长按选中
rsfile.long_click_1(sum=8, select_list=[3, 4, 5])
# 7 文件删除：0->1->7
rsfile.delete_file_7(is_delete=True, is_success=False)
# 13 menu
rsfile.menu_13(pre_num=1)
# 11 查看属性，0->1->13->11：查看文件123的属性
rsfile.properties_browse_11(select_nums=2)
# 4 待粘贴：点击cut
rsfile.to_paste_4(pre_num=1, is_paste=False, move_list=[4, -1, 5, 1, -1, 2, -1, -1])

# 1 长按选中
rsfile.long_click_1(sum=8, select_list=[3, 4, 5, 6])
# 7 文件删除：0->1->7
rsfile.delete_file_7(is_delete=True, is_success=False)
# 13 menu
rsfile.menu_13(pre_num=1)
# 11 查看属性，0->1->13->11：查看文件123的属性
rsfile.properties_browse_11(select_nums=2)
# 4 待粘贴：点击cut
rsfile.to_paste_4(pre_num=2, is_paste=False, move_list=[4, -1])

# test 8 测试音乐播放
# 进入文件夹123中，进行测试
rsfile.file_browse_0(move_list=[3])

# 测试音乐播放
rsfile.play_songs_5(song_index=5, playlist_name='myplay')

# test 9 新建文件,并且测试文本编辑
# 点击menu
rsfile.menu_13(pre_num=0)
# 新建文件txt
rsfile.new_folder_10(new_type=2, name='txt')

# 对txt进行编辑
rsfile.text_edit_9(text_index=6, encoding_list=[7, 3, 2, 4, 1, 2], text_input='add1')
# 对txt再次进行编辑
rsfile.text_edit_9(text_index=6, encoding_list=[6, 5, 2], text_input='add2')

# test 10 新建文件夹和文件
# 点击menu
rsfile.menu_13(pre_num=0)
# 新建文件夹
rsfile.new_folder_10(new_type=1, name='3')
# 进入文件夹1，新建5个文件
rsfile.file_browse_0(move_list=[1])
for i in range(7):
    rsfile.menu_13(pre_num=0)
    rsfile.new_folder_10(new_type=2, name="newfile"+str(i))
# 回到文件夹123下
rsfile.file_browse_0(move_list=[-1])

# test 11 在123文件夹下测试搜索
# 搜索2
rsfile.search_3(text='2')

# test 12 在123文件夹下测试 查看属性、重命名、失败压缩、添加bookmark、删除
temp_list = [[1], [2], [3], [4]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    rsfile.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 11 查看属性，0->1->13->11：查看文件123的属性
    rsfile.properties_browse_11(select_nums=1)

    # 7 删除失败
    rsfile.delete_file_7(is_delete=True, is_success=False)

    # 12 重命名
    rsfile.rename_12(rename_num=1, name="rename2"+str(i), is_success=False)

    # 1 长按选中：第一个123
    rsfile.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 2 失败压缩
    rsfile.compress_2()

    # 1 长按选中：第一个123
    rsfile.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    rsfile.menu_13(pre_num=1)
    # 15 bookmarks
    rsfile.bookmarks_15(name="bookmarks2"+str(i))

# test 13 测试剪切txt 到文件夹1 中
# 1 长按选中：第7个txt
rsfile.long_click_1(sum=8, select_list=[7])
# 4 待粘贴：点击cut
rsfile.to_paste_4(pre_num=2, is_paste=True, move_list=[3, -1, 2, -1, 1])
# 返回上一个目录
rsfile.file_browse_0([-1])

# test 14 删除 文件夹1
# 1 长按选中：第一个123
rsfile.long_click_1(sum=8, select_list=[1])
# 7 删除成功
rsfile.delete_file_7(is_delete=True, is_success=True)

# test 15 重命名文件夹2为1
# 1 长按选中文件夹3
rsfile.long_click_1(sum=8, select_list=[2])
# 12 重命名
rsfile.rename_12(rename_num=1, name="1", is_success=True)

# test 16 压缩 1.jpg
# 1 长按选中：1.jpg
rsfile.long_click_1(sum=8, select_list=[3])
# 13 menu
rsfile.menu_13(pre_num=1)
# 2 压缩成test1.7z
rsfile.compress_2(name='test1', compress_type=2, password='123', is_success=True)


# test 17 解压缩 test1.7z
# 1 长按选中
rsfile.long_click_1(sum=8, select_list=[6])
# 13 menu
rsfile.menu_13(pre_num=1)
# 2 解压失败
rsfile.decompress_8(is_success=False)
# 1 长按选中
rsfile.long_click_1(sum=8, select_list=[6])
# 13 menu
rsfile.menu_13(pre_num=1)
# 2 解压成功
rsfile.decompress_8(is_success=True, password='123')

# test 18 压缩 1.png
# 1 长按选中：1.jpg
rsfile.long_click_1(sum=8, select_list=[5])
# 13 menu
rsfile.menu_13(pre_num=1)
# 2 压缩
rsfile.compress_2(name='test2', compress_type=3, is_success=True)

# test 19 解压 test2.gz
# 1 长按选中 test2.gz
rsfile.long_click_1(sum=8, select_list=[8])
# 13 menu
rsfile.menu_13(pre_num=1)
# 2 解压成功
rsfile.decompress_8(is_success=True)

# test 20 测试bookmarks
# 点击侧边栏
rsfile.sidebar_6()

# 测试bookmarks
rsfile.bookmarks_15(index=1)
# 点击侧边栏
rsfile.sidebar_6()
'''
# 测试bookmarks
rsfile.bookmarks_15(index=2, new_name='new1')

# 最后一定要加入保存最后一个状态的图片的代码
rsfile.get_screen_info()


