import numpy as np
import time

# 結論
# 只要有需要位置 就要用 np.unravel_index(np.argmax(long_array),long_array.shape)
# 如果只需要 最大值就用 np.max(long_array)

# long_array = np.arange(start = 1,stop = 1000000000, step = 1, dtype=int)
# long_array = np.arange(start = 1000000000,stop = 1, step = -1, dtype=int)
# long_array = np.random.rand(1000000000)
long_array = np.random.randint(1,1000000,(1000000000))

# long_array[0] = 2000000000 # 開頭就很大
long_array[-1] = 2000000000 # 最後才是答案

# 如果是求最大值 
# << max = np.max(long_array) 比較快 >>
start = time.time()
pos = np.unravel_index(np.argmax(long_array),long_array.shape)
end = time.time()
print("max : ", long_array[pos[0]])
print(end - start) # 0.502655029296875

start = time.time()
max = np.max(long_array)
end = time.time()
print("max : ", max)
print(end - start) # 0.36103367805480957

# 如果是求最大值的位置
# << np.unravel_index(np.argmax(long_array),long_array.shape) 比較快 >>

start = time.time()
pos = np.unravel_index(np.argmax(long_array),long_array.shape)
end = time.time()
print("pos : ", pos)
print(end - start) # 0.5216042995452881

start = time.time()
pos = np.where(long_array==np.max(long_array))
end = time.time()
print("pos : ", pos)
print(end - start) # 1.266610860824585

start = time.time()
max = np.max(long_array)
pos = np.where(long_array==max)
end = time.time()
print("pos : ", pos)
print(end - start) # 1.305506944656372