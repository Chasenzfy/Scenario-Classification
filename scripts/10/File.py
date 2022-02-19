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

    def my_enter_main_storage(self):
        # 主界面点击 main storage进入文件夹
        self.my_click_text("Main storage")

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
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")

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
            self.my_long_click_xpath_text(1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
            # 然后把剩下的全部选中, i = 2,3,4,5
            for i in range(2, sum+1):  # 例如共有5行，sum=5
                self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
            # 按照sum,sum-1,。。。1的顺序全部取消选中
            for i in range(1, sum+1):  # j = 6-1,-2,-3, -4,-5
                self.my_click_xpath_text(sum+1-i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
            # 后续需要重新按照select_list进行选中
        else:   # 否则就是选中select_list中的
            for i in range(len(select_list)):
                if i == 0:
                    self.my_long_click_xpath_text(select_list[i], "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
                else:
                    self.my_click_xpath_text(select_list[i], "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
                    # 最后的状态就是, 选中提供的select_list中的行数，根据select_list的长度，判断是选中1个还是多个。
    # select_list=None表示，长按后取消选中，相当于最后没有选中

    # 文件压缩：前序状态13，长按后点击menu后的界面
    # 可以修改的参数：压缩包的名称，是否压缩成功
    def compress_2(self, name=None, is_success=None):
        '''
        :param name: 名字
        :param is_success: 是否压缩成功 True， False
        :return:
        '''
        # 之前长按的数量为1和多个的时候，对应的menu是不一样的，其中compress的位置是不一样的，用text定位
        # 点击compress
        self.my_click_text("Compress")
        # 清除文本
        self.my_clear_id("com.alphainventor.filemanager:id/compress_file_name_et_compress_file_name")
        if name is None:
            # 取消
            self.my_click_id("android:id/button2")
        else:
            # 输入名字
            self.my_edit_id("com.alphainventor.filemanager:id/compress_file_name_et_compress_file_name", name)
            if is_success:
                self.my_click_id("android:id/button1")
                time.sleep(10)
            else:
                self.my_click_id("android:id/button2")
    # 最后的状态是回到了状态0文件浏览

    # 文件搜索：前序状态0，是文件浏览的界面，点击search
    # 可以修改的参数：搜索的名称
    def search_3(self, text=None, result_index=None):
        '''
        :param text:取值为None:直接点击返回，相当于取消搜索。取值不为None：需要输入搜索的名称
        :param result_index: 在搜索的结果中点击的第几个条目
        :return:
        '''
        # 点击文件浏览界面上的search
        self.my_click_id("com.alphainventor.filemanager:id/menu_search")
        if text is None:  # 点击返回
            self.my_back()
        else:
            self.my_edit_id("com.alphainventor.filemanager:id/edit", text)
            # 点击回车键，到达搜索结果界面
            self.my_press_code(66)
            time.sleep(10)
            # 点击搜索结果中的一项
            if result_index is not None:
                self.my_click_xpath_text(result_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
                # 点击返回
                self.my_back()
                time.sleep(10)
            # 点击叉掉
            self.my_click_accessibilty_id("Navigate up")

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
            self.my_click_id("com.alphainventor.filemanager:id/bottom_menu_copy")
        else:
            # 点击cut
            self.my_click_id("com.alphainventor.filemanager:id/bottom_menu_cut")
        # 进入不同的文件夹
        self.file_browse_0(move_list)
        if is_paste:
            # 点击Paste
            self.my_click_text("Paste")
            time.sleep(8)
        else:
            # 点击清除
            self.my_click_text("Cancel")
    # 最后都是回到当前的界面

    # 音乐播放：前序状态为0，文件浏览的界面
    # 可以修改的参数：点击不同的音频文件、在不同的时间进行停止播放、保存playlist的名称
    def play_songs_5(self, song_location, index, pause_time=None, left_num=None, right_num=None, equalizer=None):
        '''
        :param song_location: 位置
        :param index: index=1，直接点开； index=2，使用音乐播放器
        :param pause_time: 设置的时间
        :param left_num: 向左点击的次数，例如2
        :param right_num: 向右点击的次数
        :param equalizer: 是否设置，True
        :return:
        '''
        self.my_click_xpath_text(song_location, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
        if index == 1:
            # 播放几秒后暂停
            time.sleep(pause_time)
            # 点击pause
            self.my_click_id("com.alphainventor.filemanager:id/play_pause")
            # 重新play
            self.my_click_id("com.alphainventor.filemanager:id/play_pause")
            # 关闭
            self.my_click_id("com.alphainventor.filemanager:id/stop")
            # 最后回到了文件浏览的界面【但是下次再打开的时候是继续之前播放的界面】
        else:
            # 点击pause
            self.my_click_id("com.alphainventor.filemanager:id/play_pause")
            # 点击左侧图标到音乐播放的界面
            self.my_click_id("com.alphainventor.filemanager:id/album_art")
            # 点击左侧的图标，播放模式
            self.my_click_id("com.alphainventor.filemanager:id/shuffle")
            # 再次点击播放模式
            self.my_click_id("com.alphainventor.filemanager:id/shuffle")

            # 点击向左切换歌曲【如果没有的话，就是由暂停播放变成开始播放】
            for i in range(left_num):
                self.my_click_id("com.alphainventor.filemanager:id/prev")

            # 点击向右切换歌曲
            for i in range(right_num):
                self.my_click_id("com.alphainventor.filemanager:id/next")

            # 点击暂停
            self.my_click_id("com.alphainventor.filemanager:id/play_pause")

            # 点击右侧的图标，播放模式
            self.my_click_id("com.alphainventor.filemanager:id/repeat")
            # 再次点击
            self.my_click_id("com.alphainventor.filemanager:id/repeat")
            # 再次点击
            self.my_click_id("com.alphainventor.filemanager:id/repeat")
            # 再次点击，回到刚刚的状态
            self.my_click_id("com.alphainventor.filemanager:id/repeat")

            if equalizer:
                # 设置均衡器
                self.my_click_id("com.alphainventor.filemanager:id/menu_equalizer")
                # 点击 switch
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.Switch")
                # 点击FX booster
                self.my_click_id("com.android.musicfx:id/eqSpinner")
                # 点击user
                self.my_click_text("User")
                # 点击surround sound
                self.my_click_id("com.android.musicfx:id/vIStrengthToggle")
                # 点击surround sound
                self.my_click_id("com.android.musicfx:id/vIStrengthToggle")
                # 点击FX booster
                self.my_click_id("com.android.musicfx:id/eqSpinner")
                # 点击FX booster
                self.my_click_text("FX booster")
                # 点击最上面的switch
                self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.Switch")
                # 点击返回
                self.my_back()

            # 点击返回
            self.my_back()
            # 点击退出播放
            self.my_click_id("com.alphainventor.filemanager:id/stop")

    # 侧边栏：前序状态0，文件浏览的界面点击侧边栏
    # 可以修改的参数：无
    def sidebar_6(self):
        self.my_click_accessibilty_id("Open navigation drawer")
        return

    # 文件删除：前序状态1，长按选择的界面
    # 可以修改的参数：删除是否成功还是不成功
    def delete_file_7(self, is_delete, is_success):
        '''
        :param is_delete: 是否删除
        :param is_success: 是否成功 True, False
        :return:
        '''
        # 点击长按选择界面的删除按钮
        self.my_click_text("Delete")
        if is_delete:
            # 取消选中
            self.my_click_id("com.alphainventor.filemanager:id/check_permanently_delete")
            # 选中
            self.my_click_id("com.alphainventor.filemanager:id/check_permanently_delete")
        else:
            # 取消选中
            self.my_click_id("com.alphainventor.filemanager:id/check_permanently_delete")
        if is_success:
            self.my_click_text("OK")
            time.sleep(5)
        else:
            self.my_click_text("CANCEL")
    # is_success=False，也就是没有删除成功的话，停留在长按选中【1】的状态，否则是文件浏览【0】的状态

    # 文件解压缩：前序状态13，是需要到达menu后的界面
    # 可以修改的参数：解压路径、解压编码、解压缩的文件
    # 这里的加密压缩有bug，不能解压缩
    def decompress_8(self, index, is_success=None, decopress_list=None):
        '''
        :param index: 1，直接返回； 2， 直接解压到默认文件夹 3，解压到指定文件夹，需要传入另外2个参数。
        :param is_success: True，就解压；False，直接取消解压
        :param decopress_list: 解压进入的文件夹目录，传入[1,2]，进入第一个文件夹下的第二个文件夹下
        :return:
        '''
        # 点击menu上的Extract
        self.my_click_text("Extract")
        if index == 1:
            # 取消解压，直接返回
            self.my_back()
        elif index == 2:
            # 解压到默认文件夹
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
            time.sleep(5)
        else:  # 解压到指定的文件夹
            # 点击 Extract to …
            self.my_click_text("Extract to …")
            # 点击 Main storage
            self.my_click_text("Main storage")
            time.sleep(5)
            for i in decopress_list:
                if i == -1:
                    self.my_back()
                    time.sleep(2)
                else:
                    self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[")
                    time.sleep(2)
            if is_success:
                self.my_click_text("EXTRACT HERE")
                time.sleep(8)
            else:
                self.my_click_text("CANCEL")

    # 文本编辑：前序状态0，直接点击文件浏览目录中的txt文件
    # 可以修改的参数：文本内容
    def text_edit_9(self, text_index, is_clear, text_input, save_index):
        '''
        :param text_index:  要点击的text的位置【例如在文件浏览界面的中第5个，传入5】
        :param is_clear: True，表示清除原来的文本；False，不清除
        :param text_input: 要输入的文本
        :param save_index: 保存的方法
        :return:
        '''
        # 点击文件[txt]
        self.my_click_xpath_text(text_index, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[")
        if is_clear:
            # 清除
            self.my_clear_id("com.alphainventor.filemanager:id/edit_line")
        # 输入文本
        self.my_edit_id("com.alphainventor.filemanager:id/edit_line", text_input)
        if save_index == 1:
            # 点击返回
            self.my_click_accessibilty_id("Navigate up")
            # 点击保存
            self.my_click_id("android:id/button1")
            # 回到了文件浏览的目录
        else:
            # 点击保存
            self.my_click_id("com.alphainventor.filemanager:id/menu_save")
            # 点击返回
            self.my_click_accessibilty_id("Navigate up")
        # 最后的状态是 回到文件浏览的界面

    # 创建文件夹：前序状态13，是需要到达menu后的界面。
    # 可以修改的参数，新建的类型【文件夹/文件】，是否成功，名称
    def new_folder_10(self, new_type, name, is_success):
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
        # 输入名字
        self.my_edit_id("com.alphainventor.filemanager:id/file_name", name + name)
        if is_success is False:
            self.my_click_text("CANCEL")
        else:
            # 清除
            self.my_clear_id("com.alphainventor.filemanager:id/file_name")
            # 重新输入名字
            self.my_edit_id("com.alphainventor.filemanager:id/file_name", name)
            # 确认
            self.my_click_text("OK")
            time.sleep(2)

    # 查看文件属性：前序状态13，是长按选中一个后点击menu，才有Properties按钮
    # 可以修改的参数：后面的界面不一样。
    def properties_browse_11(self, index):
        '''
        :param index: 1，表示文件  2，表示文件夹 或者多个文件
        :return:
        '''
        # 点击Properties
        self.my_click_text("Properties")
        if index == 1:
            # 点击checksum
            self.my_click_id("com.alphainventor.filemanager:id/btn_checksum")
            # 点击OK
            self.my_click_text("OK")
        # 点击OK
        self.my_click_text("OK")

    # 重命名：前序状态13，是点击长按选中的界面上的rename
    # 可以修改的参数，修改的文件名，是否修改
    def rename_12(self, name=None, name2=None):
        '''
        :param name:
        :param name2:
        '''
        # 点击Rename
        self.my_click_text("Rename")
        if name is None:
            # 清除文件名
            self.my_clear_id("com.alphainventor.filemanager:id/file_name")
            # 取消
            self.my_click_text("CANCEL")
        else:
            if name2 is None:
                # 清除文件名
                self.my_clear_id("com.alphainventor.filemanager:id/file_name")
                # 输入名字
                self.my_edit_id("com.alphainventor.filemanager:id/file_name", name)
                # 点击 OK
                self.my_click_text("OK")
                time.sleep(5)
            else:
                # 输入名字
                self.my_edit_id("com.alphainventor.filemanager:id/file_name", name)
                # 输入后缀名字
                self.my_edit_id("com.alphainventor.filemanager:id/file_ext", name2)
                # 点击cancel
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
            self.my_click_accessibilty_id("More options")
        else:  # 前序状态为1
            self.my_click_id("com.alphainventor.filemanager:id/bottom_menu_more")

    # 设置：前序状态为6，在侧边栏的界面点击设置按钮
    # 可以修改的参数：排序的选项，点击的checkbox，是否清理历史
    def settings_14(self, built_list, storage_list, advanced_list):
        '''
        :param built_list:  list，取值范围1-4
        :param storage_list: list, 1-8
        :param advanced_list：list， 1-6
        :return:
        '''
        # 点击home键，回到home界面
        self.my_click_id("com.alphainventor.filemanager:id/home")
        # 点击menu
        self.my_click_accessibilty_id("More options")
        # Settings
        self.my_click_text("Settings")

        # 点击 Default apps
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        # 点击返回
        self.my_click_accessibilty_id("Navigate up")

        # buid_in apps
        list1 = ['Image Viewer', 'Video player', 'Music Player', 'Text editor']
        for i in built_list:
            self.my_click_text(list1[i-1])

        # 点击 Storage is full
        for i in storage_list:  # 1-8
            self.my_click_text("Storage is full")
            self.my_click_xpath_text(i, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[")

        # 滑动
        self.my_swipe(383, 1556, 495, 170, 500)
        # 继续滑动，滑到底
        self.my_swipe(383, 1556, 495, 170, 500)

        list2 = ['Show history', 'Show system storage', 'Add Bookmark', 'Add to Home screen',
                'Hide/Unhide', 'Open as']
        for i in advanced_list:  # 1-6
            self.my_click_text(list2[i-1])

        # 点击About
        self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[11]/android.widget.RelativeLayout")
        # 点击 open source license
        self.my_click_text("Open source licenses")
        # 点击 Box Android SDK
        self.my_click_text("Box Android SDK")
        # 点击ok
        self.my_click_id("android:id/button1")
        # 点击返回
        self.my_back()
        # 点击check_box
        self.my_click_id("android:id/checkbox")
        # 取消点击
        self.my_click_id("android:id/checkbox")
        # 返回
        self.my_click_accessibilty_id("Navigate up")
        # 回到了home界面

    # bookmarks：前序状态为13【不需要长按，只能对文件夹添加，并且是当前目录的父文件夹】，只能添加bookmark，最后的bookmark是在home。测试后记得删除。
    def bookmarks_15(self, pre_num, bookmark_index=None, name=None, is_remove=None):
        '''
        :param pre_num: 1表示对文件夹进行长按后添加，2表示 不需要长按，对当前目录的父文件夹进行添加
        :param bookmark_index: 要操作的bookmark的个数
        :param name: 重新命名
        :param is_remove: 是否删除bookmark
        :return:
        '''
        if pre_num == 1:
            # 添加，只能对一个文件长按后添加
            self.my_click_text("Add Bookmark")
        else:
            # 对已经添加的进行操作，在侧边栏中
            # 点击侧边栏中的第2个图标
            self.my_click_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.a.c[2]")
            # 长按第index个bookmark
            self.my_long_click_xpath_text(bookmark_index+3, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[")
            # 点击Rename
            self.my_click_text("Rename")
            # clear
            self.my_clear_id("com.alphainventor.filemanager:id/text")
            if name is not None:
                # 输入新的名字
                self.my_edit_id("com.alphainventor.filemanager:id/text", name)
                # 点击OK
                self.my_click_text("OK")
            else:
                # 点击取消
                self.my_click_text("CANCEL")
            if is_remove:
                # 长按第index个bookmark
                self.my_long_click_xpath_text(bookmark_index + 3,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[")
                # 点击Rename
                self.my_click_text("Remove")
            # 点击返回，回到文件浏览的界面
            self.my_back()

