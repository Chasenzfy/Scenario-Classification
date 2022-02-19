# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
import os.path

from selenium.common.exceptions import NoSuchElementException

import MaterialFiles


mypath = os.path.dirname(os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'me.zhanghai.android.files'
desired_caps['appActivity'] = '.filelist.FileListActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = False


screen_path = mypath + '/screen/'
xml_path = mypath + '/xml/'
jump_pairs = mypath + '/jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

material = MaterialFiles.MaterialFiles(driver, screen_path, xml_path, jump_pairs, activity_info)

# try:
#     if material.driver.find_element_by_id("com.android.permissioncontroller:id/content_container") is not None:
#         material.my_click_id("com.android.permissioncontroller:id/permission_allow_button",0)
# except NoSuchElementException:
#     flag = False

# material.file_browse_0([0,0,-1,-1,1,-1,2,-1,3,-1,4,0,-1,-1])
# material.file_browse_0([2,1])
# material.my_back_home()
#
# material.search_3("123")
# material.search_only_3("pp")
# material.search_only_3(".zip")
# material.search_3(".txt")
#
# material.search_3(".mp3")
#
# material.file_browse_0([0])
# material.to_paste_4(copy_list=[1,2,3],move_list=[1,2,3,4],end=3)
#
# material.long_click_delete_7([0,2,3],is_success=False)
# material.long_click_delete_7([2,3],is_success=True)
# material.new_folder_10("ccsaef",True)
# material.my_back_home()
#
# material.file_browse_0([4])
# material.to_paste_43(copy_list=[2,3],move_list=[3,0,-1,-1,2],end=0)
# material.my_back_home()
# material.to_paste_43(copy_list=[0,4],move_list=[2],end=1)
# material.my_back()
# material.new_file_10("aaaass")
# material.new_file_10("abc.txt")
# material.my_back_home()

# material.file_browse_0([2])
# material.new_file_10("abc.txt",True)
# material.text_edit_9("abc.txt")
# material.my_back_home()
#
# material.file_browse_0([2])
# material.text_edit_9("aaa.txt","safeasdsas")
# material.my_back_home()
#
# material.file_browse_0([2])
# for i in range(4):
#     material.properties_11(i)
#
# material.file_browse_0([1,0])
# for i in range(7):
#     material.properties_11(i)
# material.my_back_home()
#
# material.file_browse_0([2,1,0])
# material.long_click_select_1(begin_index=0)
# material.long_click_select_1(begin_index=2)
# material.long_click_select_1(begin_index=4)
# material.my_back_home()
#
# material.file_browse_0([3])
# material.text_edit_9("lll.txt","aklfasdk;lk;lsdfc[psdas")
# material.copy_43(1,move_list=[-1,1,-1,2,0,-1,-1,3],end=0)
# material.my_back()
# material.my_back()
#
# material.file_browse_0([2,1,1])
# material.long_click_delete_7([2,3],True)
# material.file_browse_0([0])
# material.compress_2(compress_list=[0,2],is_cancel=False,file_type=2)
# material.compress_2_1(0,is_cancel=False,file_type=1)
# material.delete_7(0,is_success=True)
# material.long_click_delete_7([0,1],is_success=True)
#
# material.my_back()
# material.compress_2(compress_list=[1,2],is_cancel=False,file_type=0)
#
# material.new_file_10("sssdiiof.txt",is_success=True)
# material.text_edit_9("sssdiiof.txt","dfoihajpsc")
# material.my_back()
# material.my_back_home()

# material.file_browse_0([4])
# material.extract_8(4,move_list=[-1,0,0,-1,-1,2,-1,3],end_index=0)
# material.file_browse_0([-1,-1,4])
# material.delete_7(4,is_success=True)
# material.new_file_10("ammm.txt")
# material.new_file_10("attt.txt",True)
# material.text_edit_9("attt.txt","\nnidiujlk")
# material.my_back_home()
#
# material.file_browse_0([4])
# material.extract_8(4,move_list=[0,-1,-1,2],end_index=0)
# material.my_back_home()
# material.file_browse_0([2])
# material.text_edit_9("abc.txt","daoidglkjvz")
# material.compress_2(compress_list=[2,3],is_cancel=False,file_type=2)
# material.my_back()
#
# material.search_3(".jpg")
# material.search_3(".png")
# material.search_3("ccsaef")
# material.search_3("attt.txt")
# material.search_3("jjllkop")
# material.file_browse_0([2,1,0])
# material.compress_2(compress_list=[1,3],is_cancel=False,file_type=2)
# material.compress_2(compress_list=[2,4],is_cancel=False,file_type=1)
# material.delete_7(delete_index=1,is_success=True)
# material.new_folder_10("fdasvvz",is_success=True)
# material.new_folder_10("vfdadf",is_success=False)
# material.new_folder_10("bbozpa",is_success=True)
# material.new_folder_10("ppdfmaz",is_success=False)
# material.new_folder_10("oppsd",is_success=True)
# material.new_file_10("000vvv.txt",is_success=True)
# material.new_file_10("999.txt",is_success=True)
# material.text_edit_9("000vvv.txt","gdwopapodfbl\ndioafhsf")
#
#
# material.long_click_delete_7(delete_list=[1,4],is_success=False)
# material.my_back_home()

# material.file_browse_0([2,1,0])
# material.long_click_delete_7(delete_list=[2,6],is_success=True)
# material.copy_43(3,move_list=[-1,1,0,-1,-1,0],end=1)
# material.my_back()
# material.to_paste_4(copy_list=[4,5],move_list=None,end=2)
# material.my_back()

# material.file_browse_0([2,1,0])
# for i in range(8):
#     material.rename1_12(i,rename_name=material.generate_random_str(3),is_success=True)
# material.file_browse_0([0])
# material.rename1_12(0,rename_name=material.generate_random_str(6),is_success=True)
# material.my_back()
# for i in range(4):
#     material.properties_11(i)
#
# material.my_back_home()
# material.file_browse_0([2])
# for i in range(4):
#     material.rename1_12(i, rename_name=material.generate_random_str(4), is_success=False)
# for i in range(4):
#     material.rename1_12(i, rename_name=material.generate_random_str(6), is_success=True)
# material.my_back()
# material.file_browse_0([2])
# material.delete_7(3,is_success=True)
# material.extract_8(5,move_list=[1],end_index=0)
# material.my_back()
# material.my_back()
# material.delete_7(5,is_success=True)
# material.my_back()
# material.file_browse_0([2,0,0])
# material.extract_8(5,move_list=[1,-1,2,-1],end_index=0)
# material.my_back()
# material.long_click_delete_7(delete_list=[5],is_success=True)
# material.compress_2([2,3],is_cancel=True,file_type=1)
# material.my_back()
# material.long_click_delete_7(delete_list=[4],is_success=True)
# material.text_edit_9("sEL.txt","afiohoa[cpklasd")
# material.compress_2([1,4],is_cancel=False,file_type=2)
# material.my_back_home()
#
# material.file_browse_0([3])
# for i in range(4):
#     material.rename1_12(i,is_success=True,rename_name=material.generate_random_str(4))
# material.compress_2_1(2,is_cancel=False,file_type=0)
# material.compress_2_1(0,is_cancel=False,file_type=1)
# material.my_back()
#
# material.file_browse_0([3])
# material.new_folder_10("vaopsdop",is_success=True)
# material.new_file_10("cpasd.txt",is_success=True)
# material.new_folder_10("ppjjc",is_success=False)
# material.new_file_10("aaaapppx.txt",is_success=False)

# material.text_edit_9("NGQC.txt","papfsfsd")
# for i in range(4):
#     material.rename1_12(i,is_success=True,rename_name=material.generate_random_str(4))
# material.my_back()
# material.file_browse_0([3])
# material.extract_8(5,move_list=[0,-1,1,0,0,-1,-1,-1],end_index=0)
# material.my_back()
# material.cut_4(cut_index=2,end_index=0)
# material.my_back()
# material.copy_4(cut_index=2,end_index=0)
# material.my_back()
# material.cut_4(cut_index=2,end_index=0)
# material.my_back()
# material.text_edit_9("0CvN.txt","opvoasjo-al;sfjop")
# material.my_back()
# material.long_click_delete_7([2],is_success=True)
# material.extract_8(5,move_list=None,end_index=0)
# material.my_back()
# material.delete_7(5,is_success=True)
# material.my_back()
# for i in range(2):
#     material.add_bookmark_15([i])
#     material.browse_bookmark_15(i)
#     material.my_back_home()
#
# material.file_browse_0([2])
# material.add_bookmark_15([1])
# material.browse_bookmark_15(2)
#
# material.rename_bookmark_15(rename_index=0,text="123000sz",is_success=False)
# material.my_back()
# #
# material.rename_bookmark_15(rename_index=1,text="slv",is_success=True)
# material.my_back()
#
# material.rename_bookmark_15(rename_index=0,text=material.generate_random_str(5),is_success=True)
# material.my_back()
#
# material.rename_bookmark_15(rename_index=1,text=material.generate_random_str(4),is_success=True)
# material.my_back()
#
# material.rename_bookmark_15(rename_index=2,text=material.generate_random_str(3),is_success=True)
# material.my_back()
# material.rename_bookmark_15(rename_index=1,text=material.generate_random_str(6),is_success=True)
# material.my_back()
# material.rename_bookmark_15(rename_index=0,text=material.generate_random_str(2),is_success=True)
# material.my_back()
#
# material.delete_bookmark_15([0,0,0])
# material.my_back()
# material.my_back_home()
# material.file_browse_0([2])
# for i in range(2):
#     material.add_bookmark_15([i])
#     material.browse_bookmark_15(i)
#     material.my_back_home()
# material.file_browse_0([3])
# for i in range(2):
#     material.add_bookmark_15([i])
#     material.browse_bookmark_15(i)
#     material.my_back_home()
# material.rename_bookmark_15(rename_index=0,text=material.generate_random_str(5),is_success=True)
# material.my_back()
#
# material.rename_bookmark_15(rename_index=1,text=material.generate_random_str(4),is_success=True)
# material.my_back()
#
# material.rename_bookmark_15(rename_index=2,text=material.generate_random_str(3),is_success=True)
# material.my_back()
# material.rename_bookmark_15(rename_index=3,text=material.generate_random_str(6),is_success=True)
# material.my_back()
# material.rename_bookmark_15(rename_index=0,text=material.generate_random_str(2),is_success=True)
# material.my_back()
#
# material.delete_bookmark_15([0,0,0,0])
# material.my_back()
material.my_to_settings()
material.my_settings()
material.my_click_text("Standard folders")
material.my_back()
# material.my_click_text("Open Android package")
# material.my_back()

time.sleep(2)
material.my_click_id("me.zhanghai.android.files:id/switchWidget",0)
material.my_click_id("me.zhanghai.android.files:id/switchWidget",0)
material.my_swipe(start_x=860,start_y=860,end_x=860,end_y=1100,duration=100)
material.my_swipe(start_x=860,start_y=860,end_x=860,end_y=1100,duration=100)
material.get_screen_info()

driver.quit()
