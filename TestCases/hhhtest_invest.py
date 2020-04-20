#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 15:24

#正常场景
#前置
#1、用户余额够用 ：充值一个亿。
#2、查看有多少余额，然后不够200块，我就去充值。如果有就不充值了。
#不走web页面，走接口来实现。
#有可投资的标

#步骤
# 首页-直接选第一个标；
#标页面 - 获取用户可用余额
# 标页面-输入金额，进行投资。投资金额：200
# 点击投资成功弹出框中的   查看并激活按钮

#验证
# 个人页面：获取用户可用余额
#比对：投资金额  = 投资前的余额 - 投资后的余额
# 投资记录？？？
# 利息是多少？

import unittest
from TestDatas.CommonDatas import *
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage

import pytest

@pytest.mark.demo
def test_demo():
    print("我是模块下函数版本的测试用例！！")

def demo():
    pass

@pytest.mark.invest
class TestInvest(unittest.TestCase):


    def setUp(self):
        #打开浏览器，登陆前程贷
        self.driver = webdriver.Chrome()
        self.driver.get(web_url)
        LoginPage(self.driver).login(user,passwd)

    def tearDown(self):
        self.driver.quit()

    def demo2(self):
        pass

    @pytest.mark.smoke
    def test_invest_success(self):
        # 步骤
        # 首页-直接选第一个标；
        IndexPage(self.driver).click_first_investButton()
        # 标页面 - 获取用户可用余额
        bid_page = BidPage(self.driver)
        userMoney_before_invest = bid_page.get_user_leftMoney()
        # 标页面-输入金额，进行投资。投资金额：200
        bid_page.invest(200)
        # 标页面 - 点击投资成功弹出框中的   查看并激活按钮
        bid_page.click_activeButton_from_investSuccess_popup()
        # 验证
        # 个人页面：获取用户可用余额
        userMoney_after_invest = UserPage(self.driver).get_user_leftMoney()
        # 比对：投资金额  = 投资前的余额 - 投资后的余额
        self.assertEqual(200,int(float(userMoney_before_invest) - float(userMoney_after_invest)))
    #     pass
    #
    # def test_invest_fail_no100(self):
    #     pass
    #
    #
    # def test_invest_fail_no10(self):
    #     pass




#异常场景  - 用户余额不够 - 手功用例
#异常场景  - 投资》标的可投余额 - 手功用例