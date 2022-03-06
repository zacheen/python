from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import sys
import traceback

import datetime
import time
from bs4 import BeautifulSoup
import pandas as pd
from os import system

import os
import pyautogui
import argparse


with open("./exec_id.txt", "r", encoding='UTF-8') as exec_id_f :
    exec_id = int(exec_id_f.readline())

with open("./exec_id.txt", "w", encoding='UTF-8') as exec_id_f :
    exec_id_f.write(str(exec_id+1))
    exec_id_f.flush()

use_sel = 0
strech_size = 1

def click(x,y):
    if use_sel == 1 :
        pyautogui.click(x, y)
    
    else :
        y = y - 90
        x = x/strech_size
        y = y/strech_size
        ActionChains(game_driver).move_by_offset(x, y).click().perform()
        ActionChains(game_driver).move_by_offset(-x, -y).perform()
        # print("click_sel")

def drag(x1,y1,x2,y2):
    if use_sel == 1 :
        pyautogui.mouseDown(x1,y1)
        pyautogui.moveTo(x2,y2, 0.5) 
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(0.5)


if __name__=="__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print args.echo
    
    webdriver_path = './chromedriver.exe'
    options = Options()
    # options.headless = True 

    options.add_argument("--window-size=1960,1080")
    options.add_argument('disable-infobars')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    prefs = {"":""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option("prefs", prefs)

    # extension_path=r'C:\Users\thomas\AppData\Local\Google\Chrome\User Data\Profile 2\Extensions\bpconcjcammlapcogcnnelfmaeghhagj\9.2.9_0.crx'
    # print(extension_path)
    # options.add_extension(extension_path)

    game_driver = webdriver.Chrome(executable_path=webdriver_path, options=options) 
    game_driver.maximize_window()

    # nimbus = r'https://chrome.google.com/webstore/detail/nimbus-screenshot-screen/bpconcjcammlapcogcnnelfmaeghhagj/related?page=1&hl=zh-tw&itemlang=bg'
    # game_driver.get(nimbus)
    # time.sleep(2)
    # game_driver.find_element_by_css_selector("body > div.F-ia-k.S-ph.S-pb-qa > div.h-F-f-k.F-f-k > div > div > div.e-f-o > div.h-e-f-Ra-c.e-f-oh-Md-zb-k > div > div").click()
    # time.sleep(20)
    # try: 
    #     ActionChains(game_driver).key_down(Keys.LEFT).key_up(Keys.LEFT).perform()
    #     time.sleep(0.2)
    #     ActionChains(game_driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    # except Exception :
    #     pass

    # pyautogui.click(21, 21)
    # time.sleep(1)
    # # 叫出書籤欄
    # pyautogui.hotkey("ctrl","shift","b")
    # time.sleep(1)

    with open("./url.txt", "r", encoding='UTF-8') as url :
        # game_driver.get("")
        game_driver.get(url.readline())
        time.sleep(10)


    time.sleep(30)
    # # 音量
    # click(1872, 163)
    # time.sleep(2)

    # drag(817, 448, 687, 448)
    # drag(1129, 586, 742, 593)

    # click(1554, 238)

    # game_driver.refresh()
    # time.sleep(10)

    # # 開房間
    # click(1194, 437)
    # time.sleep(0.5)
    # click(1247, 427)
    # # click(1630, 424)
    # time.sleep(0.5)

    ISOTIMEFORMAT = '%Y_%m_%d_%H_%M_%S'

    # while True :
    #     this_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #     path = './pic'+ str(exec_id)
    #     if not os.path.isdir(path):
    #         os.mkdir(path)

    #     game_driver.get_screenshot_as_file('./pic'+ str(exec_id)+'/' + this_time+'_1start.png')

    #     for x in range(0) :
    #         click(1618, 966)
    #         time.sleep(2)
        
    #     game_driver.get_screenshot_as_file('./pic'+ str(exec_id)+'/' + this_time+'_2end.png')
    #     click(956, 511)
    #     time.sleep(10)
