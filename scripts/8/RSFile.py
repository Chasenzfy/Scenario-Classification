# -*- coding:utf8 -*-

import time
import os
from appium.webdriver.common.touch_action import TouchAction


class RSFile:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 711   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path # 保存的截图的地址，例如 screens/
        self.xml_path = xml_path  # 保存的xml的地址，例如 screens/
        self.jump_pairs = jump_pairs  # 跳转文件的地址，例如：jump_pairs.txt
        self.activity_info = activity_info  # 记录当前界面的activity信息 例如：/activity_info.txt

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

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' back\n')
        fd.close()

        self.driver.back()
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

    def my_click_id(self, id):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_long_click_id(self, id):
        self.get_screen_info()

        el = self.driver.find_element_by_id(id)
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

    def my_press_code(self, code_num):
        self.get_screen_info()

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' press_code ' + str(code_num) + '\n')
        fd.close()

        self.driver.press_keycode(code_num)
        self.index += 1

    def my_swipe(self,  start_x, start_y, end_x, end_y, duration):
        self.get_screen_info()

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe' + '\n')
        fd.close()
        self.index += 1

    def my_back_home(self):
        # 该函数是方便回到主界面，状态是浏览文件的界面上面有 X
        # 点击 X
        self.my_click_id("com.rs.explorer.filemanager:id/home_tab_content_close_img")
        # 点击第一个 Internal Storage
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]")

    def my_enter_internal(self):
        # 该函数是直接点击Internal Storage进入文件目录
        # 点击第一个 Internal Storage
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]")

    # 接下来定义每个场景的描述。
    # 该场景可修改的参数。

    # 文件浏览：前序状态算是无
    # 可以修改的参数：进入的文件夹的序列
    def file_browse_0(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
            这里使用的的xpath，其中第1个对应的xpath尾部FrameLayout[1]，第2个对应的xpath尾部FrameLayout[2]，所以直接根据
        '''
        for i in move_list:
            if i == -1:
                self.my_back()
            else:
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
                # self.my_click_classname("android.widget.FrameLayout", i+10)

    # 长按选中：前序状态0：在文件浏览的状态下进行长按选中
    # 可以修改的参数：当前界面可供选中的行数，需要选中的列表，最后选中的数量为1还是多个
    def long_click_1(self, sum, select_list=None):
        '''
        :param sum: 表示当前界面的总行数，例如sum = 10，当前界面共有10个文件
        :param select_list: 表示在当前界面需要选中的标号，例如【2，3】。注意这个标号是从【1，sum】
                            标号和实际点的index是对应的。
        '''
        if select_list is None:  # 就把当前界面的sum个数的行长按选中，再取消选中，结果是没有选中任何东西
            # 长按选中第一个
            self.my_long_click_xpath_text(1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(2, sum+1):  # 例如共有5行，sum=5
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum+1):  # j = 6-1,-2,-3, -4,-5
                self.my_click_xpath_text(sum+1-i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
            # 点击 X，返回到原来的状态【什么也没选中的状态】
            self.my_click_accessibilty_id("Navigate up")
            # 后续需要重新按照select_list进行选中
        else:   # 否则就是选中select_list中的
            for i in select_list:
                if i == select_list[0]:
                    self.my_long_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
                else:
                    self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
                    # 最后的状态就是, 选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。
    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, name=None, compress_type=None, compress_level=None, password=None, is_success=None):
        '''
        :param name: 压缩的名称, 取值为None:直接点击cancel，相当于取消压缩。取值不为None：需要输入压缩的名称，再判断是否需要确认压缩
        :param compress_type: 压缩的类型，1：zip, 2:7z， 3：gz。其中1和2是任何情况都会有，3是只有压缩文件的时候才会有【压缩文件夹没有】
        :param compress_level: List, [1, 2, 3, 4]。针对类型1的压缩，1、2、3、4分别对应Store、Fast、Standard
        :param password：针对的是压缩类型为1和2，即zip 和 7z
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 两种调用方式，compress_2() 或者 compress_2("123",True)
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        self.my_click_text("Compress")
        if name is None:  # 点击cancel
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        else:
            # 清除原来的文本
            self.my_clear_id("com.rs.explorer.filemanager:id/filename")
            # 输入名字【共同的，都有】
            self.my_edit_id("com.rs.explorer.filemanager:id/filename", name)
            # 判断输入的类型【3是只有压缩的是文件的时候才会出现，1和2在任何情况下都会出现】
            if compress_type == 1:
                # 点击zip
                self.my_click_id("com.rs.explorer.filemanager:id/archive_type_zip")
                # 点击压缩级别的按钮
                self.my_click_id("com.rs.explorer.filemanager:id/spinner_compress_level")
                for i in compress_level:
                    self.my_click_classname("android.widget.RadioButton", i - 1)
                # 点击ok[是压缩级别的按钮]
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                if password is not None:
                    # 输入密码
                    self.my_edit_id("com.rs.explorer.filemanager:id/edit_psd", password)
                # 点击show password
                self.my_click_id("com.rs.explorer.filemanager:id/show_psd_checkbox")
                # 取消点击show password
                self.my_click_id("com.rs.explorer.filemanager:id/show_psd_checkbox")
            elif compress_type == 2:
                self.my_click_id("com.rs.explorer.filemanager:id/archive_type_7zip")
                if password is not None:
                    # 输入密码
                    self.my_edit_id("com.rs.explorer.filemanager:id/edit_psd", password)
                # 点击show password
                self.my_click_id("com.rs.explorer.filemanager:id/show_psd_checkbox")
                # 取消点击show password
                self.my_click_id("com.rs.explorer.filemanager:id/show_psd_checkbox")
            else:
                self.my_click_id("com.rs.explorer.filemanager:id/archive_type_gzip")
            if is_success:  # 点击OK
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                time.sleep(15)
            else:  # 点击cancel
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
    # 最后的状态是回到了状态0文件浏览

    # 文件搜索：前序状态0，是文件浏览的界面，点击search
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None):
        '''
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :return:
        '''
        # 点击文件浏览界面上的search
        self.my_click_id("com.rs.explorer.filemanager:id/home_tab_search_btn")
        if text is None:  # 点击返回
            self.my_click_accessibilty_id("Collapse")
        else:
            # 输入文本
            self.my_edit_id("com.rs.explorer.filemanager:id/search_src_text", text)
            # 点击清除
            self.my_click_accessibilty_id("Clear query")
            # 再次输入文本
            self.my_edit_id("com.rs.explorer.filemanager:id/search_src_text", text)
            # 点击menu
            self.my_click_id("com.rs.explorer.filemanager:id/menu_overflow")
            # 点击Search in Music
            self.my_click_text("Search in Music")
            # 点击menu
            self.my_click_id("com.rs.explorer.filemanager:id/menu_overflow")
            # 点击Search in Video
            self.my_click_text("Search in Video")
            # 点击menu
            self.my_click_id("com.rs.explorer.filemanager:id/menu_overflow")
            # 点击Search in App
            self.my_click_text("Search in App")
            # 点击menu
            self.my_click_id("com.rs.explorer.filemanager:id/menu_overflow")
            # 点击Search in Document
            self.my_click_text("Search in Document")
            # 点击menu
            self.my_click_id("com.rs.explorer.filemanager:id/menu_overflow")
            # 点击Search in image
            self.my_click_text("Search in Image")
            # 点击界面上的返回
            self.my_click_accessibilty_id("Collapse")
            # 再点击返回
            self.my_back()
        # 最后的状态是，回到搜索前的文件夹目录

    def paste_move_1(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
            这里使用的的xpath，其中第1个对应的xpath尾部FrameLayout[1]，第2个对应的xpath尾部FrameLayout[2]，所以直接根据
            用于剪切和复制粘贴后进行文件夹的移动
        '''
        for i in move_list:
            if i == -1:
                self.my_back()
            else:
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")

    def paste_move_2(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
            这里使用的的xpath，其中第1个对应的xpath尾部FrameLayout[1]，第2个对应的xpath尾部FrameLayout[2]，所以直接根据
            用于move to 和 copy to的移动
        '''
        for i in move_list:
            if i == -1:
                self.my_click_id("com.rs.explorer.filemanager:id/btn_up")
            else:
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")

    # 文件待粘贴：前序状态1：长按选择的界面点击copy或者cut  前序状态13：点击menu上的move to或者copy to按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, pre_num, is_paste, move_list):
        '''
        :param pre_num: 1为前序状态长按选中的界面点击copy
                        2为前序状态长按选中的界面点击cut
                        3为前序状态点击menu后 点击Move to
                        4为前序状态点击menu后 点击copy to
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面，属于文件浏览的界面。
        '''
        if pre_num == 1 or pre_num == 2:
            if pre_num == 1:
                # 点击copy
                self.my_click_text("Copy")
            else:
                # 点击cut
                self.my_click_text("Cut")
            # 进入不同的文件夹
            self.paste_move_1(move_list)
            # 判断是否粘贴
            if is_paste:
                self.my_click_text("Paste")
                time.sleep(8)
            else:  # 取消粘贴
                self.my_click_text("Cancel")
        else:
            if pre_num == 3:
                # 点击menu上的move to
                self.my_click_text("Move to")
            else:
                # 点击menu上的copy to
                self.my_click_text("Copy to")
            # 进入不同的文件夹
            self.paste_move_2(move_list)
            # 判断是否粘贴
            if is_paste:
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                time.sleep(8)
            else:
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        # 对于pre_num=3或者4的，is_paste=False的，最后停留的界面上长按选中【1】的界面
        # 其他情况，均为文件浏览【0】的界面

    # 音乐播放：前序状态为0，文件浏览的界面
    # 可以修改的参数：点击不同的音频文件、在不同的时间进行停止播放、保存playlist的名称
    def play_songs_5(self, song_index, playlist_name):
        # 点击音乐
        self.my_click_xpath_text(song_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
        # 点击RS Media Player
        self.my_click_text("RS Media Player")
        # 点击Just once
        self.my_click_id("com.rs.explorer.filemanager:id/open_recommend_once_txt")
        # 点击暂停
        self.my_click_id("com.rs.explorer.filemanager:id/btn_play")
        # 点击播放左边的
        self.my_click_id("com.rs.explorer.filemanager:id/btn_play_pre")
        # 点击播放顺序【单曲循环】
        self.my_click_id("com.rs.explorer.filemanager:id/btn_play_order")
        # 点击播放顺序【随机播放】
        self.my_click_id("com.rs.explorer.filemanager:id/btn_play_order")
        # 点击播放列表
        self.my_click_id("com.rs.explorer.filemanager:id/btn_play_list")
        # 点击save
        self.my_click_id("com.rs.explorer.filemanager:id/tv_songlist_save")
        # 输入playlist+playlist
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", playlist_name+playlist_name)
        # 点击cancel
        self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        # 继续点击save
        self.my_click_id("com.rs.explorer.filemanager:id/tv_songlist_save")
        # 输入playlist名字
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", playlist_name)
        # 点击OK
        self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
        # 点击播放列表上的menu
        self.my_click_id("com.rs.explorer.filemanager:id/btn_music_more")
        # 点击Properties
        self.my_click_text("Properties")
        # 点击cancel
        self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        # 点击播放列表上的menu
        self.my_click_id("com.rs.explorer.filemanager:id/btn_music_more")
        # 点击Remove from playlist
        self.my_click_text("Remove from playlist")
        # 点击删除
        self.my_click_id("com.rs.explorer.filemanager:id/tv_songlist_delete")
        '''
        # 点击播放列表的menu
        self.my_click_id("com.rs.explorer.filemanager:id/btn_music_more")
        # 点击Remove from playlist
        self.my_click_text("Remove from playlist")
        '''
        # 点击返回
        self.my_back()
        # 点击播放界面的menu
        self.my_click_accessibilty_id("More")
        # 点击add to playlist
        self.my_click_text("Add to playlist")
        # 点击create new playlist
        self.my_click_text("Create new playlist")
        # 点击cancel
        self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        # 点击menu
        self.my_click_accessibilty_id("More")
        # 点击Exit
        self.my_click_text("Exit")
        # 最后回到了文件浏览的界面

    # 侧边栏：前序状态0，文件浏览的界面点击侧边栏
    # 可以修改的参数：无
    def sidebar_6(self):
        self.my_click_accessibilty_id("Navigate up")
        return

    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, is_delete, is_success):
        '''
        :param is_delete: True:删除， False：move to recycle bin
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_text("Delete")
        if is_delete:  # 取消点击move to recyle bin
            self.my_click_id("com.rs.explorer.filemanager:id/recycle_prompt_checkbox")
        if is_success:
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
            time.sleep(5)
        else:
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
    # is_success=False，也就是没有删除成功的话，停留在长按选中【1】的状态，否则是文件浏览【0】的状态

    # 文件解压缩：前序状态13，是需要到达menu后的界面
    # 可以修改的参数：解压路径、解压编码、解压缩的文件
    def decompress_8(self, is_success, password=None):
        '''
        :param is_success: True，就解压；False，直接取消解压
        :param password: 针对那些压缩时加密的压缩包，如果不传入参数说明原来没有加密。
        :return:
        '''
        self.my_click_text("Extract to")
        if is_success:
            # 点击current path
            self.my_click_id("com.rs.explorer.filemanager:id/radio_current_path")
            # 点击choose path
            self.my_click_id("com.rs.explorer.filemanager:id/radio_assign_path")
            # 点击解码编码的下拉框
            self.my_click_id("com.rs.explorer.filemanager:id/btn_charset")
            # 点击Unicode
            self.my_click_text("Unicode(UTF-8)")
            # 点击解码编码的下拉框
            self.my_click_id("com.rs.explorer.filemanager:id/btn_charset")
            # 点击GBK
            self.my_click_text("Simplified Chinese(GBK)")
            # 点击解码编码的下拉框
            self.my_click_id("com.rs.explorer.filemanager:id/btn_charset")
            # 点击Auto
            self.my_click_text("Auto")
            # 点击默认的解压文件夹路径
            self.my_click_id("com.rs.explorer.filemanager:id/radio_archive_path")
            # 点击ok
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
            time.sleep(8)
            if password is not None:
                self.my_edit_id("com.rs.explorer.filemanager:id/edit_psd", password+password)
                # 清除刚刚输入的
                self.my_clear_id("com.rs.explorer.filemanager:id/edit_psd")
                # 重新输入
                self.my_edit_id("com.rs.explorer.filemanager:id/edit_psd", password)
                # 点击show password
                self.my_click_id("com.rs.explorer.filemanager:id/show_psd_checkbox")
                # 点击ok
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                time.sleep(8)
        else:
            # 点击Cancel
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")

    # 文本编辑：前序状态0，直接点击文件浏览目录中的txt文件
    # 可以修改的参数：文本内容
    def text_edit_9(self, text_index, encoding_list, text_input):
        '''
        :param text_index:  要点击的text的位置【例如在文件浏览界面的中第5个，传入5】
        :param encoding_list: List，例如【1，2，3，1】，1对应Auto，2对应Unicode
        :param text_input: 要输入的文本
        :return:
        '''
        temp = ['Auto', 'Unicode(UTF-8)', 'Simplified Chinese(GBK)', 'Western Europe(ISO–8859–1)',
                'Western languages(Windows)', 'Korean(EUC-KR)', 'Japanese(EUC-JP)', 'Japanese(Shift_JIS)']
        # 点击文件
        self.my_click_xpath_text(text_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[")
        # 点击 text
        self.my_click_text("Text")
        # 点击RS Note
        self.my_click_text("RS Note Editor")
        # 点击Just once
        self.my_click_id("com.rs.explorer.filemanager:id/open_recommend_once_txt")
        for i in encoding_list:
            # 点击 menu
            self.my_click_id("com.rs.explorer.filemanager:id/menu_more")
            # 点击encoding
            self.my_click_text("Encoding")
            # 点击对应的编码
            self.my_click_text(temp[i-1])
        # 点击menu
        self.my_click_id("com.rs.explorer.filemanager:id/menu_more")
        # 点击edit
        self.my_click_text("Edit")
        # 输入文本
        self.my_edit_id("com.rs.explorer.filemanager:id/text_edit", text_input)
        # 点击保存
        self.my_click_id("com.rs.explorer.filemanager:id/menu_save")
        # 点击 yes
        self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
        # 点击 返回
        self.my_click_accessibilty_id("Navigate up")
        # 最后的状态是 回到文件浏览的界面

    # 创建文件夹：前序状态13，是需要到达menu后的界面。
    # 可以修改的参数，新建的类型【文件夹/文件】，是否成功，名称
    def new_folder_10(self, new_type, name=None):
        '''
        :param new_type: 1为Folder，2为File
        :param name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，然后创建成功
        :return:
        '''
        # 点击new
        self.my_click_text("New")
        if new_type == 1:  # 新建Folder
            # 点击Folder
            self.my_click_text("Folder")
        else:
            # 点击File
            self.my_click_text("File")
        # 清除上面的默认的文件夹名称Folder/File
        self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
        if name is None:
            # 点击cancel
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        else:
            # 重新输入名称
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", name)
            # 点击 ok
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")

    # 查看文件属性：前序状态13，是长按选中一个或者多个后点击menu，才有Properties按钮
    # 可以修改的参数：长按选中的个数，一个和多个，后面的界面不一样。
    def properties_browse_11(self, select_nums):
        # 点击Properties按钮。
        self.my_click_text("Properties")
        if select_nums == 1:
            # 点击more
            self.my_click_id("com.rs.explorer.filemanager:id/show_details_button")
            # 点击返回
            self.my_click_accessibilty_id("Navigate up")
        else:
            # 点击cancel
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        # 点击完返回后，查看文件后的属性还是处于长按选中的状态，可以继续进行其他测试

    # 重命名：前序状态13，是点击长按选中的界面上的rename
    # 可以修改的参数，修改的文件名，是否修改
    def rename_12(self, rename_num, name, is_success, start_number=None, prefix=None):
        '''
        :param rename_num: 1表示对一个文件进行重命名， 2 表示对多个文件重命名【分2种】
        :param name: 需要输入修改的名称【对于多文件的重命名，使用prefix的时候，name只是用于测试，但是没有真正用于修改文件名】
        :param is_success: 是否修改，True,False
        :param start_number: 多文件名命名的时候的第一种情况name+start_number
        :param prefix: 多文件命名的时候的第二种情况：prefix+original name【实际上这时候传入的name没有真正用于修改文件名】
        :return:
        '''
        # 点击Rename
        self.my_click_text("Rename")
        if rename_num == 1:  # 单文件命名
            # 清除原来的名称
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
            # 重新输入新的名称
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", name)
            if is_success:
                # 确认修改
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                time.sleep(5)
            else:
                # 取消修改
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        else:
            # 针对的是多个文件夹的命名修改
            if start_number is not None:  # 针对的是name+Number的命名方式
                # 点击new name+Number
                self.my_click_id("com.rs.explorer.filemanager:id/radio_number")
                # 输入错误的名字
                self.my_edit_id("com.rs.explorer.filemanager:id/new_name_edit", name+name)
                # 清除输入的
                self.my_clear_id("com.rs.explorer.filemanager:id/new_name_edit")
                # 重新输入
                self.my_edit_id("com.rs.explorer.filemanager:id/new_name_edit", name)
                # 输入start  number
                self.my_edit_id("com.rs.explorer.filemanager:id/num_start_value", start_number)
                if is_success:
                    self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                    time.sleep(8)
                else:
                    self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
            if prefix is not None:  # 针对的是prefix+original name
                # 点击prefix
                self.my_click_id("com.rs.explorer.filemanager:id/radio_new")
                # 输入prefix
                self.my_edit_id("com.rs.explorer.filemanager:id/new_name_suffix_edit", prefix)
                # 输入扩展名
                self.my_edit_id("com.rs.explorer.filemanager:id/new_ext_name", name)
                # 清除扩展名
                self.my_clear_id("com.rs.explorer.filemanager:id/new_ext_name")
                if is_success:
                    self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
                    time.sleep(8)
                else:
                    self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        # 最后的状态，回到文件浏览的状态0

    # 点击menu：前序状态0或者1，文件浏览的界面的menu/文件长按后的界面的menu。
    # 可以修改的参数：无
    def menu_13(self, pre_num):
        '''
        :param pre_num: 0表示前序状态为文件浏览的界面，1表示前序状态为长按选中的界面
        :return:
        '''
        if pre_num == 0:  # 前序状态为0
            self.my_click_accessibilty_id("More")
        else:  # 前序状态为1
            self.my_click_text("More")

    # 设置：前序状态为6，在侧边栏的界面点击设置按钮
    # 可以修改的参数：排序的选项，点击的checkbox，是否清理历史
    def settings_14(self):
        '''
        :param sort_list: 类型为List,表示对于排序，每次点击的选项。【取值范围0-3】
                          其中name,size,Last modified, file extension分别为0，1，2，3。
                          例如传入[1,2,1,3],就是点击size 和 Last modified，size, file extension。
                          这里设定最后还是会点击name，也就是第0项
        :param checkbox_list:类型为list，表示该次测试中点击6个checkbox中的哪几个。【取值范围0-5】
                             例如传入[1,1,2,3]，就是分别点击第i个checkbox
                             // 不能传入0。会导致原来的文件顺序改变
        :param is_clear:True，表示点击OK；False表示点击Cancel
        '''
        # 点击侧边栏的设置按钮
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView")
        # 向上滑动
        self.my_swipe(500, 1640, 500, 160, 200)
        # 点击 hide list protection
        self.my_click_text("Turn on password to protect your hide list resources")
        # 输入密码
        self.my_edit_id("com.rs.explorer.filemanager:id/code_new_passwd", "111")
        # 确认密码
        self.my_edit_id("com.rs.explorer.filemanager:id/code_confirm_passwd", "111")
        # 清理密码
        self.my_clear_id("com.rs.explorer.filemanager:id/code_confirm_passwd")
        # 点击cancel
        self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
        temp_list = [1, 2, 3, 4, 3, 2, 1, 4]
        for i in temp_list:
            self.my_click_classname("android.widget.CheckBox", i)
        # 点击rate us
        self.my_click_text("Rate us")
        # 点击close
        self.my_click_id("com.rs.explorer.filemanager:id/dialog_rate_close")
        # 点击About
        self.my_click_text("About")
        # 点击user experience program
        self.my_click_id("android:id/checkbox")
        # 点击user experience program
        self.my_click_id("android:id/checkbox")
        # 点击返回
        self.my_click_accessibilty_id("Navigate up")
        temp_list = [0, 1, 2, 2, 1, 0]
        for i in temp_list:
            self.my_click_classname("android.widget.CheckBox", i)
        # 点击Theme style
        self.my_click_text("Theme style")
        # 点击返回
        self.my_back()
        # 点击返回
        self.my_back()
        # 点击返回
        self.my_back()

    # bookmarks：前序状态为13，分为两种：
    # 一种是添加bookmarks，长按后添加bookmarks，1->13->15，注意每次只能长按一个文件进行添加
    # 另一种是对已经添加的bookmarks进行删除，长按等。前序状态为侧边栏6，点击bookmarks
    # 测试时注意，需要先添加bookmarks，再测试！
    # 可修改的参数：添加哪些bookmarks，删除的bookmark的位置，是否删除
    def bookmarks_15(self, name=None, index=None, new_name=None):
        '''
        :param long_click_list: 需要长按删除的列表，初始是有2个bookmarks【对应的classname标号为0，1】，所以从2开始标号
        :param is_delete: 是否需要删除，如果删除的话，就重新长按选中
        :return:
        '''
        if name is not None:
            # 第一种点击menu上的 Add to favorite 添加bookmark
            self.my_click_text("Add to favorite")
            # 清除原来默认的文本
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
            # 重新输入新的bookmarks名称
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", name)
            # 点击ok
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
        else:
            '''
            # 第二种是点击展开Bookmarks,前序状态为侧边栏
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[5]")
            # 长按进行操作第index个bookmark，第1个就是bookmark1
            self.my_long_click_xpath_text(index + 7, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[")
            # 点击properties
            self.my_click_text("Properties")
            # 点击cancel
            self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
            # 长按进行操作第index个bookmark，第1个就是bookmark1
            self.my_long_click_xpath_text(index + 7, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[")
            # 点击rename【bookmark重命名】
            self.my_click_text("Rename")
            if new_name is None:
                # 点击cancel
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
            else:
                # 清除名称
                self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
                # 输入名称
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", new_name)
                # 点击ok
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
            # 长按进行操作的第index个bookmark，第1个就是bookmark1
            self.my_long_click_xpath_text(index + 7, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[")
            # 点击remove from list
            self.my_click_text("Remove from list")
            '''
            # 点击Add
            self.my_click_xpath_text(6, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[')
            if new_name is None:
                # 点击cancel
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_negative")
            else:
                # 输入path
                self.my_edit_id("com.rs.explorer.filemanager:id/input_url", new_name)
                # 输入name
                self.my_edit_id("com.rs.explorer.filemanager:id/input_name", new_name)
                # 点击add
                self.my_click_id("com.rs.explorer.filemanager:id/md_button_positive")
            # 这时候回到了文件浏览的界面，需要把侧边栏的bookmarks给收起来
            # 点击侧边栏
            self.sidebar_6()
            # 点击bookmarks
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/edili.M0/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[5]")
            # 点击返回
            self.my_back()

        # 最后该场景回到的界面为文件浏览的界面
