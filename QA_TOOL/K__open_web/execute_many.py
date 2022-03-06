import os
# os.system('python 要多開的程式.py')

import threading
import time

# filename = "open_web.py"
# with open(filename, "rb") as source_file :
#     code = compile(source_file.read(), filename, "exec")

print("open many web")

id_count = 50

class Open_web_thread (threading.Thread):   #继承父类threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数     
        global id_count
        print("open website")
        # !python FKNN_selenium.py
        # exec(code)
        id_count = id_count+1
        os.system('python open_web_flag.py -id '+str(id_count))
        

for x in range(1):
    open_web_thread = Open_web_thread()
    open_web_thread.start()
    time.sleep(5)
