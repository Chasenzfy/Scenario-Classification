# -*- coding:utf8 -*-
import time
import os
import random

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class FEFileExplorer:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 901  # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path  # 保存的截图的地址，例如 screen/
        self.xml_path = xml_path  # 保存的xml的地址，例如 xml/
        self.jump_pairs = jump_pairs  # 跳转文件的地址，例如：jump_pairs.txt
        self.activity_info = activity_info  # 记录当前界面的activity信息 例如：activity_info.txt

    def get_screen_info(self):
        # 默认都是在执执行3秒后，再进行截图和保存xml。可能某些操作需要更多的时间，在测试的时候加上
        time.sleep(3)
        screen_name = str(self.index) + ".png"
        self.driver.save_screenshot(os.path.join(self.screen_path, screen_name))
        xml_name = str(self.index) + ".xml"
        with open(os.path.join(self.xml_path, xml_name), 'w+') as fps:
            fps.write(self.driver.page_source)

        with open(self.activity_info, 'a') as f:
            f.write(str(self.index) + ' ' + self.driver.current_activity + '\n')
        time.sleep(2)

    # 相当于每个动作函数为：保存执行动作之前的截图和xml，执行动作，保存执行的动作标号，更新index
    def my_back(self):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.back()
        time.sleep(2)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' back\n')
        fd.close()
        self.index += 1

    def my_search(self):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.execute_script("mobile: performEditorAction", {'action': 'search'})
        time.sleep(2)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click search\n')
        fd.close()
        self.index += 1

    def my_click_text(self, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        temp = 'new UiSelector().text("' + text + '")'  # 'new UiSelector().text("123")'
        el = self.driver.find_element_by_android_uiautomator(temp)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_text_start(self, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        temp = 'new UiSelector().textStartsWith("' + text + '")'  # 'new UiSelector().text("123")'
        el = self.driver.find_element_by_android_uiautomator(temp)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_classname(self, classname, classname_index):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_elements_by_class_name(classname)[classname_index]
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_long_click_classname(self, classname, classname_index):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_elements_by_class_name(classname)[classname_index]
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_click_accessibilty_id(self, accessibility_id):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_accessibility_id(accessibility_id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_id(self, id, id_index):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        el = self.driver.find_elements_by_id(id)[id_index]

        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()
        el.click()
        self.index += 1

    def my_long_click_id(self, id, id_index):
        self.get_screen_info()

        el = self.driver.find_elements_by_id(id)[id_index]

        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()
        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_click_xpath(self, xpath):
        self.get_screen_info()

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_xpath_text(self, index, text):
        self.get_screen_info()
        # 例如androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]
        # index = 1, text = androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[

        temp = text + str(index) + ']'
        el = self.driver.find_element_by_xpath(temp)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_long_click_xpath_text(self, index, text):
        self.get_screen_info()
        # 例如androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]
        # index = 1, text = androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[

        xpath = text + str(index) + ']'
        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_long_click_xpath(self, xpath):
        self.get_screen_info()

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_edit_id(self, id, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + text + ' ' + str(element) + '\n')
        fd.close()

        el.send_keys(text)
        self.index += 1

    def my_edit_xpath(self, xpath, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + text + ' ' + str(element) + '\n')
        fd.close()

        el.send_keys(text)
        self.index += 1

    def my_clear_id(self, id):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear ' + str(element) + '\n')
        fd.close()

        el.clear()
        self.index += 1

    def my_clear_xpath(self, xpath):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear ' + str(element) + '\n')
        fd.close()

        el.clear()
        self.index += 1

    def my_edit_class_name(self, class_name, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        el = self.driver.find_element_by_class_name(class_name)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + text + ' ' + str(element) + '\n')
        fd.close()

        el.send_keys(text)
        self.index += 1

    def my_clear_class_name(self, class_name):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        el = self.driver.find_element_by_class_name(class_name)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear ' + str(element) + '\n')
        el.clear()
        self.index += 1

    def my_press_code(self, code_num):
        self.get_screen_info()
        self.driver.press_keycode(code_num)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' press_code ' + str(code_num) + '\n')
        fd.close()
        self.index += 1

    def my_swipe(self,  start_x, start_y, end_x, end_y, duration):
        self.get_screen_info()
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe' + '\n')
        fd.close()
        self.index += 1

    def my_back_home(self):
        # 该函数是方便回到主界面
        # 点击左上角
        self.my_click_accessibilty_id("Open Drawer")
        # 点击 0，到达文件浏览的主界面
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/design_menu_item_text",1)

    def my_back_home0(self):
        # 该函数是方便回到主界面
        # 点击左上角
        self.my_click_accessibilty_id("Open Drawer")
        # 点击 0，到达文件浏览的主界面
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/design_menu_item_text", 0)

    def my_back_home1(self):
        from uiautomator import Device
        d = Device('emulator-5554')
        d.press.home()

        # 接下来定义每个场景的描述。
        # 该场景可修改的参数。

        # 文件浏览：前序状态算是无
        # 可以修改的参数：进入的文件夹的序列

    def file_browse_0(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
        '''
        if move_list is None:
            return
        for i in move_list:
            if i == -1:
                self.my_back()
            else:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_filename", i)

    def sidebar_6(self):
        self.my_click_accessibilty_id("Open Drawer")

    def search_3(self,text=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_search",0)
        if text is None:  # 点击返回
            self.my_click_accessibilty_id("Back")
        else:
            # 输入文本
            self.my_click_id("com.skyjos.apps.fileexplorerfree:id/search_scope_all_folders", 0)
            self.my_edit_id("android:id/search_src_text", text)
            self.my_click_accessibilty_id("Clear query")
            self.my_edit_id("android:id/search_src_text", text)
            # 点击回车键，到达搜索结果界面
            self.my_press_code(66)
            # self.my_back()
            self.my_click_accessibilty_id("Back")

    def search_only_3(self,text=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_search", 0)
        if text is None:  # 点击返回
            self.my_back()
        else:
            self.my_click_id("com.skyjos.apps.fileexplorerfree:id/search_scope_all_folders", 0)
            # 输入文本
            self.my_edit_id("android:id/search_src_text", text)
            self.my_press_code(66)
            self.my_click_accessibilty_id("Back")

    def new_folder_10_cancel(self):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_more", 0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/content", 1)
        # self.my_click_id("android:id/button1", 0)  # 点击ok
        self.my_click_id("android:id/button2", 0)  # 点击Cancel

    def new_folder_10(self,folder_name=None, is_success=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_more", 0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/content", 1)
        if folder_name is None:
            self.my_click_id("android:id/button2",0)
        else:
            self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_text_input",folder_name)
            if is_success:
                self.my_click_id("android:id/button1",0)  # 点击ok
            else:
                self.my_click_id("android:id/button2",0)  # 点击cancel

    def new_file_10(self,file_name=None, is_success=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_more", 0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/content", 2)
        if file_name is None:
            self.my_click_id("android:id/button2", 0)
        else:
            self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1", file_name)
            if is_success:
                self.my_click_id("android:id/button1", 0)  # 点击ok
            else:
                self.my_click_id("android:id/button2", 0)  # 点击cancel

    def text_edit_9(self, file_name,text=None):
        self.my_click_text(file_name)
        if text is not None:
            self.my_click_accessibilty_id("Edit")
            self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/reader_edittext",text)
            self.my_click_accessibilty_id("Edit")
        self.my_click_accessibilty_id("More")
        self.my_back()
        # self.my_click_id("me.zhanghai.android.files:id/content",0)
        self.my_click_accessibilty_id("Back")

    def menu_13(self):
        self.my_click_accessibilty_id("More")

    def properties_only_11(self):
        self.my_click_text("Info")
        self.my_click_accessibilty_id("Close")

    def properties_11(self, p_index):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button", p_index)
        self.properties_only_11()

    def rename1_12(self,file_index,is_success,rename_name):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button",file_index)
        self.my_click_text("Rename")
        text_before = self.driver.find_element_by_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1").get_attribute("text")
        indexss = text_before.find(".")
        if indexss == -1:
            self.my_clear_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1")
            self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1", rename_name)
        else:
            self.my_clear_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1")
            self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1", rename_name + text_before[indexss:])
        if is_success:
            self.my_click_id("android:id/button1", 0)
        else:
            self.my_click_id("android:id/button2", 0)

    def generate_random_str(self, randomlength=16):
        """
        生成一个指定长度的随机字符串
        """
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        length = len(base_str) - 1
        for i in range(randomlength):
            random_str += base_str[random.randint(0, length)]
        return random_str

    def long_click_select_1(self,begin_index):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_more",0)
        self.my_click_text("Select")
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_filename",begin_index)
        # time.sleep(2)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_deletebutton",0)
        self.my_click_id("android:id/button2",0)
        list1 = [begin_index-2,begin_index-1,begin_index+2,begin_index+1]
        for i in list1:
            if i >= 0:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_filename", i)
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_deletebutton", 0)
                self.my_click_id("android:id/button2", 0)

        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_morebutton",0)
        self.my_click_text("Archive")
        self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1", self.generate_random_str(6))
        self.my_click_id("android:id/button2", 0)
        self.my_click_classname("android.widget.ImageButton",0)

        # self.my_click_id("com.amaze.filemanager:id/action_mode_close_button",0)

        # com.amaze.filemanager: id / cpy,com.amaze.filemanager:id/delete,com.amaze.filemanager:id/cut
    def long_click_select_1_2(self, file_list):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_menu_more", 0)
        self.my_click_text("Select")
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_filename", file_list[0])
        # time.sleep(2)
        for i in range(len(file_list)):
            if i > 0:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_filename", file_list[i])

    def to_paste_4(self,copy_list,end,move_list=None):
        self.long_click_select_1_2(copy_list)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_copybutton",0)
        # self.my_back_home()
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/serverlist_local_item_title", 0)
        if move_list is not None:
            for j in move_list:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename",j)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename",end)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_save_button",0)
        self.my_click_classname("android.widget.ImageButton",0)

    def copy_43(self,copy_index,end,move_list=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button", copy_index)
        self.my_click_text("Copy to")
        # self.my_back_home()
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/serverlist_local_item_title", 0)
        if move_list is not None:
            for j in move_list:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", j)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", end)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_save_button", 0)
        # self.my_click_classname("android.widget.ImageButton", 0)

    def replace_or_skip_4(self,is_replace):
        if is_replace:
            self.my_click_id("android:id/button1",0)
        else:
            self.my_click_id("android:id/button2",0)

    def compress_2(self, compress_list, is_cancel, file_type):
        self.long_click_select_1_2(compress_list)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_morebutton", 0)
        self.my_click_text("Archive")
        self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1", self.generate_random_str(2))
        if is_cancel:
            self.my_click_id("android:id/button2", 0)
            self.my_click_classname("android.widget.ImageButton",0)
        else:
            self.my_click_id("android:id/button1", 0)

    def compress_2_1(self, compress_index, is_cancel, file_type):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button",compress_index)
        self.my_click_text("Archive")
        self.my_edit_id("com.skyjos.apps.fileexplorerfree:id/dialog_edit_text_1", self.generate_random_str(2))
        if is_cancel:
            self.my_click_id("android:id/button2", 0)
            # self.my_click_classname("android.widget.ImageButton",0)
        else:
            self.my_click_id("android:id/button1", 0)

    def delete_7(self,delete_index,is_success):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button",delete_index)
        self.my_click_text("Delete")
        if is_success:
            self.my_click_id("android:id/button1",0)
        else:
            self.my_click_id("android:id/button2",0)

    def long_click_delete_7(self,delete_list,is_success):
        self.long_click_select_1_2(delete_list)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_deletebutton",0)
        if is_success:
            self.my_click_id("android:id/button1",0)
        else:
            self.my_click_id('android:id/button2',0)
            self.my_click_classname("android.widget.ImageButton",0)

    def to_paste_41(self, cut_list, end, move_list=None):
        self.long_click_select_1_2(cut_list)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_movebutton",0)
        if move_list is not None:
            # self.my_click_id("com.skyjos.apps.fileexplorerfree:id/serverlist_local_item_title", 0)
            for j in move_list:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", j)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", end)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_save_button", 0)
        self.my_click_classname("android.widget.ImageButton", 0)

    def cut_4(self,cut_index,end,move_list=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button", cut_index)
        self.my_click_text("Move to")
        # self.my_back_home()
        # self.my_click_id("com.skyjos.apps.fileexplorerfree:id/serverlist_local_item_title", 0)
        if move_list is not None:
            for j in move_list:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", j)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", end)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_save_button", 0)
        # self.my_click_classname("android.widget.ImageButton", 0)

    def copy_4(self,cut_index,end,move_list=None):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button", cut_index)
        self.my_click_text("Copy to")
        # self.my_back_home()
        if move_list is not None:
            self.my_click_id("com.skyjos.apps.fileexplorerfree:id/serverlist_local_item_title", 0)
            for j in move_list:
                self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", j)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_item_filename", end)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_save_button", 0)
        # self.my_click_classname("android.widget.ImageButton", 0)

    def add_bookmark_15(self,add_list):
        for i in add_list:
            self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_more_button", i)
            self.my_click_text("Favorite")

    def bookmark_15(self):
        self.my_click_accessibilty_id("Open Drawer")
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/design_menu_item_text",0)
        self.my_click_text("Favorites")

    def browse_bookmark_15(self):
        self.my_click_accessibilty_id("Open Drawer")
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/design_menu_item_text", 4)

    def delete_bookmark_15(self,delete_list):
        for i in delete_list:
            self.my_swipe(start_x=950,start_y=210+100*i,end_x=750,end_y=210+100*i,duration=200)
            self.my_click_id("com.skyjos.apps.fileexplorerfree:id/favorites_item_delete",0)

    def my_swipe(self,  start_x, start_y, end_x, end_y, duration):
        self.get_screen_info()
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe' + '\n')
        fd.close()
        self.index += 1

    def music_5(self,file_index):
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folderlist_cell_list_filename", file_index)
        time.sleep(15)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_play_button",0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_repeat_button",0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_repeat_button", 0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_repeat_button", 0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_play_button", 0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_player_switch_button",0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_player_switch_button",0)
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/music_play_button", 0)
        self.my_click_accessibilty_id("Close")

    def my_to_settings(self):
        # self.my_click_accessibilty_id("Open Drawer")
        # self.my_click_id("com.skyjos.apps.fileexplorerfree:id/design_menu_item_text", 0)
        self.my_click_accessibilty_id("Settings")

    def my_settings(self):
        for i in range(3):
            self.my_click_id("android:id/switch_widget",i)
        for i in range(3):
            self.my_click_id("android:id/switch_widget",i)
        self.my_click_text("Text Encoding")
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/item_picker_cancel_button",0)
        self.my_click_text("Nearby Receive Location")
        self.my_click_id("com.skyjos.apps.fileexplorerfree:id/folder_picker_cancel_button",0)
        self.my_click_text("Maximum Cache Size")
        self.my_click_id("android:id/button2",0)
        self.my_swipe(406, 1322,406,100,500)
        self.my_click_text("Slideshow Settings")
        self.my_click_text("Play Each Slide for")
        self.my_click_id("android:id/button2",0)
        for i in range(2):
            self.my_click_id("android:id/switch_widget",i)
        for i in range(2):
            self.my_click_id("android:id/switch_widget",i)
        self.my_click_accessibilty_id("Back")
        self.my_click_accessibilty_id("Back")

