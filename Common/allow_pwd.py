#@Time :2020/4/1919:49
#@Author :helen
#@File :allow_pwd.PY

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
prefs = {}
# 设置这两个参数就可以避免密码提示框的弹出
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.baidu.com/')
browser.quit()