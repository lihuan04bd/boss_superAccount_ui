#@Time :2020/4/1622:34
#@Author :helen
#@File :index_page.PY
from selenium.webdriver.common.by import By
from Common.BasePage import BasePage
class IndexPage(BasePage):
    #渠道管理商
    channel_bid = (By.XPATH,'//a[@href="#/business"]')

    def click_channel_manger(self):
        name = "首页页面_点击渠道商管理"
        self.wait_eleVisible(self.channel_bid,model="mame")
        self.click_element(self.channel_bid, model=name)