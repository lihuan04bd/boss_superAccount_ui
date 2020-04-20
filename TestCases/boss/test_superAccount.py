#@Time :2020/4/1820:27
#@Author :helen
#@File :test_superAccount.PY
from urllib.parse import quote_plus as url_quoteplus
from urllib.parse import urlsplit
from selenium.webdriver.common.by import By as WebBy
from selenium.webdriver.support.ui import Select as WebSelect

import unittest
from selenium import webdriver
from Common.allow_flash import AllowFlash
from PageObjects.boss.login_page import LoginPage
from PageObjects.boss.index_page import IndexPage
from PageObjects.boss.helen_detail import HelenDetail
from PageObjects.boss.bid_manger import BidManger
from PageObjects.boss.boliu_page import BoLiu
from TestDatas.boss.CommonDatas import *
from TestDatas.boss.login_datas import *
from TestDatas.boss.super_account import *
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 前置
        # 打开浏览器访问网址
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-features=EnableEphemeralFlashPermission")
        # options.add_argument("--abc=qyf")
        # options.add_argument('--user-data-dir=C:\\Users\\lihua\\AppData\\Local\\Temp\\scoped_dir15440_3569\\Default')
        # options.add_argument("--user-data-dir=C:\\Users\\muji\\AppData\\Local\\Google\\Chrome\\User Data")
        # options.add_argument("chrome_options.add_argument('--allow-outdated-plugins')")
        prefs = {

            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.setting": 1
        }
        # prefs = {
        #     "profile.content_settings.exceptions.plugins.*,*.setting": 1,
        #     "profile.default_content_setting_values.plugins": 1,
        #     "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        #     "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
        #     "PluginsAllowedForUrls": web_url
        # }
        options.add_experimental_option('prefs', prefs)
        # prefs = {
        #     "profile.managed_default_content_settings.images": 1,
        #     "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        #     "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
        #
        # }
        #
        # options.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(chrome_options=options)
        print("======000=======", options.arguments)
        AllowFlash(self.driver).allow_flash(web_url)
        self.driver.get(web_url)
        print("======33333333333=======", options.experimental_options)

        self.loginp = LoginPage(self.driver)
        # self.loginp.allow_flash(web_url)
        LoginPage(self.driver).login(user, passwd)
        self.boliuPage = BoLiu(self.driver)
        self.bid_manger = BidManger(self.driver)
        self.index_page = IndexPage(self.driver)

        self.helen_detail = HelenDetail(self.driver)

    def test_normal_login(self):
        #点击渠道商管理按钮
        self.index_page.click_channel_manger()
        self.bid_manger.click_henlen_bid()
        self.bid_manger.click_superAccount()
        self.bid_manger.create_superAccount_fea(super_account["account"],super_account["passwd"])
        self.bid_manger.bind()
        self.bid_manger.binging
        import time
        time.sleep(15)
        self.bid_manger.refresh()
        time.sleep(2)
        self.bid_manger.go_login_page()
        time.sleep(10)
        self.bid_manger.wins_handles()
        # self.boliuPage.click_here()
        time.sleep(50)
if __name__ == '__main__':
    unittest.main()