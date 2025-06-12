# map(function, iterable, ...)
# 將 function 執行在 一個或多個可迭代物件的每一個元素
    # return map 的 iterator (所以不可直接 ret[1] 取值)

# 所以其實全部都能用 for 取代
# 但是有時使用 map 更精簡
# 且 map 不會全部執行，所以較省記憶體

# Ex: 轉型
# 將 str函數 應用於 nums List 上 > 把每個 item 變成 str
nums = [1,3,5]
print(list( map(str, nums) ))
print(list( str(x) for x in nums ))

# Ex: 數值運算
# 把每個數字平方
nums = [1,3,5]
print(list( map(lambda x: x**2, nums) ))
print(list( n**2 for n in nums ))

# Ex: 處理兩個 iterable array
# 將兩個陣列數值相加
import operator
l1 = [1,3,5]
l2 = [2,4,6]
print(list( map(operator.add, l1, l2) ))
print(list( x+y for x,y in zip(l1,l2) ))

# # 若數量不相符 則會跳 TypeError
# l1 = [1,3,5]
# l2 = [2,4,6]
# print(list( map(lambda x: x**2, l1, l2) ))
# print(list( map(lambda x,y,z: x+y+z, l1, l2) ))
