import numpy as np

# #------------------------------------
# # 初始化 方法1 全部都是0
# array = np.zeros( shape = (3, 5) , dtype=int ) 
#     # shape = (column, row)
#     # dtype : float int
# print(array)
# 初始化 方法2 類似range
array = np.arange(12, dtype=int)
    # np.arange(start = 3,stop = 10, step = 2, dtype=int)
print("original :",array)
# 初始化 方法3 list 轉型
array = np.array([[1,3,2],[8,5,7]])
print(array)

# < 可察看的屬性 >
# 查看形狀
# print(array.shape)
# # 查看有幾個維度
# print(array.ndim)
# # 查看是什麼型態
# print(array.dtype)
# # 不要省略中間項目 or 印出完整資料
# 取消印出長度限制
np.set_printoptions(threshold=np.inf)

# # 轉換型別
# # 但是 大轉小會出問題 EX int32 轉 int16
# new_array = array.astype("float16")
# print("float16 :",new_array)

# 找出最大值
print("max :",np.max(array))
# 找出某個項目的位置
print("where :",np.where(array==8))

# # << 較不常用到 >>
# # < 百分位數 percentile >
#     # 求數列中 第 X%分位 的數值
# # 不管前面的 list 丟進去有沒有按照順序 都沒差
# # 101 個點 , 共有 100 個區間 
# print(np.percentile(range(101),90))
# print(np.percentile(range(100,201),90))   # 不管前面的 list 丟進去有沒有按照順序 都沒差 1
# print(np.percentile(range(200,99,-1),90)) # 不管前面的 list 丟進去有沒有按照順序 都沒差 1
# print("([1,2,3,4],25) :",np.percentile([1,2,3,4],25))
# print("([1,2,2,4],50) :",np.percentile([1,2,2,4],50))
# print("([1,2,2,4],40) :",np.percentile([1,2,2,4],40))
# print("([4,2,2,4],50) :",np.percentile([4,2,2,4],50))  # 不管前面的 list 丟進去有沒有按照順序 都沒差 2
# print("([2,2,4,4],50) :",np.percentile([2,2,4,4],50))  # 不管前面的 list 丟進去有沒有按照順序 都沒差 2
# print("([2,4],50) :",np.percentile([2,4],50))

# # < 是否為純量 scalar >
# # isscalar
# # 不具方向性的物理量
# print("isscalar(1) :",np.isscalar(1))  # True
# print("isscalar([1,3,4,5]) :",np.isscalar([1,3,4,5])) # False
# print("isscalar([1]) :",np.isscalar([1])) # False
# print("isscalar(1.5) :",np.isscalar(1.5)) # True
# print("isscalar(-1) :",np.isscalar(-1)) # True

# # < 限制資料的大小 >
# # clip
# # 如果大/小於規定的數字 則會變成規定的數字
# ll = np.array([5,3,2,1,4,8,6,7,9])
# print("bef clip :",ll)
# print("aft clip :",np.clip(ll,3,7))


