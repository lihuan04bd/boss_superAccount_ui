#@Time :2020/4/1913:50
#@Author :helen
#@File :boliu_page.PY
from selenium.webdriver.common.by import By
from Common.BasePage import BasePage
class BoLiu(BasePage):
    here = (By.XPATH,'//a[text()="here"]')

    def click_here(self):
        self.wait_eleVisible(self.here,model="波流详情页面")
        self.click_element(self.here, model="波流详情页面")