# recursionlimit / recursion depth
# 有時候 recursion 會超過預設的限制

# 設定 : sys.setrecursionlimit(100000)

import sys
depth_limit = sys.getrecursionlimit()
print("depth_limit :",depth_limit)

def recur_f(n, ori_num):
    if n == 1:
        print("recur depth", ori_num, "successfully")
        return
    return recur_f(n-1, ori_num)

# 不能剛好 depth_limit, exception 會提早跳出
recur_f(depth_limit-10, depth_limit-10)

try :
    recur_f(depth_limit+10, depth_limit+10)
except RecursionError :
    print("RecursionError")

# 設定
sys.setrecursionlimit(100000)
recur_f(90000, 90000)