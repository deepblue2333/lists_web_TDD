
import time
from unittest import skip

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest

MAX_WAIT = 5

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到输入框完美地居中显示
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        time.sleep(3)
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=30.5
        )

        # 她新建了一个清单，看到输入框仍然完美地居中显示
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('testing')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=30.5
        )

