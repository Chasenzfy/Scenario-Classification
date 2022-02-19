import time
import os
from appium import webdriver
from appium.webdriver.webdriver import T
import dvfile


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'dv.fileexplorer.filebrowser.filemanager'
desired_caps['appActivity'] = 'dev.dworks.apps.anexplorer.DocumentsActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/13-DV/13-DV/screen'
xml_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/13-DV/13-DV/xml'
jump_pairs = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/13-DV/13-DV/jump_pairs.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

dvfile = dvfile.MyOIFM(driver, screen_path, xml_path, jump_pairs,'dev.dworks.apps.anexplorer.DocumentsActivity')

#test1 设置

dvfile.hometosdcard()
dvfile.file_browse_0(move_list=[0,1,-1,0,-1,1])
dvfile.my_back_home()
dvfile.sidebar_6()
dvfile.settings_14(theme_list=[0,2,1,1,0], checkbox_list=[0,2,3,1],checkbox_list_ori=[3,1,2,0])


dvfile.hometosdcard()
dvfile.file_browse_0(move_list=[0,0,0])

temp_list = [["zztest_1_0","zztest_1_1"], ["zztest_2"], ["zztest_3_0","zztest_3_1","zztest_3_2"], ["zztest_4_0","zztest_4_1","zztest_4_2"], ["zztest_5_0","zztest_5_1"]]
# temp_list = [["test_1_0","test_1_1"]]
# temp_list = [["test_2"]]
for i in range(len(temp_list)):
    length = len(temp_list[i])
    count = 0
    for filename in temp_list[i]:
        if count%2==0:
            dvfile.new_folder_10(isfile=True,folder_name=filename, is_success=True)
            count = count + 1
        else:
            dvfile.new_folder_10(isfile=False,folder_name=filename, is_success=True)
            count = count + 1
    for j in range(length):
        dvfile.long_click_1(sum=length,select_list=[j])
        tempname = temp_list[i][j] + "rename"
        dvfile.rename_12(name=tempname, is_success=True)
    for k in range(length):
        dvfile.long_click_1(sum=length,select_list=[k])
        dvfile.delete_file_7(is_success=False)
    for m in range(length):
        dvfile.search_3(temp_list[i][m])
    for n in range(length):
        dvfile.long_click_1(sum=length,select_list=[n])
        tempname = "00compress" + temp_list[i][n]
        dvfile.menu_13()
        dvfile.compress_2(name=tempname,password="123",show_password=False,is_success=True)
    for o in range(length):
        temp = o
        if length != 1:
            temp = temp + 1
        print(temp)
        dvfile.long_click_1(sum=length*2,select_list=[temp])
        dvfile.menu_13()
        tempsuccess = False
        print(o)
        print(length)
        if o == length-1:
            tempsuccess = True
        dvfile.umcompress_8(is_success=tempsuccess,choose_path=True,move_list=[0,0,0],is_code=True,code="123")
    for p in range(length):
        dvfile.long_click_1(sum=length*3,select_list=[p])
        dvfile.menu_13()
        dvfile.properties_browse_11()
    # newarr = range(length*3)
    # newlist = list(newarr)
    dvfile.long_click_1(sum=length*3,select_list=[0])
    dvfile.my_click_text("Select All")
    dvfile.delete_file_7(is_success=True)


dvfile.new_folder_10(isfile=True,folder_name="3.txt", is_success=True)
dvfile.my_click_classname("android.widget.FrameLayout", 0)
dvfile.my_click_id("android:id/button_once")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","123456")
dvfile.my_click_accessibilty_id("Revert")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","321543")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","adbd")
dvfile.my_click_accessibilty_id("Save")
dvfile.my_click_accessibilty_id("Navigate up")

dvfile.long_click_1(sum=1,select_list=[0])
dvfile.to_paste_4(pre_num=1, is_paste=False, move_list=[-1,-1,-1,1,-1,2,-1,0,1,-1,0,0])

dvfile.new_folder_10(isfile=True,folder_name="2.txt", is_success=True)
dvfile.my_click_classname("android.widget.FrameLayout", 0)
dvfile.my_click_id("android:id/button_once")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","vasdxz")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","wqewqewq")
dvfile.my_click_accessibilty_id("Revert")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","21321sad")
dvfile.my_click_accessibilty_id("Revert")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","vfdasfa")
dvfile.my_click_accessibilty_id("Save")
dvfile.my_click_accessibilty_id("Navigate up")


dvfile.long_click_1(sum=2,select_list=[0,1])
dvfile.to_paste_4(pre_num=2, is_paste=False, move_list=[-1,-1,1,-1,-1,3,-1,0,0,0])

dvfile.long_click_1(sum=2,select_list=[0])
dvfile.menu_13()
dvfile.to_paste_4_copyto(pre_num=2,is_paste=False,move_list=[0,1,-1,-1,2,-1,0,0])

dvfile.long_click_1(sum=2,select_list=[1])
dvfile.menu_13()
dvfile.to_paste_4_copyto(pre_num=2,is_paste=False,move_list=[1,-1,0,1,-1,0,0])

dvfile.new_folder_10(isfile=True,folder_name="1.txt", is_success=True)
dvfile.my_click_classname("android.widget.FrameLayout", 0)
dvfile.my_click_id("android:id/button_once")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","testestse")
dvfile.my_click_accessibilty_id("Revert")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","fdsr1234")
dvfile.my_click_accessibilty_id("Revert")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","sada2134")
dvfile.my_click_accessibilty_id("Revert")
dvfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","eqseda")
dvfile.my_click_accessibilty_id("Save")
dvfile.my_click_accessibilty_id("Navigate up")

dvfile.long_click_1(sum=3,select_list=[0,1])
dvfile.menu_13()
dvfile.compress_2(name="000",show_password=False,is_success=True)

dvfile.long_click_1(sum=4,select_list=[1,3])
dvfile.menu_13()
dvfile.compress_2(name="testcom",show_password=True,password="221123",is_success=False)

dvfile.long_click_1(sum=4,select_list=[0])
dvfile.menu_13()
dvfile.umcompress_8(is_success=True,choose_path=False)

dvfile.my_click_classname("android.widget.FrameLayout", 0)
dvfile.my_back()
dvfile.long_click_1(5,select_list=[0])
dvfile.my_click_text("Select All")
dvfile.delete_file_7(is_success=True)
dvfile.file_browse_0(move_list=[-1,-1,-1,-1])
######

dvfile.hometosdcard()
dvfile.long_click_1(sum=5,select_list=[0])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.long_click_1(sum=5,select_list=[1])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.file_browse_0(move_list=[0])
dvfile.long_click_1(sum=2,select_list=[0])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.long_click_1(sum=2,select_list=[1])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.file_browse_0(move_list=[1])
dvfile.long_click_1(sum=3,select_list=[0])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.long_click_1(sum=3,select_list=[1])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.long_click_1(sum=3,select_list=[2])
dvfile.menu_13()
dvfile.properties_browse_11()
dvfile.long_click_1(sum=3,select_list=[0])
dvfile.delete_file_7(is_success=False)
dvfile.long_click_1(sum=3,select_list=[1])
dvfile.delete_file_7(is_success=False)
dvfile.long_click_1(sum=3,select_list=[2])
dvfile.delete_file_7(is_success=False)