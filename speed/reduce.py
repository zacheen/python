# reduce
    # 使用 operator : 比較快
    # 使用 lambda   : 比較慢

import time
from functools import reduce
import operator
ll = list(range(10000000))

start = time.time()
print(reduce(operator.add,ll))
end = time.time()
print("operator :",end - start) # 0.42

start = time.time()
print(reduce(lambda x,y: x+y,ll))
end = time.time()
print("lambda   :",end - start) # 0.74