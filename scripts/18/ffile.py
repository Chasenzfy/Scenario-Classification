# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import T, TouchAction

class MyOIFM:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info):
        self.index = 862   # 当前的截图和xml的编号
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
        
        # 该函数是方便回到主界面
        # 点击顶部文件夹位置按钮
        self.my_click_id("dv.fileexplorer.filebrowser.filemanager:id/p6")
        # 点击 0，到达首页
        self.my_click_classname("android.widget.LinearLayout", 0)

    # 接下来定义每个场景的描述。
    # 该场景可修改的参数。

    def hometosdcard(self):
        self.my_click_text("Internal")

        #self.my_click_text_start("External")


    def backtohome(self):
        self.my_click_text("Home")

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
                xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout"
                xpath = xpath + '[' + str(i+1) + ']'
                xpath2 = "/android.widget.RelativeLayout"
                xpath = xpath + xpath2
                self.my_click_xpath(xpath)
                #self.my_click_classname("android.widget.RelativeLayout", i)

    # 长按选中：前序状态0：在文件浏览的状态下进行长按选中
    # 可以修改的参数：当前界面可供选中的行数，需要选中的列表，最后选中的数量为1还是多个
    def long_click_1(self, select_list=None):
        '''
        :param sum: 表示当前界面的总行数，例如sum = 5，当前界面共有5行
        :param select_list: 表示在当前界面需要选中的index，例如【2，3】。注意这个标号是从【1，sum】
        '''
        for i in select_list:
            xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout"
            xpath = xpath + '[' + str(i+1) + ']'
            xpath2 = "/android.widget.RelativeLayout"
            xpath = xpath + xpath2
            if i == select_list[0]:
                # print("long")
                # print(i)
                # print(select_list[0])
                self.my_long_click_xpath(xpath)
            else:
                # print("short")
                # print(i)
                # print(select_list[0])
                self.my_click_xpath(xpath)
            # 最后的状态就是，选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。
    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, name=None,password=None,is_success=False):
        '''
        :param name: 压缩的名称, 取值为None:直接点击cancel，相当于取消压缩。取值不为None：需要输入压缩的名称，再判断是否需要确认压缩
        :param password: 输入的密码
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 两种调用方式，compress_2() 或者 compress_2("123",True)
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        self.menu_13()
        self.my_click_text("Compress")
        if name is None:  # 点击cancel
            self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")
        else:
            self.my_clear_id("com.cvinfo.filemanager:id/input_zip")
            self.my_edit_id("com.cvinfo.filemanager:id/input_zip", name)
            if password is not None:
                self.my_edit_id("com.cvinfo.filemanager:id/input_password", password)
            if is_success:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultPositive")
                time.sleep(3)
            else:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")

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
            self.my_click_id("com.cvinfo.filemanager:id/action_up_btn")
        else:
            # 输入文本
            self.my_edit_id("com.cvinfo.filemanager:id/searchTextView", text)
            # 点击清除
            self.my_click_id("com.cvinfo.filemanager:id/action_empty_btn")
            # 再次输入文本
            self.my_edit_id("com.cvinfo.filemanager:id/searchTextView", text)
            # 点击回车键，到达搜索结果界面
            self.my_press_code(66)
            # try:
            #     self.my_click_text("GRANT")
            # except:
            #     print("无弹窗")
            # 回到搜索之前的界面
            self.my_click_id("com.cvinfo.filemanager:id/action_up_btn")

    # 文件待粘贴：前序状态1：长按选择的界面点击剪切按钮
    # 可以修改的参数：前序状态，最后是否需要粘贴，要粘贴的文件夹
    def to_paste_4(self, pre_num, move_list):
        '''
        :param pre_num: 1为前序状态长按选中的界面然后进去copy，2为前序状态为点击menu上的cut
        :param is_paste: True表示需要粘贴，False表示不需要
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        '''
        self.menu_13()
        if pre_num == 0:  # 前序状态是长按选择的界面，点击剪切【为了防止错误，剪切的都不粘贴】
            self.my_click_text("Copy")
            # org.openintents.filemanager:id/clipboard_action
        else:
            self.my_click_text("Move")
            # org.openintents.filemanager:id/clipboard_action
        self.file_browse_0(move_list)
        self.my_click_accessibilty_id("Paste")
        time.sleep(5)

    # copy to move to:前序状态0
    def sidebar_6(self):
        self.my_click_accessibilty_id("Open")



    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, way=0,is_success=False):
        '''
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        if way == 0:
            self.my_click_accessibilty_id("Search")
        else:
            self.menu_13()
            self.my_click_text("Delete")
        if is_success:
            self.my_click_id("com.cvinfo.filemanager:id/check_box")
            self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultPositive")
        else:
            self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")


    # 文件解压：前序状态0，长按后点击菜单
    # 可以修改的参数：删除是否成功还是不成功
    def umcompress_8(self, is_success,move_list=None,index=0):
        '''
        :param is_success: 是否成功 True, False
        :param choose_path: 是否点击choose path True, False
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
                  最后的状态是 根据move_list到达的界面，没有进入主界面。
        :return:
        '''
        # 点击长按选择界面的删除按钮
        xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout"
        xpath = xpath + '[' + str(index+1) + ']'
        xpath2 = "/android.widget.RelativeLayout/android.widget.ImageButton"
        xpath = xpath + xpath2
        self.my_click_xpath(xpath)
        self.my_click_text("Extract")
        for i in move_list:
            if i == -1:
                self.my_click_classname("android.widget.LinearLayout",1)
            else:
                self.my_click_classname("android.widget.LinearLayout",i+2)
        if is_success:
            self.my_click_text_start("SELECT LOCATION")
        else:
            self.my_click_text("CANCEL")
        time.sleep(5)

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
        self.menu_13()
        if isfile:
            self.my_click_text("Create New File")
            if folder_name is None:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")
            else:
                self.my_edit_id("com.cvinfo.filemanager:id/name_dir",folder_name)
                if is_success:
                    self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultPositive")  # 点击ok
                else:
                    self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")  # 点击cancel
        else:
            self.my_click_text("Create New Folder")
            if folder_name is None:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")
            else:
                self.my_edit_id("com.cvinfo.filemanager:id/name_dir",folder_name)
                if is_success:
                    self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultPositive")  # 点击ok
                else:
                    self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")  # 点击cancel


    # 查看文件属性：前序状态1，是长按选中一个后点击menu，才有Details按钮
    # 可以修改的参数：无
    def properties_browse_11(self,index=[],type=0):
        if type == 0:
            self.long_click_1(select_list=index)
            self.menu_13()
            self.my_click_text("Properties")
            # 点击OK
            self.my_back()
            self.my_back()
        else:#尝试各种方法无法定位
            xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout"
            xpath = xpath + '[' + str(index[0]+1) + ']'
            xpath2 = "/android.widget.RelativeLayout/android.widget.ImageButton"
            xpath = xpath + xpath2
            self.my_click_xpath(xpath)
            # self.my_swipe(538,1742,547,731,200)
            self.my_swipe(538,1742,547,731,200)
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[13]")
            #self.my_click_text("Rename")
            #self.my_click_classname("android.widget.LinearLayout",6)
            self.my_back()



    # 重命名：前序状态1，长按选中后点击重命名
    # 可以修改的参数，修改的文件名，是否修改
    def rename_12(self,name=None,name2=None,number=None,extension=None,index=[],type=0,mutitype=0,is_success=False):
        '''
        :param name: 取值为None: 直接点击ok，相当于不修改。取值不为None：需要输入修改的名称，再判断是否需要确认修改
        :param is_success: 是否修改，True,False
        :return:
        '''
        #0为单个重命名
        if type == 0:
            xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout"
            xpath = xpath + '[' + str(index[0]+1) + ']'
            xpath2 = "/android.widget.RelativeLayout/android.widget.ImageButton"
            xpath = xpath + xpath2
            self.my_click_xpath(xpath)
            self.my_click_text("Rename")
            self.my_clear_id("com.cvinfo.filemanager:id/name_dir")
            self.my_edit_id("com.cvinfo.filemanager:id/name_dir", name)
            if is_success:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultPositive")  # 点击ok
            else:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")
        else:
            self.long_click_1(select_list=index)
            self.menu_13()
            self.my_click_text_start("Multi")
            if mutitype == 0:
                self.my_click_id("com.cvinfo.filemanager:id/radio3")
                self.my_edit_id("com.cvinfo.filemanager:id/prename",name)
                self.my_edit_id("com.cvinfo.filemanager:id/precount",number)
            elif mutitype == 1:
                self.my_click_id("com.cvinfo.filemanager:id/radio1")
                self.my_edit_id("com.cvinfo.filemanager:id/dcount",number)
            else:
                self.my_click_id("com.cvinfo.filemanager:id/radio2")
                self.my_edit_id("com.cvinfo.filemanager:id/prefix",name)
                self.my_edit_id("com.cvinfo.filemanager:id/count",number)
                self.my_edit_id("com.cvinfo.filemanager:id/postfix",name2)
            if extension is not None:
                self.my_edit_id("com.cvinfo.filemanager:id/ext",extension)
            if is_success:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultPositive")  # 点击ok
            else:
                self.my_click_id("com.cvinfo.filemanager:id/md_buttonDefaultNegative")
                self.my_back()


    # 点击menu：前序状态1，长按后点击more
    # 可以修改的参数：无
    def menu_13(self):
        self.my_click_accessibilty_id("Rotate")

    # 设置：前序状态为6，在侧边栏点击设置
    def settings_14(self, list1,list2,list3,list4):
        '''
        :param theme_list: 012,按列表切换theme,-1为cancel
        :param checkbox_list:类型为list，表示该次测试中点击6个checkbox中的哪几个。【取值范围0-5】
                             例如传入[1,1,2,3]，就是分别点击第i个checkbox
                             // 不能传入0。会导致原来的文件顺序改变
        '''
        # 点击menu上的settings
        self.sidebar_6()
        self.my_click_text("Settings")

        #theme style
        self.my_click_text("Theme")
        self.my_click_classname("android.widget.Switch",1)
        self.my_click_classname("android.widget.Switch",0)
        self.my_click_classname("android.widget.Switch",1)
        self.my_click_classname("android.widget.Switch",0)
        self.my_click_text_start("Primary")
        self.my_back()
        self.my_click_text_start("Accent")
        self.my_back()
        self.my_back()

        for i in list1:
            self.my_click_classname("android.widget.Switch",i)
        
        self.my_click_text_start("Additional")
        #self.my_swipe(720,1370,711,764,500)
        self.my_click_text_start("Set dashboard")
        #self.my_click_classname("android.widget.RelativeLayout",2)
        self.my_click_classname("android.widget.LinearLayout",list2[0]+1)
        self.my_click_text_start("Number of records")
        #self.my_click_classname("android.widget.RelativeLayout",3)
        self.my_click_classname("android.widget.LinearLayout",list2[1]+1)
        self.my_click_text_start("Number of columns")
        #self.my_click_classname("android.widget.RelativeLayout",4)
        self.my_click_classname("android.widget.LinearLayout",list2[2]+1)
        for i in list3:
            self.my_click_classname("android.widget.Switch",i)
        self.my_back()

        # self.my_click_text_start("Language")
        # self.my_back()

        #swipe之后总是找不到元素 也无法back
        #self.my_swipe(506,1172,524,850,2000)
        # self.my_click_text_start("Change")
        # self.my_back()
        # time.sleep(3)
        # self.my_swipe(538,1190,542,676,2000)
        # for i in list4:
        #     self.my_click_classname("android.widget.Switch",i)
        # self.my_click_text_start("Cache")
        # self.my_click_classname("android.widget.LinearLayout",1)
        # self.my_click_text("SELECT")

        # self.my_swipe(593,1319,611,763,2000)
        # self.my_swipe(591,1383,510,676,2000)
        # self.my_click_text_start("Ask")
        # self.my_click_classname("android.widget.LinearLayout",5)
        # self.my_click_text("SELECT")

        # self.my_click_text("Send Feedback")
        # self.my_back()

        # self.my_click_text_start("Terms")
        # self.my_click_text("OK")
        # self.my_swipe(460,1273,455,965,2000)

        self.my_back()

#appium测试时看不见bookmarks