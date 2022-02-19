# -*- coding:utf8 -*-

import time
from appium import webdriver
import File


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0.0'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'fm.clean'
desired_caps['appActivity'] = 'fm.clean.MainActivity'
desired_caps['noReset'] = False
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
time.sleep(1)

file = File.File(driver, screen_path, xml_path, jump_pairs, activity_info)

file.my_back_home()

# 0 文件浏览
file.file_browse_0(move_list=[0, -1, 1, -1, 2, 0, -1, 1, -1, 2, -1, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1])


# test 2、主界面的设置
# 13 menu
# test 3、主界面的新建文件夹
# 10 新建文件夹(0-13-10),这里直接点击取消新建
file.new_folder_10()
file.new_folder_10(folder_name="Test1", is_success=False)
file.new_folder_10(folder_name="Test2", is_success=False)
file.new_folder_10(folder_name="Test3", is_success=False)
file.new_folder_10(folder_name="Test4", is_success=False)
file.new_folder_10(folder_name="Test5", is_success=False)
file.new_folder_10(folder_name="Test6", is_success=False)
file.new_folder_10(folder_name="Test7", is_success=False)
file.new_folder_10(folder_name="Test8", is_success=False)
file.new_folder_10(folder_name="Test234", is_success=False)
file.new_folder_10(folder_name="234t", is_success=False)
file.new_folder_10(folder_name="Tafat", is_success=False)
file.new_folder_10(folder_name="Teswear2t", is_success=False)
file.new_folder_10(folder_name="Tesad", is_success=False)
file.new_folder_10(folder_name="Teafgas3t12", is_success=False)




# test 4、主界面的文件搜索：0-13-3
file.search_3()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后回到搜索前的主界面【需要在一开始设置允许录音】
file.search_3(text="1.jpg", sucess="sucess")
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
file.search_3(text="123sda")
file.search_3(text="12sa3")
file.search_3(text="1fe23", sucess="sucess")
file.search_3(text="e3")
file.search_3(text="1232asdsa3")
file.search_3(text="12qasd a3")
file.search_3(text="12da3.zip")
file.search_3(text="1qw1223", sucess="sucess")
file.search_3(text="3ds21")
file.search_3(text="134das3")
file.search_3(text="1haha", sucess="sucess")
file.search_3(text="为")




# 1 长按选中：对主界面8行长按选中，然后取消，相当于没有选中
file.long_click_1(sum=9)
file.long_click_1(sum=9, select_list=[0, 1, 2])
file.my_back()
file.long_click_1(sum=9, select_list=[0, 2, 4])
file.my_back()
file.long_click_1(sum=9, select_list=[1, 2, 4, 5])
file.my_back()
file.long_click_1(sum=9, select_list=[2, 6, 7, 8])
file.my_back()
file.long_click_1(sum=9, select_list=[3, 4, 5, 7])
file.my_back()
file.long_click_1(sum=9, select_list=[8, 6, 3, 4, 5, 1, 2])
file.my_back()
file.long_click_1(sum=9, select_list=[1, 2, 3, 0, 6, 5])
file.my_back()
file.long_click_1(sum=9, select_list=[1, 2, 3, 6, 7, 8])
file.my_back()


#压缩
# 1 长按选中：对主界面的第1，3，4行长按选中
file.long_click_1(sum=9, select_list=[1, 3, 4])
# 13 menu
file.menu_13()
# 2 压缩
file.compress_2()
# 1 长按选中：对主界面的第1，3，4行选中
file.my_back()

file.long_click_1(sum=9, select_list=[1, 3])
# 13 menu
file.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
file.compress_2(name="afasf", is_success=False)
file.my_back()

file.file_browse_0([0])

file.long_click_1(sum=9, select_list=[1, 3])
# 13 menu
file.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
file.compress_2(name="tesad", is_success=False)
file.menu_13()
file.compress_2(name="gt34", is_success=False)
file.menu_13()
file.compress_2(name="af", is_success=False)
file.menu_13()
file.compress_2(name="萨顶顶", is_success=False)
file.my_back()
file.my_back()

# test 6、
# 对前5个文件夹 每个文件夹长按选中，分别查看属性、重命名、失败压缩、添加bookmark、删除
temp_list = [[0],[1], [2], [3], [4], [5],[6],[7],[8]]

for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    file.long_click_1(sum=9, select_list=temp_list[i])
    # 13 menu
    file.menu_13()
    # 11 查看属性，0->1->13->11：查看文件123的属性
    file.properties_browse_11()

    # 1 长按选中：第一个123
    file.long_click_1(sum=9, select_list=temp_list[i])
    # 12 重命名：0->1->13->12：点击后退出
    file.rename_12()

    # 1 长按选中：第一个123
    file.long_click_1(sum=9, select_list=temp_list[i])
    # 12 重命名：0->1->13->12：点击后退出
    file.rename_12(name="rename" + str(i), is_success=False)

    # 1 长按选中：第一个123
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    file.menu_13()
    # 2 压缩:0->1->13->2
    file.compress_2(name="compress" + str(i), is_success=False)
    file.my_back()
    # 1 长按选中：第一个123
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 7 文件删除：0->1->7
    file.delete_file_7(is_success=False)
    file.my_back()

temp_list = [[0], [1], [2], [3], [4]]
for i in range(len(temp_list)):
    file.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    file.menu_13()
    # 15 bookmarks:添加bookmark 0->1->13-15
    file.bookmarks_15()


# 7、测试多项删除


file.long_click_1(sum=8, select_list=[0])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
# 1 长按选中
file.long_click_1(sum=8, select_list=[1, 2])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
# 1 长按选中
file.long_click_1(sum=8, select_list=[1, 2, 3])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
# 1 长按选中
file.long_click_1(sum=8, select_list=[1, 2, 3, 4])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6, 7])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6, 7, 8])
# 7 文件删除：0->1->7
file.delete_file_7(is_success=False)
file.my_back()


# 9、主界面的文件测试剪切粘贴和复制粘贴
# 测试剪切粘贴：
# 1 长按选中 第一个
file.long_click_1(sum=9, select_list=[8])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[0],flag=1)

file.long_click_1(sum=9, select_list=[0])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[-1])

file.long_click_1(sum=9, select_list=[1, 3])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[0])

file.long_click_1(sum=9, select_list=[0, 1])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[-1])

file.long_click_1(sum=9, select_list=[1, 3, 5])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[0])

file.long_click_1(sum=9, select_list=[0, 1, 2])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[-1])

file.long_click_1(sum=9, select_list=[1, 3, 5, 7])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[0])

file.long_click_1(sum=9, select_list=[0, 1, 2, 3])
# 4 待粘贴：点击剪切
file.menu_13()
file.to_paste_4(pre_num=1, is_paste=False, move_list=[-1])


file.long_click_1(sum=8, select_list=[1, 2])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[1, 2])
file.menu_13()
file.compress_2()
file.my_back()


# 1 长按选中
file.long_click_1(sum=8, select_list=[1, 2, 3])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[1, 2, 3])
file.menu_13()
file.compress_2()
file.my_back()

file.long_click_1(sum=8, select_list=[1, 2, 3, 4])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[1, 2, 3, 4])
file.menu_13()
file.compress_2()
file.my_back()

file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4])
file.menu_13()
file.compress_2()
file.my_back()

file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5])
file.menu_13()
file.compress_2()
file.my_back()

file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6])
file.menu_13()
file.compress_2()
file.my_back()

file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6, 7])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6, 7])
file.menu_13()
file.compress_2()
file.my_back()

file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6, 7, 8])
file.menu_13()
file.properties_browse_11()
file.long_click_1(sum=8, select_list=[0, 1, 2, 3, 4, 5, 6, 7, 8])
file.menu_13()
file.compress_2()
file.my_back()



# 14 setting test

file.menu_13()
# file.settings_14()
file.settings_14_plus()
file.get_screen_info()
