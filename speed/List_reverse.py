# 一個項目一個項目加進來 但是後面加入的要放在前面
# 結論 :
    # 用 append 先加在後面，再整個 reverse 比較快
import time
ll1 = []
ll2 = []

# 加在後面 比較快
start = time.time()
for i in range(200000) :
    ll1.append(i)
ll1.reverse()
end = time.time()
print("reverse :",end - start)

start = time.time()
for i in range(200000) :
    ll2.insert(0,i)
end = time.time()
print("insert 0 :",end - start)
