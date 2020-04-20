#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 21:26

#测试用例 = 页面对象当中的页面功能 + 测试数据
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
#测试数据
from TestDatas.login_datas import  *
from TestDatas.CommonDatas import *
import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 前置
        #打开浏览器访问网址
        self.driver = webdriver.Chrome()
        self.driver.get(web_url)
        self.loginp = LoginPage(self.driver)

    def tearDown(self):
        #后置
        self.driver.quit()

    #正常场景用例 - 登陆成功
    def test_login_success(self):
        #步骤 - 登陆：用户名：18684720553  密码：python 比对数据：我的帐户[小小蜂96027]
        self.loginp.login(login_succs["username"],login_succs["passwd"])
        #断言
        self.assertEqual(IndexPage(self.driver).get_nickName(),login_succs["check"])

    @ddt.data(*login_noData)
    def test_login_fail_noUser(self,data):
        # 步骤 - 登陆：用户名：  密码：python 比对数据：弹出错误提示内容：请输入手机号
        self.loginp.login(data["username"], data["passwd"])
        # 断言
        self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), data["check"])

    # def test_login_fail_noPasswd(self):
    #     # 步骤 - 登陆：用户名：  密码：python 比对数据：弹出错误提示内容：请输入手机号
    #     self.loginp.login("18684720553", "")
    #     # 断言
    #     self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), "请输入密码")
    #
    # def test_login_fail_wrong_userFormat(self):
    #     # 步骤 - 登陆：用户名：  密码：python 比对数据：弹出错误提示内容：请输入手机号
    #     self.loginp.login("186847205", "")
    #     # 断言
    #     self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), "请输入正确的手机号")



    # def test_login_fail_wrongPasswd(self):
    #     pass
