# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
import SimpleFile
# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.simplemobiletools.filemanager.pro'
desired_caps['appActivity']='.activities.MainActivity'

desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/6-simple/6-simple/screen'
xml_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/6-simple/6-simple/xml'
jump_pairs = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/6-simple/6-simple/jump_pairs.txt'
print("ok")
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)

time.sleep(2)
simplefile = SimpleFile.MyOIFM(driver, screen_path, xml_path, jump_pairs,'com.simplemobiletools.filemanager.pro.activities.MainActivity')


# print("test1")
# # test 1、主界面的文件浏览
# # 回到主界面
# simplefile.my_back_home()
# # 0 文件浏览
# simplefile.file_browse_0(move_list=[1, 1, -1, 2, -1, -1, 3, 1, -1, 2, -1, -1, 6, -1])
# # 回到主界面
# simplefile.my_back_home()


# print("test2")
# # test 2、主界面的设置
# # 13 menu
# simplefile.menu_13()
# # 14 设置 (0-13-14)
# simplefile.settings_14(theme_list=[0, 2, 1, 3, 1], date_list=[1,3,-1,4,5,0], font_list=[1,3,0],checkbox_list=[1,0,0])
# print("!!!!!!!!!!!!!!!")

# print("test3")
# # test 3、主界面的新建文件夹
# # 10 新建文件夹(0-13-10),这里直接点击取消新建
# simplefile.new_folder_10()
# # # 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
# simplefile.new_folder_10(folder_name="Test", is_success=False)
# #def new_folder_10(self, folder_name=None, is_success=None,type=1):

# print("test4")
# # test 4、主界面的文件搜索：0-13-3
# # 3 文件搜索（0-13-3），这里点击取消文件搜索
# simplefile.search_3()
# simplefile.search_3(text="1.jpg")
# # 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
# simplefile.search_3(text="123")

# print("test5")
# # test 5、主界面的文件长按选中然后压缩
# # 1 长按选中：对主界面8行长按选中，然后取消，相当于没有选中
# simplefile.file_browse_0(move_list=[0, 0])
# simplefile.long_click_1(sum=3)
# # 1 长按选中：123文件夹的第1,2行长按选中
# simplefile.long_click_1(sum=3, select_list=[0, 1])
# # 13 menu
# simplefile.menu_13()
# # 2 压缩
# simplefile.compress_2(name="test2",is_success=True)
# #def compress_2(self, name=None, is_success=None):
# # 1 长按选中：123文件夹的第1，2，3行选中
# simplefile.long_click_1(sum=4, select_list=[1,2,0])
# # 13 menu
# simplefile.menu_13()
# # 2 压缩文件：123文件夹压缩文件，1-13-2。
# simplefile.compress_2(name="test3", is_success=True)

# print("test6")
# # test 6、
# # 对前5个文件夹 每个文件夹长按选中，分别查看属性、重命名、失败压缩、添加bookmark、删除
# #def rename_12(self, name=None, name2=None,is_success=None,muti=1,pre=1):
# temp_list = [[0], [1]]
# for i in range(len(temp_list)):
#     # 1 长按选中：第一个123
#     simplefile.long_click_1(sum=5, select_list=temp_list[i])
#     # 11 查看属性，0->1->13->11：查看文件123的属性
#     simplefile.properties_browse_11()

#     # 13 menu
#     simplefile.menu_13()
#     # 12 重命名：0->1->13->12：点击后退出
#     simplefile.rename_12()

#     # 13 menu
#     simplefile.menu_13()
#     # 12 重命名：0->1->13->12：点击后退出
#     simplefile.rename_12(name="rename"+str(i),name2 = "jpg",is_success=True,muti=1)

#     # 1 长按选中：第一个123
#     simplefile.long_click_1(sum=5, select_list=temp_list[i])
#     # 13 menu
#     simplefile.menu_13()
#     # 2 压缩:0->1->13->2
#     simplefile.compress_2(name="compress"+str(i), is_success=False)

#     # 7 文件删除：0->1->7
#     simplefile.delete_file_7(is_success=False)

#     simplefile.my_back()

# print("test6-2")
# temp_list = [[3,4],[1,2,0]]
# for i in range(len(temp_list)):
#     # 1 长按选中：第一个123
#     simplefile.long_click_1(sum=5, select_list=temp_list[i])
#     # 11 查看属性，0->1->13->11：查看文件123的属性
#     simplefile.properties_browse_11()

#     simplefile.menu_13()
#     # 12 重命名：0->1->13->12：点击后退出
#     simplefile.rename_12()

#     simplefile.menu_13()
#     # 12 重命名：0->1->13->12：点击后退出
#     simplefile.rename_12(name="rename",is_success=True,muti=2,pre=2)

#     simplefile.long_click_1(sum=5, select_list=temp_list[i])
#     # 13 menu
#     simplefile.menu_13()
#     # 12 重命名：0->1->13->12：点击后退出
#     simplefile.rename_12(name="test%Y%M%D_%i"+str(i),is_success=True,muti=3)

#     simplefile.long_click_1(sum=5, select_list=temp_list[i])
#     # 13 menu
#     simplefile.menu_13()
#     # 2 压缩:0->1->13->2
#     simplefile.compress_2(name="test5", is_success=False)

#     # 7 文件删除：0->1->7
#     simplefile.delete_file_7(is_success=False)

#     simplefile.my_back()

# print("test7")
# # 7、测试多项删除
# # 1 长按选中
# simplefile.long_click_1(sum=5, select_list=[1, 2])
# # 7 文件删除：0->1->7
# simplefile.delete_file_7(is_success=False)
# simplefile.my_back()
# # 1 长按选中
# simplefile.long_click_1(sum=5, select_list=[1, 2, 3])
# # 7 文件删除：0->1->7
# simplefile.delete_file_7(is_success=False)
# simplefile.my_back()
# # 1 长按选中
# simplefile.long_click_1(sum=5, select_list=[3, 4])
# # 7 文件删除：0->1->7
# simplefile.delete_file_7(is_success=False)
# simplefile.my_back()

# # 9、主界面的文件测试剪切粘贴和复制粘贴
# # 测试剪切粘贴：
# # 1 长按选中 第一个
# #def to_paste_4(self, pre_num, is_paste, move_list,total_len):

# simplefile.long_click_1(sum=5, select_list=[1])
# simplefile.menu_13()
# # 4 待粘贴：点击剪切
# simplefile.to_paste_4(pre_num=1, is_paste=False, move_list=[-1],total_len=3)
# simplefile.my_back()

# # 1 长按选中：第3个和第6个
# simplefile.long_click_1(sum=5, select_list=[3, 2])
# simplefile.menu_13()
# # 4 待粘贴：点击剪切
# simplefile.to_paste_4(pre_num=1, is_paste=False, move_list=[-1, 0],total_len=3)
# simplefile.my_back()

# # 1 长按选中 第一个
# simplefile.long_click_1(sum=5, select_list=[1,4,2])
# simplefile.menu_13()
# # 4 待粘贴：点击复制
# simplefile.to_paste_4(pre_num=2, is_paste=True, move_list=[-1],total_len=3)

# # 当前状态：就剩下一个bookmark，并且是回到主界面
# # 测试复制粘贴：
# # 1 长按选中 第一个
# simplefile.long_click_1(sum=5, select_list=[1])
# simplefile.menu_13()
# simplefile.to_paste_4(pre_num=2, is_paste=False, move_list=[-1, 1,-1],total_len=3)
# simplefile.my_back()

# # 1 长按选中 第3个和第6个
# simplefile.long_click_1(sum=8, select_list=[1,4,2])
# simplefile.menu_13()
# simplefile.to_paste_4(pre_num=2, is_paste=True, move_list=[-1],total_len=3)
# simplefile.my_click_id("com.simplemobiletools.filemanager.pro:id/conflict_dialog_radio_keep_both")
# simplefile.my_click_id("android:id/button1")

# print("test8")
# simplefile.new_folder_10()
# # 10 新建文件夹(0-13-10)，这里输入文件夹名，成功
# simplefile.new_folder_10(folder_name="Test1", is_success=True)

# # 3 文件搜索（0-13-3），这里点击取消文件搜索
# simplefile.search_3()

# # 3 文件搜索(0-13-3)，这里输入文本，搜索完成后回到搜索前的主界面【需要在一开始设置允许录音】
# simplefile.search_3(text="1")

# # 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
# simplefile.search_3(text="Test1")

# # 3 文件搜索(0-13-3)，这里输入文本，搜索完成后到达搜索前的【主界面】
# simplefile.search_3(text="jpg")

# simplefile.long_click_1(sum=5, select_list=[1])
# # 删除
# simplefile.delete_file_7(is_success=True)
# # 返回上一个界面
# simplefile.my_back()

# simplefile.long_click_1(sum=5, select_list=[2,3,4])
# # 删除
# simplefile.delete_file_7(is_success=True)

# simplefile.my_back()


# print("test9")
# #回到123
# simplefile.file_browse_0(move_list=[0, 0])
# #测试解压缩，分别为直接点开压缩文件和使用菜单中的解压功能
# simplefile.my_click_classname("android.widget.RelativeLayout",4)
# simplefile.my_click_accessibilty_id("Decompress")
# simplefile.my_click_id("android:id/button2")

# simplefile.my_click_accessibilty_id("Decompress")
# simplefile.my_click_id("android:id/button1")

# time.sleep(2)
# simplefile.long_click_1(sum=6, select_list=[1])
# simplefile.delete_file_7(is_success=True)

# simplefile.my_back()
# simplefile.long_click_1(sum=5, select_list=[3,4])
# simplefile.menu_13()
# simplefile.my_click_text("Decompress")

# simplefile.long_click_1(sum=7, select_list=[2,3])
# simplefile.delete_file_7(is_success=True)

# simplefile.file_browse_0(move_list=[0])

# #打开音乐文件，暂停后再继续
# simplefile.my_click_classname("android.widget.RelativeLayout",2)
# simplefile.my_click_text("Pause video")
# simplefile.my_click_text("Play video")
# simplefile.my_back()


#crash
# simplefile.file_browse_0(move_list=[0,0])

# #创建新的文本文件，编辑两次，保存后删除
# # simplefile.new_folder_10(folder_name="test.txt",is_success=True,type=2)
# simplefile.my_click_classname("android.widget.RelativeLayout",5)
# # simplefile.my_click_id("android:id/button_once")
# simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","21126423213")
# simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","sadcvasdcxz")
# time.sleep(2)
# simplefile.my_click_accessibilty_id("Save as")
# simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/save_as_name","testtest")
# simplefile.my_click_id("android:id/button2")
# simplefile.my_click_accessibilty_id("Save as")
# simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/save_as_name","testtest")
# simplefile.my_click_id("android:id/button1")
# simplefile.my_back()
# simplefile.long_click_1(sum=7, select_list=[5,6])
# simplefile.delete_file_7(is_success=True)

# print("test10")
# simplefile.my_click_accessibilty_id("More options")
# simplefile.bookmarks_15(add_delete_list=[0,0,-1,-3,0,-2,-3,0,0,0],is_add_delete=0)
# simplefile.my_click_accessibilty_id("More options")
# simplefile.bookmarks_15(add_delete_list=[1,0,-2,1,-1],is_add_delete=1)

# simplefile.my_click_accessibilty_id("More options")
# simplefile.bookmarks_15_2(count=0)

# #def bookmarks_15(self, add_delete_list=None, is_add_delete=0):

# # # 最后一定要加入保存最后一个状态的图片的代码
# simplefile.my_back_home()

# simplefile.file_browse_0(move_list=[0])
# simplefile.long_click_1(sum=2, select_list=[1])
# simplefile.menu_13()
# simplefile.to_paste_4(pre_num=1, is_paste=False, move_list=[0,-1,2,0,-1,-1,-1,2,-1,4,0,-1,2,-1,4,-1,-1,6,-1,8,-1,10,-1,12,-1],total_len=2)
# simplefile.my_back()

# simplefile.long_click_1(sum=2, select_list=[1])
# simplefile.menu_13()
# simplefile.compress_2(name="extracttest",is_success=True)

# simplefile.file_browse_0(move_list=[2])
# simplefile.my_click_text("__MACOSX")
# simplefile.my_click_text("123")
# simplefile.my_back()
# simplefile.my_back()
# simplefile.extract_8(move_list=[0,-1,2,0,-1,-1,-1,2,-1,4,0,-1,2,-1,4,-1,-1,6,-1,8,-1,10,-1,12,-1],is_success=False)
# simplefile.my_back()
# simplefile.long_click_1(sum=2, select_list=[2])
# simplefile.delete_file_7(is_success=True)

#crash
simplefile.file_browse_0(move_list=[0])

simplefile.menu_13()
simplefile.my_click_text("Settings")
simplefile.my_click_text("Manage favorites")
simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_classname("android.widget.RelativeLayout",1)
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_classname("android.widget.RelativeLayout",1)
simplefile.my_click_id("android:id/button1")
simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",0)
simplefile.my_click_id("android:id/button1")

simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",2)

simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",4)
simplefile.my_click_id("android:id/button1")
simplefile.my_click_accessibilty_id("Add favorites")
simplefile.my_click_classname("android.widget.RelativeLayout",6)


simplefile.my_long_click_classname("android.widget.RelativeLayout",0)
simplefile.my_long_click_classname("android.widget.RelativeLayout",1)
simplefile.my_long_click_classname("android.widget.RelativeLayout",2)
simplefile.my_long_click_classname("android.widget.RelativeLayout",3)
simplefile.my_long_click_classname("android.widget.RelativeLayout",4)
simplefile.my_long_click_classname("android.widget.RelativeLayout",5)
simplefile.my_long_click_classname("android.widget.RelativeLayout",6)
simplefile.my_click_accessibilty_id("Remove")
simplefile.my_back()
simplefile.my_back()
simplefile.my_back()




simplefile.file_browse_0(move_list=[0])

simplefile.long_click_1(sum=2, select_list=[1])
simplefile.menu_13()
simplefile.compress_2(name="decompresstest",is_success=True)

simplefile.file_browse_0(move_list=[2])
simplefile.my_click_text("__MACOSX")
simplefile.my_click_text("123")
simplefile.my_back()
simplefile.my_back()
simplefile.extract_8(move_list=[0,-1],is_success=False)
simplefile.my_back()
simplefile.long_click_1(sum=2, select_list=[2])
simplefile.delete_file_7(is_success=True)
simplefile.my_back()
simplefile.get_screen_info()