#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/17 10:58

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import win32gui
import win32con

def upload(file_path):
    # 一级顶层窗口 - 第二个参数Title会因为浏览器不同，而会不同。只需要根据浏览器修改第二个值就好。
    dialog = win32gui.FindWindow("#32770", "打开")
    # 二级窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    # 三级窗口
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    # 四级窗口 - 文件路径输入区域
    edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)
    # 二级窗口 - 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, "Button", None)
    # 1、输入文件路径
    #file = "D:\\课件目录\\web自动化-selenium\\test-3.html"
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    time.sleep(5)
    # 2、点击打开按钮
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

#https://mail.126.com/#return
#cookies处理或者加载用户数据
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\muji\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(options=options)
driver.get('https://mail.126.com/js6/main.jsp?sid=LAthTzrcVGEvZrjfnNccXZnkrKrmJRVa&df=mail126_letter#module=welcome.WelcomeModule%7C%7B%7D')

print("*********************************************")
#//span[text()="写 信"]
#点击写信按钮
WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,'//span[text()="写 信"]')))
driver.find_element_by_xpath('//span[text()="写 信"]').click()

#点击上传附件按钮
WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(@id,"_attachBrowser")]//input')))
driver.find_element_by_xpath('//div[contains(@id,"_attachBrowser")]//input').click()
time.sleep(1)

#处理上传操作
upload('D:\\课件目录\\web自动化-selenium\\html.ppt')