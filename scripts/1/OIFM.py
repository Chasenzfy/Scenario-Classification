# -*- coding:utf8 -*-

import time
import os
from appium.webdriver.common.touch_action import TouchAction


class MyOIFM:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 0   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path  # 保存的截图的地址，例如 /OIFM/screen/
        self.xml_path = xml_path  # 保存的xml的地址，例如 /OIFM/xml/
        self.jump_pairs = jump_pairs  # 跳转文件的地址，例如：/OIFM/jump_pairs.txt
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

    # 相当于每个动作函数为：保存执行动作之前的截图和xml，执行动作，保存执行的动作，更新index
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

    def my_back_home(self):
        # 该函数是方便回到主界面
        # 点击home按钮
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ViewFlipper[1]/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageButton[1]")
        # 点击 0，到达文件浏览的主界面
        self.my_click_classname("android.widget.RelativeLayout", 1)

    # 接下来定义每个场景的描述。
    # 该场景可修改的参数。

    # 文件浏览：前序状态算是无
    # 可以修改的参数：进入的文件夹的序列
    # 文件浏览的界面：第一个文件夹：android.widget.RelativeLayout，序号为1
    def file_browse_0(self, move_list):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
        '''
        for i in move_list:
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
            self.my_long_click_classname("android.widget.RelativeLayout", 1)
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(2, sum+1):  # 例如共有5行，sum=5
                self.my_click_classname("android.widget.RelativeLayout", i)
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum+1):  # j = 6-1,-2,-3, -4,-5
                self.my_click_classname("android.widget.RelativeLayout", sum+1-i)
            # 重新按照select_list进行选中
        else:   # 否则就是选中select_list中的
            for i in select_list:
                if i == select_list[0]:
                    self.my_long_click_classname("android.widget.RelativeLayout", i)
                else:
                    self.my_click_classname("android.widget.RelativeLayout", i)
            # 最后的状态就是，选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。
    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, name=None, is_success=None):
        '''
        :param name: 压缩的名称, 取值为None:直接点击cancel，相当于取消压缩。取值不为None：需要输入压缩的名称，再判断是否需要确认压缩
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 两种调用方式，compress_2() 或者 compress_2("123",True)
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        self.my_click_text("Compress (ZIP)")
        if name is None:  # 点击cancel
            self.my_click_id("android:id/button2")
        else:
            self.my_edit_id("org.openintents.filemanager:id/foldername", name)
            if is_success:
                self.my_click_id("android:id/button1")
                time.sleep(8)
            else:
                self.my_click_id("android:id/button2")

    # 文件搜索：前序状态13，是文件浏览的界面，点击menu后，点击search
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None):
        '''
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :return:
        '''
        # 点击menu界面上的search
        self.my_click_text("Search")
        if text is None:  # 点击返回
            self.my_back()
        else:
            # 输入文本
            self.my_edit_id("android:id/search_src_text", text)
            # 点击清除
            self.my_click_id("android:id/search_close_btn")
            # 点击语音输入
            self.my_click_id("android:id/search_voice_btn")
            # 点击返回
            self.my_back()
            # 再次输入文本
            self.my_edit_id("android:id/search_src_text", text)
            # 点击回车键，到达搜索结果界面
            self.my_press_code(66)
            # 回到搜索之前的界面
            self.my_click_id("android:id/up")

    # 文件待粘贴：前序状态1：长按选择的界面点击剪切按钮  前序状态13：点击menu上的copy按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, pre_num, is_paste, move_list):
        '''
        :param pre_num: 1为前序状态长按选中的界面然后进去剪切，2为前序状态为点击menu上的copy进行复制
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        '''
        if pre_num == 1:  # 前序状态是长按选择的界面，点击剪切【为了防止错误，剪切的都不粘贴】
            self.my_click_id("org.openintents.filemanager:id/menu_move")
            # org.openintents.filemanager:id/clipboard_action
        else:
            self.my_click_text("Copy")
            # org.openintents.filemanager:id/clipboard_action
        self.file_browse_0(move_list)
        if is_paste:
            # 点击menu
            self.my_click_accessibilty_id("More options")
            # 点击Paste
            self.my_click_text("Paste")
            time.sleep(5)
        else:  # 取消粘贴
            self.my_click_id("org.openintents.filemanager:id/clipboard_action")

    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, is_success):
        '''
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_id("org.openintents.filemanager:id/menu_delete")
        if is_success:
            self.my_click_id("android:id/button1")
        else:
            self.my_click_id("android:id/button2")

    # 创建文件夹：前序状态13，是需要到达menu后的界面。
    # 可以修改的参数，是否成功，文件名
    def new_folder_10(self, folder_name=None, is_success=None):
        '''
        :param folder_name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，再判断是否需要确认创建
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击create folder
        self.my_click_text("Create folder")
        if folder_name is None:
            self.my_click_id("android:id/button2")
        else:
            # 输入文件名
            self.my_edit_id("org.openintents.filemanager:id/foldername", folder_name)
            if is_success:
                self.my_click_id("android:id/button1")  # 点击ok
            else:
                self.my_click_id("android:id/button2")  # 点击cancel

    # 查看文件属性：前序状态13，是长按选中一个后点击menu，才有Details按钮
    # 可以修改的参数：无
    def properties_browse_11(self):
        # 点击details按钮。
        self.my_click_text("Details")
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
        if name is None:  # 直接点击OK，相当于不修改
            self.my_click_id("android:id/button1")
        else:
            # 清除原来的文件名
            self.my_clear_id("org.openintents.filemanager:id/foldername")
            # 输入文件名
            self.my_edit_id("org.openintents.filemanager:id/foldername", name)
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
    def settings_14(self, sort_list, checkbox_list, is_clear):
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
        # 点击menu上的settings
        self.my_click_text("Settings")
        # 对于排序，传入一个List,表示每次点击的选项，其中name,size,Last modified, file extension分别为0，1，2，3
        # 但是最后都会点击Name
        for i in sort_list:
            # 点击sort by
            self.my_click_text("Sort by")
            # 点击第i个选项
            self.my_click_classname("android.widget.CheckedTextView", i)
        # 点击sort by
        self.my_click_text("Sort by")
        # 最后还是点击Name
        self.my_click_classname("android.widget.CheckedTextView", 0)
        for i in checkbox_list:
            self.my_click_classname("android.widget.CheckBox", i)
        # 点击 clear history
        self.my_click_text("Clear history")
        if is_clear:  # OK，确认清理
            self.my_click_id("android:id/button1")
        else:  # cancel，不清理
            self.my_click_id("android:id/button2")
        # 最后离开该场景，点击返回
        self.my_click_id("android:id/up")

    # bookmarks：前序状态为13，分为两种：
    # 一种是添加bookmarks，长按后添加bookmarks，1->13->15，但是不会新增页面。但是需要为后续bookmarks的测试进行操作
    # 另一种是对已经添加的bookmarks进行删除，长按等。
    # 测试时注意，需要先添加bookmarks，再测试！【初始是有2个bookmarks】
    # 可修改的参数：添加哪些bookmarks，删除的bookmark的位置，是否删除
    # bookmarks的界面：第一个文件夹：android.widget.RelativeLayout，序号为0
    def bookmarks_15(self, long_click_list=None, is_delete=None):
        '''
        :param long_click_list: 需要长按删除的列表，初始是有2个bookmarks【对应的classname标号为0，1】，所以从2开始标号
        :param is_delete: 是否需要删除，如果删除的话，就重新长按选中
        :return:
        '''
        # 第一种是点击Bookmark，第二种是点击Bookmarks
        self.my_click_text_start("Bookmark")
        if long_click_list is not None:  # 说明是第二种情况
            # 长按选择第一个emulated
            self.my_long_click_classname("android.widget.RelativeLayout", 0)
            # 点击选择第二个0EE600BD
            self.my_click_classname("android.widget.RelativeLayout", 1)
            # 取消选择第一个emulated【此时状态是选中第二个】
            self.my_click_classname("android.widget.RelativeLayout", 0)
            # 选中要删除的行
            for i in long_click_list:  # 【2，3】
                self.my_click_classname("android.widget.RelativeLayout", i)
            # 取消选中第二个，就剩下选中要删除的
            self.my_click_classname("android.widget.RelativeLayout", 1)
            # 点击左上角的done
            self.my_click_id("android:id/action_mode_close_button")
            if is_delete:  # 需要删除的话
                # 重新长按选中需要删除的行
                for i in long_click_list:  # 【2，3】
                    if i == long_click_list[0]:
                        self.my_long_click_classname("android.widget.RelativeLayout", i)
                    else:
                        self.my_click_classname("android.widget.RelativeLayout", i)
                # 点击删除
                self.my_click_id("org.openintents.filemanager:id/menu_delete")
            # 点击返回，到文件浏览界面
            self.my_click_id("android:id/up")

