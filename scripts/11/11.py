import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class App:
    def __init__(self, driver, screen_path, xml_path, jump_pairs, activity_info, index = 0):
        self.index = index   # 当前的截图和xml的编号
        self.driver = driver  # webdriver.Remote()
        self.screen_path = screen_path 
        self.xml_path = xml_path  
        self.jump_pairs = jump_pairs
        self.activity_info = activity_info  # 记录当前界面的activity信息 例如：activity_info.txt
        
        if index == 0:
            self.main_page_at_bottom = False
        else:
            self.main_page_at_bottom = True
        self.settings_done = False

    def get_screen_info(self):
        # 默认都是在执执行3秒后，再进行截图和保存xml。可能某些操作需要更多的时间，在测试的时候加上
        time.sleep(1)
        screen_name = str(self.index) + ".png"
        self.driver.save_screenshot(os.path.join(self.screen_path, screen_name))
        xml_name = str(self.index) + ".xml"
        with open(os.path.join(self.xml_path, xml_name), 'w+',encoding='utf8') as fps:
            fps.write(self.driver.page_source)

        with open(self.activity_info, 'a') as f:
            f.write(str(self.index) + ' ' + self.driver.current_activity + '\n')
        time.sleep(1)

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

    def my_click_coordinates(self,x,y):
        self.get_screen_info()
        TouchAction(driver).tap(x=x,y=y).perform()
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' click' + '\n')
        fd.close()
        self.index += 1

    def my_long_click_text(self,text):
        self.get_screen_info()  # 保存执行动作前的截图和xml

        temp = 'new UiSelector().text("' + text + '")'  # 'new UiSelector().text("123")'
        el = self.driver.find_element_by_android_uiautomator(temp)
        element = [el.get_attribute("class"), el.get_attribute("bounds"), el.get_attribute("text"),
                   el.get_attribute("resource-id"), el.get_attribute("content-desc")]

        fd = open(self.jump_pairs, 'a')
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

    def my_swipe(self,start_x,start_y,end_x,end_y,duration):
        self.get_screen_info()

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        fd = open(self.jump_pairs, 'a')
        fd.write(str(self.index) + ' ' + str(self.index + 1) + ' swipe' + '\n')
        fd.close()

        self.index += 1


    #启动界面
    def launchable_14(self,action):
        #action 0-文件浏览  6-侧边栏
        if action == 0:
            #前往文件浏览
            if self.main_page_at_bottom == False:
                self.my_swipe(241,1193,245,357,200)
                self.main_page_at_bottom = True
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]")
        elif action == 6:
            #打开侧边栏
            self.my_click_accessibilty_id("Show navigation menu")
        elif action == 3:
            #搜索
            self.my_click_accessibilty_id("Search")
        else:
            assert False

    #文件浏览
    def file_browse_0(self, action, move_list=[]):
        '''
        :param move_list: [-1,1,2,3]，取值为-1和正数，其中-1表示进入当前界面的上层目录，1表示进入当前界面的第1个子文件夹
        '''
        #action: -1-内部跳转    13-点击menu     1-长按选择
        if action == -1:
            for i in move_list:
                if i == -1:
                    self.my_back()
                else:
                    self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[" + str(i) + ']')
        elif action == 13:
            if len(move_list) == 0:
                self.my_click_accessibilty_id("More options")
            else:
                self.my_click_xpath("(//android.widget.ImageView[@content-desc=\"Show file actions\"])[" + str(move_list[0]) + ']')
        elif action == 1:
            self.my_long_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[" + str(move_list[0]) + ']')
        elif action == 0:
            self.my_click_text(move_list[0])
        else:
            assert False

    #侧边栏
    def sidebar_6(self,action):
        #action 14-启动界面     17-设置
        if action == 14:
            #前往启动界面
            self.my_back()
        elif action == 17:
            #前往设置
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]")

    #设置
    def settings_17(self,action):
        #action 6-侧边栏    -1-完成设置
        if action == 6:
            #前往侧边栏
            self.my_back()
        elif action == -1:
            #完成设置
            if self.settings_done == False:
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]")
                self.my_back()
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]")
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]")
                self.my_back()
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout")
                self.my_back()
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView[2]")
                self.my_click_id("com.google.android.apps.nbu.files:id/confirm_dialog_accept")
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.TextView[1]")
                self.settings_done = True
        elif action == -2:
            #设置补充
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
            self.my_back()
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.RelativeLayout")
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
            #self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout")
            self.my_back()
            self.my_back()
            #self.my_back()
        else:
            assert False
    
    #点击menu
    def click_menu_13(self,action):
        #action: ?-点击第几项
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[" + str(action) + ']')

    #长按选择
    def select_1(self,action):
        #action: 0-文件浏览     7-文件删除以及垃圾箱管理    13-点击menu
        if action == 0:
            self.my_click_accessibilty_id("Done")
        elif action == 7:
            self.my_click_accessibilty_id("Delete")
        elif action == 13:
            self.my_click_accessibilty_id("More options")
        else:
            assert False

    #文件删除以及垃圾箱管理
    def delete_7(self,action):
        #action: false,true
        if action == False:
            self.my_click_id("com.google.android.apps.nbu.files:id/confirm_dialog_decline")
        else:
            self.my_click_id("com.google.android.apps.nbu.files:id/confirm_dialog_accept")

    #重命名
    def rename_12(self,action,new_name=""):
        #action: false,true
        self.my_clear_id("com.google.android.apps.nbu.files:id/file_name_edit_text")
        self.my_edit_id("com.google.android.apps.nbu.files:id/file_name_edit_text",new_name)
        if action == False:
            self.my_click_id("com.google.android.apps.nbu.files:id/cancel_button")
        else:
            self.my_click_id("com.google.android.apps.nbu.files:id/ok_button")

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

    #新建文件夹
    def new_folder_10(self,action,name=""):
        #action: false,true
        self.my_clear_id("com.google.android.apps.nbu.files:id/folder_name_edit_text")
        self.my_edit_id("com.google.android.apps.nbu.files:id/folder_name_edit_text",name)
        if action == False:
            self.my_click_id("com.google.android.apps.nbu.files:id/cancel_button")
        else:
            self.my_click_id("com.google.android.apps.nbu.files:id/accept_button")

    #搜索
    def search_3(self,action,text=""):
        #action: 14-返回    -1-按名称搜索    -2-按标签搜索
        #        1-长按选择  13-点击menu
        #        0-点击文件
        if action == 14:
            self.my_back()
        elif action == -1:
            self.my_clear_id("com.google.android.apps.nbu.files:id/search_box")
            self.my_edit_id("com.google.android.apps.nbu.files:id/search_box",text)
            self.my_press_code(66)
        elif action == -2:
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[" + str(text) + ']')
        elif action == 13:
            self.my_click_xpath("(//android.widget.ImageView[@content-desc=\"Show file actions\"])[" + str(text) + ']')
        elif action == 1:
            self.my_long_click_text(text)
        elif action == 0:
            self.my_click_text(text)
        else:
            assert False
    
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



if __name__ == '__main__':
    # 配置信息
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['appPackage'] = 'com.google.android.apps.nbu.files'
    desired_caps['appActivity'] = 'com.google.android.apps.nbu.files.home.HomeActivity'
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True


    screen_path = 'screen\\'
    xml_path = 'xml\\'
    jump_pairs = 'jump_pairs.txt'
    activity_info = 'activity_info.txt'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    time.sleep(2)

    app = App(driver, screen_path, xml_path, jump_pairs,activity_info, 597)

    os.system("pause")

    '''
    
    #测试文件浏览+设置
    app.launchable_14(0)

    app.file_browse_0(-1, move_list=[1, -1, 2, 1, -1, 3, -1, -1, 3, -1, 4, -1, 5, -1])

    app.my_back()

    app.launchable_14(6)

    app.sidebar_6(17)

    app.settings_17(-1)

    app.settings_17(6)

    app.my_click_accessibilty_id("Browse")
    app.main_page_at_bottom = False
    
    

    
    #测试对文件夹的操作
    app.launchable_14(0)

    app.file_browse_0(-1, [6])

    app.file_browse_0(13,[1])

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[1])

    app.click_menu_13(1)

    app.select_1(0)

    app.file_browse_0(13,[1])

    app.click_menu_13(1)

    app.select_1(7)

    app.delete_7(False)

    app.select_1(13)

    app.click_menu_13(5)

    app.my_back()

    app.file_browse_0(13,[1])

    app.click_menu_13(2)

    app.delete_7(False)

    app.select_1(0)

    app.file_browse_0(13,[1])

    app.click_menu_13(2)

    app.delete_7(False)

    app.select_1(7)

    app.delete_7(False)

    app.select_1(13)

    app.click_menu_13(1)

    

    app.my_back()

    app.file_browse_0(13,[1])

    app.click_menu_13(1)

    app.select_1(13)

    app.click_menu_13(2)

    app.my_back()

    app.select_1(13)

    app.click_menu_13(3)

    app.my_back()

    app.select_1(13)

    app.click_menu_13(4)

    app.rename_12(True,"12345")
    

    #测试复制操作
    app.file_browse_0(-1,[1])

    app.file_browse_0(1,[1])

    app.select_1(0)

    app.file_browse_0(1,[1])

    app.select_1(7)

    app.delete_7(False)

    app.select_1(13)

    app.click_menu_13(2)

    app.select_1(7)

    app.delete_7(False)

    app.select_1(13)

    app.click_menu_13(3)

    app.to_paste_4(False)

    app.select_1(13)

    app.click_menu_13(3)

    app.to_paste_4(True,[2,-1,3,2,-1,4,-1,-1,7,"TEST","test",],[False,True])

    app.file_browse_0(-1,[-1])

    app.file_browse_0(13,[2])

    app.click_menu_13(1)

    app.select_1(7)

    app.delete_7(False)

    app.select_1(13)

    app.click_menu_13(4)

    app.rename_12(True,"TestV")
    

    #测试新建操作
    app.file_browse_0(13,[2])

    app.click_menu_13(3)

    app.to_paste_4(True,["A","b","NJU","SEG","Android","Appium","WOW","CN","Nanjing","Xianlin",-1],[False,False,False,False,False,False,False,False,False,False])

    app.select_1(7)

    app.delete_7(False)

    app.select_1(13)

    app.click_menu_13(4)

    app.rename_12(False)

    app.select_1(13)

    app.click_menu_13(5)

    app.my_back()
    
    #测试新建文件夹
    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"A")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"b")
    
    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"Android")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"NJU")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"SEG")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"Apple")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"HELLO")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"WORLD")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(False,"159")

    app.file_browse_0(13)

    app.click_menu_13(3)

    app.new_folder_10(True,"T")

    app.file_browse_0(13,[2])

    app.click_menu_13(2)

    app.delete_7(True)
    

    #测试侧边栏
    app.file_browse_0(-1,[-1,-1])

    app.launchable_14(6)

    app.sidebar_6(14)

    app.launchable_14(6)

    app.sidebar_6(17)

    app.settings_17(6)

    app.sidebar_6(17)

    app.settings_17(6)

    app.sidebar_6(14)

    app.launchable_14(6)

    app.sidebar_6(14)

    app.launchable_14(0)

    app.my_back()

    app.launchable_14(6)

    app.sidebar_6(17)

    app.settings_17(6)

    app.sidebar_6(14)

    app.launchable_14(6)

    app.sidebar_6(14)
    

    #测试搜索
    app.launchable_14(3)

    app.search_3(14)

    app.launchable_14(3)

    app.search_3(-1,"123")

    app.search_3(1,"1.zip")

    app.select_1(0)

    app.search_3(1,"1.zip")

    app.select_1(7)

    app.delete_7(False)

    app.search_3(13,2)

    app.click_menu_13(9)

    app.my_back()

    app.search_3(13,3)

    app.click_menu_13(4)

    app.rename_12(False)

    app.select_1(0)

    app.search_3(13,4)

    app.click_menu_13(4)

    app.rename_12(False)

    app.select_1(0)

    app.search_3(0,"1.zip")

    app.extract_8(False)

    app.search_3(-2,2)

    app.search_3(0,"1.zip")

    app.extract_8(False)

    app.search_3(14)
    

    #测试解压缩、重命名、查看属性
    app.launchable_14(0)

    app.file_browse_0(-1,[6,2])

    app.file_browse_0(13,[1])

    app.click_menu_13(7)

    app.rename_12(False)

    app.select_1(13)

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[2])

    app.click_menu_13(7)

    app.rename_12(False)

    app.select_1(13)

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)
    
    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(False)

    app.file_browse_0(0,['1.zip'])

    app.extract_8(True,True)

    app.file_browse_0(13,[1])

    app.click_menu_13(2)

    app.delete_7(True)

    app.file_browse_0(1,[1])

    app.select_1(13)

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[2])

    app.click_menu_13(7)

    app.rename_12(False)

    app.select_1(0)

    app.file_browse_0(13,[2])

    app.click_menu_13(7)

    app.rename_12(False)

    app.select_1(0)

    app.file_browse_0(13,[2])
    

    app.click_menu_13(7)

    app.rename_12(False)

    app.select_1(0)
    

    #补充
    app.file_browse_0(-1,[-1])

    app.file_browse_0(13,[2])

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[2])

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[2])

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[2])

    app.click_menu_13(6)

    app.my_back()

    app.file_browse_0(13,[2])

    app.click_menu_13(2)

    app.delete_7(True)
    

    #补充2
    app.file_browse_0(-1,[-1,-1])

    app.launchable_14(3)

    app.search_3(-1,"a")

    app.search_3(-1,"1234")

    app.search_3(-1,"test")

    app.search_3(-2,3)

    app.search_3(-2,2)

    app.search_3(14)

    app.launchable_14(3)

    app.search_3(-1,'android')

    app.search_3(-1,'txt')

    app.search_3(-2,2)

    app.search_3(14)
    

    #补充3
    app.launchable_14(0)

    app.file_browse_0(13,[1])

    app.click_menu_13(3)

    app.to_paste_4(True,[5,-1,6,-1,7,2,-1,-1,-1])

    app.select_1(7)

    app.delete_7(False)

    app.select_1(0)

    app.file_browse_0(-1,[2])

    app.file_browse_0(13,[1])

    app.click_menu_13(2)

    app.delete_7(False)

    app.select_1(0)

    app.file_browse_0(-1,[-1,6,1])

    app.file_browse_0(13,[1])

    app.click_menu_13(3)

    app.delete_7(False)

    app.select_1(0)

    app.file_browse_0(13,[2])

    app.click_menu_13(3)

    app.delete_7(False)

    app.select_1(0)

    app.file_browse_0(13,[3])

    app.click_menu_13(3)

    app.delete_7(False)

    app.select_1(0)

    app.file_browse_0(13,[4])

    app.click_menu_13(3)

    app.delete_7(False)

    app.select_1(0)

    

    app.file_browse_0(13,[5])

    app.click_menu_13(3)

    app.delete_7(False)

    app.select_1(0)
    
    

    #补充5
    app.file_browse_0(-1,[-1,-1,-1])

    app.launchable_14(6)

    app.sidebar_6(17)

    app.settings_17(-2)

    app.my_back()

    

    app.launchable_14(0)
    

    #测试对文件的操作
    app.file_browse_0(-1,[6,2])

    name_list = ['z222.zip','z333.zip','z444.zip','z555.zip','z666.zip','z777.zip','z888.zip','z999.zip','z2345.zip','z3456.zip','z7890.zip']

    for name in name_list:

        app.file_browse_0(13,[5])

        app.click_menu_13(7)

        app.rename_12(False,name)

        app.select_1(0)

        app.file_browse_0(13,[5])

        app.click_menu_13(8)

        app.my_back()

        app.file_browse_0(-1,[3])

        app.extract_8(0,False)

        app.file_browse_0(13,[1])

        app.click_menu_13(3)

        app.delete_7(False)

        app.select_1(0)

    app.get_screen_info()

    '''

    #补充
    name_list = ['345.zip','564.zip','123.zip','568.zip','DAF.zip','EWT.zip','AFDA.zip','ETH.zip','WT.zip','QWE.zip','SDBG.zip']

    for name in name_list:

        app.file_browse_0(1,[1])

        app.select_1(7)

        app.delete_7(False)

        app.select_1(13)

        app.click_menu_13(3)

        app.my_back()

        app.select_1(0)

        app.file_browse_0(13,[6])

        app.click_menu_13(7)

        app.rename_12(False,name)

        app.select_1(13)

        app.click_menu_13(6)

        app.my_back()

    app.get_screen_info()
    