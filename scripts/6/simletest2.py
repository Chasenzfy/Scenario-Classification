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

simplefile.my_back_home()

simplefile.long_click_1(sum=9, select_list=[2,3])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[0])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[4])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[7,8,9])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[7])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[6,7])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[0,2,7])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[2,7])
simplefile.properties_browse_11()
simplefile.my_back()
simplefile.long_click_1(sum=9, select_list=[2,1])
simplefile.properties_browse_11()
simplefile.my_back()

simplefile.file_browse_0(move_list=[0])

simplefile.long_click_1(sum=5, select_list=[3])
simplefile.menu_13()
simplefile.rename_12(name="TEST3",name2 = "PNG",is_success=False,muti=1)
simplefile.menu_13()
simplefile.rename_12(name="testtestfor",name2 = "jpg",is_success=False,muti=1)
simplefile.menu_13()
simplefile.rename_12(name="1235g9",name2 = "img",is_success=False,muti=1)
simplefile.menu_13()
simplefile.rename_12(name="testfortest",name2 = "imgjpg",is_success=False,muti=1)
simplefile.menu_13()
simplefile.rename_12(name="TEST3test",name2 = "PNG",is_success=False,muti=1)
simplefile.my_back()

simplefile.file_browse_0(move_list=[1,0])

simplefile.new_folder_10(folder_name="newfile.txt",is_success=False,type=2)
simplefile.new_folder_10(folder_name="newfolder",is_success=False,type=1)
simplefile.new_folder_10(folder_name="new22222",is_success=False,type=1)
simplefile.new_folder_10(folder_name="file12345.txt",is_success=True,type=2)
simplefile.new_folder_10(folder_name="newnewnew",is_success=False,type=1)
simplefile.new_folder_10(folder_name="filefilefile.txt",is_success=True,type=2)
simplefile.new_folder_10(folder_name="newtest",is_success=False,type=1)
simplefile.new_folder_10(folder_name="testnew.txt",is_success=True,type=2)
simplefile.my_click_classname("android.widget.RelativeLayout",0)
# simplefile.my_click_id("android:id/button_once")
simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","123321")
simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","saasaasaa")
simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","ddfdfffdf")
simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","321321")
simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","43434434")
simplefile.my_edit_id("com.simplemobiletools.filemanager.pro:id/read_text_view","hghghggg")
simplefile.my_back()
simplefile.long_click_1(sum=1, select_list=[0])
simplefile.delete_file_7(is_success=True)
simplefile.my_back()
simplefile.my_back()
simplefile.long_click_1(sum=5, select_list=[3,4])
simplefile.menu_13()
simplefile.compress_2(name="testfor2",is_success=False)
simplefile.menu_13()
simplefile.compress_2(name="compresscom",is_success=False)
simplefile.menu_13()
simplefile.compress_2(name="compresscom22",is_success=False)
simplefile.menu_13()
simplefile.compress_2(name="test22test",is_success=False)
simplefile.menu_13()
simplefile.compress_2(name="213213sqadas",is_success=False)
simplefile.my_back()
simplefile.my_back_home()

simplefile.get_screen_info()
