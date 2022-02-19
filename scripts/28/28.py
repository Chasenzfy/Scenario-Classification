# -*- coding:utf8 -*-

import time

from appium import webdriver

# 配置信息
from FileBrowser_28.FB import FB

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'Pixel 2 API 29'
desired_caps['appPackage'] = 'filebrowser.filemanager.file.folder.app'
desired_caps['appActivity'] = 'filebrowser.filemanager.file.folder.app.activities.MainActivity'
desired_caps['autoGrantPermissions'] = True
# desired_caps['noReset'] = True
# desired_caps['unicodeKeyboard'] = True

screen_path = 'screen/'
xml_path = 'xml/'
jump_pairs = './jump_pairs.txt'
activity_info = './activity_info.txt'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(20)

fb = FB(driver, screen_path, xml_path, jump_pairs, activity_info, True)


# def pre_testing():
#     el1 = driver.find_element_by_id("filebrowser.filemanager.file.folder.app:id/next")
#     el1.click()
#     el1.click()
#     el2 = driver.find_element_by_id("filebrowser.filemanager.file.folder.app:id/done")
#     el2.click()
#     time.sleep(1)
#     el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
#     el3.click()
#     time.sleep(1)
#     el4 = driver.find_element_by_id("android:id/button1")
#     el4.click()
#     time.sleep(1)
#     driver.back()
#     time.sleep(1)
#     el5 = driver.find_element_by_id("filebrowser.filemanager.file.folder.app:id/internal_header")
#     el5.click()
#
#
# pre_testing()


def batch_compress(select_list, name=None, is_success=False):
    fb.long_click_1(select_list)
    fb.menu_13(True)
    fb.compress_2(True, name, is_success)


def single_compress(select_index, name=None, is_success=False):
    fb.menu_13(False, select_index)
    fb.compress_2(False, name, is_success)


def extract(move_to, selected_index, name, back):
    fb.file_browse_0(move_to)
    single_compress(selected_index, name, True)
    time.sleep(1)
    fb.menu_13(False, 4)
    fb.extract_8()
    delete_single(2, True)
    fb.file_browse_0(back)


def search(text, move_list):
    fb.search_3(text, move_list)
    # fb.my_back()


def to_paste_batch(selected_list, move_to):
    fb.long_click_1(selected_list)
    fb.to_paste_4(1, move_to)


def to_paste_single(selected_index, move_to):
    fb.menu_13(False, selected_index)
    fb.to_paste_4(13, move_to)


def delete_batch(selected_list):
    fb.long_click_1(selected_list)
    fb.menu_13(True)
    fb.delete_file_7(True, False)
    fb.my_back()


def delete_single(select_index, is_success=False):
    fb.menu_13(False, select_index)
    fb.delete_file_7(False, is_success)


def rename(selected_index, new_name):
    fb.menu_13(False, selected_index)
    fb.rename_12(new_name, False)


def check_property(selected_index):
    fb.menu_13(False, selected_index)
    fb.properties_browse_11()


def create_folder(name):
    fb.menu_13(True)
    fb.new_folder_10(name, False)


def setting(language, zip_name):
    fb.sidebar_6()
    fb.settings_14(language, zip_name)


fb.file_browse_0([1, -1])
fb.file_browse_0([2, 1, 1, 1, -1, -1, -1, -1])
fb.file_browse_0([3, -1])
fb.file_browse_0([4, -1])
fb.file_browse_0([5, -1])
fb.file_browse_0([6, -1])
fb.file_browse_0([7, -1])

batch_compress([1, 2, 3], '1.zip', False)
batch_compress([1, 2, 4], '2.zip', False)
batch_compress([1, 2, 5], '3.zip', False)
batch_compress([1, 2, 6], '4.zip', False)
batch_compress([1, 2, 7], '5.zip', False)
batch_compress([2, 3, 4], '6.zip', False)
batch_compress([2, 3, 5], '7.zip', False)
batch_compress([3, 4, 5], '8.zip', False)
batch_compress([4, 5, 6], '9.zip', False)
batch_compress([4, 5, 7], '10.zip', False)

single_compress(1, 'a.zip', False)
single_compress(2, 'b.zip', False)
single_compress(3, 'c.zip', False)
single_compress(4, 'd.zip', False)
single_compress(5, 'd.zip', False)
single_compress(6, 'e.zip', False)
single_compress(7, 'f.zip', False)

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

to_paste_batch([1, 2, 3], [1, -1])
to_paste_batch([1, 2, 4], [2, 1, 1, 1, -1, -1, -1, -1])
to_paste_batch([1, 2, 5], [3, -1])
to_paste_batch([1, 2, 6], [4, -1])
to_paste_batch([1, 2, 7], [5, -1])
to_paste_batch([2, 3, 4], [6, -1])
to_paste_batch([2, 3, 5], [7, -1])
to_paste_batch([3, 4, 5], [2, 1, 3, 1, -1, -1, -1, -1])
to_paste_batch([4, 5, 6], [3, -1])
to_paste_batch([4, 5, 7], [4, -1])

to_paste_single(1, [1, -1])
to_paste_single(2, [2, 1, 1, 1, -1, -1, -1, -1])
to_paste_single(3, [3, -1])
to_paste_single(4, [4, -1])
to_paste_single(5, [5, -1])
to_paste_single(6, [6, -1])
to_paste_single(7, [7, -1])

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

check_property(1)
check_property(2)
check_property(3)
check_property(4)
check_property(5)
check_property(6)
check_property(7)

create_folder('aa')
create_folder('bb')
create_folder('cc')
create_folder('dd')
create_folder('ee')
create_folder('ff')
create_folder('gg')
create_folder('tt')
create_folder('yy')
create_folder('ii')

setting(1, 'qw')
setting(2, 'er')
setting(3, 'rf')
setting(4, 'tg')
setting(5, 'ds')
setting(6, 'fg')
setting(7, 'zx')
setting(8, 'df')
setting(9, 'op')
setting(10, 'lk')

# 最后一定要加入保存最后一个状态的图片的代码
fb.get_screen_info()
