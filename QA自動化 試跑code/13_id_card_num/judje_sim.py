import pythoncom
import pyautogui
import time
import random
import numpy as np
import cv2

pyautogui.screenshot('D:\\python_code\\13_id_card_num\\new_cut.PNG',region=(965, 762, 42, 47)) 
img_cut = cv2.imread("D:\\python_code\\13_id_card_num\\new_cut.PNG")
img_cut = cv2.calcHist([img_cut], [0], None, [256], [0, 256]) 
img_cut = cv2.normalize(img_cut, img_cut, 0, 1, cv2.NORM_MINMAX, -1) 

def num_to_card(num) :
    if num == 1:
        return 'a'
    elif num == 11:
        return 'j'
    elif num == 12:
        return 'q'
    elif num == 13:
        return 'k'
    else:
        return str(num)

max_sim = 0
sim_num = 0

for x in range(13):
    img = cv2.imread('D:\\python_code\\13_id_card_num\\b'+ num_to_card(x+1)+'.PNG')
    img = cv2.calcHist([img], [0], None, [256], [0, 256]) 
    img = cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX, -1) 
    sim = cv2.compareHist(img_cut, img, 0)
    print(num_to_card(x+1) + "b : " + str(sim))
    if sim > max_sim:
        max_sim = sim
        sim_num = num_to_card(x+1) + "b"


    img = cv2.imread('D:\\python_code\\13_id_card_num\\r'+ num_to_card(x+1)+'.PNG')
    img = cv2.calcHist([img], [0], None, [256], [0, 256]) 
    img = cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX, -1) 
    sim = cv2.compareHist(img_cut, img, 0)
    print(num_to_card(x+1) + "r : " + str(sim))
    if sim > max_sim:
        max_sim = sim
        sim_num = num_to_card(x+1) + "r"

print(max_sim)
print(sim_num)
