# -*- coding:utf8 -*-

import time
from appium import webdriver
import File


# 配置信息
# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0.0'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'com.speedsoftware.explorer'
desired_caps['appActivity'] = '.Explorer'


desired_caps['noReset'] = False
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
time.sleep(1)
explore = File.File(driver, screen_path, xml_path, jump_pairs, activity_info)








explore.my_start()
# 0 文件浏览
explore.file_browse_0(move_list=[2, -1,
                                 3, -1,
                                 4,
                                 1 -1,
                                 2,-1,
                                 3,-1,
                                 4,-1,
                                 5,-1,
                                 -1,
                                 5, -1,
                                 6, -1,
                                 7, -1,
                                 8, -1,
                                 9, -1,
                                 10, -1,
                                 11,-1,
                                 12,-1])



# test 3.1、主界面的新建文件夹

# 10 新建文件夹(0-10),这里直接点击取消新建
explore.new_folder_10()

explore.new_folder_10(name="A", type=1, is_success=False)

explore.new_folder_10(name="AA", type=1, is_success=False)

explore.new_folder_10(name="AAA", type=1, is_success=False)

explore.new_folder_10(name="AAAA", type=1, is_success=False)

explore.new_folder_10(name="AAAAA", type=1, is_success=False)

explore.new_folder_10(name="AAAAAA", type=1, is_success=False)

explore.new_folder_10(name="AAAAAAA", type=1, is_success=False)

explore.new_folder_10(name="AAAAAAAA", type=1, is_success=False)

explore.new_folder_10(name="AAAAAAAAA", type=1, is_success=False)

# test 3.2、主界面的新建文件
explore.new_folder_10(name="A", type=0, is_success=False)

explore.new_folder_10(name="AA", type=0, is_success=False)

explore.new_folder_10(name="AAA", type=0, is_success=False)

explore.new_folder_10(name="AAAA", type=0, is_success=False)

explore.new_folder_10(name="AAAAA", type=0, is_success=False)

explore.new_folder_10(name="AAAAAA", type=0, is_success=False)

explore.new_folder_10(name="AAAAAAA", type=0, is_success=False)

explore.new_folder_10(name="AAAAAAAA", type=0, is_success=False)

explore.new_folder_10(name="AAAAAAAAA", type=0, is_success=False)


# test 4、主界面的文件搜索：0-6-3

# 6 sidebar
explore.sidebar_6()
# 3 文件搜索（0-13-3），这里点击取消文件搜索
explore.search_3()
# 13 menu

explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本
explore.search_3(text="1.jpg", is_success=False)
explore.my_back_home()
# 13 menu
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="123", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="1234", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="12345", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="123456", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="1234567", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="12345678", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="123456789", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="1231", is_success=False)
explore.my_back_home()
explore.sidebar_6()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
explore.search_3(text="123234", is_success=False)
explore.my_back_home()






# test 5、主界面的文件长按选中然后压缩
# 1 长按选中：对主界面8行长按选中，然后取消，相当于没有选中
explore.long_click_1(sum=5,select_list=[2,3])
# 13 menu
explore.menu_13()
# 2 压缩
explore.compress_2()

explore.menu_13()
# 2 压缩
explore.compress_2()

explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="1", is_success=False)


explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="2", is_success=False)

# 13 menu
explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="3", is_success=False)

# 13 menu
explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="4", is_success=False)

# 13 menu
explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="5", is_success=False)


explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="6", is_success=False)


explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="7", is_success=False)



explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="8", is_success=False)

# 13 menu
explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="9", is_success=False)

# 13 menu
explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="0", is_success=False)

explore.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="10", is_success=False)


explore.menu_13()

# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
explore.compress_2(num=4,name="11", is_success=False)




# test 6、
# 对前5个文件夹 每个文件夹长按选中，分别查看属性、重命名、删除
temp_list = [[2], [3], [4], [5], [6],[7],[8]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    explore.long_click_1(sum=11, select_list=temp_list[i])
    # 13 menu
    explore.menu_13()
    # 11 查看属性，0->1->13->11：查看文件123的属性
    explore.properties_browse_11()

    # 1 长按选中：第一个123
    explore.long_click_1(sum=11, select_list=temp_list[i])
    # 13 menu
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12()

    # 1 长按选中：第一个123
    explore.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="1" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="2" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="3" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="4" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="5" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="6" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="7" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="8" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    explore.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    explore.rename_12(name="9" + str(i), is_success=False)

    explore.long_click_1(sum=8, select_list=temp_list[i])
    # 7 文件删除：0->1->7
    explore.delete_file_7(is_success=False)





# 7、测试多项删除
# 1 长按选中
explore.long_click_1(sum=8, select_list=[2, 3])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()

explore.long_click_1(sum=8, select_list=[2, 3,4])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5,6])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5,6,7])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5,6,7,8])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5,6,7,8,9])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5,6,7,8,9,10])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()
explore.long_click_1(sum=8, select_list=[2, 3,4,5,6,7,8,9,10,11])
# 7 文件删除：0->1->7
explore.delete_file_7(is_success=False)
explore.my_back()


# 9、主界面的文件测试剪切粘贴和复制粘贴
# 测试剪切粘贴：
# 1 长按选中 第一个
explore.long_click_1(sum=8, select_list=[2])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()

explore.long_click_1(sum=8, select_list=[4])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()


explore.long_click_1(sum=8, select_list=[5])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()


explore.long_click_1(sum=8, select_list=[6])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()


explore.long_click_1(sum=8, select_list=[2,4])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()


explore.long_click_1(sum=8, select_list=[4,5])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()


explore.long_click_1(sum=8, select_list=[5,6])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()
explore.long_click_1(sum=8, select_list=[6,7])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()
explore.long_click_1(sum=8, select_list=[2,6])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()
explore.long_click_1(sum=8, select_list=[2,4,5,6])

# 4 待粘贴：点击剪切
explore.to_paste_4(pre_num=1, is_paste=False, move_list=[3])
# 回到主界面
explore.my_back_home()

# 测试 bookmarks
# 13 点击menu
explore.sidebar_6()
# 15 bookmarks:对已经添加的bookmark进行删除
explore.bookmarks_15()



# 13 点击menu
explore.my_back()



file.get_screen_info()
'''

explore.sidebar_6()
# 15 bookmarks:对已经添加的bookmark进行删除
explore.settings_14()
# 13 点击menu
explore.my_back()



explore.get_screen_info()




















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


'''