import time
import os
from appium import webdriver
from appium.webdriver.webdriver import T
import mkfile


# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'pl.mkexplorer.kormateusz'
desired_caps['appActivity'] = '.MKexplorerActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True

screen_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/33-MK/33-MK/screen'
xml_path = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/33-MK/33-MK/xml'
jump_pairs = 'C:/Users/chasen/Desktop/newfilesapp/newfilesapp/33-MK/33-MK/jump_pairs.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(2)

mkfile = mkfile.MyOIFM(driver, screen_path, xml_path, jump_pairs,'pl.mkexplorer.kormateusz.MKexplorerActivity')

#test1 设置
print("start")



# mkfile.settings_14(checkbox_list=[0,2,7],colorcheck=[0,1],colorlist=[0,1,2,3])
# mkfile.file_browse_0(move_list=[0,0])
# mkfile.rename_12(name="2.jpg",index=0,is_success=True)
# mkfile.properties_browse_11_total()
# mkfile.long_click_1(sum=3,select_list=[0])
# mkfile.to_paste_4(pre_num=1,move_list=[-1,-1,0])
# mkfile.file_browse_0(move_list=[0])
# mkfile.long_click_1(sum=3,select_list=[1])
# mkfile.to_paste_4(pre_num=2,move_list=[-1,-1,0])


#start
mkfile.hometosdcard()
mkfile.settings_14(checkbox_list=[0,2,7,3,4,7,2,6,4,5,0,2,6,0,2,5,3,6,7,0,2,4,3,0,5,2,7,0,4,3,5,6])


mkfile.file_browse_0(move_list=[0,1,0])

temp_list = [["z27test_1_0","z27test_1_1"], ["z27test_2"], ["z27test_3_0","z27test_3_1","z27test_3_2"], ["z27test_4_0","z27test_4_1","z27test_4_2"], ["z27test_5_0","z27test_5_1"]]
# temp_list = [["test_1_0","test_1_1"]]
# temp_list = [["test_1_0","test_1_1","test_1_2"],["test_2"],["test_1_0","test_1_1"]]
# temp_list = [["test_0"]]
# temp_list = [["test_1_0","test_1_1","test_1_2"],["test_2"],["test_3_0","test_3_1"],["test_4_0","test_4_1"],["test_5_0","test_5_1","test_5_2"],["test_6"]]
for i in range(len(temp_list)):
    time.sleep(10)
    length = len(temp_list[i])
    count = 0
    for filename in temp_list[i]:
        tempfilename = "temp"+filename
        if count%2==0:
            mkfile.new_folder_10(isfile=True,folder_name=tempfilename, is_success=False)
            mkfile.new_folder_10(isfile=True,folder_name=filename,type=1, is_success=True)
            count = count + 1
        else:
            mkfile.new_folder_10(isfile=False,folder_name=tempfilename, is_success=False)
            mkfile.new_folder_10(isfile=False,folder_name=filename, is_success=True)
            count = count + 1
    for j in range(length):
        tempname = temp_list[i][j] + "rename"
        temp = "temp" + tempname
        mkfile.rename_12(name=temp,index = j,is_success=False)
        mkfile.rename_12(name=tempname, index = j,is_success=True)
    for k in range(length):
        mkfile.long_click_1(sum=length,select_list=[k])
        mkfile.delete_file_7(is_success=False)
    for m in range(length):
        mkfile.search_3(text=temp_list[i][m])
        mkfile.search_3(text=temp_list[i][m])
    #for n in range(length):
    mkfile.long_click_1(sum=length,select_list=[0])
    mkfile.compress_2(is_success=False)
    mkfile.long_click_1(sum=length,select_list=[length-1])
    mkfile.compress_2(is_success=True)
    temp = length//2
    mkfile.umcompress_8(move_list=[-1,-1,1],index=temp)
    mkfile.long_click_1(sum=length*3,select_list=[1])
    mkfile.delete_file_7(is_success=True)
    mkfile.file_browse_0(move_list=[0])
    mkfile.long_click_1(sum=length*3,select_list=[temp])
    mkfile.delete_file_7(is_success=True)
    mkfile.properties_browse_11_total()
    for p in range(length):
        mkfile.properties_browse_11(index=p)
    newarr = range(length)
    newlist = list(newarr)
    mkfile.long_click_1(sum=length*3,select_list=newlist)
    mkfile.menu_13()
    mkfile.my_click_text("Properties")
    mkfile.my_back()
    mkfile.delete_file_7(is_success=True)
mkfile.file_browse_0(move_list=[-1,-1,-1,-1])


mkfile.hometosdcard()
mkfile.file_browse_0(move_list=[0,1,0])

mkfile.new_folder_10(isfile=True,folder_name="tete3.txt",is_success=False)
mkfile.new_folder_10(isfile=True,folder_name="1sda",type=1,is_success=True)
mkfile.file_browse_0(move_list=[0])

mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","asdasxzc")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeplus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeplus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","das213")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeminus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","21312")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeplus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeplus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","213")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeminus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeminus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","213213")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeplus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","123csda")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeminus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","qevc341")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeminus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeminus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=False)
mkfile.file_browse_0(move_list=[0])
mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","SADAS")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/sizeplus")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/save")

mkfile.my_edit_id("pl.mkexplorer.kormateusz:id/text","QWEA")
mkfile.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
mkfile.my_click_id("pl.mkexplorer.kormateusz:id/positivebutton")
mkfile.long_click_1(sum=0,select_list=[0])
mkfile.delete_file_7(is_success=True)
mkfile.file_browse_0(move_list=[-1,-1,-1,-1])




mkfile.hometosdcard()
mkfile.file_browse_0(move_list=[0,1,0])
mkfile.new_folder_10(isfile=True,type=1,folder_name="paste1test",is_success=True)
mkfile.new_folder_10(isfile=True,folder_name="paste2test",is_success=True)

mkfile.long_click_1(sum=2,select_list=[0])
mkfile.to_paste_4(pre_num=2,move_list=[-1,-1,-1,1,-1,2,1,-1,-1,3,-1,0,0,-1,-1,4,-1,5,-1,6,-1,7,-1,0,1])
mkfile.long_click_1(sum=2,select_list=[1])
mkfile.delete_file_7(is_success=True)
mkfile.file_browse_0(move_list=[0])
mkfile.long_click_1(sum=2,select_list=[0])
mkfile.to_paste_4(pre_num=1, move_list=[-1,-1,-1,1,-1,2,1,-1,-1,3,-1,0,0,-1,-1,4,-1,5,-1,6,-1,7,-1,0,1])
mkfile.long_click_1(sum=2,select_list=[1])
mkfile.delete_file_7(is_success=True)
mkfile.file_browse_0(move_list=[0])
mkfile.long_click_1(sum=2,select_list=[0])
mkfile.delete_file_7(is_success=True)

mkfile.file_browse_0(move_list=[-1,-1,-1,-1])

mkfile.hometosdcard()
mkfile.bookmark_15(index=0,name="bookmark1",is_success=False)
mkfile.bookmark_15(index=1,name="alarmmark",is_success=True)
mkfile.bookmark_15(index=2,name="androidmark",is_success=False)
mkfile.bookmark_15(index=3,name="backup",is_success=True)
mkfile.bookmark_15(index=4,name="audio",is_success=False)
mkfile.bookmark_15(index=5,name="dcim",is_success=False)
mkfile.bookmark_15(index=6,name="documents",is_success=True)
mkfile.bookmark_15(index=7,name="download",is_success=False)
mkfile.sidebar_6()
mkfile.my_back()
mkfile.file_browse_0(move_list=[-1])


mkfile.hometosdcard()
mkfile.file_browse_0(move_list=[0,1,0])
mkfile.new_folder_10(isfile=True,folder_name="compresstest",is_success=True)
mkfile.long_click_1(sum=1,select_list=[0])
mkfile.compress_2(is_success=True)
mkfile.umcompress_8(move_list=[-1,-1,-1,1,-1,2,1,-1,-1,3,-1,4,-1,5,-1,6,-1,7,-1,0,1],index=0)
mkfile.long_click_1(sum=2,select_list=[1])
mkfile.delete_file_7(is_success=True)
mkfile.file_browse_0(move_list=[-1,-1,-1])
mkfile.get_screen_info()