#@Time :2020/4/1622:55
#@Author :helen
#@File :bid_manger.PY

from selenium.webdriver.common.by import By
from Common.BasePage import BasePage
class BidManger(BasePage):
    helen = (By.XPATH,'//a[contains(@href,"helen")]')
    #点击超级管理
    channel_bid = (By.XPATH, '//ol/li[7]')
    # 点击创建超级账号
    create_superAccount = (By.XPATH,'//label/a[contains(text(),"创建超级账号")]')
    #账号类型
    account_type = (By.XPATH,'//input[@class="el-input__inner"]')
    #qq类型
    qq_account = (By.XPATH,'//li[contains(@class,"el-select-dropdown__item")]')
    #账号
    account = (By.XPATH,'//div[@class="input-left"]/input')
    #密码
    pwd = (By.XPATH,'//div[@class="input-right"]/input')
    #创建button
    create_button = (By.XPATH,'//a[@class="act"]')
    #去绑定  绑定两个入口公用
    go_to_bind= (By.XPATH,'//td[@class="boss-business-conf"]/a[text()="去绑定"][1]')
    # 选择游戏
    choose_play = (By.XPATH,'//div[contains(@class,"c2-account-list")]//input[@icon="caret-top"]')
    #选中王者游戏
    choose_wangzhe = (By.XPATH,'//li//span[contains(text(),"王者")]')
    #选择节点
    choose_idc = (By.XPATH,'//div[@class="input-right"]//input[@class="el-input__inner"]')
    # 选中idc 节点
    switch_one_idc = (By.XPATH, '//li//span[contains(text(),"腾讯REL")]')
    #实例数
    instance_num = (By.XPATH,'//input[@type="number"]')
    #去登录
    go_login = (By.XPATH,'//a[contains(@href,"super")]')

    #弹框去绑定
    bid_ond = (By.XPATH,'//a[@class="act"]')
    def click_henlen_bid(self):
        name = "渠道管理页面--点击henlen "
        self.click_element(self.helen,model=name)



    def click_superAccount(self):
        name = "helen渠道商页面_点击"
        self.wait_eleVisible(self.channel_bid, model="mame")
        self.click_element(self.channel_bid, model=name)

    def create_superAccount_fea(self,username,pwd):
        name = "helen渠道商页面_创建超级账号"
        self.wait_eleVisible(self.create_superAccount, model=name)
        self.click_element(self.create_superAccount, model=name)
        self.wait_eleVisible(self.account_type, model=name)
        self.click_element(self.account_type,model=name)
        self.wait_eleVisible(self.qq_account, model=name)
        self.click_element(self.qq_account)

        self.input_text(self.account,username,model=name)
        self.input_text(self.pwd, pwd, model=name)
        self.wait_eleVisible(self.create_button, model=name)
        self.click_element(self.create_button,model=name)
    def bind(self):
        name = "点击去绑定"
        self.wait_eleVisible(self.bid_ond, model=name)
        self.click_element(self.bid_ond, model=name)
    def go_bind(self):
        name = "超级账号页面--去绑定"
        self.wait_eleVisible(self.go_to_bind, model=name)
        self.click_element(self.go_to_bind, model=name)
    @property
    def binging(self):
        name = "真正的绑定"
        self.wait_eleVisible(self.choose_play, model=name)
        self.click_element(self.choose_play, model=name)

        self.wait_eleVisible(self.choose_wangzhe, model=name)
        self.click_element(self.choose_wangzhe, model=name)
        import time
        time.sleep(2)
        self.wait_eleVisible(self.choose_idc, model=name)
        self.click_element(self.choose_idc, model=name)

        self.wait_eleVisible(self.switch_one_idc, model=name)
        self.click_element(self.switch_one_idc, model=name)


        self.input_text(self.instance_num,1)
        self.click_element(self.create_button, model=name)

    def go_login_page(self):
        name ="点击去登录"
        self.wait_eleVisible(self.go_login, model=name)
        self.click_element(self.go_login, model=name)
