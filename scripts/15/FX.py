# -*- coding:utf8 -*-

import time
import os
from appium.webdriver.common.touch_action import TouchAction


class FX:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 948   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path  # 保存的截图的地址，例如 /Users/lgy/Desktop/测试脚本/RSFileManager/screens/
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

    def my_enter_main_storage(self):
        # 主界面点击 main storage进入文件夹
        self.my_click_text("Main Storage")

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
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")

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
            self.my_long_click_xpath_text(1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(2, sum+1):  # 例如共有5行，sum=5
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum+1):  # j = 6-1,-2,-3, -4,-5
                self.my_click_xpath_text(sum+1-i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
            # 点击 X，返回到原来的状态【什么也没选中的状态】
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
            # 后续需要重新按照select_list进行选中
        else:   # 否则就是选中select_list中的
            for i in range(len(select_list)):
                if i == 0:
                    self.my_long_click_xpath_text(select_list[i], "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
                else:
                    self.my_click_xpath_text(select_list[i], "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
                    # 最后的状态就是, 选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。
    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，长按后点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, is_success, compress_type=None, password=None):
        '''
        :param compress_type: list, 例如[2,3,4,1] 对于单个文件，有10种[取值范围<=10]，多个文件的压缩有7种【取值范围<=7】。
        :param password：针对的是压缩类型为1和2，即zip 和 7z
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        self.my_click_text("Archive")
        # 点击ADVANCED
        self.my_click_text("ADVANCED")
        # 点击checkbox
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.CheckBox")
        # 取消点击checkbox
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.CheckBox")
        # 点击CONTENT
        self.my_click_text("CONTENT")
        # 点击ADVANCED
        self.my_click_text("ADVANCED")
        # 点击SETUP
        self.my_click_text("SETUP")
        if is_success:
            for i in compress_type:
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.view.View[")
            if password is not None:   # 针对的是第二种带密码的zip压缩
                # 点击下拉框
                self.my_click_id("android:id/text1")
                # 点击返回
                self.my_back()
                # 输入密码
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]", password)
                # 确认密码
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]", password)
                # 点击确认
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View")
                time.sleep(10)
            else:
                # 点击确认
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View")
                time.sleep(10)
        else:
            # 点击返回
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

    # 最后的状态是回到了状态0文件浏览

    # 文件搜索：前序状态0，是文件浏览的界面，点击search
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None, new_text=None, include_system_file=None, close_location=None, kind_index=None):
        '''
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :param new_text: 第二次搜索的文本【每次搜索相当于搜索2次】
        :param include_system_file: 取值为true的话，搜索的时候点击include system files
        :param close_location:取值为true的话，关闭location，搜索后返回的时候，会回到home界面，非原来的文件目录
        :param kind_index: 1为ALL，2为Folder，3为File，依次这样的顺序
        :return:
        '''
        # 点击文件浏览界面上的search
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
        if text is None:  # 点击返回
            self.my_back()
        else:
            if include_system_file:
                # 点击include system files
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.CheckBox")
            if close_location:
                # 点击关闭location【如果点击这个，搜索的结果返回的是home界面】
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageButton")
                # 输入文本
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText", text)
                # 直接点击返回【搜索返回的时候，会回到home界面，所以不进行搜索，直接返回】
                self.my_back()
            else:
                # 点击Kind
                self.my_click_text("Kind")
                kind_list = ['All', 'Folder', 'File', 'Document', 'Text', 'Image', 'Music', 'Video', 'App', 'Archive']
                # 点击具体的kind
                self.my_click_text(kind_list[kind_index-1])
                # 点击date
                self.my_click_text('Date')
                # 点击cancel
                self.my_click_text('CANCEL')
                # 点击size
                self.my_click_text('Size')
                # 点击cancel
                self.my_click_text('CANCEL')
                # 输入文本
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText", text)
                # 点击搜索
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View")
                time.sleep(10)
                # 点击返回
                self.my_back()
                # 清除刚刚的文本
                self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
                # 重新输入新的文本
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText", new_text)
                # 点击搜索
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View")
                time.sleep(10)
                # 点击返回
                self.my_back()
                # 点击返回
                self.my_back()
        # 最后回到了搜索之前的文件目录

    # 文件待粘贴：前序状态1：长按选择的界面点击copy或者cut  前序状态13：点击menu上的move to或者copy to按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, pre_num, is_paste, move_list):
        '''
        :param pre_num: 1为前序状态长按选中的界面点击copy
                        2为前序状态长按选中的界面点击cut
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面，属于文件浏览的界面。
        '''
        if pre_num == 1:
            # 点击copy
            self.my_click_text("COPY")
        else:
            # 点击cut
            self.my_click_text("CUT")
        # 进入不同的文件夹
        self.file_browse_0(move_list)
        # 点击clipboard
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout")
        if is_paste:
            # 点击Paste
            self.my_click_text("PASTE")
            time.sleep(8)
        else:
            # 点击清除
            self.my_click_text("CLEAR")
    # 最后都是回到当前的界面

    # 音乐播放：前序状态为0，文件浏览的界面
    # 可以修改的参数：点击不同的音频文件、在不同的时间进行停止播放、保存playlist的名称
    def play_songs_5(self, song_location, index, pause_time=None):
        '''
        :param song_location: 位置
        :param index: index=1，直接点开； index=2，使用音乐播放器
        :param pause_time: 设置的时间
        :return:
        '''
        self.my_click_xpath_text(song_location,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
        if index == 1:
            time.sleep(pause_time)
            # 点击pause
            self.my_click_text("Pause")
            # 点击play
            self.my_click_text("Play")
            # 关闭
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
        else:
            # 点击open with
            self.my_click_text("Open With")
            # 点击media player
            self.my_click_text("Media Player")
            # 测试的时候手动点击 让界面不熄灭!!!!!!!
            # 点击暂停
            self.my_click_id("nextapp.fx:id/exo_pause")
            # 点击右边
            self.my_click_id("nextapp.fx:id/exo_ffwd")
            # 点击右边
            self.my_click_id("nextapp.fx:id/exo_ffwd")
            # 点击右边
            self.my_click_id("nextapp.fx:id/exo_ffwd")
            # 点击⬅
            self.my_click_id("nextapp.fx:id/exo_rew")
            # 点击audio track
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageView")
            # 点击None
            self.my_click_text("None")
            # 点击返回
            self.my_back()
            # 点击info
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.ImageView")
            # 点击关闭
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
            # 点击⬅
            self.my_click_id("nextapp.fx:id/exo_rew")
            # 点击返回
            self.my_back()
        # 最后回到了文件浏览的界面

    # 侧边栏：前序状态0，文件浏览的界面点击侧边栏
    # 可以修改的参数：无
    def sidebar_6(self):
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
        return

    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, is_success):
        '''
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_text("DELETE")
        time.sleep(1)
        # 点击checkbox
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.CheckBox")
        time.sleep(1)
        if is_success:
            self.my_click_text("DELETE")
            time.sleep(8)
        else:
            self.my_click_text("CANCEL")
    # is_success=False，也就是没有删除成功的话，停留在长按选中【1】的状态，否则是文件浏览【0】的状态

    # 文件解压缩：前序状态13，是需要到达menu后的界面
    # 可以修改的参数：解压路径、解压编码、解压缩的文件
    # 这里的加密压缩有bug，不能解压缩
    def decompress_8(self, is_success, decopress_list=None):
        '''
        :param is_success: True，就解压；False，直接取消解压
        :param decopress_list: 解压进入的文件夹目录，传入[1,2]，进入第一个文件夹下的第二个文件夹下
        :return:
        '''
        # 点击menu上的Open With
        self.my_click_text("Open With")
        # 点击Archive Extractor
        self.my_click_text("Archive Extractor")
        # 点击menu
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageView")
        # 点击exact to
        self.my_click_text("Extract To")
        if is_success:
            for i in decopress_list:
                if i == -1:
                    self.my_back()
                else:
                    self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
            # 点击 EXTRACT HERE
            self.my_click_text("EXTRACT HERE")
            time.sleep(5)
        else:
            # 点击Cancel
            self.my_click_text("CANCEL")
            # 点击返回
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
            # 回到了文件浏览的界面

    # 文本编辑：前序状态0，直接点击文件浏览目录中的txt文件
    # 可以修改的参数：文本内容
    def text_edit_9(self, text_index, text_input, colors):
        '''
        :param text_index:  要点击的text的位置【例如在文件浏览界面的中第5个，传入5】
        :param text_input: 要输入的文本
        :param colors: List，例如【2，3，1】，1表示Default，2表示white on black。取值范围1-9
        :return:
        '''
        # 点击文件[txt]
        self.my_click_xpath_text(text_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/nextapp.maui.ui.d.e/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.E/android.widget.FrameLayout[")
        # 点击编辑
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageView")
        # 输入文本
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText", text_input)
        # 点击第二个图标
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.ImageView")
        # 点击Autocorrect
        self.my_click_text("Autocorrect")
        # 点击Autocorrect
        self.my_click_text("Autocorrect")
        # 点击Line Wrap
        self.my_click_text("Line Wrap")
        # 点击Line Wrap
        self.my_click_text("Line Wrap")
        # 点击Font Size
        self.my_click_text("Font Size")
        # 点击CANCEL
        self.my_click_text("CANCEL")
        # 点击 Fixed Font
        self.my_click_text("Fixed Font")
        # 点击 Fixed Font
        self.my_click_text("Fixed Font")
        # 点击 Colors
        self.my_click_text("Colors")
        color_list = ['Default (from active theme)', 'White on Black', 'Black on White', 'Green on Black',
                      'Amber on Black', 'White on Blue', 'Blue on Cyan', 'Green', 'Red Brown']
        # 点击具体的颜色
        for i in colors:
            self.my_click_text(color_list[i-1])
        # 点击返回
        self.my_back()
        # 点击Shortcuts
        self.my_click_text("Shortcuts")
        # 再次点击Shortcuts
        self.my_click_text("Shortcuts")
        # 点击返回到文本编辑的界面
        self.my_back()
        # 点击第三个按钮
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.ImageView")
        # 点击To Top
        self.my_click_text('To Top')
        # 点击第三个按钮
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.ImageView")
        # 点击To Bottom
        self.my_click_text("To Bottom")
        # 点击menu
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.ImageView")
        # 点击Save
        self.my_click_text("Save")
        # 点击返回
        self.my_back()
        # 最后的状态是 回到文件浏览的界面

    # 创建文件夹：前序状态13，是需要到达menu后的界面。
    # 可以修改的参数，新建的类型【文件夹/文件】，是否成功，名称
    def new_folder_10(self, new_type, name=None, type_list=None):
        '''
        :param new_type: 1为Folder，2为File
        :param name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，然后创建成功
        :param type_list:list, 1对应Empty，2对应于Text，3对应word 依次类推 【最后应该创建text文件】，也就是【1，3，2】
        :return:
        '''
        if new_type == 1:  # 新建Folder
            # 点击Folder
            self.my_click_text("Folder")
            # 清除
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
            if name is None:
                # 点击CANCEL
                self.my_click_text("CANCEL")
            else:
                # 输入名字
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText", name)
                # 点击OK
                self.my_click_text("OK")
                time.sleep(5)
                # 点击返回
                self.my_back()
        else:
            # 点击File
            self.my_click_text("File")
            # 清除
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
            if name is None:
                file_list = ['Empty', 'Text', 'Word', 'Excel', 'PowerPoint']
                for i in type_list:
                    self.my_click_text(file_list[i - 1])
                # 点击cancel
                self.my_click_text("CANCEL")
            else:
                # 输入名字
                self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText", name)
                file_list = ['Empty', 'Text', 'Word', 'Excel', 'PowerPoint']
                for i in type_list:
                    self.my_click_text(file_list[i-1])
                # 点击ok
                self.my_click_text("OK")
                time.sleep(2)
                # 会默认点开这个文件，所以需要返回
                self.my_back()

    # 查看文件属性：前序状态13，是长按选中一个后点击menu，才有Properties按钮
    # 可以修改的参数：后面的界面不一样。
    def properties_browse_11(self, index):
        '''
        :param index: 1，表示图片  2，表示其他类型的文件 3，表示文件夹
        :return:
        '''
        # 点击属性图标
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
        if index == 1:
            # 点击FILE
            self.my_click_text("FILE")
            # 点击IMAGE
            self.my_click_text("IMAGE")
        if index == 3:
            # 点击 Folder
            self.my_click_text("FOLDER")
            # 点击 USAGE
            self.my_click_text("USAGE")
        # 点击CHECKSUM【1，2，3均有】
        self.my_click_text("CHECKSUM")
        # 点击CALCULATE
        self.my_click_text("CALCULATE")
        time.sleep(5)
        if index == 1:
            # 点击image
            self.my_click_text("IMAGE")
        if index == 2:
            # 点击file
            self.my_click_text("FILE")
        if index == 3:
            # 点击USAGE
            self.my_click_text("USAGE")
        # 点击返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
    # 回到文件目录下

    # 重命名：前序状态13，是点击长按选中的界面上的rename
    # 可以修改的参数，修改的文件名，是否修改
    def rename_12(self, name=None):
        '''
        :param rename_num: 1表示对一个文件进行重命名， 2 表示对多个文件重命名【分2种】
        '''
        # 点击Rename
        self.my_click_text("Rename")
        if name is None:
            # 清除文件名
            self.my_clear_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
            self.my_click_text("CANCEL")
        else:
            # 清除文件名
            self.my_clear_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
            # 输入新的文件名
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText", name)
            # 点击 OK
            self.my_click_text("OK")
            time.sleep(5)
        # 最后的状态，回到文件浏览的状态0

    # 点击menu：前序状态0或者1，文件浏览的界面的menu/文件长按后的界面的menu。
    # 可以修改的参数：无
    def menu_13(self, pre_num):
        '''
        :param pre_num: 0表示前序状态为文件浏览的界面，1表示前序状态为长按选中的界面
        :return:
        '''
        if pre_num == 0:  # 前序状态为0
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.ImageView")
        else:  # 前序状态为1
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/nextapp.maui.ui.d.e/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.ImageView")

    # 设置：前序状态为6，在侧边栏的界面点击设置按钮
    # 可以修改的参数：排序的选项，点击的checkbox，是否清理历史
    def settings_14(self, style_list, dynamic_material, shape, file_checkbox):
        '''
        :param style_list:  list，取值范围1-16
        :param dynamic_material:  list，1-5
        :param shape: list，1-4【最后一个应该选1，例如[2,3,1]】
        :param file_checkbox: list，1-6
        :return:
        '''
        # 点击settings
        self.my_click_text("Settings")

        # 测试Theme
        self.my_click_text("Theme")
        # 点击style下面的图标
        for i in style_list:  # 1-16
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.View[")
        # 点击 TRIM COLORS
        self.my_click_text("TRIM COLORS")
        # 点击 Trim color的custom
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.view.View")
        # 点击关闭
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
        # 点击 option text color
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout[2]/android.view.View")
        # 点击 关闭
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
        # 点击icons
        self.my_click_text("ICONS")
        # 点击Dynamic Material
        for i in dynamic_material:  # 1-5
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[")
        # 点击shape
        for i in shape:  # 1-4
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.LinearLayout[")
        # 点击 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # 测试Appearance
        self.my_click_text("Appearance")
        # Inline Path Bar
        self.my_click_text("Inline Path Bar")
        # cancel
        self.my_click_id("android:id/button2")
        # 点击 Swipe Down to Refresh
        self.my_click_text("Swipe Down to Refresh")
        # 点击 Enlarge Navigation
        self.my_click_text("Enlarge Navigation")
        # 点击 Enlarge Navigation
        self.my_click_text("Enlarge Navigation")
        # 点击 Swipe Down to Refresh
        self.my_click_text("Swipe Down to Refresh")
        # 点击 Explore Animations
        self.my_click_text("Explore Animations")
        # 点击 Explore Animations
        self.my_click_text("Explore Animations")
        # 点击 Animation
        self.my_click_text("Animation")
        # 点击 Animation
        self.my_click_text("Animation")
        # 点击 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # 测试Home Screen
        self.my_click_text("Home Screen")
        # 点击 Quick Search
        self.my_click_text("Quick Search")
        # 点击 Expand Bookmark Paths
        self.my_click_text("Expand Bookmark Paths")
        # 点击 Expand Bookmark Paths
        self.my_click_text("Expand Bookmark Paths")
        # 点击 Quick Search
        self.my_click_text("Quick Search")
        # 点击 Back Button
        self.my_click_text("Back Button")
        # 点击cancel
        self.my_click_text("CANCEL")
        # 点击 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # 测试 help
        self.my_click_text("Help")
        # 点击 checkbox
        self.my_click_id("android:id/checkbox")
        # 点击 checkbox
        self.my_click_id("android:id/checkbox")
        # 点击 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # 向上滑动
        self.my_swipe(400, 1726, 400, 500, 200)
        # 返回
        self.my_back()

        '''
        # 测试 Opening Files
        self.my_click_text("Opening Files")
        for i in file_checkbox:  # 1-6
            # 选中
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[")
            # 取消选中
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[")
        # 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # 点击File Management
        self.my_click_text("File Management")
        for i in file_checkbox:  # 1-6
            # 选中
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[")
            # 取消选中
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[")
        # 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # Media Management
        self.my_click_text("Media Management")
        # android.widget.CheckBox 0
        self.my_click_classname("android.widget.CheckBox", 0)
        # android.widget.CheckBox 0
        self.my_click_classname("android.widget.CheckBox", 0)
        # android.widget.CheckBox 0
        self.my_click_classname("android.widget.CheckBox", 1)
        # android.widget.CheckBox 0
        self.my_click_classname("android.widget.CheckBox", 1)
        # 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # Special Folders
        self.my_click_text("Special Folders")
        # 返回
        self.my_back()

        # Thumbnails
        self.my_click_text("Thumbnails")
        for i in file_checkbox:  # 1-6
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[")
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[")
        # 返回
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")

        # 返回到文件浏览的界面
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
        '''

    # bookmarks：前序状态为13【不需要长按，只能对文件夹添加，并且是当前目录的父文件夹】，只能添加bookmark，最后的bookmark是在home。测试后记得删除。
    def bookmarks_15(self, pre_num, group_name=None, bookmark_name=None, icon_index=None, icon_label=None, location_index=None):
        '''
        :param pre_num: 1表示对文件夹进行长按后添加，2表示 不需要长按，对当前目录的父文件夹进行添加
        :param group_name:  新建的群组名称
        :param bookmark_name: bookmark的名字
        :param icon_index: 点击第icon_index个图标，第一个对应的index=1。 取值范围1-18
        :param icon_label: icon label
        :param location_index: 第1个表示home bookmark，第3个是自己新建的
        :return:
        '''
        if pre_num == 1:
            # 点击bookmark按钮
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
        else:
            # 点击bookmark按钮
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
        # 点击home bookmark
        self.my_click_id("android:id/text1")
        # 点击New Bookmark Group
        self.my_click_text("New Bookmark Group")
        if group_name is None:
            self.my_click_text("CANCEL")
        else:
            # 输入 group name[g1]
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]", group_name)
            # 输入 Icon label
            self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[2]", group_name)
            # 点击第一个按钮
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ImageView")
            # 点击关闭
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
            # 点击第二个style设置
            self.my_click_text("None")
            # 返回
            self.my_back()
            # OK
            self.my_click_text("OK")
            time.sleep(5)
        # 点击home bookmark下拉框
        self.my_click_id("android:id/text1")
        # 点击 第几个条目
        self.my_click_classname("android.widget.CheckedTextView", location_index-1)
        # 清除默认的bookmark名字
        self.my_clear_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]")
        # 输入 icon label
        # 输入bookmark
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]", bookmark_name)
        # 输入 icon label
        self.my_edit_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[2]", icon_label)
        # 点击第一个按钮
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/nextapp.fx.ui.n.m/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ImageView")
        # 点击第icon_index个图标
        self.my_click_xpath_text(icon_index, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.view.View[")
        # 点击None
        self.my_click_text("None")
        # 返回
        self.my_back()
        # 点击ok
        self.my_click_text("OK")
        time.sleep(2)
        # 添加成功，回到原文件目录
