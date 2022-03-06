import pyautogui
import time
import random



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

# for x in range(13):
#     print(num_to_card(x+1))

def find_num(this_region):
    number = None
    total = 0
    for x in range(13):
        place = pyautogui.locateCenterOnScreen('D:\\python_code\\9_test_card\\b'+ num_to_card(x+1)+'.PNG', region = this_region, confidence=0.95)
        if place != None :
            print(x+1)
            total = total +1
            number = num_to_card(x+1)
        # print('D:\\python_code\\9_test_card\\r'+ num_to_card(x+1)+'.PNG')
        place = pyautogui.locateCenterOnScreen('D:\\python_code\\9_test_card\\r'+ num_to_card(x+1)+'.PNG', region = this_region, confidence=0.95)
        if place != None :
            print(x+1)
            total = total +1
            number = num_to_card(x+1)
    
    if total != 1:
        print("find_num error!!!!!!!!!!!!!!!!!! find :" +str(total))
    return number


# numb1 = 0
# sui1 = ""
# numb1 = 0
# sui1 = ""

suits_name = ["spad", "heart", "diamond", "club"]
suit_chinese = {"spad":"黑桃" , "heart" : "愛心", "diamond" : "菱形", "club" : "梅花"}
def find_suits(this_region):
    suits = None
    total = 0
    for x in range(4):
        place = pyautogui.locateCenterOnScreen('D:\\python_code\\9_test_card\\'+ suits_name[x] +'.PNG', region = this_region, confidence=0.95)
        if place != None :
            print(suit_chinese[suits_name[x]])
            suits = suits_name[x]
            total = total+1
    if total != 1:
        print("find_suits error!!!!!!!!!!!!!!!!!! find :" +str(total))
    return suits

while(True):
    region = (957, 751, 60, 93)
    sui = find_suits( region )
    if sui != None:
        num = find_num( region )


    region = (1023, 755, 56, 89)
    sui = find_suits( region )
    if sui != None:
        num = find_num( region )

    print("finsish")
    time.sleep(1)

print(place)
pyautogui.click(place)