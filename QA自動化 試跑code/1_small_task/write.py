""" write in word """

import random
import datetime
import time

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'

# 注意在這裡是寫入 但另外一個py是讀取
write_dst = "D:\\dont_move\\num_text.txt"

with open(write_dst, "a") as write_dst_f:
    # while(True) :
    for xx in range(1000) :
        num_list = []
        for x in range(5) :
            num_list.append(random.randint(10,99))
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        num_list.append(theTime)
        write_dst_f.write(str(num_list)[1:-1]+"\n")
        # write_dst_f.flush()
        # time.sleep(0.5)