import time

from appium import webdriver
import FMP
import os.path

mypath = os.path.dirname(os.path.abspath(__file__))

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0.0'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['appPackage'] = 'com.michaldabski.filemanager'
desired_caps['appActivity'] = '.folders.FolderActivity'
desired_caps['noReset'] = False
desired_caps['unicodeKeyboard'] = True

screen_path = mypath + '/screen/'
xml_path = mypath + '/xml/'
jump_pairs = mypath + '/jump_pairs.txt'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(5)

fmp = FMP.FMP(driver, screen_path, xml_path, jump_pairs)
# 初始化app
fmp.index = 471
fmp.my_start()





'''
# test 1、主界面的文件浏览
# 0 文件浏览
fmp.file_browse_0(move_list=[1, -1, 2, -1,3,1, -1,2,-1, 3, -1, -1,4, -1, 5, -1, 6, -1, 7, -1,8,-1,9,-1,10,-1,11,-1,12,-1,13,-1,14,1,-1,-1,15,-1,16,-1])


# test 2、主界面的新建文件夹
# 13 menu
fmp.menu_13()
# 10 新建文件夹(0-13-10),这里直接点击取消新建
fmp.new_folder_10()
# 13 menu
fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aa", is_success=True)
# 13 menu
fmp.my_back()
fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaa", is_success=True)
# 13 menu
fmp.my_back()
fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaa", is_success=True)
fmp.my_back()
fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaa", is_success=True)
fmp.my_back()
fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaa", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaab", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaabb", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaabbb", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaabbbb", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaabvvv", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaavb", is_success=False)

fmp.menu_13()
# 10 新建文件夹(0-13-10)，这里输入文件夹名，然后取消
fmp.new_folder_10(folder_name="aaaaaavvb", is_success=False)

# test 3、274
# 对前5个文件夹 每个文件夹长按选中，分别查看属性、重命名、删除
temp_list = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17]]

for i in range(len(temp_list)):
    # 1 长按选中：第一个123
    fmp.long_click_1(sum=8, select_list=temp_list[i])
    # 13 menu
    fmp.menu_13()
    # 11 查看属性，0->1->13->11：查看文件123的属性
    fmp.properties_browse_11()

    # 13 menu
    fmp.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    fmp.rename_12()

    # 13 menu
    fmp.menu_13()
    # 12 重命名：0->1->13->12：点击后退出
    fmp.rename_12(name="rename" + str(i), is_success=False)

    # 7 文件删除：0->1->7
    fmp.delete_file_7(is_success=False)
    fmp.my_back()


# Test 4、测试多项删除
# 1 长按选中
fmp.long_click_1(sum=8, select_list=[0, 1])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[0, 1, 2, 3])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[1])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[0, 1, 5, 6, 7])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[5, 7, 8])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[0, 1, 2, 4, 5, 7])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[0, 2, 5])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
fmp.long_click_1(sum=8, select_list=[3, 7, 1])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
# 1 长按选中
fmp.long_click_1(sum=8, select_list=[4, 5, 6])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()
# 1 长按选中
fmp.long_click_1(sum=8, select_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()

'''

fmp.long_click_1(sum=8, select_list=[2,5,13, 16, 15])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()

fmp.long_click_1(sum=8, select_list=[3,5,13,14, 16])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()


fmp.long_click_1(sum=8, select_list=[4,5,7,12, 14, 15])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()


fmp.long_click_1(sum=8, select_list=[1,2,3,14, 16, 15])
# 7 文件删除：0->1->7
fmp.delete_file_7(is_success=False)
fmp.my_back()

'''

# Test 5、测试音乐播放
# 1 长按选中
fmp.file_browse_0(move_list=[1])
fmp.play_song_5(1)
time.sleep(3)
fmp.play2pause_song_5()
time.sleep(3)
fmp.pause2play_song_5()
time.sleep(3)
fmp.my_back()

fmp.play_song_5(5)
time.sleep(3)
fmp.play2pause_song_5()
time.sleep(3)
fmp.pause2play_song_5()
time.sleep(3)
fmp.my_back()

fmp.play_song_5(8)
time.sleep(3)
fmp.play2pause_song_5()
time.sleep(3)
fmp.pause2play_song_5()
time.sleep(3)
fmp.my_back()

fmp.play_song_5(11)
time.sleep(3)
fmp.play2pause_song_5()
time.sleep(3)
fmp.pause2play_song_5()
time.sleep(3)
fmp.my_back()

fmp.my_back()

# Test 6、侧边栏

fmp.sidebar_6()
fmp.my_back()



# Test 21 视频
fmp.file_browse_0(move_list=[0])
fmp.play_movie_21(2)
fmp.my_back()

'''
