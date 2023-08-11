import time

## 測試用 function ##########################################
finish_flag = False
# 印出執行了 & set flag
def print_str():
    print("execute function")
    global finish_flag
    finish_flag = True

# wait 直到 flag set
def wait_execute():
    while(not finish_flag) :
        time.sleep(5)
    print("finish_flag == True")

## apscheduler ##########################################
# < 到指定時間點執行 >
finish_flag = False
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler(timezone="Asia/Taipei")
    # timezone 可看 pytz 的時區
# scheduler.add_job(print_str, 'cron', day_of_week='0-3', hour=4, minute=0) # 只有禮拜一到四
scheduler.add_job(print_str, 'cron', hour=19, minute=52) # 每天執行
scheduler.start()
wait_execute()



