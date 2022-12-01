# 時間格式 https://www.geeksforgeeks.org/python-strftime-function/

# timeformat # time string 
from datetime import datetime

now = datetime.now()
print("Without formatting", now)

#----------------------------------------------- 
# # 時間轉字串
# s = now.strftime("%a %m %y")
# print('\nExample 1:', s)

# s = now.strftime("%A %#m %Y")  # windows
# # s = now.strftime("%A %-m %Y")  # else
# print('\nExample 2:', s)

#-----------------------------------------------
# # 字串轉時間
time = datetime.strptime("7.5.2022 14:44", "%d.%m.%Y %H:%M")
print(time)
time = datetime.strptime("07.05.2022 14:44", "%d.%m.%Y %H:%M")
print(time)

#-----------------------------------------------
# # 時間相差秒數
def time_delta(t1, t2):
    # print(t1, t2)
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")  # 時間格式 Sat 02 May 2015 19:54:36 +0530
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    timedelta = t1-t2
    return abs(int(timedelta.total_seconds()))

print(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
# print(time_delta("Fri 01 May 2015 13:54:36 -0000", "Sat 02 May 2015 19:54:36 +0530")) # 交換位置