# -*- coding:utf8 -*-

import time
from appium import webdriver
import OIFM

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'org.openintents.filemanager'
desired_caps['appActivity'] = '.FileManagerActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = 'jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(10)

oifm = OIFM.MyOIFM(driver, screen_path, xml_path, jump_pairs, activity_info)

# 需要提前开启录音的权限，
# test 1、主界面的文件浏览
# 回到主界面
oifm.my_back_home()
# 0 文件浏览
oifm.file_browse_0(move_list=[1, 1, -1, 2, -1, -1, 3, 1, -1, 2, -1, -1, 6, -1, 8, -1])
# 回到主界面
oifm.my_back_home()

# test 2、主界面的设置
# 13 menu
oifm.menu_13()
# 14 设置 (0-13-14)
oifm.settings_14(sort_list=[1, 0, 2, 0, 3, 1], checkbox_list=[0, 1, 1, 3, 4, 3, 4, 0, 5, 5], is_clear=True)

# test 3、主界面的新建文件夹
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10),这里直接点击取消新建
oifm.new_folder_10()
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
oifm.new_folder_10(folder_name="Test1", is_success=False)
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
oifm.new_folder_10(folder_name="Test2", is_success=False)
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
oifm.new_folder_10(folder_name="Test3", is_success=False)
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
oifm.new_folder_10(folder_name="Test5", is_success=False)
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
oifm.new_folder_10(folder_name="Test6", is_success=False)


# test 4、主界面的文件搜索：0-13-3
# 13 menu
oifm.menu_13()
# 3 文件搜索（0-13-3），这里点击取消文件搜索
oifm.search_3()
# 13 menu
oifm.menu_13()

# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后回到搜索前的主界面【需要在一开始设置允许录音】
oifm.search_3(text="1.jpg")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="123")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="1")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="D")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="apk")


# test 5、主界面的文件长按选中然后压缩
# 1 长按选中：对主界面8行长按选中，然后取消，相当于没有选中
oifm.long_click_1(sum=8)
# 1 长按选中：对主界面的第1，3，4行长按选中
oifm.long_click_1(sum=8, select_list=[1, 3, 4])
# 13 menu
oifm.menu_13()
# 2 压缩
oifm.compress_2()
# 1 长按选中：对主界面的第1，3，4行选中
oifm.long_click_1(sum=8, select_list=[1, 3])
# 13 menu
oifm.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
oifm.compress_2(name="test1", is_success=False)

# 1 长按选中
oifm.long_click_1(sum=8, select_list=[1, 3])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=False)

# 1 长按选中：对主界面的第1, 4行选中
oifm.long_click_1(sum=8, select_list=[1, 4])
# 13 menu
oifm.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩失败
oifm.compress_2(name="zip1", is_success=False)

# 1 长按选中
oifm.long_click_1(sum=8, select_list=[1, 4])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=False)

# test 6、
# 对前5个文件夹 每个文件夹长按选中，分别查看属性、重命名、失败压缩、添加bookmark、删除
temp_list = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 11 查看属性，0->1->13->11：查看文件123的属性
    oifm.properties_browse_11()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    oifm.rename_12()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    oifm.rename_12(name="rename"+str(i), is_success=False)

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 2 压缩:0->1->13->2
    oifm.compress_2(name="compress"+str(i), is_success=False)

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 15 bookmarks:添加bookmark 0->1->13-15
    oifm.bookmarks_15()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=temp_list[i])
    # 7 文件删除：0->1->7
    oifm.delete_file_7(is_success=False)

# 7、测试多项删除
# 1 长按选中
oifm.long_click_1(sum=8, select_list=[1, 2])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=False)
# 1 长按选中
oifm.long_click_1(sum=8, select_list=[1, 2, 3])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=False)
# 1 长按选中
oifm.long_click_1(sum=8, select_list=[1, 2, 3, 4])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=False)
# 1 长按选中
oifm.long_click_1(sum=8, select_list=[3, 4])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=False)

# 当前状态：文件主界面
# 8、对已经添加的bookmark进行操作
# 测试对添加的bookmarks进行操作，先取消删除，后删除
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2, 3], is_delete=False)
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2, 2, 6], is_delete=True)
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2], is_delete=True)
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2, 3], is_delete=True)
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2], is_delete=True)
# 当前状态：就剩下一个bookmark，并且是回到主界面

# 9、主界面的文件测试剪切粘贴和复制粘贴
# 测试剪切粘贴：
# 1 长按选中 第一个
oifm.long_click_1(sum=8, select_list=[1, 3])
# 4 待粘贴：点击剪切
oifm.to_paste_4(pre_num=1, is_paste=False, move_list=[1, 1, -1, -1, 3, 2, -1])
# 回到主界面
oifm.my_back_home()
# 1 长按选中：第3个和第6个
oifm.long_click_1(sum=8, select_list=[3, 6])
# 4 待粘贴：点击剪切，然后到不同的文件夹
oifm.to_paste_4(pre_num=1, is_paste=False, move_list=[1, 2, -1, 1, -1, -1])
# 1 长按选中 第一个
oifm.long_click_1(sum=8, select_list=[1])
# 4 待粘贴：点击剪切
oifm.to_paste_4(pre_num=1, is_paste=False, move_list=[1, 2, -1, -1])

# 当前状态：就剩下一个bookmark，并且是回到主界面
# 测试复制粘贴：
# 1 长按选中 第一个
oifm.long_click_1(sum=8, select_list=[1, 2])
# 13 点击menu
oifm.menu_13()
# 4 待粘贴：点击copy
oifm.to_paste_4(pre_num=2, is_paste=False, move_list=[1, 2, -1, -1, 3, -1])

# 1 长按选中 第3个和第6个
oifm.long_click_1(sum=8, select_list=[3, 6])
# 13 点击menu
oifm.menu_13()
# 4 待粘贴：点击copy
oifm.to_paste_4(pre_num=2, is_paste=False, move_list=[6, -1, 2, -1, 4, -1])
# 回到主界面
oifm.my_back_home()


# 当前状态：主界面, 进入到文件夹123下进行测试：

# 0：进入文件夹123进行测试：
oifm.file_browse_0(move_list=[1])
# 13：menu
oifm.menu_13()
# 14：测试设置 0-13-14
oifm.settings_14(sort_list=[2, 1, 3], checkbox_list=[5, 4, 3, 3, 2, 4, 5, 2], is_clear=False)


# 在文件夹123下：测试新建文件夹
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10),这里直接点击取消新建
oifm.new_folder_10()
# 13 menu
oifm.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，成功
oifm.new_folder_10(folder_name="Test1", is_success=True)

# 在文件夹123下：测试搜索
# 13 menu
oifm.menu_13()
# 3 文件搜索（0-13-3），这里点击取消文件搜索
oifm.search_3()
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后回到搜索前的主界面【需要在一开始设置允许录音】
oifm.search_3(text="1")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="Test1")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="test")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="jpg")
# 13 menu
oifm.menu_13()
# 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
oifm.search_3(text="mp3")


# 在文件夹123下：测试压缩：
# 1 长按选中：对主界面8行长按选中，然后取消，相当于没有选中
oifm.long_click_1(sum=5)
# 1 长按选中：对主界面的第4，5行长按选中
oifm.long_click_1(sum=5, select_list=[4, 5])
# 13 menu
oifm.menu_13()
# 2 压缩失败
oifm.compress_2()

# 1 长按选中：对主界面的第4，5行选中
oifm.long_click_1(sum=5, select_list=[4, 5])
# 13 menu
oifm.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩
oifm.compress_2(name="test-compress", is_success=True)


# 对文件夹Test1和test-compress.zip长按选中，分别查看属性、重命名、失败压缩、添加bookmark、删除
# 删除后顺序编号
temp_list = [[1], [2], [4], [1]]
for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 11 查看属性，0->1->13->11：查看文件123的属性
    oifm.properties_browse_11()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    oifm.rename_12()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    oifm.rename_12(name="rename2"+str(i), is_success=False)

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=temp_list[i])
    # 13 menu
    oifm.menu_13()
    # 15 bookmarks:添加bookmark 0->1->13-15
    oifm.bookmarks_15()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=temp_list[i])
    # 7 文件删除：0->1->7
    oifm.delete_file_7(is_success=True)

for i in range(5):
    oifm.menu_13()
    # 10 新建文件夹(0-13-10)，这里输入文件夹名，
    oifm.new_folder_10(folder_name="new"+str(i), is_success=True)

# 进入文件夹n1，新建三个文件夹
oifm.file_browse_0([1])
for i in range(3):
    oifm.menu_13()
    # 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
    oifm.new_folder_10(folder_name="n1-new"+str(i), is_success=True)




# 重命名
# for i in range(3):
for i in range(1, 3):
    # 1 长按选中：第一个123
    oifm.long_click_1(sum=8, select_list=[i+1])
    # 13 menu
    oifm.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    oifm.rename_12(name="a"+str(i), is_success=True)

# 进入文件夹n2，新建三个文件夹
oifm.file_browse_0([-1, 2])
for i in range(3):
    oifm.menu_13()
    # 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
    oifm.new_folder_10(folder_name="n2-new"+str(i), is_success=True)

oifm.file_browse_0([-1])

# 测试复制粘贴：
# 1 长按选中 第3个
oifm.long_click_1(sum=5, select_list=[6])
# 13 点击menu
oifm.menu_13()
# 4 待粘贴：点击copy
oifm.to_paste_4(pre_num=2, is_paste=True, move_list=[1, -1, 2, 1, -1, 2, -1])
# 回到刚刚到界面
oifm.my_back()

# 1 长按选中 第3个
oifm.long_click_1(sum=5, select_list=[6, 7])
# 13 点击menu
oifm.menu_13()
# 4 待粘贴：点击copy
oifm.to_paste_4(pre_num=2, is_paste=True, move_list=[1, -1, 1, 1, -1])

# 在文件夹n0中 进行压缩
for i in range(5):
    # 1 长按选中：对主界面的第行选中
    oifm.long_click_1(sum=5, select_list=[i+1])
    # 13 menu
    oifm.menu_13()
    # 2 压缩文件：主界面压缩文件，1-13-2。设置压缩
    oifm.compress_2(name="no-compress"+str(i), is_success=True)


# 测试删除
# 删除文件夹1中到所有文件：
oifm.long_click_1(sum=3, select_list=[1, 2, 3])
# 删除
oifm.delete_file_7(is_success=True)
# 删除文件夹1中到所有文件：
oifm.long_click_1(sum=3, select_list=[1, 2])
# 删除
oifm.delete_file_7(is_success=True)
# 删除文件夹1中到所有文件：
oifm.long_click_1(sum=3, select_list=[1, 2, 3])
# 删除
oifm.delete_file_7(is_success=True)

# 返回上一个界面
oifm.my_back()

# 测试 bookmarks
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2, 3], is_delete=False)
# 13 点击menu
oifm.menu_13()
# 15 bookmarks:对已经添加的bookmark进行删除
oifm.bookmarks_15(long_click_list=[2, 3], is_delete=True)

# 查看文件属性
for i in range(5):
    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=[1])
    # 13 menu
    oifm.menu_13()
    # 11 查看属性，0->1->13->11：查看文件123的属性
    oifm.properties_browse_11()

    # 1 长按选中：第一个123
    oifm.long_click_1(sum=5, select_list=[1])
    # 7 文件删除：0->1->7
    oifm.delete_file_7(is_success=True)

oifm.menu_13()
# 10 新建文件夹1
oifm.new_folder_10(folder_name="1", is_success=True)
oifm.menu_13()
# 10 新建文件夹1
oifm.new_folder_10(folder_name="2", is_success=True)


oifm.long_click_1(sum=5, select_list=[1, 2])
# 13 menu
oifm.menu_13()
# 2 压缩文件：主界面压缩文件，1-13-2。设置压缩
oifm.compress_2(name="folder1", is_success=True)

# 1 长按选中：第一个123
oifm.long_click_1(sum=5, select_list=[5])
# 7 文件删除：0->1->7
oifm.delete_file_7(is_success=True)

# 最后一定要加入保存最后一个状态的图片的代码
oifm.get_screen_info()

