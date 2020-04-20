#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/16 21:33

from urllib.parse import quote_plus as url_quoteplus
from urllib.parse import urlsplit
from selenium.webdriver.common.by import By as WebBy
from selenium.webdriver.support.ui import Select as WebSelect



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Common import logger
import logging
import time
from Common.dir_config import screenshot_dir


class BasePage:
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver
    def __init__(self,driver):
        self.driver = driver

    #等待元素可见 - 失败的时候有截图有日志
    def wait_eleVisible(self,locator,wait_times=20,poll_frequency=0.5,model=""):
        """
        :param locator: 类型为元组(By.XXX,定位表达式)
        :return:
        """
        try:
            #开始时间
            logging.info("等待操作----")
            #start_time = time.time()
            WebDriverWait(self.driver,wait_times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束时间 - 求差值，转换成单位秒。写入日志。
            #end_time = time.time()
            logging.info("等待元素可见{0}".format(locator))
        except:
            #捕获异常到日志中；
            logging.exception("等待元素可见：")
            #截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            #抛出异常
            raise

    #查找元素
    def get_element(self,locator,model=""):
        #
        try:
            return self.driver.find_element(locator[0],locator[1])
        except:
            pass
            # 捕获异常到日志中；
            logging.exception("查找元素失败：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise


            #输入操作
    def input_text(self,locator,text,model=""):
        #找到元素
        ele = self.get_element(locator)
        #输入操作
        try:
            ele.send_keys(text)
        except:
            # 捕获异常到日志中；
            logging.exception("输入操作失败：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

            #点击操作
    def click_element(self,locator,model=""):
        # 找到元素
        ele = self.get_element(locator)
        #点击操作
        try:
            ele.click()
        except:
            # 捕获异常到日志中；
            logging.exception("等待元素可见：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr_name,model=""):
        # 找到元素
        ele = self.get_element(locator)
        # 获取元素的属性
        try:
            logging.info("获取什么元素的什么属性")
            return ele.get_attribute(attr_name)
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素的属性失败：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    #获取元素的文本
    def get_text(self,locator,model=""):
        # 找到元素
        ele = self.get_element(locator)
        # 获取元素的属性
        try:
            return ele.text
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素的文本内容失败：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise
     #鼠标移动到下拉框位置
    def move_to_element(self,locator,model=""):
        #找到元素
        ele = self.get_element(locator)
        #移动到该元素上
        time.sleep(3)
        try:
            actionChains = ActionChains(self.driver)
            actionChains.move_to_element(locator).perform()
        except:
            # 捕获异常到日志中；
            logging.exception("鼠标移动到下拉框位置：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise


    def _screenshot(self,model_name):
        #时间
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name,time.strftime("%Y%m%d_%H%M%S"))
        self.driver.save_screenshot(filePath)
        logging.info("截图成功，图片路径为：{0}".format(filePath))

    def refresh(self):
        self.driver.refresh()


    def wins_handles(self):

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
    #上传操作
    def upload(self):
        pass

    # 上传操作
    def getUrl(self):
        return self.getUrl()

    def allow_flash(self,url):
        def _base_url(url):
            if url.find("://") == -1:
                url = "http://{}".format(url)
            urls = urlsplit(url)
            return "{}://{}".format(urls.scheme, urls.netloc)

        def _shadow_root(driver, element):
            return driver.execute_script("return arguments[0].shadowRoot", element)

        base_url = _base_url(url)
        self.driver.get("chrome://settings/content/siteDetails?site={}".format(url_quoteplus(base_url)))

        root1 = self.driver.find_element(WebBy.TAG_NAME, "settings-ui")
        shadow_root1 = _shadow_root(self.driver, root1)
        root2 = shadow_root1.find_element(WebBy.ID, "container")
        root3 = root2.find_element(WebBy.ID, "main")
        shadow_root3 = _shadow_root(self.driver, root3)
        root4 = shadow_root3.find_element(WebBy.CLASS_NAME, "showing-subpage")
        shadow_root4 = _shadow_root(self.driver, root4)
        root5 = shadow_root4.find_element(WebBy.ID, "advancedPage")
        root6 = root5.find_element(WebBy.TAG_NAME, "settings-privacy-page")
        shadow_root6 = _shadow_root(self.driver, root6)
        root7 = shadow_root6.find_element(WebBy.ID, "pages")
        root8 = root7.find_element(WebBy.TAG_NAME, "settings-subpage")
        root9 = root8.find_element(WebBy.TAG_NAME, "site-details")
        shadow_root9 = _shadow_root(self.driver, root9)
        root10 = shadow_root9.find_element(WebBy.ID, "plugins")  # Flash
        shadow_root10 = _shadow_root(self.driver, root10)
        root11 = shadow_root10.find_element(WebBy.ID, "permission")
        WebSelect(root11).select_by_value("allow")
if __name__ == '__main__':
    dreiver = webdriver.Chrome()
    BasePage(dreiver).allow_flash("https://hometest-boss-web.haimawan.com/#/login")