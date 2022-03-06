from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe' # 改成你自己firefox.exe的位置
# webdriver_path = 'D:\\dont_move\\chromedriver.exe' # 改成你檔案的位置
webdriver_path = 'D:\\dont_move\\geckodriver.exe'

binary = FirefoxBinary(firefox_path)
driver = webdriver.Firefox(executable_path=webdriver_path,firefox_binary=binary) #開啟firefox
driver.maximize_window()
# 
driver.get("https://XXX/") #前往這個網址


time.sleep(15)
print("url : ")
print (driver.current_url)
page_source_soup = BeautifulSoup( driver.page_source, 'html.parser')

write_dst = "D:\\python_code\\4_control_leg\\leg1.xml"
with open(write_dst, "w" ,encoding="utf-8") as write_dst_f:
    write_dst_f.write(page_source_soup.prettify())

all_script = page_source_soup.findAll("script")

script_str = str(all_script[2])

url_start = script_str.find("var url = \"")+11
url_end = script_str.find("\" + href;")
# print(url_start)
# print(url_end)
full_url = script_str[url_start:url_end] + driver.current_url
print(full_url)
driver.get(full_url) #前往這個網址
time.sleep(30)
page_source_soup = BeautifulSoup( driver.page_source, 'html.parser')
write_dst = "D:\\python_code\\4_control_leg\\leg2.xml"
with open(write_dst, "w" ,encoding="utf-8") as write_dst_f:
    write_dst_f.write(page_source_soup.prettify())


# iframe_object = driver.find_element_by_tag_name("iframe")
# driver.switch_to.frame(iframe_object)
# time.sleep(10)
# print(BeautifulSoup( driver.page_source, 'html.parser').prettify())

# driver.quit()