# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
import os.path
import Amaze


mypath = os.path.dirname(os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'com.amaze.filemanager'
desired_caps['appActivity'] = '.ui.activities.MainActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = False


screen_path = mypath + '/screen/'
xml_path = mypath + '/xml/'
jump_pairs = mypath + '/jump_pairs.txt'
activity_info = 'activity_info.txt'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

amaze = Amaze.Amaze(driver, screen_path, xml_path, jump_pairs,activity_info)

# 0 文件浏览 and 6
# amaze.file_browse_0(move_list=[0])
# amaze.menu_13()
# amaze.my_back()
# amaze.my_back_home()
#
# amaze.file_browse_0(move_list=[0, 0])
# amaze.menu_13()
# amaze.my_back()
# amaze.my_back_home()
#
# amaze.file_browse_0(move_list=[1])
# amaze.menu_13()
# amaze.my_back()
# amaze.my_back_home()
#
#
# amaze.search_3("123")
# amaze.my_back_home()
#
# amaze.search_3("test")
# amaze.my_back_home()

# test 10
# amaze.new_folder_10()
# amaze.new_folder_10("123_test")
# amaze.new_file_10()
# amaze.new_file_10("skaldjals")
# amaze.new_folder_10("123cbjsdkh",True)
# amaze.new_folder_10("123sdascxzz",True)
# amaze.new_folder_10("123uucliid",True)
# amaze.new_folder_10("123pppckjdjlla",True)
# amaze.new_folder_10("123fdvcoasid",True)
# amaze.new_file_10("dsackopsa")
# amaze.new_file_10("coopasdc")
# amaze.new_file_10("aaffllsasd")
#
# amaze.search_3("123")
# amaze.my_back_home()
#
# amaze.search_3("cbjsdkh")
# amaze.my_back_home()
#
# amaze.search_3("sdascxzz")
# amaze.my_back_home()
#
# amaze.search_3("uucliid")
# amaze.my_back_home()
#
# amaze.search_3("ppp")
# amaze.my_back_home()

# amaze.file_browse_0(move_list=[0])
# amaze.new_file_10("lll.txt", True)
# amaze.text_edit_9("lll.txt", "dsdadddss")
#
# amaze.my_back_home()

# amaze.file_browse_0(move_list=[0])
# for i in range(4):
#     amaze.my_click_id("com.amaze.filemanager:id/properties",i)
#     amaze.properties_only_11(False)
#
# for i in range(4):
#     amaze.my_click_id("com.amaze.filemanager:id/properties",i)
#     amaze.rename_12_only()
#
# amaze.my_back_home()
# for i in range(4):
#     amaze.my_click_id("com.amaze.filemanager:id/properties",i)
#     amaze.rename_12_only()
#
# amaze.file_browse_0(move_list=[0])
# amaze.long_click_select_1(0)
# amaze.long_click_select_1(2)
# amaze.to_paste_4(copy_list=[1,2],move_list=[1,2,3,4,5],end=2)
# amaze.my_back_home()
# amaze.file_browse_0([0])
# amaze.to_paste_4(copy_list=[0,1],move_list=[1,3],end=2)
# amaze.cancel_or_skip_4(is_cancel=True)
# amaze.my_back_home()
# amaze.file_browse_0([0])
# amaze.to_paste_4(copy_list=[0,1],end=2)
# amaze.cancel_or_skip_4(is_cancel=False)
# amaze.my_back_home()
# amaze.file_browse_0([0])
# amaze.to_paste_4(copy_list=[1,2,3],end=4)
# amaze.compress_2(compress_list=[0,1],is_cancel=True)
# amaze.compress_2(compress_list=[0],is_cancel=False)
# amaze.compress_2(compress_list=[1,2],is_cancel=False)
# amaze.delete_7(2,False)
# amaze.delete_7(2,True)
# amaze.my_back_home()
# amaze.file_browse_0([0])
# amaze.to_paste_4([0,3,4],4)
# amaze.compress_2(compress_list=[0,1],is_cancel=True)
# amaze.compress_2(compress_list=[0,1],is_cancel=False)
# amaze.delete_7(0,False)
# amaze.delete_7(1,True)
# amaze.long_click_delete_7(delete_list=[1,2],is_success=False)
# amaze.long_click_delete_7(delete_list=[1,2],is_success=True)
# amaze.long_click_delete_7(delete_list=[0,1],is_success=True)
# amaze.new_folder_10("123"+amaze.generate_random_str(8),is_success=True)
# amaze.new_folder_10("123"+amaze.generate_random_str(4),is_success=True)
#
# amaze.properties_11(is_detail=False,p_index=0)
# amaze.properties_11(is_detail=False,p_index=1)
# amaze.properties_11(is_detail=False,p_index=4)
# amaze.my_back_home()
# amaze.rename_12(file_index=2,is_success=True)
#
# amaze.file_browse_0([3])
# amaze.to_paste_41(cut_list=[0,2,3],end=4)
# amaze.my_back_home()
#
# amaze.file_browse_0([4])
# amaze.new_file_10("dddsss",is_success=True)
# amaze.new_folder_10("123"+amaze.generate_random_str(5),is_success=True)
#
# amaze.cut_4(cut_index=0, end_index=2)
# amaze.new_folder_10("123"+amaze.generate_random_str(8),is_success=True)
# amaze.new_folder_10("123"+amaze.generate_random_str(4),is_success=True)
#
# amaze.copy_4(cut_index=2,end_index=4)
# amaze.copy_4(cut_index=1,end_index=3)
#
# amaze.properties_11(is_detail=False,p_index=2)
# amaze.rename_12(file_index=2,is_success=True)
# amaze.properties_11(is_detail=False,p_index=2)
# amaze.copy_4(cut_index=2,end_index=1)
#
# amaze.new_file_10("cndi.txt",is_success=True)
# amaze.properties_11(is_detail=False,p_index=1)
# amaze.text_edit_9(file_name="cndi.txt",text="nlkafjpoj;lsak;dk;;;sfffddd",search_ch="k")
#
# amaze.properties_11(is_detail=False,p_index=1)
# amaze.my_back_home()
#
# amaze.search_only_3(text=".txt")
# amaze.my_back_home()
#
# amaze.search_only_3(text="1")
# amaze.my_back_home()
#
# amaze.search_only_3(text="fodaidfos")
# amaze.my_back_home()
#
# amaze.search_only_3(text=".zip")
# amaze.my_back_home()
# amaze.add_bookmark_15([0])
# amaze.browse_bookmark_15(0)
# amaze.my_back_home()
#
# amaze.add_bookmark_15([3])
# amaze.browse_bookmark_15(1)
# amaze.my_back_home()
#
# amaze.add_bookmark_15([5])
# amaze.browse_bookmark_15(2)
# amaze.my_back_home()
#
# amaze.file_browse_0([2])
#
# amaze.add_bookmark_15([0,1])
# amaze.my_back_home()
#
# amaze.browse_bookmark_15(1)
# amaze.my_back_home()
# amaze.browse_bookmark_15(4)
# amaze.my_back_home()
#
# amaze.browse_bookmark_15(2)
# amaze.my_back()
# amaze.my_back()
#
# amaze.delete_bookmark_15(delete_list=[2])
# amaze.my_back()
#
# amaze.rename_bookmark_15(rename_index=1,text="123ccfsgsz",is_success=False)
# amaze.my_back()
#
# amaze.rename_bookmark_15(rename_index=1,text="123slv",is_success=True)
# amaze.my_back()
# amaze.browse_bookmark_15(3)
# amaze.my_back_home()
#
# amaze.rename_bookmark_15(rename_index=0,text="123pplca",is_success=True)
# amaze.my_back()
# amaze.rename_bookmark_15(rename_index=3,text="123lll",is_success=True)
# amaze.my_back()
# amaze.rename_bookmark_15(rename_index=2,text="123ccc",is_success=True)
# amaze.my_back()
#
# amaze.delete_bookmark_15(delete_list=[0,1,0,0])
# amaze.my_back()
# amaze.my_to_settings()
# amaze.my_settings()
# amaze.get_screen_info()

amaze.my_to_settings()
amaze.my_swipe(406, 300, 406, 100, 100)
amaze.my_swipe(406, 300, 406, 100, 100)
amaze.my_swipe(406, 500, 406, 100, 100)
amaze.my_click_accessibilty_id("Navigate up")
amaze.file_browse_0([2])
amaze.delete_7(1,True)
amaze.compress_2([0,1,2],is_cancel=False)
amaze.delete_7(0,is_success=True)
amaze.delete_7(0,is_success=True)
amaze.my_back()
amaze.file_browse_0([3])
amaze.compress_2([0],is_cancel=False)
amaze.my_back()
amaze.file_browse_0([4])
amaze.compress_2([0,1],is_cancel=True)
amaze.compress_2([3],is_cancel=False)
amaze.long_click_delete_7([0,1,2],is_success=True)
amaze.my_back()
amaze.long_click_delete_7([1,5],is_success=True)
amaze.file_browse_0([4])
amaze.compress_2([0,1],is_cancel=False)
amaze.compress_2([1,2],is_cancel=False)
amaze.get_screen_info()
time.sleep(2)
driver.quit()
