# -*- coding:utf8 -*-

import time
from appium import webdriver

from FileExplorer_21.FM import FileManager

# 配置信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'Pixel 2 API 29'
desired_caps['appPackage'] = 'filemanager.fileexplorer.manager'
desired_caps['appActivity'] = 'filemanager.fileexplorer.manager.activities.MainActivity'
desired_caps['autoGrantPermissions'] = True
# desired_caps['noReset'] = True
# desired_caps['unicodeKeyboard'] = True

screen_path = './screen/'
xml_path = './xml/'
jump_pairs = './jump_pairs.txt'
activity_info = 'activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
# time.sleep(20)

fm = FileManager(driver, screen_path, xml_path, jump_pairs, activity_info, True)

# def pre_testing():
#     driver.find_element_by_id("filemanager.fileexplorer.manager:id/skip").click()
#     # driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
#     # time.sleep(1)
#     driver.find_element_by_id("filemanager.fileexplorer.manager:id/internal_storage_text").click()


time.sleep(20)


def compress_batch_cancel(selected_list, name):
    fm.long_click_1(7, selected_list)
    fm.menu_13(1, False)
    # 文件压缩 压缩不要成功
    fm.compress_2(True, str(name))


def compress_single_cancel(selected_index, name):
    fm.menu_13(0, True, selected_index)
    fm.compress_2(False, str(name))


def search(text):
    fm.search_3(text)
    # 回到0 文件浏览
    # fm.my_back()


def batch_paste(selected_list, move_to):
    fm.long_click_1(7, selected_list)
    fm.to_paste_4(1, False, move_to)


def single_paste(selected_index, move_to):
    fm.menu_13(0, True, selected_index)
    fm.to_paste_4(13, False, move_to)


def delete_batch(selected_list):
    fm.long_click_1(7, selected_list)
    fm.menu_13(1, False)
    fm.delete_file_7(True)


def delete_single(selected_index):
    fm.menu_13(0, True, selected_index)
    fm.delete_file_7(False)


def rename(name, selected_index):
    fm.menu_13(0, True, selected_index)
    fm.rename_12(name, False)


def extract(move_to, move_back, selected_index):
    fm.file_browse_0(move_to)
    fm.menu_13(0, True, selected_index)
    fm.extract_8(False)
    fm.file_browse_0(move_back)


def create_folder(name):
    fm.menu_13(0, False)
    fm.new_folder_10(name, False)


def check_property(selected_index):
    fm.menu_13(0, True, selected_index)
    fm.properties_browse_11()
    fm.my_back()


def setting(change_theme, primary_color, accent_color, toggle_bar_color):
    fm.sidebar_6()
    fm.settings_14(change_theme, primary_color, accent_color, toggle_bar_color)
    fm.my_back()
    # fm.my_back()


# pre_testing()

fm.file_browse_0([2, 1, 1, 1, -1, -1, -1, -1])
fm.file_browse_0([1, -1])
fm.file_browse_0([3, -1])
fm.file_browse_0([4, -1])
fm.file_browse_0([5, -1])

compress_batch_cancel([2, 1, 4], 'as')
compress_batch_cancel([1, 5, 8], '23')
compress_batch_cancel([3, 4, 8], 'w')
compress_batch_cancel([4, 3, 6], '333')
compress_batch_cancel([5, 1, 3, 2], 'df')
compress_batch_cancel([1, 4, 6, 7], 'fr')
compress_batch_cancel([3, 8, 2, 4], 'gt')
compress_batch_cancel([1, 5], 'tt')
compress_batch_cancel([3, 8], 'ty')
compress_batch_cancel([6, 7, 8], 'yy')

search('Android')
search('BatteryDog')
search('Download')
search('DCIM')
search('tmp')
search('Music')
search('Notifications')
search('Pictures')
search('Podcasts')

for i in range(1, 8):
    compress_single_cancel(i, i)

batch_paste([1, 2, 3, 4], [2, 1, 1, 1, -1, -1, -1, -1])
batch_paste([1, 3, 4, 5], [4, -1])
batch_paste([1, 4, 6], [1, -1])
batch_paste([3, 4, 5], [3, -1])
batch_paste([2, 3, 6], [6, -1])
batch_paste([2, 7, 6], [7, -1])
batch_paste([2, 5, 6], [4, -1])
batch_paste([3, 4, 5], [8, -1])
batch_paste([3, 5, 6], [5, -1])

single_paste(1, [2, 1, 1, 1, -1, -1, -1, -1])
single_paste(2, [4, -1])
single_paste(3, [1, -1])
single_paste(4, [3, -1])
single_paste(5, [6, -1])
single_paste(6, [7, -1])
single_paste(7, [4, -1])

delete_batch([1])
delete_batch([1, 2])
delete_batch([1, 2, 3])
delete_batch([1, 2, 3, 4])
delete_batch([1, 2, 3, 4, 5])
delete_batch([1, 2, 3, 4, 5, 6])
delete_batch([1, 2, 3, 4, 5, 6, 7])
delete_batch([1, 2, 4, 5, 6, 7])

for i in range(1, 8):
    delete_single(i)

for i in range(1, 8):
    rename(i, i)

create_folder('dasd')
create_folder('12312')
create_folder('fasda')
create_folder('234dd')
create_folder('yyyyyyy')
create_folder('234')
create_folder('3432d')
create_folder('wqerw')
create_folder('ewqe324')
create_folder('fsd2')

for i in range(1, 8):
    check_property(i)

extract([1], [-1], 1)
extract([2], [-1], 4)
extract([2, 2], [-1, -1], 1)
extract([3], [-1], 1)
extract([4], [-1], 1)
extract([5], [-1], 1)
extract([6], [-1], 1)
extract([7], [-1], 1)

setting(True, [0, 1], [0, 3], True)
setting(True, [3, 4], [3, 1], False)
setting(True, [5, 0], [4, 2], True)
setting(False, [2, 1], [2, 4], True)
setting(True, [2, 3], [1, 3], True)
setting(True, [0, 2], [2, 3], True)
setting(True, [3, 3], [3, 1], False)
setting(True, [5, 1], [5, 2], True)
setting(False, [2, 4], [2, 4], True)
setting(True, [2, 5], [1, 3], True)

# 最后一定要加入保存最后一个状态的图片的代码
fm.get_screen_info()
