from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

firefox_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe' # 改成你自己firefox.exe的位置
webdriver_path = 'D:\\dont_move\\chromedriver.exe' # 改成你檔案的位置
options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
driver.maximize_window()
driver.get('https://demo.XXX/') #前往這個網址

time.sleep(30)



iframe_object = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe_object)
time.sleep(10)
print("111111111111111111111111111111111111111111111111111")
driver.switch_to.default_content()
time.sleep(10)
print("src = ")
iframe_object = driver.find_element_by_tag_name("iframe")
print("check iframe_object is not null : " + str(iframe_object))
try :
    iframe_object.get_attribute("src")
except :
    print("get src fail")
driver.switch_to.frame(iframe_object)
print("2222222222222222222222222222222222222222222222222222222222222")
print(BeautifulSoup( driver.page_source, 'html.parser').prettify())
time.sleep(10)

print("33333333333333333333333333333333333333333333333333333333333333333")

# search_input = driver.find_element_by_name("q")
# search_input.send_keys('python is awesome')
# print(BeautifulSoup( driver.page_source, 'html.parser').prettify())
time.sleep(20)

# print("111111111111111111111111111111111111111111111111111")
# print(BeautifulSoup( driver.page_source, 'html.parser').prettify())


# cut_success = driver.get_screenshot_as_file("D:/dont_move/cut/abc.png")
# if cut_success == False :
#     print("cut pic fial")

# # driver.switch_to.frame( driver.find_element_by_id("myiframe"))
# # # print(driver.page_source)
# # print("2222222222222222222222222222222222222222222222222222222222222")
# # print(BeautifulSoup( driver.page_source, 'html.parser').prettify())

# time.sleep(60)
# driver.switch_to.frame( driver.find_element_by_id("myiframe"))
# # print("src = ")
# # src = driver.find_element_by_name("myiframe").get_attribute("src")
# print("33333333333333333333333333333333333333333333333333333333333333333")
# print(BeautifulSoup( driver.page_source, 'html.parser').prettify())
# time.sleep(10)
# driver.switch_to.parent_frame()


# time.sleep(10)
# # print("src = ")
# # src = driver.find_element_by_name("myiframe").get_attribute("src")

# print("444444444444444444444444444444444444444444444444444444444444444444")
# print(BeautifulSoup( driver.page_source, 'html.parser').prettify())

# time.sleep(10)
# driver.switch_to.frame( driver.find_element_by_id("myiframe"))

# print("55555555555555555555555555555555555555555555555555555555555555")
# print(BeautifulSoup( driver.page_source, 'html.parser').prettify())

# # start_search_btn = driver.find_element_by_name("btnK")
# # start_search_btn.click()

# # time.sleep(100)



# time.sleep(30)
# time.sleep(15)
driver.quit()