import os
import time
from unittest import skip

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from lists.models import List, Item
from selenium.common.exceptions import WebDriverException
from django.core.exceptions import ValidationError
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 伊迪丝访问首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))

        # 她输入一些文字，然后再次提交，这次没问题了
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Buy milk')

        # 她有点儿调皮，又提交了一个空待办事项
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # 她在列表页面看到了一条类似的错误消息
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))

        # 输入文字之后就没问题了
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Buy milk')
        self.wait_for_row_in_list_table('Make tea')

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()


