#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 16:23

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class UserPage:
    user_money = '//*[@class="color_sub"]'

    def __init__(self,driver):
        self.driver = driver

    def get_user_leftMoney(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.user_money)))
        text = self.driver.find_element_by_xpath(self.user_money).text
        return text.strip("元")