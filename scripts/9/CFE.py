# -*- coding:utf8 -*-
import time
import os
from appium.webdriver.common.touch_action import TouchAction


class CFE:
    def __init__(self, driver, screen_path, xml_path, jump_pairs):
        self.index = 0  # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path  # 保存的截图的地址，例如 /Users/lgy/Desktop/测试脚本/RSFileManager/screens/
        self.xml_path = xml_path  # 保存的xml的地址，例如 /Users/lgy/Desktop/测试脚本/RSFileManager/screens/
        self.jump_pairs = jump_pairs  # 跳转文件的地址，例如：'/Users/lgy/Desktop/测试脚本/RSFileManager/jump_pairs.txt'

    def get_screen_info(self):
        # 默认都是在执执行3秒后，再进行截图和保存xml。可能某些操作需要更多的时间，在测试的时候加上
        time.sleep(3)
        screen_name = str(self.index) + ".png"
        self.driver.save_screenshot(os.path.join(self.screen_path, screen_name))
        xml_name = str(self.index) + ".xml"
        with open(os.path.join(self.xml_path, xml_name), 'w+') as fps:
            fps.write(self.driver.page_source)
        time.sleep(2)

    # 相当于每个动作函数为：保存执行动作之前的截图和xml，执行动作，保存执行的动作标号，更新index
    def my_back(self):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.back()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' back\n')
        fd.close()
        self.index += 1

    def my_click_text(self, text):
        # 问题1：如果按照修改参数的形式多次执行同一个简单的脚本，无非获取bounds信息，因为bounds信息是每次需要识别
        self.get_screen_info()  # 保存执行动作前的截图和xml
        temp = 'new UiSelector().text("' + text + '")'  # 'new UiSelector().text("123")'
        self.driver.find_element_by_android_uiautomator(temp).click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_click_text_start(self, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        temp = 'new UiSelector().textStartsWith("' + text + '")'  # 'new UiSelector().text("123")'
        self.driver.find_element_by_android_uiautomator(temp).click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_click_classname(self, classname, classname_index):
        # 问题1：如果按照修改参数的形式多次执行同一个简单的脚本，无非获取bounds信息，因为bounds信息是每次需要识别
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_elements_by_class_name(classname)[classname_index].click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_long_click_classname(self, classname, classname_index):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        temp = self.driver.find_elements_by_class_name(classname)[classname_index]
        TouchAction(self.driver).long_press(temp).perform()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click' + '\n')
        fd.close()
        self.index += 1

    def my_click_accessibilty_id(self, accessibility_id):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_element_by_accessibility_id(accessibility_id).click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_click_id(self, id):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_element_by_id(id).click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_click_id1(self, id, id2):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_elements_by_id(id)[id2].click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_long_click_id(self, id):
        self.get_screen_info()
        temp = self.driver.find_element_by_id(id)
        TouchAction(self.driver).long_press(temp).perform()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click' + '\n')
        fd.close()
        self.index += 1

    def my_click_xpath(self, xpath):
        self.get_screen_info()
        self.driver.find_element_by_xpath(xpath).click()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_long_click_xpath(self, xpath):
        self.get_screen_info()
        temp = self.driver.find_element_by_xpath(xpath)
        TouchAction(self.driver).long_press(temp).perform()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click' + '\n')
        fd.close()
        self.index += 1

    def my_edit_id(self, id, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_element_by_id(id).send_keys(text)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + ' ' + text + '\n')
        fd.close()
        self.index += 1

    def my_edit_xpath(self, xpath, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_element_by_xpath(xpath).send_keys(text)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + ' ' + text + '\n')
        fd.close()
        self.index += 1

    def my_clear_id(self, id):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_element_by_id(id).clear()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear' + '\n')
        fd.close()
        self.index += 1

    def my_clear_xpath(self, xpath):
        self.get_screen_info()  # 保存执行动作前的截图和xml
        self.driver.find_element_by_xpath(xpath).clear()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear' + '\n')
        fd.close()
        self.index += 1

    def my_press_code(self, code_num):
        self.get_screen_info()
        self.driver.press_keycode(code_num)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' press_code ' + str(code_num) + '\n')
        fd.close()
        self.index += 1

    def my_back_home(self):
        self.my_click_id("com.android.permissioncontroller:id/permission_allow_button")
        self.my_click_id1("com.cxinventor.file.explorer:id/icon",0)

    # 接下来定义每个场景的描述。
    # 该场景可修改的参数。

    # 文件浏览：前序状态算是无
    # 可以修改的参数：进入的文件夹的序列

    def file_browse_0(self, move_list):
        '''
        :param move_list: [-1,0,1,2]，取值为-1和正数，其中-1表示进入当前界面的上层目录，0表示进入当前界面的第1个子文件夹
        '''
        for i in move_list:
            if i == -1:
                self.my_back()
            else:
                self.my_click_classname("android.widget.LinearLayout", i*3+6)

    # 长按选中：前序状态0：在文件浏览的状态下进行长按选中
    # 可以修改的参数：当前界面可供选中的行数，需要选中的列表，最后选中的数量为1还是多个

    #0-6,1-9 2-12
    def long_click_1(self, select_list=None):
        '''
        :param sum: 表示当前界面的总行数，例如sum = 5，当前界面共有5行
        :param select_list: 表示在当前界面需要选中的index，例如【2，3】。注意这个标号是从【1，sum】
        '''
        for i in select_list:
            if i == select_list[0]:
                self.my_long_click_classname("android.widget.LinearLayout", i*3+6)
            else:
                self.my_click_classname("android.widget.LinearLayout", i*3+5)
            # 最后的状态就是，选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。

    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self,i=None):
        '''
        :param name: 压缩的名称, 取值为None:直接点击cancel，相当于取消压缩。取值不为None：需要输入压缩的名称，再判断是否需要确认压缩
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_more")
        self.my_click_text("Compress")
        if i!=None:
            self.my_clear_id("com.cxinventor.file.explorer:id/compress_file_name_et_compress_file_name")
            self.my_edit_id("com.cxinventor.file.explorer:id/compress_file_name_et_compress_file_name", "test"+str(i))
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
        if text != None:
            self.my_edit_id("com.cxinventor.file.explorer:id/edit", text)
        self.my_back()

    # 文件待粘贴：前序状态1：长按选择的界面点击剪切按钮  前序状态13：点击menu上的copy按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, is_paste=None):
        '''
        :param pre_num: 1为前序状态长按选中的界面然后进去剪切，2为前序状态为点击menu上的copy进行复制
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        '''
        self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_cut")

        self.my_click_classname("android.widget.LinearLayout", 24)
        self.my_back()

        self.my_click_classname("android.widget.LinearLayout", 27)
        self.my_back()

        self.my_click_classname("android.widget.LinearLayout", 30)
        self.my_back()

        self.my_click_classname("android.widget.LinearLayout", 33)
        self.my_back()
        if is_paste == None:
            self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_cancel")
        else:
            self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_paste")
        self.my_back()


    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def music5(self,i):
        self.my_click_classname("android.widget.LinearLayout",6+3*i)
        self.my_click_accessibilty_id("Pause")
        self.my_click_accessibilty_id("Play")
        self.my_click_accessibilty_id("play or pause")


    def delete_file_7(self, is_success):
        '''
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_delete")
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
        self.my_click_text("New")

        self.my_click_text("File")
        if folder_name is None:
            self.my_click_id("android:id/button2")
        else:
            # 输入文件名
            self.my_edit_id(("com.cxinventor.file.explorer:id/file_name"), folder_name)
            if is_success:
                self.my_click_id("android:id/button1")  # 点击ok
            else:
                self.my_click_id("android:id/button2")  # 点击cancel

    def new_folder_11(self, folder_name=None, is_success=None):
        '''
        :param folder_name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，再判断是否需要确认创建
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击create folder
        self.my_click_text("New")

        self.my_click_text("Folder")
        if folder_name is None:
            self.my_click_id("android:id/button2")
        else:
            # 输入文件名
            self.my_edit_id(("com.cxinventor.file.explorer:id/file_name"), folder_name)
            if is_success:
                self.my_click_id("android:id/button1")  # 点击ok
            else:
                self.my_click_id("android:id/button2")  # 点击cancel



    # 查看文件属性：前序状态13，是长按选中一个后点击menu，才有Details按钮
    # 可以修改的参数：无
    def properties_browse_11(self):
        # 点击details按钮。
        self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_more")
        self.my_click_text("Properties")
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
        self.my_click_id("com.cxinventor.file.explorer:id/bottom_menu_rename")
        if name is None:  # 直接点击OK，相当于不修改
            self.my_click_id("android:id/button2")
        else:
            # 清除原来的文件名
            self.my_clear_id("com.cxinventor.file.explorer:id/file_name")
            # 输入文件名
            self.my_edit_id("com.cxinventor.file.explorer:id/file_name", name)
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
        self.my_click_accessibilty_id("More options")
        self.my_click_id("files.fileexplorer.filemanager:id/content")
        self.my_click_id("files.fileexplorer.filemanager:id/hidden_switch")
        self.my_click_id("files.fileexplorer.filemanager:id/hidden_switch")
        self.my_click_id("files.fileexplorer.filemanager:id/lan_pane")
        self.my_back()
        self.my_click_id("files.fileexplorer.filemanager:id/hide_list_pane")
        self.my_back()
        self.my_back()

    # bookmarks：前序状态为13，分为两种：
    # 一种是添加bookmarks，长按后添加bookmarks，1->13->15，但是不会新增页面。但是需要为后续bookmarks的测试进行操作
    # 另一种是对已经添加的bookmarks进行删除，长按等。
    # 测试时注意，需要先添加bookmarks，再测试！【初始是有2个bookmarks】
    # 可修改的参数：添加哪些bookmarks，删除的bookmark的位置，是否删除
