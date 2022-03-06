import pythoncom
import pyautogui
import time
import random
import numpy as np
import cv2



pyautogui.screenshot('D:\\python_code\\14_background\\new_cut.PNG',region=(790, 786, 121, 53))

img_cut = cv2.imread("D:\\python_code\\14_background\\new_cut.PNG")
img_cut = cv2.calcHist([img_cut], [0], None, [256], [0, 256]) 
img_cut = cv2.normalize(img_cut, img_cut, 0, 1, cv2.NORM_MINMAX, -1) 


img = cv2.imread('D:\\python_code\\14_background\\win.PNG')
img = cv2.calcHist([img], [0], None, [256], [0, 256]) 
img = cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX, -1) 
print(cv2.compareHist(img_cut, img, 0))

img = cv2.imread('D:\\python_code\\14_background\\not_win.PNG')
img = cv2.calcHist([img], [0], None, [256], [0, 256]) 
img = cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX, -1) 
print(cv2.compareHist(img_cut, img, 0))

img = cv2.imread('D:\\python_code\\14_background\\during.PNG')
img = cv2.calcHist([img], [0], None, [256], [0, 256]) 
img = cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX, -1) 
print(cv2.compareHist(img_cut, img, 0))


