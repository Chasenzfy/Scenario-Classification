import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class App:
    def __init__(self, driver, screen_path, xml_path, jump_pairs,activity_info, index = 0):
        self.index = index   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path 
        self.xml_path = xml_path  
        self.jump_pairs = jump_pairs
        self.activity_info = activity_info  # 记录当前界面的activity信息 例如：activity_info.txt
        self.search_content = False

    def get_screen_info(self):
        # 默认都是在执执行3秒后，再进行截图和保存xml。可能某些操作需要更多的时间，在测试的时候加上
        time.sleep(1)
        screen_name = str(self.index) + ".png"
        self.driver.save_screenshot(os.path.join(self.screen_path, screen_name))
        xml_name = str(self.index) + ".xml"
        with open(os.path.join(self.xml_path, xml_name), 'w+',encoding='utf8') as fps:
            fps.write(self.driver.page_source)

        with open(self.activity_info, 'a', encoding='utf8') as f:
            f.write(str(self.index) + ' ' + self.driver.current_activity + '\n')
        time.sleep(1)

    # 相当于每个动作函数为：保存执行动作之前的截图和xml，执行动作，保存执行的动作标号，更新index
    def my_back(self):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        fd = open(self.jump_pairs, 'a', encoding='utf8')
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

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_coordinates(self,x,y):
        self.get_screen_info()
        TouchAction(driver).tap(x=x,y=y).perform()
        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_long_click_text(self,text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        temp = 'new UiSelector().text("' + text + '")'  # 'new UiSelector().text("123")'
        el = self.driver.find_element_by_android_uiautomator(temp)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_click_text_start(self, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        temp = 'new UiSelector().textStartsWith("' + text + '")'  # 'new UiSelector().text("123")'
        el = self.driver.find_element_by_android_uiautomator(temp)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_classname(self, classname, classname_index):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_elements_by_class_name(classname)[classname_index]
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_long_click_classname(self, classname, classname_index):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_elements_by_class_name(classname)[classname_index]
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_click_accessibilty_id(self, accessibility_id):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_accessibility_id(accessibility_id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_click_id(self, id):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_long_click_id(self, id):
        self.get_screen_info()

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_click_xpath(self, xpath):
        self.get_screen_info()

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click ' + str(element) + '\n')
        fd.close()

        el.click()
        self.index += 1

    def my_long_click_xpath(self, xpath):
        self.get_screen_info()

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' long_click ' + str(element) + '\n')
        fd.close()

        TouchAction(self.driver).long_press(el).perform()
        self.index += 1

    def my_edit_id(self, id, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + text + ' ' + str(element) + '\n')
        fd.close()

        el.send_keys(text)
        self.index += 1

    def my_edit_xpath(self, xpath, text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' edit ' + text + ' ' + str(element) + '\n')
        fd.close()

        el.send_keys(text)
        self.index += 1

    def my_clear_id(self, id):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_id(id)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear ' + str(element) + '\n')
        fd.close()

        el.clear()
        self.index += 1

    def my_clear_xpath(self, xpath):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        el = self.driver.find_element_by_xpath(xpath)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' clear ' + str(element) + '\n')
        fd.close()

        el.clear()
        self.index += 1

    def my_press_code(self, code_num):
        self.get_screen_info()

        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' press_code ' + str(code_num) + '\n')
        fd.close()

        self.driver.press_keycode(code_num)
        self.index += 1

    def my_swipe(self,start_x,start_y,end_x,end_y,duration):
        self.get_screen_info()

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        fd = open(self.jump_pairs, 'a',encoding='utf8')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe' + '\n')
        fd.close()

        self.index += 1


    #启动界面
    def launchable_14(self,action):
        #action 6-侧边栏
        if action == 6:
            #打开侧边栏
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton")
        else:
            assert False

    #文件浏览
    def file_browse_0(self, action, move_list=[]):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
        '''
        #action: -1-内部跳转    13-点击menu     1-长按选择      3-搜索    14-启动界面
        if action == -1:
            for i in move_list:
                if i == -1:
                    self.my_back()
                else:
                    self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[" + str(i) + ']')
        elif action == 13:
            if len(move_list) == 0:
                self.my_click_id("com.root.clean.boost.explorer.filemanager:id/file_menu_button")
            else:
                #self.my_click_xpath("(//android.widget.TextView[@content-desc=\"More options\"])[" + str(move_list[0]) + ']')
                #self.my_click_xpath("(//android.widget.TextView[@content-desc=\"More options\"])[2]")
                #self.my_click_classname('android.widget.TextView',10)
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[" + str(move_list[0]) + "]/android.widget.TextView")
                #assert False
        elif action == 1:
            self.my_long_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[" + str(move_list[0]) + ']')
        #elif action == 0:
        #    self.my_click_text(move_list[0])
        elif action == 3:
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/search_button")
        elif action == 14:
            self.my_click_accessibilty_id("To-do")
        else:
            assert False

    #侧边栏
    def sidebar_6(self,action):
        #action 14-启动界面  0-文件浏览   17-设置
        if action == 14:
            #前往启动界面
            self.my_back()
        elif action == 0:
            #前往文件浏览
            #self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]")
            self.my_click_text("SDCARD")
        elif action == 17:
            #前往设置
            #self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.LinearLayout[5]")
            self.my_click_text("Settings")

    #设置
    def settings_17(self,action):
        #action 6-侧边栏    -1-完成设置
        if action == 6:
            #前往侧边栏
            self.my_back()
        elif action == -1:
            #完成设置
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")
            self.my_back()
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switchcompat_setting_notificaiton_boost")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switchcompat_setting_notificaiton_clean")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switchcompat_setting_notificaiton_cpu")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switchcompat_setting_notificaiton_battery")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switchcompat_setting_notificaiton_battery")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switchcompat_setting_notificaiton_analysis")
            self.my_back()
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/switch_charging_improver")
            self.my_back()
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]")
            self.my_swipe(485,1761,500,250,500)
            self.my_back()
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
            #此时应用重启，回到启动界面
        elif action == -2:
            #完成设置
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]")
            self.my_back()
            self.my_back()            
        else:
            assert False
    
    #点击menu
    def click_menu_13(self,action):
        #action: ?-点击第几项
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[" + str(action) + ']')

    #长按选择
    def select_1(self,action):
        #action: 0-文件浏览     7-文件删除以及垃圾箱管理    13-点击menu     11-查看属性
        if action == 0:
            self.my_click_accessibilty_id("com.root.clean.boost.explorer.filemanager:id/action_mode_close_button")
        elif action == 11:
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/menu_info")
        elif action == 13:
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/menu_edit")
        elif action == 1:
            #全选
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/menu_select_all")
        else:
            assert False

    #文件删除以及垃圾箱管理
    def delete_7(self,action):
        #action: false,true
        if action == False:
            self.my_click_id("android:id/button2")
        else:
            self.my_click_id("android:id/button1")

    #重命名
    def rename_12(self,action,new_name=""):
        #action: false,true
        if new_name != "":
            self.my_clear_id("android:id/text1")
            self.my_edit_id("android:id/text1",new_name)
        if action == False:
            self.my_click_id("android:id/button2")
        else:
            self.my_click_id("android:id/button1")

    '''
    #待粘贴
    def to_paste_4(self,action,move_list=[],param1=[]):
        #action: false,true
        if action == False:
            self.my_back()
        else:
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")
            pointer = 0
            for element in move_list:
                if isinstance(element,int) == True:
                    #路径选择
                    if element == -1:
                        self.my_back()
                    elif element == 1:
                        self.my_click_id("com.google.android.apps.nbu.files:id/action_button")
                    else:
                        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[" + str(element) + ']')
                elif isinstance(element,str) == True:
                    #新建文件夹
                    self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]")
                    self.my_clear_id("com.google.android.apps.nbu.files:id/folder_name_edit_text")
                    self.my_edit_id("com.google.android.apps.nbu.files:id/folder_name_edit_text",element)
                    if param1[pointer] == True:
                        self.my_click_id("com.google.android.apps.nbu.files:id/accept_button")
                        return
                    else:
                        self.my_click_id("com.google.android.apps.nbu.files:id/cancel_button")
                    pointer += 1
    '''
    #新建文件夹
    def new_folder_10(self,action,name=""):
        #action: false,true
        self.my_clear_id("android:id/text1")
        self.my_edit_id("android:id/text1",name)
        if action == False:
            self.my_click_id("android:id/button2")
        else:
            self.my_click_id("android:id/button1")

    #搜索
    def search_3(self,action,text=""):
        #action: -2-返回    -1-按名称搜索
        #        1-长按选择  13-点击menu
        #        0-点击文件
        if action == -2:
            if self.search_content:
                self.my_click_id("com.root.clean.boost.explorer.filemanager:id/search_close_btn")
            self.my_click_id("com.root.clean.boost.explorer.filemanager:id/search_close_btn")
            self.search_content = False
        elif action == -1:
            self.my_clear_id("com.root.clean.boost.explorer.filemanager:id/search_src_text")
            self.my_edit_id("com.root.clean.boost.explorer.filemanager:id/search_src_text",text)
            self.my_press_code(66)
            self.search_content = True
        elif action == 13:
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[" + str(text) + "]/android.widget.TextView")
        elif action == 1:
            self.my_long_click_text(text)
        elif action == 0:
            self.my_click_text(text)
        else:
            assert False
    
    '''
    #文件解压缩
    def extract_8(self,action,param1=False):
        #action: false,true
        if action == 0:
            self.my_click_id("com.google.android.apps.nbu.files:id/unzip_dialog_cancel")
        else:
            self.my_click_id("com.google.android.apps.nbu.files:id/unzip_dialog_accept")
            if param1 == True:
                self.my_click_id("com.google.android.apps.nbu.files:id/delete_after_checkbox")
            self.my_click_id("com.google.android.apps.nbu.files:id/unzip_dialog_accept")
    '''

    def show_info_11(self,action,mode=0):
        if mode == 0:
            if action == 0:
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton")
            else:
                assert False
        elif mode == 3:
            if action == 0:
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout")
            else:
                assert False
        else:
            assert False


if __name__ == '__main__':
    # 配置信息
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['appPackage'] = 'com.root.clean.boost.explorer.filemanager'
    desired_caps['appActivity'] = 'com.best.filemaster.StartActivity'
    #desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True


    screen_path = 'screen\\'
    xml_path = 'xml\\'
    jump_pairs = 'jump_pairs.txt'
    activity_info = 'activity_info.txt'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    time.sleep(2)

    app = App(driver, screen_path, xml_path, jump_pairs,activity_info,0)

    os.system("pause")
    
    #测试文件浏览+设置
    app.launchable_14(6)

    app.sidebar_6(0)

    app.file_browse_0(-1, move_list=[1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, 1, -1, -1])

    app.file_browse_0(14)

    app.launchable_14(6)

    app.sidebar_6(17)

    app.settings_17(-1)

    app.launchable_14(6)

    app.sidebar_6(17)

    app.settings_17(-2)

    app.sidebar_6(14)
    
    
    #测试对文件夹的操作
    app.launchable_14(6)

    app.sidebar_6(0)

    app.file_browse_0(-1,[6])

    name_list = ['222','333','444','555','666','777','888','999','2345','3456','7890']

    for name in name_list:

        app.file_browse_0(13)

        app.click_menu_13(3)

        app.click_menu_13(2)

        app.new_folder_10(True,name)

        app.file_browse_0(-1,[-1])

        app.file_browse_0(1,[2])

        app.select_1(11)

        app.show_info_11(0)

        app.file_browse_0(13,[2])

        app.click_menu_13(3)

        app.rename_12(True,name + 'i')

        app.file_browse_0(1,[2])

        app.select_1(13)

        app.click_menu_13(4)

        app.delete_7(True)
    
    

    #测试对文件的操作
    app.file_browse_0(-1,[1])

    name_list = ['z222.txt','z333.py','z444.docx','z555.md','z666.jpg','z777.exe','z888.java','z999.c','z2345.nju','z3456.edu','z7890.cn']

    for name in name_list:

        app.file_browse_0(13)

        app.click_menu_13(3)

        app.click_menu_13(1)

        app.new_folder_10(True,name)

        app.file_browse_0(1,[6])

        app.select_1(11)

        app.show_info_11(0)

        app.file_browse_0(13,[6])

        app.click_menu_13(2)

        app.rename_12(True,name + 'i')

        app.file_browse_0(1,[6])

        app.select_1(13)

        app.click_menu_13(4)

        app.delete_7(True)

    
    #测试搜索

    app.file_browse_0(3)

    name_list = ['1','2','3','4','a','b','c','d','txt','mp3','jpg']

    for name in name_list:

        app.search_3(-1,name)

        app.search_3(13,1)

        app.click_menu_13(1)

        app.show_info_11(0,3)

        app.search_3(13,1)

        app.click_menu_13(3)

        app.rename_12(False,name)

        app.search_3(13,1)

        app.click_menu_13(6)

        app.delete_7(False)

    app.search_3(-2)

    app.get_screen_info()

    