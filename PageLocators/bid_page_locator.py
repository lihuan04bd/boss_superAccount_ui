#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/18 17:33

from selenium.webdriver.common.by import By
class BidPageLocator:
    # 投资输入框
    invest_input = (By.XPATH,'//input[@data-url="/Invest/invest"]')
    # 投资按钮
    invest_button = (By.XPATH,'//button[text()="投标"]')
    # 投资成功 - 查看并激活按钮
    active_button_in_successPopup = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
