#@Time :2020/4/1621:41
#@Author :helen
#@File :login_page_locator.PY
from selenium.webdriver.common.by import By

class LoginPageLocator:
    #用户名
     login_name = (By.XPATH,'//input[@placeholder="请输入您的账号"]')
    # 密码
     login_pwd = (By.XPATH,'//input[@placeholder="请输入您的密码"]')
    #login btton
     login_btn = (By.XPATH,'//a[contains(@class,"login-btn")]')


