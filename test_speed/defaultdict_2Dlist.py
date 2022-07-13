# two_D                                 # ddict
    # two_D init: 2.4763736724853516        ddict init: 0.0
    # two_D add: 0.5704736709594727         ddict add: 2.5940656661987305
# two_D add again: 0.5664851665496826       ddict add again: 0.6482460498809814
    # two_D get: 0.38995790481567383        ddict get: 0.5435473918914795
    # total two_D : 4.003290414810181       total ddict : 3.7858591079711914

# 分界線
    # get set 共3次  
    # 只取一半項目

from collections import defaultdict
import time

number = 10000000
two_D_t = 0.0
ddict_t = 0.0

# 每個項目 ##############################################
# print(" 每個項目 -------------------")

# # 初始化
# start = time.time()
# two_D = [[] for _ in range(number)]
# end = time.time()
# print("two_D init:",end - start)
# two_D_t += (end - start)

# start = time.time()
# ddict = defaultdict(list)
# end = time.time()
# print("ddict init:",end - start)
# ddict_t += (end - start)

# # 加入項目
# start = time.time()
# for i in range(number) :
#     two_D[i].append(i)
# end = time.time()
# print("two_D add:",end - start)
# two_D_t += (end - start)

# start = time.time()
# for i in range(number) :
#     ddict[i].append(i)
# end = time.time()
# print("ddict add:",end - start)
# ddict_t += (end - start)

# # 取用項目
# start = time.time()
# for i in range(number) :
#     ret = two_D[i]
# end = time.time()
# print("two_D get:",end - start)
# two_D_t += (end - start)

# start = time.time()
# for i in range(number) :
#     ret = ddict[i]
# end = time.time()
# print("ddict get:",end - start)
# ddict_t += (end - start)

# print("total two_D :", two_D_t)
# print("total ddict :", ddict_t)


# 一半項目 ##############################################
print(" 一半項目 -------------------")
interval = 2

two_D_t = 0.0
ddict_t = 0.0

# 初始化
start = time.time()
two_D = [[] for _ in range(number)]
end = time.time()
print("two_D init:",end - start)
two_D_t += (end - start)

start = time.time()
ddict = defaultdict(list)
end = time.time()
print("ddict init:",end - start)
ddict_t += (end - start)

# 加入項目
start = time.time()
for i in range(0, number, interval) :
    two_D[i].append(i)
end = time.time()
print("two_D add:",end - start)
two_D_t += (end - start)

start = time.time()
for i in range(0, number, interval) :
    ddict[i].append(i)
end = time.time()
print("ddict add:",end - start)
ddict_t += (end - start)

# 加入項目 again
start = time.time()
for i in range(0, number, interval) :
    two_D[i].append(i)
end = time.time()
print("two_D add again:",end - start)
two_D_t += (end - start)

start = time.time()
for i in range(0, number, interval) :
    ddict[i].append(i)
end = time.time()
print("ddict add again:",end - start)
ddict_t += (end - start)

# 取用項目
start = time.time()
for i in range(0, number, interval) :
    ret = two_D[i]
end = time.time()
print("two_D get:",end - start)
two_D_t += (end - start)

start = time.time()
for i in range(0, number, interval) :
    ret = ddict[i]
end = time.time()
print("ddict get:",end - start)
ddict_t += (end - start)

print("total two_D :", two_D_t)
print("total ddict :", ddict_t)