import os
# os.system('python 要多開的程式.py')

import threading
import time

total = 0
class My_thread (threading.Thread):   #繼承父類threading.Thread
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self): #把要執行的代碼寫到run函數里面 線程在創建後會直接運行run函數     
        global total
        while True :
            total += 1
            print("this is Thread", self.id, ", now total :",total)
            time.sleep(3)

for x in range(3):
    open_web_thread = My_thread(x)
    open_web_thread.start()
    time.sleep(1)
