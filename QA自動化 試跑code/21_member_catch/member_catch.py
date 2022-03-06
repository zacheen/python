import time
from bs4 import BeautifulSoup
import pandas as pd
from os import system

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
webdriver_path = 'D:\\dont_move\\chromedriver.exe'
options = Options() 
driver = webdriver.Chrome(executable_path=webdriver_path, options=options) 
driver.maximize_window()
url="http://192.168.X.X:port/default"
driver.get(url)

abs_loc = "D:\\python_code\\21_member_catch\\"

with open(abs_loc + "member_catch_input.txt", "r", encoding='UTF-8') as read_input_f :
    # account = read_input_f.readline()
    account = str(read_input_f.readline().split(" -:")[1]).strip()
    print(account)
    password = str(read_input_f.readline().split(" -:")[1]).strip()
    print(password)
    b_date = str(read_input_f.readline().split(" -:")[1]).strip()
    print(b_date)
    e_date = str(read_input_f.readline().split(" -:")[1]).strip()
    print(e_date)
    ID = "70022_" + str(read_input_f.readline().split(" -:")[1].strip())
    print(ID)
# account=input("請輸入帳號:")
# password=input("請輸入密碼:")
# print("====================================")
# print("日期輸入範例:2020-01-01 18:00")
# b_date=input("請輸入開始日期:")
# e_date=input("請輸入結束日期:")
# print("====================================")
# ID=input("請輸入會員ID:")
def sleep():
    time.sleep(0.3)

def login():
    ID=driver.find_element_by_name("MERCHANT_USERNAME")
    ID.send_keys(account)#輸入帳號
    sleep()
    
    PASSWORD=driver.find_element_by_name("MERCHANT_PWD")
    PASSWORD.send_keys(password)#請輸入密碼
    sleep()
    
    commit=driver.find_element_by_css_selector("#login")
    commit.click()
    time.sleep(8)
    
login()

def search(b_date,e_date,ID):
    report=driver.find_element_by_css_selector("#side-menu > li:nth-child(6) > a")
    report.click()
    time.sleep(1)
    
    LoseWin_report=driver.find_element_by_css_selector("#side-menu > li.active > ul > li:nth-child(2) > a")
    LoseWin_report.click()
    time.sleep(1)

    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[contains(@src,"/winAndLoseReport")]'))
    begin_date=driver.find_element_by_name("BEGIN_DATE")
    begin_date.send_keys(b_date)#輸入開始日期
    sleep()
  
    end_date=driver.find_element_by_name("END_DATE")
    end_date.send_keys(e_date)#輸入結束日期
    sleep()
    
    member_id=driver.find_element_by_name("txtAccounts")
    member_id.send_keys(ID)#輸入會員編號
    sleep()
    
    driver.find_element_by_css_selector("#btnSearch").click()
    print("搜尋中......請稍後.......")
    time.sleep(8)

    pages_nums_begin=1

    pages=driver.find_element_by_css_selector("#no-more-tables > div.bootstrap-table > div.fixed-table-container > div.fixed-table-pagination > div.pull-left.pagination-detail > span.pagination-info").text
    # print(type(pages))
    pages_list=pages.split(" ")
    # print(pages_list)
    pages__nums=(int(pages_list[5])//20)+1
    # print(pages__nums)


    while True:
        soup=BeautifulSoup(driver.page_source,"lxml")
        member_information=soup.select_one("#tblData")
        # print(member_information)
        df = pd.read_html(str(member_information))[0]

        # print(df)
        # with open("D:\\python_code\\21_member_catch\\pass.txt", "w", encoding='UTF-8') as pass_f :
        #     pass_f.write(str(df))
        # print(type(df))
        # print(df.iloc[0,0])

        # df.to_csv("member_information.csv",mode="a")
        df.to_csv(abs_loc+"member_information.csv", mode="a", header = False, encoding = "utf-8" )

        try:
            print(str(pages_nums_begin)+ " : "+str(pages__nums))
            if pages_nums_begin < pages__nums :
                pages_nums_begin = pages_nums_begin+1
            else:
                # end reading
                print("end page : " + str(pages_nums_begin))
                break
            
            driver.find_element_by_css_selector("#no-more-tables > div.bootstrap-table > div.fixed-table-container > div.fixed-table-pagination > div.pull-right.pagination > ul > li.page-next > a").click()
            time.sleep(0.5)
        except Exception:
            # didn't have next page
            print("error !!!!! in member_catch")
            break



if __name__ == '__main__' :
    search(b_date,e_date,ID)
    driver.quit()




