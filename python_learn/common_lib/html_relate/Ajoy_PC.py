from lib_selenium import *

demo = Basic_functions()
demo.init_web_driver(load_pic = True, size="PC")
# demo.init_web_driver(load_pic = True)
demo.go_to_web("https://www.feastogether.com.tw/booking/Ajoy")

# 關閉廣告
adv_css = "#root > div > main > div.sc-evZas.hdSubm > div > div.sc-ksZaOG.czEzjO > div.sc-hAZoDl.fDKeZZ > svg"
demo.click_element(By.CSS_SELECTOR, adv_css)

# 登入會員
login_css = "#root > div > header > div > div > div > nav > ul > li:nth-child(5) > button"
demo.click_element(By.CSS_SELECTOR, login_css)

# 登入
time.sleep(1)
demo.log_web()
demo.fill_element(By.NAME, "phoneNumber", "0983992425")
demo.fill_element(By.NAME, 'password', "notImportant123")
demo.click_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/button")

# time.sleep(1)
input("wait until 12")

demo.click_element(By.XPATH,     "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[2]/div[2]/div[1]")
for _ in range(4):
    demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/button[2]")
    
# 選擇用餐時間
demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[3]/div[2]/div")
time.sleep(0.1)
demo.click_element(By.XPATH, "/html/body/div[2]/div[3]/ul/li[2]") # 午餐一
# demo.click_element(By.XPATH, "/html/body/div[2]/div[3]/ul/li[3]") # 午餐二


# 選擇用餐日期
time.sleep(0.1)
demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[4]/div[2]/div[1]")
demo.scroll_down()
# demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div[4]/div[4]/div/div[1]", "日期 20")
# demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div[4]/div[5]/div/div[1]", "日期 21")
# demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div[4]/div[6]/div/div[1]", "日期 22")
demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div[4]/div[6]/div/div[1]", "日期 23")

# 搜尋
demo.click_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[1]/div/form/div/div[3]/div[5]/button")

input("stop_end")
