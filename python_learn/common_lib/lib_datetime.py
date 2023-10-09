# 時間格式 https://www.geeksforgeeks.org/python-strftime-function/

import datetime as datetimeLib

# timeformat # time string 
from datetime import datetime,timezone,timedelta
import pytz  # 時區 / timezone
# 1. 查詢各時區名稱 https://www.jianshu.com/p/a211e3494524
    # san francisco : "America/Los_Angeles"
    # Taiwan : "Asia/Taipei"
# 2. 使用國家查詢
# print(pytz.country_timezones("us"))
        
# # 取得現在時間
now = datetime.now()
print("Without formatting :", now)

# # 印出各個屬性
# print("年 :",now.year)
# print("月 :",now.month)
# print("日 :",now.day)
# print("時 :",now.hour)
# print("分 :",now.minute)
# print("秒 :",now.second)
# print("星期 :",now.weekday()) # int
# # print(dir(now))

#----------------------------------------------- 
# # 時間轉字串
# s = now.strftime("%a %m %y")
# print('\nExample 1:', s)

# s = now.strftime("%A %#m %Y")  # windows
# # s = now.strftime("%A %-m %Y")  # else
# print('\nExample 2:', s)

#-----------------------------------------------
# # 字串轉時間
# time = datetime.strptime("7.5.2022 14:44", "%d.%m.%Y %H:%M")
# print(time)
# time = datetime.strptime("07.05.2022 14:44", "%d.%m.%Y %H:%M")
# print(time)

#-----------------------------------------------
# # 時間加上一天
# print("bef add time : ", now)
# add_time = now + timedelta(days=1)
# print("aft add time : ", add_time)

#-----------------------------------------------
# # 時間相差秒數
# def time_delta(t1, t2):
#     # print(t1, t2)
#     t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")  # 時間格式 Sat 02 May 2015 19:54:36 +0530
#     t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
#     timedelta = t1-t2
#     return abs(int(timedelta.total_seconds()))

# print(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
# # print(time_delta("Fri 01 May 2015 13:54:36 -0000", "Sat 02 May 2015 19:54:36 +0530")) # 交換位置

#-----------------------------------------------
# # 計算紀念日天數
# anniversary = datetime.strptime("2023 03 08 20:00:00", "%Y %m %d %H:%M:%S")  # 這個日期格式不要加上時區
# anniversary_days = (datetime.now() - anniversary).days + 1
# print("第",anniversary_days,"天")

#-----------------------------------------------
# # timezone
# # timezone 只能用名稱指定一個時區，就是 +00:00 的時區
# tzinfo = timezone.utc
# print("tzinfo :",tzinfo)
# # 其他都是用 UTC 去表示
# tzinfo = timezone(timedelta(hours=8))
# print("tzinfo :",tzinfo)

# # 目前想到最好的方法是 ??
# time_zone_num = datetime.now(pytz.timezone("America/Los_Angeles"))
# print(time_zone_num)
# #-----------------------------------------------
# # 時區處理(指定時區)
# dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
# dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區: +8 的時區
# print("時區處理 :",dt2.hour)

# # 時區處理(使用地區)
# print(pytz.timezone("America/Los_Angeles"))
# print("舊金山 : ", datetime.now(pytz.timezone("America/Los_Angeles")))
# print("台灣   : ", datetime.now(pytz.timezone("Asia/Taipei")))

# # 常遇到的 error
# # TypeError: can't subtract offset-naive and offset-aware datetimes
#     # 這代表一個時間有時區 一個沒有 不能相減
# # EX:
# t1 = datetime.strptime("Sat 02 May 2015 19:54:36 +0530", "%a %d %b %Y %H:%M:%S %z")  # 時間格式 Sat 02 May 2015 19:54:36 +0530
# t2 = datetime.strptime("Sat 02 May 2015 19:55:36"      , "%a %d %b %Y %H:%M:%S")
# timedelta = t1-t2

