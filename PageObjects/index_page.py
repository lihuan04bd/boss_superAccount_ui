#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 21:00
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IndexPage:
    bid_name_loc = '//*[@class="fs-22"]'

    def __init__(self,driver):
        self.driver = driver

    def get_nickName(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,'//a[@href="/Member/index.html"]')))
        return self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]').text

    def click_first_investButton(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,self.bid_name_loc)))
        self.driver.find_element_by_xpath(self.bid_name_loc).click()

