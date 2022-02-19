# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class MyOIFM:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 0   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path  # 保存的截图的地址，例如 /OIFM/screen/
        self.xml_path = xml_path  # 保存的xml的地址，例如 /OIFM//xml/
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


    def my_swipe(self,x1,y1,x2,y2,mytime):
        self.get_screen_info()
        self.driver.swipe(x1,y1,x2,y2,mytime)
        bounds = '('+str(x1)+', '+str(y1)+', '+str(x2)+', '+str(y2)+', '+str(mytime)+')'
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe ' + bounds + '\n')
        fd.close()
        self.index += 1
        # bounds = '('+str(x1)+', '+str(y1)+', '+str(x2)+', '+str(y2)+', '+str(mytime)+')'
        # global number
        # newline = str(number) + ' '+ str(number+1) + ' swipe ' + bounds +"\n"
        # jump_pairs = open('jump_pairs.txt','a+')
        # jump_pairs.writelines(newline)
        # jump_pairs.close()
        # number =  save_activity_xml(number)
        # driver.swipe(x1,y1,x2,y2,mytime)
        # time.sleep(2)
        

    def my_back_home(self):
        # 该函数是方便回到主界面
        # 点击顶部文件夹位置按钮
        self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/p6")
        # 点击 0，到达首页
        self.my_click_classname("android.widget.LinearLayout", 0)

    # 接下来定义每个场景的描述。
    # 该场景可修改的参数。

    def hometosdcard(self):
        self.my_click_classname("android.widget.ImageView", 0)


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
                #FrameLayout i+1
                self.my_click_classname("android.widget.FrameLayout", i+1)

    # 长按选中：前序状态0：在文件浏览的状态下进行长按选中
    # 可以修改的参数：当前界面可供选中的行数，需要选中的列表，最后选中的数量为1还是多个
    def long_click_1(self, sum, select_list=None):
        '''
        :param sum: 表示当前界面的总行数，例如sum = 5，当前界面共有5行
        :param select_list: 表示在当前界面需要选中的index，例如【2，3】。注意这个标号是从【1，sum】
        '''
        if select_list is None:  # 就把当前界面的sum个数的行长按选中，再取消选中，结果是没有选中任何东西
            # 长按选中第一个
            self.my_long_click_classname("android.widget.FrameLayout", 1)
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(2, sum+1):  # 例如共有5行，sum=5
                self.my_click_classname("android.widget.FrameLayout", i+1)
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum+1):  # j = 6-1,-2,-3, -4,-5
                self.my_click_classname("android.widget.FrameLayout", sum+1-i)
            # 重新按照select_list进行选中
        else:   # 否则就是选中select_list中的
            # print(select_list)
            for i in select_list:
                if i == select_list[0]:
                    # print("long")
                    # print(i)
                    # print(select_list[0])
                    self.my_long_click_classname("android.widget.FrameLayout", i+1)
                else:
                    # print("short")
                    # print(i)
                    # print(select_list[0])
                    self.my_click_classname("android.widget.FrameLayout", i+1)
            # 最后的状态就是，选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。
    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, name=None,password=None,show_password=False,is_success=False):
        '''
        :param name: 压缩的名称, 取值为None:直接点击cancel，相当于取消压缩。取值不为None：需要输入压缩的名称，再判断是否需要确认压缩
        :param password: 输入的密码
        :param name: 是否点击显示密码
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 两种调用方式，compress_2() 或者 compress_2("123",True)
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        self.my_click_text("Compress")
        if name is None:  # 点击cancel
            self.my_click_id("android:id/button2")
        else:
            self.my_clear_id("dv.fileexplorer.filebrowser.filemanager:id/f3")
            self.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/f3", name)
            if password is not None:
                self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/d7")
                self.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/f5", password)
            if show_password == False and password is None:
                self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/d7")
            if is_success:
                self.my_click_id("android:id/button1")
                time.sleep(3)
            else:
                self.my_click_id("android:id/button2")

    # 文件搜索：前序状态0，是文件浏览的界面
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None):
        '''
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :return:
        '''
        # 点击menu界面上的search
        self.my_click_accessibilty_id("Search")
        if text is None:  # 点击返回
            self.my_back()
        else:
            # 输入文本
            self.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/oc", text)
            # 点击清除
            self.my_click_accessibilty_id("Clear query")
            # 再次输入文本
            self.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/oc", text)
            # 点击回车键，到达搜索结果界面
            self.my_press_code(66)
            try:
                self.my_click_text("GRANT")
            except:
                print("无弹窗")
            # 回到搜索之前的界面
            self.my_back()

    # 文件待粘贴：前序状态1：长按选择的界面点击剪切按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, pre_num, is_paste, move_list):
        '''
        :param pre_num: 1为前序状态长按选中的界面然后进去copy，2为前序状态为点击menu上的cut
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        '''
        if pre_num == 1:  # 前序状态是长按选择的界面，点击剪切【为了防止错误，剪切的都不粘贴】
            self.my_click_text("Copy")
            # org.openintents.filemanager:id/clipboard_action
        else:
            self.my_click_text("Cut")
            # org.openintents.filemanager:id/clipboard_action
        self.file_browse_0(move_list)
        if is_paste:
            # 点击Paste
            self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/j9")
            time.sleep(2)
        else:  # 取消粘贴
            self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/j5")

    
    # copy to move to:前序状态13
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4_copyto(self,pre_num,is_paste,move_list):
        '''
        :param pre_num: 1为前序状态长按选中的界面然后进去copy to，2为前序状态为点击move to
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        '''
        if pre_num == 1:  # 前序状态是长按选择的界面，点击剪切【为了防止错误，剪切的都不粘贴】
            self.my_click_text("Copy to")
        else:
            self.my_click_text("Move to")
        for i in move_list:
            if i == -1:
                self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/ho")
            else:
                self.my_click_classname("android.widget.LinearLayout", i)
        if is_paste:
            # 点击Paste
            self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/si")
            time.sleep(2)
        else:  # 取消粘贴
            self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/rv")



    # copy to move to:前序状态0
    def sidebar_6(self):
        self.my_click_accessibilty_id("Show roots")



    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, is_success):
        '''
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_text("Delete")
        if is_success:
            self.my_click_id("android:id/button1")
        else:
            self.my_click_id("android:id/button2")


    # 文件解压：前序状态13，长按后点击菜单
    # 可以修改的参数：删除是否成功还是不成功
    def umcompress_8(self, is_success,choose_path=False,move_list=None,is_code=False,code=None):
        '''
        :param is_success: 是否成功 True, False
        :param choose_path: 是否点击choose path True, False
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_text("Uncompress")
        if choose_path:
            self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/n5")
            self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/su")
            for i in move_list:
                if i == -1:
                    self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/ho")
                else:
                    self.my_click_classname("android.widget.LinearLayout", i)
            if is_success:
                self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/si")
            else:
                self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/rv")
        if is_success:
            self.my_click_id("android:id/button1")
            if is_code:
                try:
                    self.my_click_text("Show Password")
                    self.my_edit_id("dv.fileexplorer.filebrowser.filemanager:id/f5",code)
                    self.my_click_id("android:id/button1")
                except:
                    print("no code")

        else:
            try:
                self.my_click_id("android:id/button2")
            except:
                print("no cancel")
    

    # 创建文件夹：前序状态0，需要先点击菜单
    # 可以修改的参数，是否成功，文件名，文件或文件夹
    def new_folder_10(self, isfile=True,folder_name=None, is_success=False):
        '''
        :param isfile: 新建文件或文件夹 True, False
        :param folder_name: 取值为None:直接点击cancel，相当于取消创建。取值不为None：需要输入创建的名称，再判断是否需要确认创建
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击create folder
        self.my_click_accessibilty_id("More options")
        if isfile:
            self.my_click_text("Create file")
            if folder_name is None:
                self.my_click_id("android:id/button2")
            else:
                self.my_clear_id("android:id/text1")
                self.my_edit_id("android:id/text1",folder_name)
                if is_success:
                    self.my_click_id("android:id/button1")  # 点击ok
                else:
                    self.my_click_id("android:id/button2")  # 点击cancel
        else:
            self.my_click_text("Create folder")
            if folder_name is None:
                self.my_click_id("android:id/button2")
            else:
                self.my_edit_id("android:id/text1",folder_name)
                if is_success:
                    self.my_click_id("android:id/button1")  # 点击ok
                    self.my_back()
                else:
                    self.my_click_id("android:id/button2")  # 点击cancel


    # 查看文件属性：前序状态13，是长按选中一个后点击menu，才有Details按钮
    # 可以修改的参数：无
    def properties_browse_11(self):
        # 点击details按钮。
        self.my_click_text("Info")
        # 点击OK
        self.my_back()


    # 重命名：前序状态1，长按选中后点击重命名
    # 可以修改的参数，修改的文件名，是否修改
    def rename_12(self, name=None, is_success=False):
        '''
        :param name: 取值为None: 直接点击ok，相当于不修改。取值不为None：需要输入修改的名称，再判断是否需要确认修改
        :param is_success: 是否修改，True,False
        :return:
        '''
        # 点击Rename
        self.my_click_text("Rename")
        if name is None:  # 直接点击OK，相当于不修改
            self.my_click_id("android:id/button2")
        else:
            # 输入文件名
            self.my_edit_id("android:id/text1", name)
            if is_success:  # 确认修改
                self.my_click_id("android:id/button1")
            else:
                self.my_click_id("android:id/button2")

    # 点击menu：前序状态1，长按后点击more
    # 可以修改的参数：无
    def menu_13(self):
        self.my_click_text("MORE")

    # 设置：前序状态为6，在侧边栏点击设置
    def settings_14(self, theme_list, checkbox_list,checkbox_list_ori):
        '''
        :param theme_list: 012,按列表切换theme,-1为cancel
        :param checkbox_list:类型为list，表示该次测试中点击6个checkbox中的哪几个。【取值范围0-5】
                             例如传入[1,1,2,3]，就是分别点击第i个checkbox
                             // 不能传入0。会导致原来的文件顺序改变
        '''
        # 点击menu上的settings
        self.my_click_text("SETTINGS")
        #theme style
        for i in checkbox_list_ori:
            self.my_click_classname("android.widget.Switch", i)

        for i in theme_list:
            self.my_click_classname("android.widget.RelativeLayout",0)
            if i == -1:
                self.my_clear_id("android:id/button2")
            else:
                self.my_click_classname("android.widget.CheckedTextView",i)
        
        #primary color
        self.my_click_classname("android.widget.RelativeLayout",1)
        self.my_back()
        #accent color
        self.my_click_classname("android.widget.RelativeLayout",2)
        self.my_back()
        
        self.my_swipe(533,1158,506,809,500)

        for i in checkbox_list:
            self.my_click_classname("android.widget.Switch", i)
        
        self.my_click_text("About")
        self.my_click_accessibilty_id("Navigate up")

        self.my_click_accessibilty_id("Navigate up")
        


#appium测试时看不见bookmarks