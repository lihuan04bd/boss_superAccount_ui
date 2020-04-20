#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 20:59

from PageLocators.login_page_locator import LoginPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage

class LoginPage(LoginPageLocator,BasePage):

    def login(self,username,passwd):
        #日志内容：登陆页面的登陆功能
        name = "登陆页面_登陆功能"
        self.wait_eleVisible(self.user_input,model=name)
        self.input_text(self.user_input,username,model=name)
        self.input_text(self.passwd_input,passwd,model=name)
        self.click_element(self.login_button,model=name)

    def get_errorMsg_fromLoginArea(self):
        name="登陆页面_登陆区域错误提示"
        return self.get_text(self.error_prompt_fromLoginArea,model=name)

    def register(self):
        pass