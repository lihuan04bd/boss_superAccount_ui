#@Time :2020/4/1621:54
#@Author :helen
#@File :test_login.PY
import unittest
from selenium import webdriver
from PageObjects.boss.login_page import LoginPage
from TestDatas.boss.CommonDatas import *
from TestDatas.boss.login_datas import *
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 前置
        # 打开浏览器访问网址
        self.driver = webdriver.Chrome()
        self.driver.get(web_url)
        self.loginp = LoginPage(self.driver)

    def test_normal_login(self):
        self.loginp.login(login_succs["username"],login_succs["passwd"])

if __name__ == '__main__':
    unittest.main()