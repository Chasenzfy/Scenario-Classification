# -*- coding:utf8 -*-

import time

from appium import webdriver

# 配置信息
from FileManager_25.FM import FM

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'Pixel 2 API 28'
desired_caps['appPackage'] = 'com.cv.filemanager'
desired_caps['appActivity'] = 'com.cv.filemanager.activities.MainActivity'
desired_caps['autoGrantPermissions'] = True
# desired_caps['noReset'] = True
# desired_caps['unicodeKeyboard'] = True

screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = './jump_pairs.txt'
activity_info = './activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
# time.sleep(20)

fm = FM(driver, screen_path, xml_path, jump_pairs, activity_info, True)


def pre_testing():
    # driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    # driver.find_element_by_xpath(
    #     '//*[@resource-id="com.cv.filemanager:id/circles"]/android.widget.ImageView[5]').click()
    # driver.swipe(1013, 1510, 54, 1534)
    time.sleep(2)
    driver.swipe(1013, 1510, 54, 1534)
    driver.swipe(1013, 1510, 54, 1534)
    driver.swipe(1013, 1510, 54, 1534)
    driver.swipe(1013, 1510, 54, 1534)
    driver.find_element_by_id("com.cv.filemanager:id/done").click()
    driver.find_element_by_id("com.cv.filemanager:id/internal_card").click()


# time.sleep(3)
pre_testing()


def batch_compress(select_list, name=None, password=None, is_success=False):
    fm.long_click_1(select_list)
    fm.menu_13(False)
    fm.compress_2(True, name, password, is_success)


def single_compress(select_index, name=None, password=None, is_success=False):
    fm.menu_13(True, select_index)
    fm.compress_2(False, name, password, is_success)


def search(text, move_to):
    fm.search_3(text, move_to)
    # 回到0 文件浏览
    # fm.my_back()


def to_paste(selected_list, move_to):
    fm.long_click_1(selected_list)
    fm.to_paste_4(move_to)


def delete_batch(selected_list):
    fm.long_click_1(selected_list)
    fm.menu_13(False)
    fm.delete_file_7(True, False)


def delete_single(select_index):
    fm.menu_13(True, select_index)
    fm.delete_file_7(False, False)


def rename(selected_index, new_name):
    fm.menu_13(True, selected_index)
    fm.rename_12(new_name, False)


def check_property_batch(selected_list):
    fm.long_click_1(selected_list)
    fm.menu_13(False)
    fm.properties_browse_11(True)
    fm.my_back()


def check_property_single(selected_index):
    fm.menu_13(True, selected_index)
    fm.properties_browse_11(False)
    # fm.my_back()


def create_folder(name):
    fm.menu_13(False)
    fm.new_folder_10(name, False)


def setting(primary_color, accent_color):
    fm.sidebar_6()
    fm.settings_14(primary_color, accent_color)


def bookmark(item_index, new_name, is_deleted):
    fm.sidebar_6()
    fm.bookmarks_15(item_index, new_name, is_deleted)
    fm.my_back()


def extract(browse_list, selected_index, back):
    fm.file_browse_0(browse_list)
    fm.menu_13(True, selected_index)
    fm.extract_8(True)
    fm.menu_13(True, 1)
    fm.delete_file_7(False, True)
    fm.file_browse_0(back)


fm.file_browse_0([1, -1])
fm.file_browse_0([2, 1, 1, -1, 2, -1, 3, -1, -1, -1])
fm.file_browse_0([3, -1])
fm.file_browse_0([4, -1])
fm.file_browse_0([5, -1])
fm.file_browse_0([6, -1])
fm.file_browse_0([7, -1])

batch_compress([1, 2, 3], '1.zip', '1', False)
batch_compress([1, 2, 4], '2.zip', '2', False)
batch_compress([1, 2, 5], '3.zip', '3', False)
batch_compress([1, 2, 6], '4.zip', '4', False)
batch_compress([1, 2, 7], '5.zip', '5', False)
batch_compress([2, 3, 4], '6.zip', '6', False)
batch_compress([2, 3, 5], '7.zip', '7', False)
batch_compress([3, 4, 5], '8.zip', '8', False)
batch_compress([4, 5, 6], '9.zip', '9', False)
batch_compress([4, 5, 7], '10.zip', '10', False)

single_compress(1, 'a.zip', 'a', False)
single_compress(2, 'b.zip', 'b', False)
single_compress(3, 'c.zip', 'c', False)
single_compress(4, 'd.zip', 'd', False)
single_compress(5, 'd.zip', 'e', False)
single_compress(6, 'e.zip', 'f', False)
single_compress(7, 'f.zip', 'g', False)

search('Alarms', [1, -1])
search('Android', [1, 1, 2, 1, -1, -1, -1, -1])
search('DCIM', [1, -1])
search('Download', [1, -1])
search('Movies', [1, -1])
search('Music', [1, -1])
search('Notifications', [1, -1])
search('Pictures', [1, -1])
search('Podcasts', [1, -1])
search('tmp', [1, -1])

to_paste([1, 2, 3], [1, -1])
to_paste([1, 2, 4], [2, 1, 1, 1, -1, -1, -1, -1])
to_paste([1, 2, 5], [3, -1])
to_paste([1, 2, 6], [4, -1])
to_paste([1, 2, 7], [5, -1])
to_paste([2, 3, 4], [6, -1])
to_paste([2, 3, 5], [7, -1])
to_paste([4, 5, 6], [3, -1])
to_paste([4, 5, 7], [4, -1])

delete_batch([1, 2, 3])
delete_batch([1, 2, 4])
delete_batch([1, 2, 5])
delete_batch([1, 2, 6])
delete_batch([1, 2, 7])
delete_batch([2, 3, 4])
delete_batch([2, 3, 5])
delete_batch([3, 4, 5])
delete_batch([4, 5, 6])
delete_batch([4, 5, 7])

delete_single(1)
delete_single(2)
delete_single(3)
delete_single(4)
delete_single(5)
delete_single(6)
delete_single(7)

rename(1, 'a')
rename(2, 'b')
rename(3, 'c')
rename(4, 'd')
rename(5, 'e')
rename(6, 'f')
rename(7, 'g')

check_property_batch([1, 2, 3])
check_property_batch([1, 2, 4])
check_property_batch([1, 2, 5])
check_property_batch([1, 2, 6])
check_property_batch([1, 3, 5])
check_property_batch([2, 3, 4])
check_property_batch([2, 4, 5])
check_property_batch([3, 4, 5])
check_property_batch([2, 5, 6])
check_property_batch([1, 4, 5])

check_property_single(1)
check_property_single(2)
check_property_single(3)
check_property_single(4)
check_property_single(5)
check_property_single(6)
check_property_single(7)

create_folder('a')
create_folder('b')
create_folder('c')
create_folder('d')
create_folder('e')
create_folder('f')
create_folder('g')
create_folder('h')
create_folder('i')
create_folder('G')

extract([1], 1, [-1])
extract([2, 2], 1, [-1, -1])
extract([3], 1, [-1])
extract([4], 1, [-1])
extract([5], 1, [-1])
extract([6], 1, [-1])
extract([7], 1, [-1])

fm.sidebar_6()
fm.my_scroll_xpath(
    '//*[@resource-id="com.cv.filemanager:id/material_drawer_recycler_view"]/android.widget.LinearLayout[9]',
    '//*[@resource-id="com.cv.filemanager:id/material_drawer_recycler_view"]/android.widget.LinearLayout[1]')
fm.my_click_xpath(
    '//*[@resource-id="com.cv.filemanager:id/material_drawer_recycler_view"]/android.widget.LinearLayout[7]')
fm.my_back()
bookmark(1, '1', False)
bookmark(2, '2', False)
bookmark(3, '3', False)
bookmark(4, '4', False)
bookmark(1, '5', False)
bookmark(2, '6', False)
bookmark(3, '7', False)
bookmark(1, '8', False)
bookmark(1, 'kk', True)
bookmark(1, 'aa', True)
bookmark(1, 'bb', True)
bookmark(1, 'ff', True)

setting(1, 1)
setting(24, 24)
setting(2, 3)
setting(3, 5)
setting(4, 6)
setting(5, 7)
setting(6, 8)
setting(7, 9)
setting(8, 10)
setting(9, 11)

# 最后一定要加入保存最后一个状态的图片的代码
fm.get_screen_info()
