#@Time :2020/4/1622:06
#@Author :helen
#@File :bossRun.PY


import unittest
import HTMLTestRunnerNew
from TestCases.boss import test_superAccount


# C:\mySpace\python9_WEB_Framework - V4_20181018\TestCases\boss\hhhtest_login.py
suite=unittest.TestSuite()
#ddt 加载用例 loader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_superAccount))
# runner = unittest.TextTestRunner()
#生成测试报告 HTML
with open("HtmlTestReport//test_result.html",'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file,
                                            title='BOSS平台',
                                            description='BOSS平台----超级账号绑定播流',
                                            tester='Helen')
    runner.run(suite)
