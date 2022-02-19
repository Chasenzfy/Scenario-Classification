import time

from appium import webdriver
import CFE
import os.path


mypath = os.path.dirname( os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0.0'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'com.cxinventor.file.explorer'
desired_caps['appActivity'] = "com.alphainventor.filemanager.activity.MainActivity"
desired_caps['noReset'] = False
desired_caps['unicodeKeyboard'] = True


screen_path = mypath + '/screen/'
xml_path = mypath + '/xml/'
jump_pairs = mypath + '/jump_pairs.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
time.sleep(5)
cfe = CFE.CFE(driver, screen_path, xml_path, jump_pairs)
cfe.index=876


# test 1、主界面的文件浏览
# 回到主界面
cfe.my_back_home()




cfe.file_browse_0(move_list=[0,-1,1,-1,2,1,-1,2,-1,-1,3,-1,4,-1,5,-1,6,-1,7,0,-1,-1,8,0,-1,1,-1,2,-1,-1,9,-1])


cfe.long_click_1(select_list=[0, 1, 2, 3, 4, 5, 6, 7, 8])
cfe.my_back()
cfe.long_click_1(select_list=[8, 7, 6, 5, 4, 3, 2, 1, 0])
cfe.my_back()
cfe.long_click_1(select_list=[1, 3, 5, 7])
cfe.my_back()
cfe.long_click_1(select_list=[2, 4, 6, 8])
cfe.my_back()
cfe.long_click_1(select_list=[1, 3, 6, 3])
cfe.my_back()
cfe.long_click_1(select_list=[3, 5, 8, 3, 8])
cfe.my_back()
cfe.long_click_1(select_list=[1, 2, 3, 4, 8, 6])
cfe.my_back()
cfe.long_click_1(select_list=[2, 5, 7, 4, 1, 3])
cfe.my_back()


temp_list = [[0],[1],[2],[3],[4],[5],[6],[7],[8]]

for i in range(len(temp_list)):
    cfe.long_click_1(select_list=temp_list[i])
    cfe.properties_browse_11()
    cfe.long_click_1(select_list=temp_list[i])
    cfe.rename_12()

    cfe.long_click_1(select_list=temp_list[i])
    cfe.rename_12(name="rename" + str(i))

    cfe.long_click_1(select_list=temp_list[i])
    cfe.delete_file_7(is_success=False)

    cfe.long_click_1(select_list=temp_list[i])
    cfe.compress_2()

    cfe.long_click_1(select_list=temp_list[i])
    cfe.compress_2(i)
    cfe.long_click_1(select_list=temp_list[i])
    cfe.to_paste_4()

cfe.menu_13()
cfe.search_3(text="1")

cfe.menu_13()
cfe.search_3(text="2")

cfe.menu_13()
cfe.search_3(text="3")

cfe.menu_13()
cfe.search_3(text="4")

cfe.menu_13()
cfe.search_3(text="5")

cfe.menu_13()
cfe.search_3(text="6")

cfe.menu_13()
cfe.search_3(text="7")

cfe.menu_13()
cfe.search_3(text="8")

cfe.menu_13()
cfe.search_3(text="19")

cfe.menu_13()
cfe.search_3(text="10")

cfe.menu_13()
cfe.search_3(text="17")

cfe.menu_13()
cfe.search_3(text="15")

cfe.menu_13()
cfe.search_3(text="113213123")




cfe.menu_13()
cfe.new_folder_10(folder_name="a", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="ab", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="ac", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="ad", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="ae", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="af", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="ag", is_success=False)
cfe.menu_13()
cfe.new_folder_10(folder_name="ahh", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="aasdad", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="aert", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="tgra", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="fa", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="23rfa", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="dsfsva", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="adfegrb  rwf", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="asfbew", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="aasgte", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="aewdefa", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="agtgtge", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="a", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="a", is_success=False)
cfe.menu_13()
cfe.new_folder_11(folder_name="a", is_success=False)


select_list=[1, 3, 5, 7]
cfe.long_click_1(select_list)
cfe.delete_file_7(is_success=False)

cfe.long_click_1(select_list)
cfe.properties_browse_11()

cfe.long_click_1(select_list)
cfe.compress_2()


cfe.long_click_1(select_list)
cfe.compress_2(11312)


select_list=[1, 2, 3, 5, 7]
cfe.long_click_1(select_list)
cfe.delete_file_7(is_success=False)

cfe.long_click_1(select_list)
cfe.properties_browse_11()

cfe.long_click_1(select_list)
cfe.compress_2()


cfe.long_click_1(select_list)
cfe.compress_2(113312)



select_list=[1, 3, 4, 5, 7]
cfe.long_click_1(select_list)
cfe.delete_file_7(is_success=False)

cfe.long_click_1(select_list)
cfe.properties_browse_11()

cfe.long_click_1(select_list)
cfe.compress_2()


cfe.long_click_1(select_list)
cfe.compress_2(114312)




select_list=[1, 3, 5, 7, 8]
cfe.long_click_1(select_list)
cfe.delete_file_7(is_success=False)

cfe.long_click_1(select_list)
cfe.properties_browse_11()

cfe.long_click_1(select_list)
cfe.compress_2()


cfe.long_click_1(select_list)
cfe.compress_2(1131562)



select_list=[0, 1, 3, 5, 7]
cfe.long_click_1(select_list)
cfe.delete_file_7(is_success=False)

cfe.long_click_1(select_list)
cfe.properties_browse_11()

cfe.long_click_1(select_list)
cfe.compress_2()


cfe.long_click_1(select_list)
cfe.compress_2(1134512)



select_list=[0, 1, 3, 5, 6, 7]
cfe.long_click_1(select_list)
cfe.delete_file_7(is_success=False)

cfe.long_click_1(select_list)
cfe.properties_browse_11()

cfe.long_click_1(select_list)
cfe.compress_2()


cfe.long_click_1(select_list)
cfe.compress_2(113765412)

cfe.get_screen_info()