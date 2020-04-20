#@Time :2020/4/1621:39
#@Author :helen
#@File :login_page.PY
from PageLocators.boss.login_page_locator import LoginPageLocator
from Common.BasePage import BasePage
# https://hometest-boss-web.haimawan.com/#/login
class LoginPage(LoginPageLocator,BasePage):

    def login(self, username, passwd):
        print("============",username)
        # 日志内容：登陆页面的登陆功能
        name = "登陆页面_登陆功能"
        self.wait_eleVisible(self.login_name, model=name)
        self.input_text(self.login_name, username, model=name)
        self.input_text(self.login_pwd, passwd, model=name)
        self.click_element(self.login_btn, model=name)
        import time
        time.sleep(10)

    # def get_errorMsg_fromLoginArea(self):
    #     name = "登陆页面_登陆区域错误提示"
    #     return self.get_text(self.error_prompt_fromLoginArea, model=name)
    #
    # def register(self):
    #     pass