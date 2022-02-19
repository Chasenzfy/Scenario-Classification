# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
import os.path

from selenium.common.exceptions import NoSuchElementException

import SimpleExplorer


mypath = os.path.dirname(os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'com.dnielfe.manager'
desired_caps['appActivity'] = '.BrowserActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = False


screen_path = mypath + '/screen/'
xml_path = mypath + '/xml/'
jump_pairs = mypath + '/jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

se = SimpleExplorer.SimpleExplorer(driver, screen_path, xml_path, jump_pairs,activity_info)
# se.my_to_settings()
# se.my_settings()
#
# se.my_click_accessibilty_id("Navigate up")
# se.my_click_accessibilty_id("Open navigation drawer")
#
# se.search_3("123")
# se.file_browse_0([4,0])
# se.to_paste_4(copy_list=[4,5],move_list=[-1,1,-1,0,0],end=0)
# se.new_folder_10(se.generate_random_str(4),True)
# se.file_browse_0([0])
# se.long_click_delete_7([0,2,3],is_success=False)
# se.long_click_delete_7([1,4],is_success=True)
# time.sleep(2)
# se.new_folder_10(se.generate_random_str(4),True)
# se.my_back_home()
# se.search_3("jj")
#
#
# se.file_browse_0([3])
# se.new_folder_10(folder_name="7"+se.generate_random_str(3),is_success=True)
# se.file_browse_0([0])
# se.long_click_delete_7(delete_list=[2],is_success=True)
# se.my_back()
# se.file_browse_0([2,0])
# se.extract_8(3,"/storage/emulated/0/1Gab/123yyy/5x4W")
# se.long_click_delete_7(delete_list=[3],is_success=True)
# for i in range(3):
#     se.rename1_12(i,is_success=True,rename_name=se.generate_random_str(4))
# se.new_folder_10(se.generate_random_str(3),is_success=True)
# se.my_back_home()
# se.search_3(".zip")
#
# se.file_browse_0([3,0])
# se.to_paste_4(copy_list=[0,2],move_list=[-1],end=1)
# se.new_file_10("ozuvy")
# se.new_file_10("abc.txt",is_success=True)
# # 加edit
# se.my_back()
# # 加edit
# for i in range(4):
#     se.properties_11(i)
# se.file_browse_0([2,0,1])
# se.long_click_select_1(begin_index=0)
# se.long_click_select_1(begin_index=2)
# for i in range(5):
#     se.properties_11(i)
# #
# se.extract_8(4,"/storage/emulated/0/123yyy/ykq/uzR9rtFZ/ciK/")
# se.rename1_12(4,is_success=True,rename_name=se.generate_random_str(3))
# se.to_paste_41([2,3],move_list=[-1,-1,-1],end=0)
# se.compress_2([0,1,2],is_cancel=False)
# se.my_back_home()
# se.search_3(".txt")
#

# se.file_browse_0([0])
# se.to_paste_4([1,3,5],2,[-1])
# se.new_file_10("pox.txt",is_success=True)
# se.new_file_10("zzz.txt")
# se.new_file_10("zss.txt",True)
# se.new_folder_10("vps",is_success=True)
# for i in range(6):
#     se.rename1_12(i,rename_name=se.generate_random_str(3),is_success=True)
# se.compress_2([0,2],is_cancel=False)
# se.long_click_delete_7([4],is_success=True)
# se.my_back_home()
# se.file_browse_0([2])
# se.search_3(".mp3")
# se.my_back_home()
# se.file_browse_0([0])
# se.compress_2([4,5,6],is_cancel=False)
# se.long_click_delete_7([2,5],is_success=False)
# se.long_click_delete_7([3,4,6],is_success=True)
# for i in range(4):
#     se.properties_11(i)
# se.file_browse_0([0])
# for i in range(4):
#     se.rename1_12(i,is_success=True,rename_name=se.generate_random_str(4))
# se.new_folder_10(folder_name=se.generate_random_str(5),is_success=True)
# se.new_file_10(file_name="osos.txt")
# se.new_file_10(file_name="smsm.txt",is_success=True)
#
# se.compress_2([0,1],is_cancel=False)
#
# se.my_back_home()
# se.search_3("yyy")
#
# se.file_browse_0([2])
# se.compress_2(compress_list=[1,3],is_cancel=False)
# se.compress_2(compress_list=[2,4],is_cancel=False)
# se.long_click_delete_7([0],is_success=True)
#
# se.my_back_home()
# se.search_3(".jpg")
# se.file_browse_0([1])
# for i in range(5):
#     se.properties_11(i)
#
# se.new_file_10(file_name=se.generate_random_str(3)+".txt",is_success=True)
#
# se.new_file_10(file_name=se.generate_random_str(3)+".txt",is_success=False)
# se.file_browse_0([0])
# se.compress_2(compress_list=[0],is_cancel=False)
# se.compress_2(compress_list=[1,2],is_cancel=True)
# se.long_click_delete_7([4],is_success=True)
# se.compress_2([1,2],is_cancel=True)
# se.file_browse_0([1])
# se.new_folder_10(folder_name=se.generate_random_str(4),is_success=True)
# se.new_folder_10(folder_name=se.generate_random_str(6),is_success=False)
# se.file_browse_0([0])
# se.new_folder_10(folder_name=se.generate_random_str(3),is_success=False)
# se.new_folder_10(folder_name=se.generate_random_str(3),is_success=True)
#
# se.compress_2([1],is_cancel=False)
#
# se.my_back_home()
# se.search_3(".png")

# se.file_browse_0([4,0])
# se.extract_8(7,"/storage/emulated/0/123jjllkop/Y55T/xert/gBzm")
# se.long_click_delete_7([3],is_success=True)
# se.extract_8(7,"/storage/emulated/0/1Gab/123yyy/E9D")
#
# se.to_paste_41([3,6],end=1,move_list=[0,0])
# se.my_back()
# se.long_click_delete_7([2],is_success=True)
# se.compress_2([2,3],is_cancel=False)
# se.file_browse_0([0])
# se.to_paste_41([2],end=0,move_list=None)
# se.my_back_home()
# se.search_3("attt.txt")
# se.search_3("cpasdoa")
# se.search_3("jjllkop")
# se.file_browse_0([1,0])
# se.compress_2([1,3],is_cancel=False)
# se.extract_8(4,"/storage/emulated/0/123Ng/qH2")
# se.file_browse_0([0])
# se.extract_8(2,extract_path="/storage/emulated/0/123jjllkop/Y55T")
# se.long_click_delete_7([2],is_success=True)
# se.my_back_home()
se.file_browse_0([2])
se.extract_8(4,"/storage/emulated/0/123yyy/7boc")
se.long_click_delete_7([4],is_success=True)
se.to_paste_41([3],move_list=[-1,1],end=0)
se.file_browse_0([-1,2,0,1])
se.extract_8(4,"/storage/emulated/0/123yyy/ykq/uzR9rtFZ/ciK")
se.my_back_home()

se.get_screen_info()
driver.quit()