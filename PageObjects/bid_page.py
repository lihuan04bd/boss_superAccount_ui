#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 16:17

from PageLocators.bid_page_locator import BidPageLocator
from Common.BasePage import BasePage
class BidPage(BidPageLocator,BasePage):

    #获取用户余额
    def get_user_leftMoney(self):
        #等待
        self.wait_eleVisible(self.invest_input)
        return self.get_element_attribute(self.invest_input,"data-amount")

    #投资操作
    def invest(self,money):
        #输入框，输入值
        self.wait_eleVisible(self.invest_input)
        self.input_text(self.invest_input,money)
        # 点击按钮
        self.click_element(self.invest_button)

    #投资成功 - 弹出框 - 点击激活并查看按钮
    def click_activeButton_from_investSuccess_popup(self):
        self.wait_eleVisible(self.active_button_in_successPopup)
        self.click_element(self.active_button_in_successPopup)

    #投资失败 - 2种场景