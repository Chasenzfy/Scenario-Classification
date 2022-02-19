# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
import os.path

from selenium.common.exceptions import NoSuchElementException

import FEFileExplorer


mypath = os.path.dirname(os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'com.skyjos.apps.fileexplorerfree'
desired_caps['appActivity'] = 'com.skyjos.fileexplorer.ui.SplashActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = False


screen_path = mypath + '/screen/'
xml_path = mypath + '/xml/'
jump_pairs = mypath + '/jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

fefile = FEFileExplorer.FEFileExplorer(driver, screen_path, xml_path, jump_pairs,activity_info)

# fefile.my_click_id("com.skyjos.apps.fileexplorerfree:id/home_section_item_imageview",0)
#
# fefile.file_browse_0([0,0,-1,-1,1,-1,2,-1,3,-1,4,0,-1,-1])
# fefile.file_browse_0([2,1])
# fefile.my_back_home()
#
# fefile.search_3("123")
# fefile.search_only_3("pp")
# fefile.search_only_3(".zip")
# fefile.search_3(".txt")
#
# fefile.search_3(".mp3")
#
# fefile.file_browse_0([0])
# fefile.to_paste_4(copy_list=[2,3,4],move_list=[2,1],end=0)
#
# fefile.file_browse_0([-1,2])
# fefile.long_click_delete_7([0,2,3],is_success=False)
# fefile.long_click_delete_7([2,3],is_success=True)
# fefile.new_folder_10("aosdo",True)
# fefile.my_back_home()
#
# fefile.file_browse_0([2])
# fefile.to_paste_4(copy_list=[2,3],move_list=[2,1,0],end=0)
# fefile.my_back_home()
# fefile.new_folder_10(folder_name="123yyy",is_success=True)
# fefile.file_browse_0([3])
# fefile.to_paste_4(copy_list=[3,4],move_list=None,end=0)
# fefile.my_back()
# fefile.file_browse_0([3])
# fefile.to_paste_4(copy_list=[3,4],move_list=None,end=4)
# fefile.my_back()
# fefile.file_browse_0([4])
# fefile.new_file_10("aaaass")
# fefile.new_file_10("abc",is_success=True)
# fefile.text_edit_9("abc.txt","kklfoix;ofc")
# fefile.my_back_home()
#
# for i in range(4):
#     fefile.properties_11(i)
#
# fefile.file_browse_0([2])
# for i in range(4):
#     fefile.properties_11(i)
#
# fefile.long_click_select_1(begin_index=0)
# fefile.long_click_select_1(begin_index=2)
# fefile.long_click_select_1(begin_index=4)

# fefile.text_edit_9("abc.txt","aklfasdk;lk;lsdfc[psdas")
#
# fefile.copy_43(1,move_list=None,end=4)
# fefile.my_back()

# fefile.file_browse_0([4,0])
# fefile.music_5(file_index=2)
# fefile.my_back_home()

# fefile.file_browse_0(move_list=[2])
# fefile.long_click_delete_7([2,3],True)
# fefile.file_browse_0([0,0])
# fefile.delete_7(delete_index=2,is_success=True)
# fefile.compress_2(compress_list=[2,4],is_cancel=True,file_type=2)
# fefile.compress_2_1(1,is_cancel=False,file_type=1)
# fefile.delete_7(2,is_success=True)
# fefile.long_click_delete_7([0,1],is_success=True)
# # #
# fefile.my_back()
# fefile.compress_2(compress_list=[0,1],is_cancel=False,file_type=0)
# fefile.my_back_home()
# #
# fefile.file_browse_0([4])
# fefile.new_file_10("opcp",is_success=True)
# fefile.text_edit_9("opcp.txt","klvaiso")
# fefile.my_back()
#
# fefile.file_browse_0([3])
# #
# #
# fefile.delete_7(3,is_success=True)
# fefile.new_file_10("axxx")
# fefile.new_file_10("aooo",True)
# fefile.text_edit_9("aooo.txt","pvsdopov")
#
# fefile.text_edit_9("snpX.txt","daoidglkjvz")
# fefile.compress_2(compress_list=[2,3],is_cancel=False,file_type=2)
# fefile.my_back()
# #
# fefile.search_3(".jpg")
# fefile.search_3(".png")
# fefile.search_3("ccsaef")
# fefile.search_3("attt.txt")
# fefile.search_3("jjllkop")
# fefile.file_browse_0([4])
# fefile.delete_7(delete_index=4,is_success=True)
# fefile.compress_2(compress_list=[1,3],is_cancel=False,file_type=2)
# fefile.compress_2(compress_list=[2],is_cancel=False,file_type=1)
#
# fefile.new_folder_10("aaFol",is_success=True)
# fefile.new_folder_10("coias",is_success=False)
# fefile.new_folder_10("ppvia",is_success=True)
# fefile.new_folder_10("cdeazx",is_success=False)
# fefile.new_folder_10("mlapoi",is_success=True)
# #
# fefile.file_browse_0([0])
# fefile.new_file_10("000vvv",is_success=True)
# fefile.new_file_10("999", is_success=True)
# fefile.text_edit_9("000vvv.txt","gdwopapodfbl,dioafhsf")
# fefile.text_edit_9("999.txt","gdwopapodfbl,dioafhsf")
#
# fefile.my_back()
# fefile.long_click_delete_7(delete_list=[1,4],is_success=False)
# fefile.my_back_home()

# fefile.to_paste_4(copy_list=[0,1],move_list=None,end=5)
# fefile.file_browse_0([5,0,1])
# fefile.music_5(0)
# fefile.my_back()
# fefile.long_click_delete_7(delete_list=[2,6],is_success=True)
# fefile.to_paste_4(copy_list=[4,5],move_list=None,end=2)
# #
# for i in range(5):
#     fefile.rename1_12(i,rename_name=fefile.generate_random_str(3),is_success=True)
# fefile.file_browse_0([1])
# fefile.rename1_12(0,rename_name=fefile.generate_random_str(6),is_success=True)
# fefile.my_back()
# for i in range(4):
#     fefile.properties_11(i)
# #
# fefile.my_back_home()
# time.sleep(1)

# fefile.file_browse_0([2])
# fefile.new_folder_10("vaopsdop",is_success=True)
# fefile.new_file_10("cpasd.txt",is_success=True)
# fefile.new_folder_10("ppjjc",is_success=False)
# fefile.new_file_10("aaaapppx.txt",is_success=False)
# for i in range(4):
#     fefile.rename1_12(i, rename_name=fefile.generate_random_str(4), is_success=False)
# fefile.file_browse_0([0])
# for i in range(3):
#     fefile.rename1_12(i, rename_name=fefile.generate_random_str(5), is_success=True)

# fefile.file_browse_0([1])
# fefile.delete_7(1,is_success=True)
# fefile.extract_8(0,move_list=[2],end_index=2)
# fefile.delete_7(5,is_success=True)
#
#
# fefile.long_click_delete_7(delete_list=[3],is_success=True)
# fefile.rename1_12(file_index=1,is_success=True,rename_name="ddd")
# fefile.text_edit_9("ddd.txt","afiohoa[cp,klasd")
# fefile.compress_2([3,4],is_cancel=True,file_type=1)
# #
#
# fefile.long_click_delete_7(delete_list=[2],is_success=True)
# fefile.my_back()
# fefile.file_browse_0([0])
# fefile.compress_2([1,4],is_cancel=False,file_type=2)
# fefile.delete_7(2,True)
# fefile.file_browse_0([0])
# fefile.music_5(file_index=1)
# fefile.my_back_home()
#
# fefile.file_browse_0([3])
# for i in range(4):
#     fefile.rename1_12(i,is_success=True,rename_name=fefile.generate_random_str(4))
# fefile.compress_2_1(2,is_cancel=False,file_type=0)
# fefile.compress_2_1(0,is_cancel=False,file_type=1)
# fefile.my_back()
#
# fefile.file_browse_0([2])
# fefile.text_edit_9("snpX.txt","papfsfsd")
# fefile.cut_4(cut_index=4,end=0,move_list=[3])
# fefile.copy_4(cut_index=4,end=1,move_list=[3])
# fefile.delete_7(4,is_success=True)
# fefile.cut_4(cut_index=3,end=1,move_list=[3])

#
# for i in range(4):
#     fefile.rename1_12(i,is_success=True,rename_name=fefile.generate_random_str(4))
#
# fefile.long_click_delete_7([0,1],is_success=True)
# fefile.my_back()
#
# fefile.file_browse_0([3,1])
# fefile.text_edit_9("cpasd.txt.txt","ofjopal;sfjop")
# for i in range(4):
#     fefile.properties_11(i)
#
# fefile.file_browse_0([-1,-1,4])
# fefile.delete_7(1,is_success=True)
# fefile.delete_7(2,is_success=True)
# fefile.compress_2([0,1,5],is_cancel=True,file_type=0)
# fefile.compress_2([0],is_cancel=False,file_type=0)
# fefile.my_back()
# fefile.file_browse_0([3])
# fefile.delete_7(2,is_success=True)
# fefile.delete_7(3,is_success=True)
# fefile.delete_7(3,is_success=True)
# fefile.compress_2([0,1],is_cancel=True,file_type=0)
# fefile.compress_2_1(3,is_cancel=False,file_type=0)
# fefile.my_back()
# fefile.file_browse_0([4])
# fefile.compress_2([0,1],is_cancel=False,file_type=0)
# fefile.my_back()
# fefile.browse_bookmark_15()
# fefile.my_back_home()
#
# for i in range(5):
#     fefile.add_bookmark_15([i])
#
# fefile.file_browse_0([3])
# for i in range(3):
#     fefile.add_bookmark_15([i])
# fefile.my_back()
# fefile.file_browse_0([2])
# for i in range(3):
#     fefile.add_bookmark_15([i])

# fefile.my_back()
# fefile.browse_bookmark_15()
# fefile.delete_bookmark_15([0,1,2,3,4,5])
# fefile.delete_bookmark_15([0,1,2,0,0])
# fefile.my_back_home0()
# fefile.my_to_settings()
# fefile.my_settings()
# fefile.my_click_id("com.skyjos.apps.fileexplorerfree:id/home_section_item_imageview",0)
# fefile.file_browse_0([2,1])
# fefile.music_5(6)
# fefile.my_back_home0()
# fefile.get_screen_info()

# fefile.file_browse_0([1])
# for i in range(3):
#     fefile.add_bookmark_15([i])
#
# fefile.browse_bookmark_15()

# fefile.rename_bookmark_15(rename_index=0,text="123000sz",is_success=False)
# fefile.my_back()
# #
# fefile.rename_bookmark_15(rename_index=1,text="slv",is_success=True)
# fefile.my_back()
#
# fefile.rename_bookmark_15(rename_index=0,text=fefile.generate_random_str(5),is_success=True)
# fefile.my_back()
#
# fefile.rename_bookmark_15(rename_index=1,text=fefile.generate_random_str(4),is_success=True)
# fefile.my_back()
#
# fefile.rename_bookmark_15(rename_index=2,text=fefile.generate_random_str(3),is_success=True)
# fefile.my_back()
# fefile.rename_bookmark_15(rename_index=1,text=fefile.generate_random_str(6),is_success=True)
# fefile.my_back()
# fefile.rename_bookmark_15(rename_index=0,text=fefile.generate_random_str(2),is_success=True)
# fefile.my_back()
#
# fefile.delete_bookmark_15([0,0,0])
#
# fefile.my_back_home()
# fefile.file_browse_0([2])
# for i in range(2):
#     fefile.add_bookmark_15([i])
#     fefile.browse_bookmark_15()
#     fefile.my_back_home()
# fefile.file_browse_0([3])
# for i in range(2):
#     fefile.add_bookmark_15([i])
#     fefile.browse_bookmark_15()
#     fefile.my_back_home()

fefile.delete_bookmark_15([0,0,0])

fefile.get_screen_info()

driver.quit()
