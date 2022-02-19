# -*- coding:utf8 -*-

import time
import os
from appium.webdriver.common.touch_action import TouchAction


class ES:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 800   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path # 保存的截图的地址，例如 /Users/lgy/Desktop/测试脚本/RSFileManager/screens/
        self.xml_path = xml_path  # 保存的xml的地址，例如 /Users/lgy/Desktop/测试脚本/RSFileManager/screens/
        self.jump_pairs = jump_pairs  # 跳转文件的地址，例如：'/Users/lgy/Desktop/测试脚本/RSFileManager/jump_pairs.txt'
        self.activity_info = activity_info  # 记录当前界面的activity信息 例如：/OIFM/activity_info.txt

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
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
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
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")

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
            self.my_long_click_xpath_text(1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(2, sum+1):  # 例如共有5行，sum=5
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum+1):  # j = 6-1,-2,-3, -4,-5
                self.my_click_xpath_text(sum+1-i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
            # 点击 cancel
            self.my_click_id("com.estrongs.android.pop:id/tool_select_cancel")
            # 后续需要重新按照select_list进行选中
        else:   # 否则就是选中select_list中的
            for i in range(len(select_list)):
                if i == 0:
                    self.my_long_click_xpath_text(select_list[i], "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
                else:
                    self.my_click_xpath_text(select_list[i], "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
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
        self.my_click_text("COMPRESS")
        if name is None:  # 点击cancel
            self.my_click_id("com.estrongs.android.pop:id/negativeBtn")
        else:
            # 清除原来的文本
            self.my_clear_id("com.estrongs.android.pop:id/filename")
            # 输入名字【共同的，都有】
            self.my_edit_id("com.estrongs.android.pop:id/filename", name)
            # 判断输入的类型【3是只有压缩的是文件的时候才会出现，1和2在任何情况下都会出现】
            if compress_type == 1:
                # 点击zip
                self.my_click_id("com.estrongs.android.pop:id/archive_type_zip")
                # 点击压缩级别的按钮
                self.my_click_id("com.estrongs.android.pop:id/spinnerCompressLevel")
                for i in compress_level:
                    self.my_click_classname("android.widget.RadioButton", i - 1)
                # 点击ok[是压缩级别的按钮]
                self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
                if password is not None:
                    # 输入密码
                    self.my_edit_id("com.estrongs.android.pop:id/etPassword", password)
                # 点击show password
                self.my_click_id("com.estrongs.android.pop:id/cbxShowPassword")
                # 取消点击show password
                self.my_click_id("com.estrongs.android.pop:id/cbxShowPassword")
            elif compress_type == 2:
                self.my_click_id("com.estrongs.android.pop:id/archive_type_7zip")
                if password is not None:
                    # 输入密码
                    self.my_edit_id("com.estrongs.android.pop:id/etPassword", password)
                # 点击show password
                self.my_click_id("com.estrongs.android.pop:id/cbxShowPassword")
                # 取消点击show password
                self.my_click_id("com.estrongs.android.pop:id/cbxShowPassword")
            else:
                self.my_click_id("com.estrongs.android.pop:id/archive_type_gzip")
            if is_success:  # 点击OK
                self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
                time.sleep(15)
            else:  # 点击cancel
                self.my_click_id("com.estrongs.android.pop:id/negativeBtn")
    # 最后的状态是回到了状态0文件浏览

    # 文件搜索：前序状态0，是文件浏览的界面，点击search
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None, menu_list=None):
        '''
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :param menu_list: menu中筛选的list。取值范围1-5。【1，2】
        :return:
        '''
        # 点击文件浏览界面上的search
        self.my_click_id("com.estrongs.android.pop:id/main_tab_search_icon_iv")
        if text is None:  # 点击返回
            self.my_click_accessibilty_id("Collapse")
        else:
            # 输入文本
            self.my_edit_id("com.estrongs.android.pop:id/search_src_text", text + text)
            time.sleep(2)
            # 点击清除
            self.my_click_accessibilty_id("Clear query")
            # 再次输入文本
            self.my_edit_id("com.estrongs.android.pop:id/search_src_text", text)
            time.sleep(2)

            list1 = ['SEARCH IN IMAGE', 'SEARCH IN MUSIC', 'SEARCH IN VIDEO', 'SEARCH IN APP', 'SEARCH IN DOCUMENT']
            for i in menu_list:
                # 点击menu
                self.my_click_id("com.estrongs.android.pop:id/menu_overflow")
                # 点击search in
                self.my_click_text(list1[i-1])

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
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")

    def paste_move_2(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
            这里使用的的xpath，其中第1个对应的xpath尾部FrameLayout[1]，第2个对应的xpath尾部FrameLayout[2]，所以直接根据
            用于move to 和 copy to的移动
        '''
        for i in move_list:
            if i == -1:
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
            else:
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")

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
                self.my_click_text("MOVE TO")
            else:
                # 点击menu上的copy to
                self.my_click_text("COPY TO")
            # 进入不同的文件夹
            self.paste_move_2(move_list)
            # 判断是否粘贴
            if is_paste:
                self.my_click_text("OK")
                time.sleep(8)
            else:
                self.my_click_text("CANCEL")
        # 对于pre_num=3或者4的，is_paste=False的，最后停留的界面上长按选中【1】的界面
        # 其他情况，均为文件浏览【0】的界面

    # 音乐播放：前序状态为0，文件浏览的界面
    # 可以修改的参数：点击不同的音频文件、在不同的时间进行停止播放、保存playlist的名称
    def play_songs_5(self, song_index, playlist_name, new_name):
        '''
        :param song_index:  点击的第几首歌
        :param playlist_name: 新建的playList名字
        :param new_name: 重命名
        :return:
        '''
        # 点击音乐
        self.my_click_xpath_text(song_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
        # 点击ES Media Player
        self.my_click_text("ES Media Player")
        # 点击This Time Only
        self.my_click_text("This Time Only")
        # 点击暂停
        self.my_click_id("com.estrongs.android.pop:id/btn_play")

        # 点击保存到play list
        self.my_click_id("com.estrongs.android.pop:id/btn_playlist_add")
        # 点击 Create new play list
        self.my_click_text("Create new play list")
        # 输入 名字
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", playlist_name)
        # 点击ok
        self.my_click_text("OK")

        # 点击最右边的图标
        self.my_click_id("com.estrongs.android.pop:id/btn_playlist")
        # 点击list下拉
        self.my_click_id("com.estrongs.android.pop:id/iv_icon_down_arrow")
        # 点击刚刚添加的 playlist_name
        self.my_click_text(playlist_name)
        # 选中音乐
        self.my_click_id("com.estrongs.android.pop:id/btn_music_more")
        # 点击 Remove from playlist
        self.my_click_text("Remove from playlist")

        # 点击 menu
        self.my_click_id("com.estrongs.android.pop:id/menu_overflow")
        # 点击 RENAME PLAYLIST
        self.my_click_text("RENAME PLAYLIST")
        # 输入新名字，重命名播放列表
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", new_name)
        # 点击 ok
        self.my_click_text("OK")
        # 点击 menu
        self.my_click_id("com.estrongs.android.pop:id/menu_overflow")
        # 点击 DELETE PLAYLIST，删除播放列表
        self.my_click_text("DELETE PLAYLIST")

        # 点击list下拉
        self.my_click_id("com.estrongs.android.pop:id/iv_icon_down_arrow")
        # 点击 返回
        self.my_back()
        # 点击左上角的返回
        self.my_click_accessibilty_id("Navigate up")

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
            self.my_click_id("com.estrongs.android.pop:id/recycle_prompt_checkbox")
        if is_success:
            self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
            time.sleep(5)
        else:
            self.my_click_id("com.estrongs.android.pop:id/negativeBtn")
    # is_success=False，也就是没有删除成功的话，停留在长按选中【1】的状态，否则是文件浏览【0】的状态

    # 文件解压缩：前序状态13，是需要到达menu后的界面
    # 可以修改的参数：解压路径、解压编码、解压缩的文件
    def decompress_8(self, is_success, index=None, password=None, path_list=None, encoding_list=None):
        '''
        :param is_success: True，就解压；False，直接取消解压
        :param index: 1 解压到默认到文件夹下  2 解压到自己选的文件夹下
        :param password: 针对那些压缩时加密的压缩包，如果不传入参数说明原来没有加密。
        :param path_list: list，进入的文件夹
        :param encoding_list: list，点击的encoding，取值范围1-10，最后一个肯定得是1
        :return:
        '''
        self.my_click_text("EXTRACT TO")
        if is_success:
            if index == 1:  # 解压到默认文件夹下
                # 点击current path
                self.my_click_id("com.estrongs.android.pop:id/toCurrentPath")
                # 点击choose path
                self.my_click_id("com.estrongs.android.pop:id/toPathAssinged")
                # 点击默认的文件夹
                self.my_click_id("com.estrongs.android.pop:id/toArchiveNameAsPath")
            else:  # 解压到选择的文件夹下
                # 点击choose path
                self.my_click_id("com.estrongs.android.pop:id/toPathAssinged")
                # 点击路径进行选中
                self.my_click_id("com.estrongs.android.pop:id/filename")
                for i in path_list:
                    if i == -1:
                        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
                        time.sleep(3)
                    else:
                        self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
                        time.sleep(3)
                # 点击OK
                self.my_click_id("com.estrongs.android.pop:id/positiveBtn")

            for i in encoding_list:
                # 点击解码编码的下拉框
                self.my_click_id("com.estrongs.android.pop:id/btnCharset")
                # 点击Unicode
                self.my_click_classname("android.widget.RadioButton", i-1)
            # 点击ok
            self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
            time.sleep(10)
            if password is not None:
                # 输入
                self.my_edit_id("com.estrongs.android.pop:id/etPassword", password)
                # 点击show password
                self.my_click_id("com.estrongs.android.pop:id/cbxShowPassword")
                # 点击ok
                self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
                time.sleep(15)
        else:
            # 点击Cancel
            self.my_click_id("com.estrongs.android.pop:id/negativeBtn")

    # 文本编辑：前序状态0，直接点击文件浏览目录中的txt文件
    # 可以修改的参数：文本内容
    def text_edit_9(self, text_index, is_clear, start, text_input, is_undo, save_index, line_num=None, new_text=None):
        '''
        :param text_index:  要点击的text的位置【例如在文件浏览界面的中第5个，传入5】
        :param is_clear: 是否清除已有的文本，True就是清除
        :param start: 1的话，直接在开头输入文本； 2的话在末尾输入； 3的话在换行输入。需要传入line_num
        :param text_input: 要输入的文本
        :param is_undo: 是否撤销之前刚刚的输入。True的话，重新输入新的new_text，需要传入new_text
        :param save_index: 两种保存方式
        :param line_num: start=3的时候，传入line_num。int。例如2
        :param new_text: is_undo为True的时候，需要传入new_text。
        :return:
        '''
        # 点击文件
        self.my_click_xpath_text(text_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ViewAnimator/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[")
        # 点击 text
        self.my_click_text("Text")
        # 点击ES Note Editor
        self.my_click_text("ES Note Editor")
        # 点击This Time Only
        self.my_click_text("This Time Only")

        # 点击Edit
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.RelativeLayout[1]/android.widget.LinearLayout")
        if is_clear:  # 是否清除已有的文本
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/com.jecelyin.editor.v2.widget.BottomDrawerLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.EditText")

        if start == 1:   # 在开头输入文本
            # 点击menu
            self.my_click_accessibilty_id("More menus")
            # 点击start
            self.my_click_text("Jump to Start")
        elif start == 2:  # 在末尾输入文本
            # 点击menu
            self.my_click_accessibilty_id("More menus")
            # 点击start
            self.my_click_text("Jump to Start")
            # 点击menu
            self.my_click_accessibilty_id("More menus")
            # 点击Jump to End
            self.my_click_text("Jump to End")
        else:   # 向下换行输入
            # 点击 editText
            self.my_click_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/com.jecelyin.editor.v2.widget.BottomDrawerLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.EditText")
            for _ in range(line_num):
                # 输入换行符
                self.my_press_code(66)

        # 输入文本
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/com.jecelyin.editor.v2.widget.BottomDrawerLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.EditText", text_input)

        if is_undo:
            # 点击undo回到刚刚的上一次输入前的状态
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.RelativeLayout[4]/android.widget.LinearLayout")
            # 输入新文本
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/com.jecelyin.editor.v2.widget.BottomDrawerLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.EditText", new_text)

        if save_index == 1:
            # 点击 save
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.RelativeLayout[5]/android.widget.LinearLayout")
            # 返回
            self.my_back()
        else:
            # 返回
            self.my_back()
            # 点击yes
            self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
        # 最后的状态是 回到文件浏览的界面

    # 创建文件夹：前序状态13，是需要到达menu后的界面。
    # 可以修改的参数，新建的类型【文件夹/文件】，是否成功，名称
    def new_folder_10(self, new_type, name=None):
        '''
        :param new_type: 1-5 为'Folder', 'Word', 'Excel', 'PowerPoint', 'File'，新建的只有1和5能打开
        :param name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，然后创建成功
        :return:
        '''
        # 点击new
        self.my_click_text("NEW")
        list1 = ['Folder', 'Word', 'Excel', 'PowerPoint', 'File']
        self.my_click_text(list1[new_type-1])
        # 清除上面的默认的文件夹名称Folder/File
        self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
        if name is None:
            # 点击cancel
            self.my_click_id("com.estrongs.android.pop:id/negativeBtn")
        else:
            # 重新输入名称
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", name)
            # 点击 ok
            self.my_click_id("com.estrongs.android.pop:id/positiveBtn")
            time.sleep(2)

    # 查看文件属性：前序状态13，是长按选中一个或者多个后点击menu，才有Properties按钮
    # 可以修改的参数：长按选中的个数，一个和多个，后面的界面不一样。
    def properties_browse_11(self, select_nums):
        # 点击Properties按钮。
        self.my_click_text("PROPERTIES")
        if select_nums == 1:   # 针对的是单个文件
            # 点击checksum
            self.my_click_id("com.estrongs.android.pop:id/show_check_button")
            # 点击 CANCEL
            self.my_click_text("CANCEL")
            time.sleep(2)
            # 点击 CANCEL
            self.my_click_text("CANCEL")
        else:   # 针对的是 单个文件夹 或者 多个文件
            # 点击cancel
            self.my_click_text("CANCEL")
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
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
            # 重新输入新的名称
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", name)
            if is_success:
                # 确认修改
                self.my_click_text("OK")
                time.sleep(5)
            else:
                # 取消修改
                self.my_click_text("CANCEL")
        else:
            # 针对的是多个文件夹的命名修改
            if start_number is not None:  # 针对的是name+Number的命名方式
                # 点击new name+Number
                self.my_click_id("com.estrongs.android.pop:id/radio_number")
                # 重新输入
                self.my_edit_id("com.estrongs.android.pop:id/new_name_1", name)
                # 输入start  number
                self.my_edit_id("com.estrongs.android.pop:id/num_start_value", start_number)
                if is_success:
                    self.my_click_text("OK")
                    time.sleep(8)
                else:
                    self.my_click_text("CANCEL")
            if prefix is not None:  # 针对的是prefix+original name
                # 点击prefix
                self.my_click_id("com.estrongs.android.pop:id/radio_new")
                # 输入prefix
                self.my_edit_id("com.estrongs.android.pop:id/new_name_2", prefix)
                # 输入扩展名
                self.my_edit_id("com.estrongs.android.pop:id/new_ext_name", name)
                # 清除扩展名
                self.my_clear_id("com.estrongs.android.pop:id/new_ext_name")
                if is_success:
                    self.my_click_text("OK")
                    time.sleep(8)
                else:
                    self.my_click_text("CANCEL")
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
    def settings_14(self, display_list, notification_list):
        '''
        :param display_list: list, 1-8。例如【1，2，3，2，3，1】
        :param notification_list: list，1-5. 例如【1，2，2，1】
        '''
        # 点击侧边栏中的设置按钮
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]")

        # Display settings
        self.my_click_text("Display settings")
        # Language settings
        self.my_click_text("Language settings")
        # 返回
        self.my_back()
        for i in display_list:  # 1-8
            self.my_click_classname("android.widget.CheckBox", i-1)
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Cleanup settings
        self.my_click_text("Cleanup settings")
        # Clear cache
        self.my_click_text("Clear cache")
        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_classname("android.widget.CheckBox", 1)
        self.my_click_classname("android.widget.CheckBox", 1)
        self.my_click_classname("android.widget.CheckBox", 0)
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Directory settings
        self.my_click_text("Directory settings")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Search engine setting
        self.my_click_text("Search engine setting")
        self.my_click_id("android:id/checkbox")
        self.my_click_id("android:id/checkbox")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Notification settings
        self.my_click_text("Notification settings")
        for i in notification_list:  # 1-5
            self.my_click_classname("android.widget.CheckBox", i-1)
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Logger floating widget settings
        self.my_click_text("Logger floating widget settings")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Password settings
        self.my_click_text("Password settings")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Backup settings
        self.my_click_text("Backup settings")
        self.my_click_id("android:id/checkbox")
        self.my_click_id("android:id/checkbox")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # APP
        self.my_click_text("APP")
        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_text("Clean associated folders after uninstallation")
        self.my_click_text("Clean associated folders after uninstallation")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Download Manager
        self.my_click_text("Download Manager")
        self.my_click_classname("android.widget.CheckBox", 1)
        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_classname("android.widget.CheckBox", 1)
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        self.my_swipe(500, 1525, 460, 150, 500)

        # Window settings
        self.my_click_text("Window settings")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Recycle Bin
        self.my_click_text("Recycle Bin")
        self.my_click_id("android:id/checkbox")
        self.my_click_id("android:id/checkbox")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # Update settings
        self.my_click_text("Update settings")
        self.my_click_id("android:id/checkbox")
        self.my_click_id("android:id/checkbox")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # About
        self.my_click_text("About")
        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # 返回
        self.my_click_accessibilty_id("Navigate up")

        # 返回
        self.my_back()

    # bookmarks：前序状态为13，分为两种：
    # 一种是添加bookmarks，长按后添加bookmarks，1->13->15，注意每次只能长按一个文件进行添加
    # 另一种是对已经添加的bookmarks进行删除，长按等。前序状态为侧边栏6，点击bookmarks
    # 测试时注意，需要先添加bookmarks，再测试！
    # 可修改的参数：添加哪些bookmarks，删除的bookmark的位置，是否删除
    def bookmarks_15(self, pre_num, name=None, path=None):
        '''
        :param pre_num: 1的话为长按添加，2的话为侧边栏添加
        :param name:  新增的name名字
        :param path:  path名字
        :return:
        '''
        if pre_num == 1:
            # 第一种点击menu上的 Add to favorite 添加bookmark
            self.my_click_text("ADD TO FAVORITE")
            # 清除原来默认的文本
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText")
            # 重新输入新的bookmarks名称
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText", name)
            # 点击ok
            self.my_click_text("OK")
        else:
            # 第二种是点击展开Bookmarks,前序状态为侧边栏
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[6]")
            # 点击Add
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[7]")

            if path is None:
                # 点击cancel
                self.my_click_text("CANCEL")
            else:
                # 输入path
                self.my_edit_id("com.estrongs.android.pop:id/input_url", path)
                # 输入name
                self.my_edit_id("com.estrongs.android.pop:id/input_name", name)
                # 点击add
                self.my_click_text("ADD")
            # 这时候回到了文件浏览的界面，需要把侧边栏的bookmarks给收起来
            # 点击侧边栏
            self.sidebar_6()
            # 点击bookmarks
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.i/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[6]")
            # 点击返回
            self.my_back()
        # 最后该场景回到的界面为文件浏览的界面
