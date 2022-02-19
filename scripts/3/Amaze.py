# -*- coding:utf8 -*-
import time
import os
import random

from appium.webdriver.common.touch_action import TouchAction


class Amaze:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 592  # 当前的截图和xml的编号
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
        self.my_click_accessibilty_id("Navigate up")
        # 点击 0，到达文件浏览的主界面
        self.my_click_id('com.amaze.filemanager:id/design_menu_item_text', 0)
        time.sleep(2)

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
        for i in move_list:
            if i == -1:
                self.my_back()
            else:
                self.my_click_id("com.amaze.filemanager:id/firstline", i)

    def sidebar_6(self):
        self.my_click_accessibilty_id("Navigate up")

    def search_3(self,text=None):
        self.my_click_id("com.amaze.filemanager:id/search",0)
        if text is None:  # 点击返回
            self.my_back()
        else:
            # 输入文本
            self.my_edit_id("com.amaze.filemanager:id/search_edit_text", text)
            self.my_click_id("com.amaze.filemanager:id/search_close_btn",0)
            self.my_click_id("com.amaze.filemanager:id/img_view_back",0)
            self.my_click_id("com.amaze.filemanager:id/search", 0)
            self.my_edit_id("com.amaze.filemanager:id/search_edit_text", text)
            self.my_search()

    def search_only_3(self,text=None):
        self.my_click_id("com.amaze.filemanager:id/search", 0)
        if text is None:  # 点击返回
            self.my_back()
        else:
            # 输入文本
            self.my_edit_id("com.amaze.filemanager:id/search_edit_text", text)
            self.my_search()

    def new_folder_10_cancel(self):
        self.my_click_id("com.amaze.filemanager:id/fabs_menu", 0)
        self.my_click_id("com.amaze.filemanager:id/sd_main_fab", 0)

    def new_folder_10(self,folder_name=None, is_success=None):
        self.my_click_id("com.amaze.filemanager:id/fabs_menu",0)
        self.my_click_id("com.amaze.filemanager:id/menu_new_folder", 0)
        if folder_name is None:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNeutral",0)
        else:
            self.my_edit_id("com.amaze.filemanager:id/singleedittext_input",folder_name)
            if is_success:
                self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)  # 点击ok
            else:
                self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNeutral",0)  # 点击cancel

    def new_file_10(self,file_name=None, is_success=None):
        self.my_click_id("com.amaze.filemanager:id/fabs_menu",0)
        self.my_click_id("com.amaze.filemanager:id/menu_new_file",0)
        if file_name is None:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNeutral",0)
        else:
            self.my_edit_id("com.amaze.filemanager:id/singleedittext_input",file_name)
            if is_success:
                self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)  # 点击ok
            else:
                self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNeutral",0)  # 点击cancel

    def text_edit_only_9(self, file_name,text=None):
        self.my_click_text(file_name)
        if text is not None:
            self.my_edit_id("com.amaze.filemanager:id/fname",text)
            self.my_click_id("com.amaze.filemanager:id/save",0)
        self.menu_13()
        self.properties_only_11(is_detail=True)
        self.my_click_id("com.amaze.filemanager:id/find",0)
        self.my_edit_id("com.amaze.filemanager:id/search_box","d")
        self.my_click_id("com.amaze.filemanager:id/next",0)
        self.my_click_id("com.amaze.filemanager:id/next", 0)
        self.my_click_id("com.amaze.filemanager:id/close",0)
        self.my_click_accessibilty_id("Navigate up")

    def text_edit_9(self, file_name,search_ch,text=None,):
        self.my_click_text(file_name)
        if text is not None:
            self.my_edit_id("com.amaze.filemanager:id/fname",text)
            self.my_click_id("com.amaze.filemanager:id/save",0)
        self.menu_13()
        self.properties_only_11(is_detail=True)
        self.my_click_id("com.amaze.filemanager:id/find",0)
        self.my_edit_id("com.amaze.filemanager:id/search_box",search_ch)
        self.my_click_id("com.amaze.filemanager:id/next",0)
        self.my_click_id("com.amaze.filemanager:id/next", 0)
        self.my_click_id("com.amaze.filemanager:id/close",0)
        self.my_click_accessibilty_id("Navigate up")

    def menu_13(self):
        self.my_click_accessibilty_id("More options")

    def properties_only_11(self,is_detail):
        if is_detail:
            self.my_click_text("Details")
        else:
            self.my_click_text("Properties")
        self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)

    def properties_11(self, is_detail, p_index):
        self.my_click_id("com.amaze.filemanager:id/properties", p_index)
        if is_detail:
            self.my_click_text("Details")
        else:
            self.my_click_text("Properties")
        self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive", 0)

    def rename_12_only(self):
        self.my_click_text("Rename")
        text_before = self.driver.find_element_by_id("com.amaze.filemanager:id/singleedittext_input").get_attribute("text")
        indexss = text_before.find(".")
        if indexss == -1:
            self.my_clear_id("com.amaze.filemanager:id/singleedittext_input")
            self.my_edit_id("com.amaze.filemanager:id/singleedittext_input", "123"+self.generate_random_str(8))
        else:
            self.my_clear_id("com.amaze.filemanager:id/singleedittext_input")
            self.my_edit_id("com.amaze.filemanager:id/singleedittext_input","123"+self.generate_random_str(8)+text_before[indexss:])
        self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative",0)

    def rename_12(self,file_index,is_success):
        self.my_click_id("com.amaze.filemanager:id/properties",file_index)
        self.my_click_text("Rename")
        text_before = self.driver.find_element_by_id("com.amaze.filemanager:id/singleedittext_input").get_attribute(
            "text")
        indexss = text_before.find(".")
        if indexss == -1:
            self.my_clear_id("com.amaze.filemanager:id/singleedittext_input")
            self.my_edit_id("com.amaze.filemanager:id/singleedittext_input", "123" + self.generate_random_str(8))
        else:
            self.my_clear_id("com.amaze.filemanager:id/singleedittext_input")
            self.my_edit_id("com.amaze.filemanager:id/singleedittext_input",
                            "123" + self.generate_random_str(8) + text_before[indexss:])
        if is_success:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive", 0)
        else:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative", 0)

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
        self.my_long_click_id("com.amaze.filemanager:id/firstline",begin_index)
        self.my_click_accessibilty_id("Delete")
        self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative",0)
        list1 = [begin_index-2,begin_index-2,begin_index+2,begin_index+1]
        for i in list1:
            if i >= 0:
                self.my_long_click_id("com.amaze.filemanager:id/firstline", i)
                self.my_click_accessibilty_id("Delete")
                self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative",0)

        self.my_click_accessibilty_id("More options")
        self.my_click_text("Compress")
        self.my_edit_id("com.amaze.filemanager:id/singleedittext_input", self.generate_random_str(8)+".zip")
        self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative", 0)

        # self.my_click_id("com.amaze.filemanager:id/action_mode_close_button",0)

        # com.amaze.filemanager: id / cpy,com.amaze.filemanager:id/delete,com.amaze.filemanager:id/cut

    def to_paste_4(self,copy_list,end,move_list=None):
        for i in copy_list:
            self.my_long_click_id("com.amaze.filemanager:id/firstline", i)
        self.my_click_accessibilty_id("Copy")
        self.my_back_home()
        if move_list is not None:
            for j in move_list:
                self.my_click_id("com.amaze.filemanager:id/firstline",j)
                self.my_back_home()
        self.my_click_id("com.amaze.filemanager:id/firstline",end)
        self.my_click_id("com.amaze.filemanager:id/snackbar_action",0)

    def cancel_or_skip_4(self,is_cancel):
        if is_cancel:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNeutral",0)
        else:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)

    def compress_2(self,compress_list,is_cancel):
        for i in compress_list:
            self.my_long_click_id("com.amaze.filemanager:id/firstline", i)
        self.my_click_accessibilty_id("More options")
        self.my_click_text("Compress")
        self.my_edit_id("com.amaze.filemanager:id/singleedittext_input", self.generate_random_str(8) + ".zip")
        if is_cancel:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative", 0)
        else:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)

    def delete_7(self,delete_index,is_success):
        self.my_click_id("com.amaze.filemanager:id/properties",delete_index)
        self.my_click_text("Delete")
        if is_success:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)
        else:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative",0)

    def long_click_delete_7(self,delete_list,is_success):
        for i in delete_list:
            self.my_long_click_id("com.amaze.filemanager:id/firstline", i)
        self.my_click_accessibilty_id("Delete")
        if is_success:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)
        else:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative",0)
            self.my_click_id("com.amaze.filemanager:id/action_mode_close_button", 0)

    def to_paste_41(self,cut_list,end,move_list=None):
        for i in cut_list:
            self.my_long_click_id("com.amaze.filemanager:id/firstline", i)
        self.my_click_accessibilty_id("Cut")
        self.my_back_home()
        if move_list is not None:
            for j in move_list:
                self.my_click_id("com.amaze.filemanager:id/firstline",j)
                self.my_back_home()
        self.my_click_id("com.amaze.filemanager:id/firstline",end)
        self.my_click_id("com.amaze.filemanager:id/snackbar_action",0)

    def cut_4(self,cut_index,end_index):
        self.my_click_id("com.amaze.filemanager:id/properties", cut_index)
        self.my_click_text("Cut")
        self.my_back_home()
        self.file_browse_0([end_index])
        self.my_click_id("com.amaze.filemanager:id/snackbar_action", 0)

    def copy_4(self,cut_index,end_index):
        self.my_click_id("com.amaze.filemanager:id/properties", cut_index)
        self.my_click_text("Cut")
        self.my_back_home()
        self.file_browse_0([end_index])
        self.my_click_id("com.amaze.filemanager:id/snackbar_action", 0)

    def add_bookmark_15(self,add_list):
        for i in add_list:
            self.my_click_id("com.amaze.filemanager:id/properties", i)
            self.my_click_text("Add to Bookmarks")

    def browse_bookmark_15(self,browse_index):
        self.my_click_accessibilty_id("Navigate up")
        self.my_click_id("com.amaze.filemanager:id/design_menu_item_text", browse_index+2)

    def rename_bookmark_15(self,rename_index,text,is_success):
        self.my_click_accessibilty_id("Navigate up")
        self.my_click_id("com.amaze.filemanager:id/design_menu_item_action_area",rename_index+2)
        self.my_edit_id("com.amaze.filemanager:id/editText4",text)
        if is_success:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultPositive",0)
        else:
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNeutral",0)

    def delete_bookmark_15(self,delete_list):
        self.my_click_accessibilty_id("Navigate up")
        for i in delete_list:
            self.my_click_id("com.amaze.filemanager:id/design_menu_item_action_area",i+2)
            self.my_click_id("com.amaze.filemanager:id/md_buttonDefaultNegative",0)

    def my_swipe(self,  start_x, start_y, end_x, end_y, duration):
        self.get_screen_info()
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe' + '\n')
        fd.close()
        self.index += 1

    def my_to_settings(self):
        self.my_click_accessibilty_id("Navigate up")
        self.my_swipe(406, 1322,406,100,500)
        self.my_click_id("com.amaze.filemanager:id/design_menu_item_text", -1)

    def my_settings(self):
        # Theme
        self.my_click_id("android:id/title",1)
        # Material Light
        self.my_click_classname("android.widget.TextView",1)

        # Color
        self.my_click_id("android:id/title",2)
        # Select color config
        self.my_click_id("android:id/title",1)
        # Preselected configs
        self.my_click_id("android:id/title",0)
        # Orange
        self.my_click_classname("android.widget.TextView",2)
        # CANCEL
        self.my_click_id("android:id/button2",0)
        # Preselected configs
        self.my_click_id("android:id/title",0)
        # Custom
        self.my_click_classname("android.widget.TextView",5)
        # OK
        self.my_click_id("android:id/button1",0)
        # Primary Color (Left Tab)
        self.my_click_id("android:id/title",2)
        # tap red color
        self.my_click_id("com.amaze.filemanager:id/icon",0)
        # back
        self.my_click_accessibilty_id("Navigate up")
        # Colorize Icons
        self.my_click_id("android:id/title",2)

        # Colorize Navigation bar
        self.my_click_id("android:id/title",3)
        self.my_click_id("android:id/title",3)
        # back
        self.my_click_accessibilty_id("Navigate up")
        ### test Use circular icons: 56-66
        self.my_click_id("android:id/title",3)
        self.my_click_id("android:id/title", 9)
        self.my_click_accessibilty_id("Navigate up")
        self.my_swipe(406, 1322, 406, 100, 100)

