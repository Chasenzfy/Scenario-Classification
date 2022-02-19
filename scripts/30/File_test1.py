# -*- coding:utf8 -*-
import os
import time
from appium import webdriver
import File

mypath = os.path.dirname(os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.photovideotools.file.manager'
desired_caps['appActivity'] = ".DocumentsActivity"
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

# test 1、主界面的文件浏览
# 回到主界面
file.my_back_home()

file.my_back_home1()

file.settings_14()
file.my_back()


file.file_browse_0(move_list=[0, -1,
                              1, -1,
                              2, 0, -1,
                              1, -1,
                              2, -1, -1,
                              3, -1,
                              4, -1,
                              5, -1,
                              6, -1])

file.long_click_1(select_list=[0, 1, 2, 3, 4, 5, 6])
file.my_back()
file.long_click_1(select_list=[6, 5, 4, 3, 2, 1, 0])
file.my_back()
file.long_click_1(select_list=[1, 3, 5])
file.my_back()
file.long_click_1(select_list=[2, 4, 6])
file.my_back()
file.long_click_1(select_list=[1, 3, 6, 3])
file.my_back()
file.long_click_1(select_list=[3, 5, 3])
file.my_back()
file.long_click_1(select_list=[1, 2, 3, 4, 6])
file.my_back()
file.long_click_1(select_list=[2, 5, 4, 1, 3])
file.my_back()

file.my_back_home1()
file.search_3(text="1")
file.search_3(text="2")
file.search_3(text="3")
file.search_3(text="4")
file.search_3(text="5")
file.search_3(text="6")
file.search_3(text="7")
file.search_3(text="8")

file.search_3(text="19")
file.search_3(text="10")
file.search_3(text="17")
file.search_3(text="15")

file.search_3(text="113213123")

file.menu_13()
file.new_folder_10(folder_name="a", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="ab", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="ac", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="ad", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="ae", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="af", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="ag", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="ahh", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="aasdad", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="aert", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="tgra", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="fa", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="23rfa", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="dsfsva", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="adfegrb  rwf", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="asfbew", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="aasgte", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="aewdefa", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="agtgtge", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="a", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="a", is_success=False)
file.menu_13()
file.new_folder_10(folder_name="a", is_success=False)

temp_list = [[0], [1], [2], [3], [4], [5], [6]]

for i in range(len(temp_list)):
    file.long_click_1(select_list=temp_list[i])
    file.properties_browse_11()

    file.long_click_1(select_list=temp_list[i])
    file.rename_12()

    file.long_click_1(select_list=temp_list[i])
    file.rename_12(name="rename" + str(i), is_success=False)

    file.long_click_1(select_list=temp_list[i])
    file.delete_file_7(is_success=False)

    file.long_click_1(select_list=temp_list[i])
    file.to_paste_4()

file.long_click_1(select_list=[1, 3, 5, 7])
file.delete_file_7(is_success=False)

file.long_click_1(select_list=[1, 2, 3, 5, 7])
file.delete_file_7(is_success=False)

file.long_click_1(select_list=[1, 3, 4, 5, 7])
file.delete_file_7(is_success=False)

file.long_click_1(select_list=[1, 3, 4, 5, 7])
file.delete_file_7(is_success=False)

file.long_click_1(select_list=[0, 1, 3, 5, 7])
file.delete_file_7(is_success=False)

file.long_click_1(select_list=[0, 1, 3, 5, 6, 7])
file.delete_file_7(is_success=False)

file.long_click_1(select_list=[1, 2])
file.to_paste_4()

file.long_click_1(select_list=[0, 1, 2])
file.to_paste_4()

file.long_click_1(select_list=[1, 2, 3, 4])
file.to_paste_4()

file.long_click_1(select_list=[0, 1, 2, 3, 4])
file.to_paste_4()

file.long_click_1(select_list=[0, 1, 2, 3, 4, 5])
file.to_paste_4()

file.long_click_1(select_list=[0, 1, 2, 3, 4, 5])
file.to_paste_4()

file.long_click_1(select_list=[0, 1, 2, 3, 4, 5, 6])
file.to_paste_4()

file.file_browse_0(move_list=[0])

temp_list = [[0], [1], [2], [3], [4], [5], [6]]

for i in range(len(temp_list)):
    file.long_click_1(select_list=temp_list[i])
    file.properties_browse_11()

file.my_back()

file.get_screen_info()
