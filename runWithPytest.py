#@Time :2020/4/1920:30
#@Author :helen
#@File :runWithPytest.PY

#unitest收集测试用例
import pytest

pytest.main(["--html=HtmlTestReport/report.html"])

# 持续集成 jenkins docker
#
# 基于 python语言开发， 用selenium 框架做的ui自动化，  ddt 做了数据驱动 ,excel 组织测试用例
# unittest  单元测试，htmlTestResult 出据测试报告