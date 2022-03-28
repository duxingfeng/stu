# -*- coding:utf-8-*-
# @Time:  2022/3/27 11:27
# @File:  pg_test.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

path = "/Users/feng/Documents/tools/chrome/chromedriver"
# opt = ChromeOptions()            # 创建Chrome参数对象
# opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.implicitly_wait(300)
# driver.get("http://rds-console-stag.jdcloud.com/rds/detail?instanceId=pg-o1pajudv97&regionId=cn-north-1&currentTab=performance")
driver.get(
    "http://rds-console-stag.jdcloud.com/rds/detail?instanceId=mysql-pl8pijx30x&regionId=cn-north-1&currentTab=dbManager")
driver.find_element(By.XPATH, '//*[@id="switch_jdcloud"]').click()
driver.find_element(By.XPATH, '//*[@id="loginName"]').send_keys('jcloudtest02')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('360buy@jd123')
driver.find_element(By.XPATH, '//*[@id="loginSubmit"]').click()
driver.find_element(By.XPATH, '//*[contains(text(),"登录数据库")]').click()

all_windows = driver.window_handles
print(all_windows)
main_windows = driver.current_window_handle

for handle in all_windows:
    if handle != main_windows:
        driver.switch_to.window(handle)
register_windows = driver.current_window_handle

# pg数据库
# driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("testmf")
# driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[4]/td/input').send_keys("Testtest1")
# driver.find_element(By.XPATH, '//*[@id="content"]/form/p/input').click()
# driver.find_element(By.XPATH, '//*[@id="Db-testmf"]').click()
# driver.find_element(By.XPATH, '//*[@id="menu"]/p/a[1]').click()
# driver.find_element(By.XPATH, '//*[@id="form"]/p[1]/textarea').send_keys('select pg_sleep(1.01) from test_slow')
# for i in range(200):
#     driver.find_element(By.XPATH, '//*[@id="form"]/p[2]/input[1]').click()
#     print(f"{i}")
#     i += 1

# mysql 数据库
driver.find_element(By.XPATH, '//*[@id="input_password"]').send_keys("Testtest1")
driver.find_element(By.XPATH, '//*[@id="input_username"]').send_keys("testmf")
driver.find_element(By.XPATH, '//*[@id="input_go"]').click()
# driver.find_element(By.XPATH, '//*[@id="topmenu"]/li[1]/a').click()
db = driver.find_elements(By.XPATH, '//*[contains(text(),"tttt")]')
for i in db:
    print(f"{db}")
    i.click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="topmenu"]/li[2]/a/img').click()
# # fail
driver.find_element(By.XPATH,
                    '//*[@id="sqlquerycontainerfull"]/div[1]/div[6]/div[1]/div/div/div/div[5]/div/pre').send_keys('select sleep(2.01) from test_slow;')
