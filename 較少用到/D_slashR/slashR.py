# 這裡的範例是為了測試 /r 的效果
############################################################
import time
import threading

class Identify_money_thread (threading.Thread):   #继承父类threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        for x in range(100):
            print(x)
            time.sleep(1)


identify_money_thread = Identify_money_thread()
identify_money_thread.start()

print("")
for x in range(100):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX", end="\r")
    time.sleep(1)
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO", end="\r")
    time.sleep(1)
print("")
print("end")

#####################################################
# print("AAA")
# time.sleep(2)
# print("\r","BBB",end="",flush=True)
