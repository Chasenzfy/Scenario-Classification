# -*- coding:utf8 -*-

import time
import os
from appium.webdriver.common.touch_action import TouchAction


class File:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 0   # 当前的截图和xml的编号
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

    def my_start(self):
        # 该函数是方便回到主界面
        # 点击home按钮
        self.my_click_text("Allow")
        # 点击 0，到达文件浏览的主界面
        self.my_click_id("android:id/button1")



    def my_back_home(self):
        self.my_click_classname("android.widget.TextView", 2)
        self.my_click_accessibilty_id("Navigate up")
        self.my_click_classname("android.widget.LinearLayout", 6)

    def file_browse_0(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
        '''
        for i in move_list:
            try:
                if self.driver.find_element_by_id("android:id/button1"):
                    self.my_click_id("android:id/button1")
                    self.my_click_id("android:id/button1")
                    self.my_click_id("android:id/button1")
                if i == -1:
                    self.my_back()
                else:
                    self.my_click_classname("android.widget.RelativeLayout", i)
            except:
                if i == -1:
                    self.my_back()
                else:
                    self.my_click_classname("android.widget.RelativeLayout", i)

    # 长按选中：前序状态0：在文件浏览的状态下进行长按选中
    # 可以修改的参数：当前界面可供选中的行数，需要选中的列表，最后选中的数量为1还是多个
    def long_click_1(self, sum, select_list=None):
        '''
        :param sum: 表示当前界面的总行数，例如sum = 5，当前界面共有5行
        :param select_list: 表示在当前界面需要选中的index，例如【2，3】。注意这个标号是从【1，sum】
        '''
        if select_list is None:  # 就把当前界面的sum个数的行长按选中，再取消选中，结果是没有选中任何东西
            # 长按选中第一个
            self.my_long_click_classname("android.widget.RelativeLayout", 2)
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(3, sum + 1):  # 例如共有5行，sum=5
                self.my_click_classname("android.widget.RelativeLayout", i)
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum):  # j = 6-1,-2,-3, -4,-5
                self.my_click_classname("android.widget.RelativeLayout", sum + 1 - i)
            # 重新按照select_list进行选中
        else:  # 否则就是选中select_list中的
            for i in select_list:
                if i == select_list[0]:
                    self.my_long_click_classname("android.widget.RelativeLayout", i)
                else:
                    self.my_click_classname("android.widget.RelativeLayout", i)
            # 最后的状态就是，选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。

    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, num=None, name=None, is_success=None):
        '''
        :param name: 压缩的名称, 取值为None:直接点击cancel，相当于取消压缩。取值不为None：需要输入压缩的名称，再判断是否需要确认压缩
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 两种调用方式，compress_2() 或者 compress_2("123",True)
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        self.my_click_classname("android.widget.LinearLayout", 0)
        if name is None:  # 点击cancel
            self.my_click_id("android:id/button2")
        else:
            if num != 1:
                self.my_edit_id("com.speedsoftware.explorer:id/txtName", name)
                if is_success:
                    self.my_click_id("android:id/button1")
                    time.sleep(10)
                else:
                    self.my_click_id("android:id/button2")
            else:
                self.my_click_text("Zip this folder")

    # 文件搜索：前序状态13，是文件浏览的界面，点击menu后，点击search
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None, is_success=None):
        """
        :param is_success: 是否查询
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :return:
        """
        # 点击menu界面上的search
        self.my_click_classname("android.widget.RelativeLayout", 2)
        if text is None:  # 点击返回
            self.my_back()
        else:
            # 输入文本
            self.my_edit_id("com.speedsoftware.explorer:id/txtSearchText", text)
            # 清除
            self.my_clear_id("com.speedsoftware.explorer:id/txtSearchText")
            if is_success:
                self.my_click_id("com.speedsoftware.explorer:id/buttonSearch")
            else:
                self.my_click_id("com.speedsoftware.explorer:id/buttonSearchCancel")

    # 文件待粘贴：前序状态1：长按选择的界面点击剪切按钮  前序状态13：点击menu上的copy按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, pre_num, is_paste, move_list):
        """
        :param pre_num: 1为前序状态长按选中的界面然后进去剪切，2为前序状态为点击menu上的copy进行复制
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        """

        self.my_click_accessibilty_id("Move")

        # org.openintents.filemanager:id/clipboard_action
        self.file_browse_0(move_list)
        if is_paste:
            # 点击menu
            self.my_click_id("com.speedsoftware.explorer:id/fab_1")

            time.sleep(5)
        else:  # 取消粘贴
            self.my_click_id("com.speedsoftware.explorer:id/fab_2")

    # 侧边栏
    def sidebar_6(self):
        self.my_click_accessibilty_id("Navigate up")

    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, is_success):
        """
        :param is_success: 是否成功 True, False
        :return:
        """
        # 点击长按选择界面的删除按钮
        self.my_click_accessibilty_id("Delete")
        if is_success:
            self.my_click_id("android:id/button1")
        else:
            self.my_click_id("android:id/button2")

    # 创建文件夹：前序状态13，是需要到达menu后的界面。
    # 可以修改的参数，是否成功，文件名
    def new_folder_10(self, name=None, type=None, is_success=None):
        '''
        :param folder_name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，再判断是否需要确认创建
        :param is_success: 是否成功 True, False
        :param type :0文件夹，1文件 其他：报错
        :return:
        '''
        # 点击加号
        self.my_click_id("com.speedsoftware.explorer:id/fab_add")
        if name is None:
            self.my_back()
        else:
            if type == 0:
                self.my_click_classname("android.widget.LinearLayout", 2)
            elif type == 1:
                self.my_click_classname("android.widget.LinearLayout", 3)
            else:
                return
            # 输入文件名
            self.my_edit_id("com.speedsoftware.explorer:id/txtName", name)
            if is_success:
                self.my_click_id("android:id/button1")  # 点击ok
            else:
                self.my_click_id("android:id/button2")  # 点击cancel

    # 查看文件属性：前序状态13，是长按选中一个后点击menu，才有Details按钮
    # 可以修改的参数：无
    def properties_browse_11(self):
        '''
        :return:
        '''
        # 点击details按钮。
        self.my_click_text("Properties")
        # 点击OK
        self.my_click_id("android:id/button1")

    # 重命名：前序状态13，是长按选中一个后点击menu，才会有rename。
    # 可以修改的参数，修改的文件名，是否修改
    def rename_12(self, name=None, is_success=None):
        '''
        :param name: 取值为None: 直接点击ok，相当于不修改。取值不为None：需要输入修改的名称，再判断是否需要确认修改
        :param is_success: 是否修改，True,False
        :return:
        '''
        # 点击Rename
        self.my_click_text("Rename")
        if name is None:  # 直接点击cancel，相当于不修改
            self.my_click_id("android:id/button2")
        else:
            # 清除原来的文件名
            self.my_clear_id("com.speedsoftware.explorer:id/txtName")
            # 输入文件名
            self.my_edit_id("com.speedsoftware.explorer:id/txtName", name)
            if is_success:  # 确认修改
                self.my_click_id("android:id/button1")
            else:
                self.my_click_id("android:id/button2")

    # 点击menu：前序状态0或者1，文件浏览的界面的menu/文件长按后的界面的menu。
    # 可以修改的参数：无
    def menu_13(self):
        self.my_click_accessibilty_id("More options")

    # 设置：前序状态为13，在文件浏览界面的menu点击setting进入
    # 可以修改的参数：排序的选项，点击的checkbox，是否清理历史
    def settings_14(self):
        self.my_click_classname("android.widget.LinearLayout", 10)

        self.my_click_classname("android.widget.RelativeLayout", 0)
        self.my_click_id("android:id/button2")
        for i in range(0, 3):
            self.my_click_classname("android.widget.RelativeLayout", 0)
            self.my_click_classname("android.widget.CheckedTextView", 2-i)



        self.my_click_classname("android.widget.RelativeLayout", 1)
        self.my_click_id("android:id/button2")
        for i in range(0,9):
            self.my_click_classname("android.widget.RelativeLayout", 1)
            self.my_click_classname("android.widget.CheckedTextView", 8-i)


        self.my_click_classname("android.widget.RelativeLayout", 2)
        self.my_click_id("android:id/button2")
        for i in range(0,8):
            self.my_click_classname("android.widget.RelativeLayout", 2)
            self.my_click_classname("android.widget.CheckedTextView", 7-i)

        self.my_click_classname("android.widget.RelativeLayout", 3)
        self.my_click_id("android:id/button2")

        self.my_click_classname("android.widget.RelativeLayout", 3)
        self.my_click_classname("android.widget.CheckedTextView",1)
        self.my_click_id("android:id/button1")

        self.my_click_classname("android.widget.RelativeLayout", 3)
        self.my_click_classname("android.widget.CheckedTextView",0)


        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_classname("android.widget.CheckBox", 1)
        self.my_click_classname("android.widget.CheckBox", 2)
        self.my_click_classname("android.widget.CheckBox", 0)
        self.my_click_classname("android.widget.CheckBox", 1)
        self.my_click_classname("android.widget.CheckBox", 2)

    # bookmarks：前序状态为13，分为两种：
    # 一种是添加bookmarks，长按后添加bookmarks，1->13->15，但是不会新增页面。但是需要为后续bookmarks的测试进行操作
    # 另一种是对已经添加的bookmarks进行删除，长按等。
    # 测试时注意，需要先添加bookmarks，再测试！【初始是有2个bookmarks】
    # 可修改的参数：添加哪些bookmarks，删除的bookmark的位置，是否删除
    def bookmarks_15(self):
        '''
       进入bookmark
       :return:
       '''
        self.my_click_classname("android.widget.LinearLayout", 7)
