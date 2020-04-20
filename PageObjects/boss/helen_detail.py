#@Time :2020/4/1623:07
#@Author :helen
#@File :helen_detail.PY
from selenium.webdriver.common.by import By
from Common.BasePage import BasePage
class HelenDetail(BasePage):
    #渠道管理商
    channel_bid = (By.XPATH,'//ol/li[7]')

    def click_helen_channel_bid(self):
        name = "helen渠道商页面_查看详情"
        self.wait_eleVisible(self.channel_bid,model="mame")
        self.click_element(self.channel_bid, model=name)
