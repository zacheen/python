from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

import time
import pyautogui

testing = True

# 常用 function 整理 ################################################
# < 開啟 webdriver 相關直接複製 Basic_functions 比較快 >
# < element 相關 >
    # 找 element
        # find_element
    # 等待 element 出現
        # WebDriverWait().until
    # 操作
        # 點擊 : click (要注意點擊只能夠點擊到畫面內的 element )
        # 輸入 : send_keys
# < 對網頁操控 >
    # 向下捲動(scroll down) : 
# < 執行 java script >
    # execute_script
#####################################################################

class Basic_functions():
    def __init__(self):
        pass

    def init_web_driver(self, headless = False, full_screen = False, load_pic = testing, size = "PC", F12 = False) :
        webdriver_path = 'chromedriver.exe'
        options = Options()
        #    https://peter.sh/experiments/chromium-command-line-switches/
        options.headless = headless #Headless Browser是没有沒有圖形介面(GUI)的web瀏覽視窗
        if size == "PC" :
            options.add_argument("--window-size=1200,800") # 比例 1.5 最好
        elif size == "moble" :
            options.add_argument("--window-size=500,800")
        elif len(size) == 2 :
            options.add_argument(f"--window-size={size[0]},{size[1]}")
        options.add_argument('disable-infobars')
        if not load_pic :
            options.add_argument('--blink-settings=imagesEnabled=false')# 不加載圖片
            # F12 不能與 不加載圖片同時存在
            if F12 :
                print("load_pic and F12 cannot set False together")
                F12 = False
        if F12 :
            options.add_argument("--auto-open-devtools-for-tabs") # 自動叫出 F12
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        prefs = {"":""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        
        self.web_driver = webdriver.Chrome(executable_path=webdriver_path, options=options) #透過設定值開啟瀏覽器
        if "full" in size : # "full_screen"
            self.web_driver.maximize_window() #全螢幕

        if (not headless) and full_screen :
            # 記得這邊一定要用 pyautogui.click
            # 網頁置頂
            pyautogui.click(21, 21) #點擊溜覽器視窗頁面，確保置頂
            # 叫出書籤欄
            # pyautogui.hotkey("ctrl","shift","b")
            pyautogui.moveTo(952, 21) #定義為初始位置，避免滑鼠在溜覽器任意位置內出現提示訊息影響辨識或截圖
            time.sleep(1)
            pyautogui.hotkey("f11")

        if testing :
            print(self.web_driver.get_window_size())
        # actionChains = ActionChains(self.web_driver)

        if F12 :
            time.sleep(3)

    def go_to_web(self, url):
        self.web_driver.get(url)

    # 等待網頁讀取完畢
    def wait_loading(self, ele_type, ele):
        WebDriverWait(self.web_driver, 10, 0.5) \
        .until(EC.presence_of_element_located((ele_type, ele)))

    # type : 
        # By.CSS_SELECTOR : element 右鍵 > copy > copy selector
        # By.XPATH : element 右鍵 > copy > copy XPath
        # By.ID
        # By.TAG_NAME
        # By.CLASS_NAME
        # By.NAME
    # 找不到 element 的處理方法
        # https://blog.csdn.net/qq_16555103/article/details/108716594
        # 有可能名稱是動態設定的
    def click_element(self, ele_type, ele, wait = True, name = ""):
        if wait:
            self.wait_loading(ele_type, ele)
        temp=self.web_driver.find_element(ele_type, ele)
        try :
            temp.click()
        except Exception :
            input("cant click "+ name)
            pass

    def fill_element(self, ele_type, ele, input_str, wait = True):
        if wait:
            self.wait_loading(ele_type, ele)
        temp=self.web_driver.find_element(ele_type, ele)
        temp.send_keys(input_str)#輸入帳號

    def scroll_down(self, height = 100):
        if height < 0:
            command_str = "window.scrollBy(0,document.body.scrollHeight)"
               # 直接捲到螢幕最下方 (因為 document.body.scrollHeight)
        else :
            command_str = f"window.scrollBy(0,{height})"
        self.web_driver.execute_script(command_str)
        time.sleep(0.2)

    def log_web(self):
        with open("log.txt", "w", encoding='UTF-8') as fw :
            fw.write(self.web_driver.page_source)

if __name__ == "__main__":
    demo = Basic_functions()
    demo.init_web_driver(load_pic = False, size=[500,500])
    # demo.init_web_driver(load_pic = True)
    demo.go_to_web("https://www.feastogether.com.tw/booking/Ajoy")
    input("end_testing")
