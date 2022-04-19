# -*- coding:utf-8-*-
# @Time:  2021/12/27 20:47
# @File:  test_selenium.py
import time

from selenium import webdriver


class TestJDCloud(object):

    def setup(self):
        path = "/Users/feng/Documents/tools/chrome/chromedriver"
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)
        time.sleep(3)

    def teardown(self):
        self.driver.quit()

    def test_jdcloud(self):
        self.driver.get("https://www.jdcloud.com/")
        time.sleep(5)

    # inspect.stack()
    # func.__name__
    # repr()