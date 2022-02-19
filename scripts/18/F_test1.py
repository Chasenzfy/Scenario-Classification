import time
import os
from appium import webdriver
from appium.webdriver.webdriver import T
import ffile


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.cvinfo.filemanager'
desired_caps['appActivity'] = 'com.cvinfo.filemanager.activities.MainActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True


screen_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/18-file/18-file/screen'
xml_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/18-file/18-file/xml'
jump_pairs = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/18-file/18-file/jump_pairs.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)
time.sleep(10)

nfile = ffile.MyOIFM(driver, screen_path, xml_path, jump_pairs,'com.cvinfo.filemanager.activities.MainActivity')

#test1 设置
print("start")
#nfile.hometosdcard()
#nfile.file_browse_0(move_list=[0,1,0])
#nfile.long_click_1(select_list=[0,2])
#nfile.compress_2(name="123",password="3321",is_success=False)
#nfile.search_3(text="1")
# nfile.umcompress_8(is_success=False,move_list=[-1,-1,0],index=0)
# nfile.long_click_1(select_list=[1])
# nfile.delete_file_7(way=0,is_success=True)
# nfile.long_click_1(select_list=[0])
# nfile.delete_file_7(way=1,is_success=True)

#nfile.settings_14(style_list=[0,2,1,3,4], icon_list=[0,2,3,1],checkbox_list=[3,1,2,0])
#nfile.settings_14(style_list=[0], icon_list=[0],checkbox_list=[3])
#nfile.properties_browse_11(index=[0,1],type=0)
#nfile.properties_browse_11(index=[1],type=1)

#list1 01234
#list2 3 numbers
#list3 012
#list4 012
#nfile.settings_14(list1=[0,3,1,2,4,1,0,2,4,3],list2=[2,3,1],list3=[1,0,2,0,2,1],list4=[0,1])

## run start
# nfile.hometosdcard()
# nfile.file_browse_0(move_list=[0,1,0])
# nfile.settings_14(list1=[0,3,1,2,0,4,1,3,0,1,4,2],list2=[2,3,1],list3=[1,0,2,0,1,2,0,1,2],list4=[0,1])


# temp_list = [["z18ztest_1_0","z18ztest_1_1"], ["z18ztest_2"], ["z18ztest_3_0","z18ztest_3_1","z18ztest_3_2"], ["z18ztest_4_0","z18ztest_4_1","z18ztest_4_2"], ["z18ztest_5_0","z18ztest_5_1"]]
# #temp_list = [["test_1_0","test_1_1","test_1_2"],["test_2"],["test_3_0","test_3_1"],["test_4_0","test_4_1"],["test_5"]]
# #temp_list = [["test_2"]]
# #temp_list = [["test_1_0","test_1_1"]]
# #temp_list = [["test_1_0","test_1_1","test_1_2"]]
# # temp_list = [["test_1_0","test_1_1","test_1_2"],["test_2"],["test_3_0","test_3_1"],["test_4_0","test_4_1"],["test_5_0","test_5_1","test_5_2"],["test_6"]]
# for i in range(len(temp_list)):
#     time.sleep(5)
#     length = len(temp_list[i])
#     count = 0
#     for filename in temp_list[i]:
#         if count%2==0:
#             nfile.new_folder_10(isfile=True,folder_name=filename, is_success=True)
#             count = count + 1
#         else:
#             nfile.new_folder_10(isfile=False,folder_name=filename, is_success=True)
#             count = count + 1


#     tempname = temp_list[i][0] + "_rename"
#     tempname2 = tempname + "muti1"
#     tempname3 = tempname + "muti3"
#     newarr = range(length)
#     newlist = list(newarr)
#     nfile.rename_12(name=tempname,index=[0],type=0,is_success=False)
#     nfile.rename_12(name=tempname,index=[length-1],type=0,is_success=True)
#     nfile.rename_12(name=tempname2,number="00",extension=".txt",index=newlist,type=1,mutitype=0,is_success=False)
#     nfile.rename_12(name=tempname2,number="01",extension=".tmp",index=newlist,type=1,mutitype=0,is_success=True)
#     nfile.rename_12(number="000",extension=".test",index=newlist,type=1,mutitype=1,is_success=True)
#     nfile.rename_12(name=tempname3,name2="testsuff",number="0",extension=".try",index=newlist,type=1,mutitype=2,is_success=True)

#     for k in range(length):
#         nfile.long_click_1(select_list=[k])
#         nfile.delete_file_7(way=0,is_success=False)
#         nfile.long_click_1(select_list=[k])
#         nfile.delete_file_7(way=1,is_success=False)
#     for m in range(length):
#         nfile.search_3(text=temp_list[i][m])
#     nfile.search_3(text="test")
#     nfile.search_3(text="1")
#     nfile.search_3(text="2")

#     #for n in range(length):
#     nfile.long_click_1(select_list=[0])
#     tempname = "00compress" + temp_list[i][0] + '.zip'
#     tempname2 = "11compress" + temp_list[i][0]+ '.zip'
#     #有密码时无法正确解压
#     nfile.compress_2(name=tempname,password="123",is_success=False)
#     nfile.long_click_1(select_list=[0])
#     nfile.compress_2(name=tempname2,is_success=True)
#     #for o in range(length):
#         # temp = o
#         # if length != 1:
#         #     temp = temp + 1
#         # print(temp)
#     temp = length//2
#     if i == 0 or i == 1:
#         nfile.umcompress_8(is_success=False,move_list=[-1,-1,0,-1,-1,4,0,-1,1,-1,2,-1,-1,5,-1,3,-1,6],index=temp)
#     nfile.umcompress_8(is_success=True,move_list=[-1,0],index=temp)

#     newarr = range(length+2)
#     newlist = list(newarr)
#     nfile.properties_browse_11(index=newlist,type=0)
#     # newarr = range(length*3)
#     # newlist = list(newarr)
#     nfile.long_click_1(select_list=newlist)
#     nfile.delete_file_7(way=0,is_success=True)

# nfile.file_browse_0(move_list=[-1,-1,-1])
# nfile.backtohome()

# nfile.hometosdcard()
# nfile.file_browse_0(move_list=[0,1,0])

# nfile.new_folder_10(isfile=True,folder_name="test3.txt",is_success=False)
# nfile.new_folder_10(isfile=True,folder_name="test1.txt",is_success=True)
# nfile.file_browse_0(move_list=[0])

# nfile.my_click_text("Text Reader")
# nfile.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")

# nfile.my_edit_id("com.cvinfo.filemanager:id/fname","ttttqqq111qqtt212")
# nfile.my_click_accessibilty_id("Find in page")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","qq")
# nfile.my_click_id("com.cvinfo.filemanager:id/close")
# nfile.my_click_accessibilty_id("Find in page")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","ttt")
# nfile.my_clear_id("com.cvinfo.filemanager:id/search_box")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","11")
# nfile.my_click_id("com.cvinfo.filemanager:id/close")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_click_accessibilty_id("Save")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Open with")
# nfile.my_back()
# nfile.my_edit_id("com.cvinfo.filemanager:id/fname","aasscasadxzcaswq")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_click_accessibilty_id("Save")
# nfile.my_click_accessibilty_id("Find in page")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","as")
# nfile.my_click_id("com.cvinfo.filemanager:id/close")
# nfile.my_click_accessibilty_id("Find in page")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","ad")
# nfile.my_clear_id("com.cvinfo.filemanager:id/search_box")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","a")
# nfile.my_click_id("com.cvinfo.filemanager:id/close")
# nfile.my_edit_id("com.cvinfo.filemanager:id/fname","fgr31231123221")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_click_accessibilty_id("Save")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_click_accessibilty_id("Find in page")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","11")
# nfile.my_click_id("com.cvinfo.filemanager:id/close")
# nfile.my_click_accessibilty_id("Find in page")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","22")
# nfile.my_clear_id("com.cvinfo.filemanager:id/search_box")
# nfile.my_edit_id("com.cvinfo.filemanager:id/search_box","31")
# nfile.my_click_id("com.cvinfo.filemanager:id/close")
# nfile.my_edit_id("com.cvinfo.filemanager:id/fname","dsa12")
# nfile.my_click_accessibilty_id("Save")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_edit_id("com.cvinfo.filemanager:id/fname","122")
# nfile.my_click_accessibilty_id("Save")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_edit_id("com.cvinfo.filemanager:id/fname","2232dfs")
# nfile.my_click_accessibilty_id("Save")
# nfile.my_click_accessibilty_id("More options")
# nfile.my_click_text("Details")
# nfile.my_back()
# nfile.my_back()

# nfile.long_click_1(select_list=[0])
# nfile.delete_file_7(is_success=True)
# nfile.file_browse_0(move_list=[-1,-1,-1])
# nfile.backtohome()
# nfile.get_screen_info()



nfile.hometosdcard()
nfile.file_browse_0(move_list=[0,0])
nfile.properties_browse_11(index=[0],type=0)
nfile.properties_browse_11(index=[1],type=0)
nfile.properties_browse_11(index=[2],type=0)
nfile.properties_browse_11(index=[0,1],type=0)
nfile.properties_browse_11(index=[0,2],type=0)
nfile.properties_browse_11(index=[1,2],type=0)
nfile.properties_browse_11(index=[0,1,2],type=0)


nfile.long_click_1(select_list=[0])
nfile.to_paste_4(pre_num=0, move_list=[-1,1,0])
nfile.long_click_1(select_list=[0])
nfile.delete_file_7(is_success=True)
nfile.file_browse_0(move_list=[-1,-1,0])

nfile.long_click_1(select_list=[1])

#crash
nfile.to_paste_4(pre_num=1, move_list=[-1,-1,2,0,-1,1,-1,2,-1,-1,3,-1,4,-1,5,-1,6,-1,0,1])
nfile.long_click_1(select_list=[1])
nfile.to_paste_4(pre_num=1, move_list=[-1,0])
nfile.file_browse_0(move_list=[-1,-1])
nfile.backtohome()

nfile.get_screen_info()