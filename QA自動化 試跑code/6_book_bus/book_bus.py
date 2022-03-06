"""
如果還想改善 就看arr中有沒有重複的 重複的刪除
"""


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import datetime

assing_time = 1
# 1 : assing
# 2 : now
if assing_time == 1 :
    now_time = datetime.datetime.strptime("2020-07-17-18-30", "%Y-%m-%d-%H-%M")
else:
    now_time = 	(datetime.datetime.now()+datetime.timedelta(minutes=200))

Tai_to_cha = 1
# 1 : Taipei to chayi
# 2 : chayi to Taipei

firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe' # 改成你自己firefox.exe的位置
# webdriver_path = 'D:\\dont_move\\chromedriver.exe' # 改成你檔案的位置
webdriver_path = 'D:\\dont_move\\geckodriver.exe'

binary = FirefoxBinary(firefox_path)
driver = webdriver.Firefox(executable_path=webdriver_path,firefox_binary=binary) #開啟firefox
driver.maximize_window()
# 
# driver.get("https://order.kingbus.com.tw/ORD/Ord_M_1500_HomePage.aspx") #前往這個網址
driver.get("https://order.kingbus.com.tw/ORD/ORD_M_1510_OrderGo.aspx") #前往這個網址

time.sleep(2)

write_dst = "D:\\python_code\\6_book_bus\\html.xml"
with open(write_dst, "w" ,encoding="utf-8") as write_dst_f:
    page_source_soup = BeautifulSoup( driver.page_source, 'html.parser')
    write_dst_f.write(page_source_soup.prettify())

write_in_id = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtCustomer_ID")
write_in_id.send_keys('I100439255')

write_in_tel = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtPhone")
write_in_tel.send_keys('0983992425')

write_in_OK = driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnStep1_OK")
write_in_OK.click()

write_dst = "D:\\python_code\\6_book_bus\\html2.xml"
with open(write_dst, "w" ,encoding="utf-8") as write_dst_f:
    page_source_soup = BeautifulSoup( driver.page_source, 'html.parser')
    write_dst_f.write(page_source_soup.prettify())

time.sleep(5)

from selenium.webdriver.support.ui import Select




# #如果要印出select裡面的選項
# for op in select_from.options:
#     print(op.text)

if Tai_to_cha == 1 :
    select_from = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStation_ID_From'))
    select_from.select_by_visible_text("台北轉運")
    time.sleep(5)
    select_end = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStation_ID_To'))
    select_end.select_by_visible_text("嘉　　義")
elif Tai_to_cha == 2 :
    select_from = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStation_ID_From'))
    select_from.select_by_visible_text("嘉　　義")
    time.sleep(1)
    select_end = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStation_ID_To'))
    select_end.select_by_visible_text("台北轉運")



arr = []

periods = 2

for x in range(periods) :
    ISOTIMEFORMAT = '%Y/%m/%d'
    theTime = now_time.strftime(ISOTIMEFORMAT)
    print(theTime)
    write_in_date = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtOut_Dt")
    write_in_date.send_keys(theTime)

    select_from = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlHour'))
    ISOTIMEFORMAT = '%H'
    theTime = now_time.strftime(ISOTIMEFORMAT)
    select_from.select_by_visible_text(theTime)

    select_from = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlMinute'))
    ISOTIMEFORMAT = '%M'
    theTime = now_time.strftime(ISOTIMEFORMAT)
    theTime = str((int(theTime)//10)*10)

    if theTime == "0" :
        theTime = "00"

    select_from.select_by_visible_text(theTime)

    write_in_OK = driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnStep2_OK")
    write_in_OK.click()

    time.sleep(5)

    first_period = driver.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_grdList']/tbody/tr")
    # print(first_period)

    
    for yy in range(3):
        arr1 = (first_period[yy+1].text).split(" ") #以空格拆分成若干個(個數與列的個數相同)一維列表
        arr.append(arr1)

    
    if x == periods-1 :
        break

    now_time = (now_time+datetime.timedelta(minutes=90))

    write_in_OK = driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnStep3ReSelect")
    write_in_OK.click()

    time.sleep(5)

# time.sleep(3)
# write_dst = "D:\\python_code\\6_book_bus\\html3.xml"
# with open(write_dst, "w" ,encoding="utf-8") as write_dst_f:
#     page_source_soup = BeautifulSoup( driver.page_source, 'html.parser')
#     write_dst_f.write(page_source_soup.prettify())



print(arr)

import pandas as pd

print(pd.DataFrame(arr))


