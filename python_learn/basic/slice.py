# 只取中間部分的 class : slice

ll = list(range(10))

# slice(起始, 終點, 間隔)
sl = slice(2, 5)
print(ll[sl])
sl = slice(1, 8, 3)
print(ll[sl])

# 印出裡面的變數
print("start :",sl.start)
print("stop :",sl.stop)
print("step :",sl.step)

