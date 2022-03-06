import pythoncom
import pyautogui
import time
import random
import numpy as np
import cv2

# 之後再找方法直接轉
pyautogui.screenshot('D:\\python_code\\12_compare_pic\\cut2.PNG',region=(965, 762, 42, 47)) 
print("cut")

img_cut = []
img_cut.append(cv2.imread("D:\\python_code\\12_compare_pic\\cut.PNG"))
img_cut.append(cv2.imread("D:\\python_code\\12_compare_pic\\cut2.PNG"))

for x in range(len(img_cut)):
    img_cut[x] = cv2.calcHist([img_cut[x]], [0], None, [256], [0, 256]) 
    img_cut[x] = cv2.normalize(img_cut[x], img_cut[x], 0, 1, cv2.NORM_MINMAX, -1) 

print(cv2.compareHist(img_cut[0], img_cut[1], 0))
