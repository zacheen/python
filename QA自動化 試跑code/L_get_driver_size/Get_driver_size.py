# 取得視窗大小 (那時候為了可以四個視窗多開 要等比例調整點選的位置)
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

import time

options = Options()
# options.headless = True
options.add_argument('disable-infobars')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
driver.maximize_window()
time.sleep(2)
print(driver.get_window_size())
time.sleep(2)

