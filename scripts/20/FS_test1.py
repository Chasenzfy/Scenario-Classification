import time
import os
from appium import webdriver
from appium.webdriver.webdriver import T
import fsfile


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.ioapps.fsexplorer'
desired_caps['appActivity'] = 'com.ioapps.fsexplorer.MainActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/20-FS/20-FS/screen'
xml_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/20-FS/20-FS/xml'
jump_pairs = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/20-FS/20-FS/jump_pairs.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

fsfile = fsfile.MyOIFM(driver, screen_path, xml_path, jump_pairs,'com.ioapps.fsexplorer.MainActivity')

# #test1 设置

fsfile.hometosdcard()
fsfile.file_browse_0(move_list=[0,1,-1,0,-1,1])
fsfile.my_back_home()
#fsfile.settings_14(style_list=[0,2,1,3,4], icon_list=[0,2,3,1],checkbox_list=[3,1,2,0])
fsfile.settings_14(style_list=[0], icon_list=[0],checkbox_list=[3])



fsfile.hometosdcard()
fsfile.file_browse_0(move_list=[0,1,0])

# temp_list = [["zztest_1_0","zztest_1_1"], ["zztest_2"], ["zztest_3_0","zztest_3_1","zztest_3_2"], ["zztest_4_0","zztest_4_1","zztest_4_2"], ["zztest_5_0","zztest_5_1"]]
# temp_list = [["test_1_0","test_1_1"]]
# temp_list = [["test_1_0","test_1_1","test_1_2"],["test_2"],["test_1_0","test_1_1"]]
# temp_list = [["test_2"]]
temp_list = [["test_1_0","test_1_1","test_1_2"],["test_2"],["test_3_0","test_3_1"],["test_4_0","test_4_1"],["test_5_0","test_5_1","test_5_2"],["test_6"]]
for i in range(len(temp_list)):
    time.sleep(10)
    length = len(temp_list[i])
    count = 0
    for filename in temp_list[i]:
        if count%2==0:
            fsfile.new_folder_10(isfile=True,folder_name=filename, is_success=True)
            count = count + 1
        else:
            fsfile.new_folder_10(isfile=False,folder_name=filename, is_success=True)
            count = count + 1
    for j in range(length):
        fsfile.long_click_1(sum=length,select_list=[j])
        tempname = temp_list[i][j] + "rename"
        fsfile.rename_12(name=tempname, is_success=True)
    for k in range(length):
        fsfile.long_click_1(sum=length,select_list=[k])
        fsfile.delete_file_7(is_success=False)
        fsfile.my_back()
    for m in range(length):
        fsfile.search_3(type=0,size=1,time=1,text=temp_list[i][m],hierarchy=True,is_success=True)
        fsfile.search_3(type=5,size=0,time=0,text=temp_list[i][m],hierarchy=False,is_success=True)
    #for n in range(length):
    fsfile.long_click_1(sum=length,select_list=[0])
    tempname = "00compress" + temp_list[i][0]
    fsfile.compress_2(name=tempname,password="123",path=[],type=1,level=1,is_success=False,is_hiden=True)
    fsfile.compress_2(name=tempname,password="1234",path=[],type=0,level=2,is_success=True,is_hiden=False)
    #for o in range(length):
        # temp = o
        # if length != 1:
        #     temp = temp + 1
        # print(temp)
    temp = 1
    if length == 1:
        temp = 0
    fsfile.long_click_1(sum=length*2,select_list=[temp])
    fsfile.umcompress_8(is_success=False,name="extract1",choose_path=True,move_list=[-1,-1,1],extract_here=False,code="1234")
    fsfile.umcompress_8(is_success=True,name="extract2",choose_path=True,move_list=[-1,-1,-1],extract_here=True,code="1234")
    for p in range(length):
        fsfile.long_click_1(sum=length*3,select_list=[p])
        fsfile.properties_browse_11()
    # newarr = range(length*3)
    # newlist = list(newarr)
    fsfile.long_click_1(sum=length*3,select_list=[0])
    fsfile.my_click_text_start("Selection")
    fsfile.my_click_text_start("Select")
    fsfile.delete_file_7(is_success=True)

fsfile.file_browse_0(move_list=[-1,-1,-1,-1])


fsfile.hometosdcard()
fsfile.file_browse_0(move_list=[0,1,0])

fsfile.new_folder_10(isfile=True,folder_name="3.txt",is_success=False)
fsfile.new_folder_10(isfile=True,folder_name="1.txt",is_success=True)
fsfile.file_browse_0(move_list=[0])
try:
    fsfile.my_click_text_start("Edit")
    fsfile.my_click_text_start("Just")
except:
    print("nochoice")
fsfile.my_click_classname("android.widget.ImageView",2)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editText","asdasxzc")
fsfile.my_click_classname("android.widget.ImageView",2)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editText","das213")
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",2)
fsfile.my_click_text("Cancel")
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",3)
fsfile.my_click_text("Cancel")
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",4)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editTextInput","21312")
fsfile.my_click_text("Cancel")
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",4)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editTextInput","213")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchMatchCase")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchRegex")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchMultiLine")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchRegex")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchCompleteWord")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchMatchCase")
fsfile.my_click_id("com.ioapps.fsexplorer:id/switchCompleteWord")
fsfile.my_click_text("Accept")
fsfile.my_click_classname("android.widget.ImageView",2)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editText","213213")
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",0)
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",1)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editText","123csda")
fsfile.my_click_classname("android.widget.ImageView",3)
fsfile.my_click_classname("android.widget.LinearLayout",0)
fsfile.my_edit_id("com.ioapps.fsexplorer:id/editText","qevc341")
fsfile.my_back()
fsfile.my_click_text("Yes")
fsfile.my_back()
fsfile.long_click_1(sum=0,select_list=[0])
fsfile.delete_file_7(is_success=True)
fsfile.file_browse_0(move_list=[-1,-1,-1,-1])
# fsfile.get_screen_info()



fsfile.hometosdcard()
fsfile.file_browse_0(move_list=[0,1,0])
fsfile.new_folder_10(isfile=True,folder_name="paste1.txt",is_success=True)
fsfile.new_folder_10(isfile=True,folder_name="paste2.txt",is_success=True)

fsfile.long_click_1(sum=2,select_list=[0])
fsfile.to_paste_4(pre_num=2, paste_list=[0],is_paste=False,clean=False, move_list=[-1,-1,1])
fsfile.file_browse_0(move_list=[0])
fsfile.long_click_1(sum=2,select_list=[1])
fsfile.to_paste_4(pre_num=1, paste_list=[],is_paste=True,clean=False, move_list=[-1,-1,1])
time.sleep(5)
fsfile.file_browse_0(move_list=[0])
fsfile.long_click_1(sum=2,select_list=[0])
fsfile.to_paste_4_copyto(pre_num=2,is_paste=False,move_list=[-1,-1,1,0])
fsfile.long_click_1(sum=2,select_list=[0])
fsfile.to_paste_4_copyto(pre_num=1,is_paste=True,move_list=[-1,-1,-1,1,-1,0,1,0])
fsfile.file_browse_0(move_list=[-1,-1,-1,-1])
fsfile.get_screen_info()
#end


# fsfile.new_folder_10(isfile=True,folder_name="3.txt", is_success=True)
# fsfile.my_click_classname("android.widget.FrameLayout", 0)
# fsfile.my_click_id("android:id/button_once")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","123456")
# fsfile.my_click_accessibilty_id("Revert")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","321543")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","adbd")
# fsfile.my_click_accessibilty_id("Save")
# fsfile.my_click_accessibilty_id("Navigate up")

# fsfile.long_click_1(sum=1,select_list=[0])
# fsfile.to_paste_4(pre_num=1, is_paste=False, move_list=[-1,-1,-1,1,-1,2,-1,0,1,-1,0,0])

# fsfile.new_folder_10(isfile=True,folder_name="2.txt", is_success=True)
# fsfile.my_click_classname("android.widget.FrameLayout", 0)
# fsfile.my_click_id("android:id/button_once")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","vasdxz")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","wqewqewq")
# fsfile.my_click_accessibilty_id("Revert")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","21321sad")
# fsfile.my_click_accessibilty_id("Revert")
# fsfile.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/hh","vfdasfa")
# fsfile.my_click_accessibilty_id("Save")
# fsfile.my_click_accessibilty_id("Navigate up")

