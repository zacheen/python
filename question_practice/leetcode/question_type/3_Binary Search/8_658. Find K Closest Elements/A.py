import bisect
# My Runtime: 323 ms, faster than 79.02% of Python3 
# class Solution:
#     def findClosestElements(self, arr, k, x):
#         first_small = bisect.bisect_right(arr, x)-1
#         # print("first_small :",first_small)
#         if arr[first_small] != x :
#             # first_small右邊還有位置 或 右邊比較近
#             if first_small==len(arr)-1 :
#                 # 右邊沒位子了
#                 pass
#             elif first_small == -1 or abs((arr[first_small] - x)) > abs((arr[first_small+1] - x)) :
#                 first_small = first_small +1
#         # print("first_small :",first_small)
#         l = first_small-1
#         r = first_small+1
#         # print(l,r)

#         while k > 1 :  # 要扣除 first_small
#             k -= 1
#             # l在合理範圍 或 r超出範圍 或 l比較近
#             if r>=len(arr) or (l >= 0 and abs((arr[l] - x)) <= abs((arr[r] - x))) :
#                 l -= 1
#             else :
#                 r += 1
#             # print(l,r)
#         return arr[l+1:r]
        
# given ans 
# 好猛喔 他直接移動整個區間
# 條件是找到 l
    # 規則就看 左邊比較遠 還是 右邊比較遠 (左邊比較遠就往右移)
# 要注意的是 這裡的l跟r 不是指ans的l跟r
# 而是 ans的l有可能的位置 的 l跟r
class Solution:
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] <= arr[m + k] - x:  # 比較遠近的優化
                r = m
            else:
                l = m + 1

        return arr[l:l + k]

# 用比較直觀的規則也是可以達成目的的
# class Solution:
#     def findClosestElements(self, arr, k, x):
#         l = 0
#         r = len(arr) - k

#         while l < r:
#             m = (l + r) // 2
#             if abs(x - arr[m]) <= abs(x-arr[m + k]) :  # 比較遠近的優化
#                 r = m
#             else:
#                 l = m + 1

#         return arr[l:l + k]

    
s = Solution()
print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
print(s.findClosestElements(arr = [1,2,4,5], k = 2, x = 3))
print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))
print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 6))
print(s.findClosestElements(arr = [1,2,5,5,5,6,7], k = 3, x = 5))
print(s.findClosestElements(arr = [1,2,5,5,5,6,7], k = 4, x = 5))
print(s.findClosestElements(arr = [1,5,6,7], k = 2, x = 4))
print(s.findClosestElements(arr = [1,2,5,6,7], k = 2, x = 4))
