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

game_driver = None
use_sel = 1
strech_size = 1

def open_web():
    global game_driver
    
    webdriver_path = './chromedriver.exe'
    options = Options()

    options.add_argument("--window-size=1936,1056")

    options.add_argument('disable-infobars')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation']) 
    prefs = {"":""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option("prefs", prefs)

    game_driver = webdriver.Chrome(executable_path=webdriver_path, options=options) 

    pyautogui.hotkey("ctrl","shift","b")
    time.sleep(1)

    if use_sel == 0 or strech_size == 1:
        game_driver.maximize_window()
        print(game_driver.get_window_size())
    elif use_sel == 1 :
        bookmark_height = 110
        width = (1936/strech_size)
        height = (1056-bookmark_height)/strech_size+bookmark_height
        print("width : " + str(width)+" height : " + str(height))
        game_driver.set_window_size(width,height)
    else :
        print("error!!!")

    # pyautogui.click(21, 21)
    # time.sleep(1)
    # 叫出書籤欄
    

def click(x,y):
    if use_sel == 0 :
        pyautogui.click(x, y)
    else :
        y = y - 100

        # x = x/((strech_size-1)*1.03+1)
        # y = y/((strech_size-1)*1.03+1)
        x = x/strech_size
        y = y/strech_size
        
        # print("x : "+str(x)+" y : "+str(y))
        ActionChains(game_driver).move_by_offset(x, y).click().perform()
        ActionChains(game_driver).move_by_offset(-x, -y).perform()
        # print("click_sel")

def drag(x1,y1,x2,y2):
    if use_sel == 0 :
        pyautogui.mouseDown(x1,y1)
        pyautogui.moveTo(x2,y2, 0.5)
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(0.5)

save_loc = "C:\\C_record\\for_auto_click2\\"
ISOTIMEFORMAT = '%Y_%m_%d_%H_%M_%S'

if __name__=="__main__": 
    num = 1
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", dest='id', default=0, help="player_id")
    args = parser.parse_args()
    exec_id = args.id
    print("exec_id : " +str(exec_id))

    # if use_sel == 1 :
    open_web()
    with open("./url.txt", "r", encoding='UTF-8') as url_f :
        game_driver.get(url_f.readline())
    
    input("等待設定完成後 按 enter")

    while True :
        click(350,184)
        time.sleep(1)
        click(385,958)
        time.sleep(1)
        click(1536,959)
        time.sleep(1)


  