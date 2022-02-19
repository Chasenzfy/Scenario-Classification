# -*- coding:utf8 -*-

import time

from appium import webdriver

from MiFileManager_7.MFM import MFM

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'Pixel 2 API 28'
desired_caps['appPackage'] = 'com.mi.android.globalFileexplorer'
desired_caps['appActivity'] = 'com.android.fileexplorer.FileExplorerTabActivity'
desired_caps['autoGrantPermissions'] = True
# desired_caps['noReset'] = True
# desired_caps['unicodeKeyboard'] = True

screen_path = './screen/'
xml_path = './xml/'
jump_pairs = './jump_pairs.txt'
activity_info = './activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)

mfm = MFM(driver, screen_path, xml_path, jump_pairs, activity_info, True)


def pre_testing():
    start_elem = driver.find_element_by_id("com.mi.android.globalFileexplorer:id/privacy_message_tv")
    end_elem = driver.find_element_by_id("com.mi.android.globalFileexplorer:id/privacy_desc_tv")
    driver.scroll(start_elem, end_elem)
    driver.find_element_by_id("com.mi.android.globalFileexplorer:id/experience_check_box").click()
    driver.find_element_by_id("com.mi.android.globalFileexplorer:id/confirm_btn").click()
    # time.sleep(1)
    # driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
    # time.sleep(1)
    # 进入app
    # driver.find_element_by_xpath(
    #     '//*[@resource-id="com.android.launcher3:id/apps_list_view"]/android.widget.TextView[12]').click()
    try:
        driver.find_element_by_id("android:id/button2").click()
    except Exception:
        pass
    # 进入文件浏览
    driver.find_element_by_xpath(
        '//*[@resource-id="com.mi.android.globalFileexplorer:id/scrollingTabContainer"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]').click()


pre_testing()


# time.sleep(20)

def compress_cancel(selected_list, name):
    mfm.long_click_1(8, selected_list)
    mfm.menu_13(1)
    # 文件压缩 压缩不要成功
    mfm.compress_2(str(name), False)


def search(text, move_list):
    mfm.search_3(text, move_list)
    # mfm.my_back()


def to_paste(selected_list, move_to):
    mfm.long_click_1(8, selected_list)
    mfm.menu_13(1)
    mfm.to_paste_4(False, move_to)


def delete(selected_list):
    mfm.long_click_1(8, selected_list)
    mfm.delete_file_7(False)


def rename(name, selected_index):
    mfm.long_click_1(8, [selected_index])
    mfm.menu_13(1)
    mfm.rename_12(name)


def extract(move_to, extract_to, move_back):
    mfm.file_browse_0(move_to)
    mfm.extract_8(extract_to, False)
    mfm.file_browse_0(move_back)


def create_folder(name):
    mfm.menu_13(0)
    mfm.new_folder_10(name, False)


def check_property(selected_index):
    mfm.long_click_1(8, [selected_index])
    mfm.menu_13(1)
    mfm.properties_browse_11()
    mfm.my_back()


def play_audio(file_path, move_back):
    mfm.play_audio_5(file_path)
    mfm.file_browse_0(move_back)


def setting(feedback, rate):
    mfm.sidebar_6()
    mfm.settings_14(feedback, rate)
    mfm.my_back()


time.sleep(30)
for i in range(1, 10):
    compress_cancel([i], str(i))

search('Alarms', [1, -1, -1])
search('Android', [1, 1, 1, -1, -1, -1, -1])
search('DCIM', [1, -1, -1])
search('Download', [1, -1, -1])
search('Movies', [1, -1, -1])
search('Music', [1, -1, -1])
search('Notifications', [1, -1, -1])
search('tmp', [1, -1, -1])

to_paste([1, 2, 3], [1, -1])
to_paste([1, 4, 3], [3, -1])
to_paste([1, 6, 3], [2, 1, 1, 1, -1, -1, -1, -1])
to_paste([7, 5, 2], [4, -1])
to_paste([2, 8], [5, -1])
to_paste([9, 3], [6, -1])
to_paste([1, 4, 7], [7, -1])
to_paste([1, 9, 2], [8, -1])
to_paste([1, 4, 5, 6], [9, -1])

for i in range(1, 10):
    delete([i])

for i in range(1, 10):
    rename(str(i), i)

extract([1, 1], [1, -1], [-1])
extract([2, 2, 1], [3, -1], [-1, -1])
extract([3, 1], [2, 1, 1, 1, -1, -1, -1, -1], [-1])
extract([4, 1], [3, -1], [-1])
extract([5, 1], [4, -1], [-1])
extract([6, 1], [5, -1], [-1])
extract([7, 1], [6, -1], [-1])
extract([7, 1], [2, -1], [-1])
extract([7, 1], [1, -1], [-1])

for i in range(1, 11):
    create_folder(str(i))

for i in range(1, 10):
    check_property(i)

play_audio([1, 2], [-1])
play_audio([2, 3], [-1])
play_audio([3, 2], [-1])
play_audio([4, 2], [-1])
play_audio([5, 2], [-1])
play_audio([6, 2], [-1])
play_audio([7, 2], [-1])
play_audio([8, 1], [-1])

setting('awsd', 5)
setting('awqwsd', 2)
setting('asqwqd', 3)
setting('asad', 4)
setting('as21d', 5)
setting('as213d', 2)
setting('qwwqasd', 4)
setting('a323sd', 3)
setting('a213sd', 5)
setting('as213123d', 1)

# 最后一定要加入保存最后一个状态的图片的代码
mfm.get_screen_info()
