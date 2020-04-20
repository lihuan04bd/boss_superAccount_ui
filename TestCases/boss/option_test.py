#@Time :2020/4/1918:57
#@Author :helen
#@File :option_test.PY
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-features=EnableEphemeralFlashPermission")
options.add_argument("--abc=qyf")
# options.add_argument('--user-data-dir=C:\\Users\\lihua\\AppData\\Local\\Temp\\scoped_dir15440_3569\\Default')
prefs = {

    "profile.managed_default_content_settings.images": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.setting": 1
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
print("======000=======", options.arguments)

driver.get("https://www.baidu.com/")
print("======33333333333=======", options.experimental_options)