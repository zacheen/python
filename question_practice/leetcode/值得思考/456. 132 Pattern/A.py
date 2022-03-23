# 思考 : 有時候換方向做 反而比較簡單

# 找出有沒有任何 subsequence 第一個 < 第三個 < 第二個
# My v1 Time Limit Exceeded
# class Solution:
#     def find132pattern(self, nums):
#         # 紀錄所有最好的區間 (如果可以合併就合併)
#         first = []
#         third = []

#         def check_in_his(num):
#             for i in range(len(first)) :
#                 if first[i] < num and num < third[i] :
#                     return True
#             return False

#         indx = 1
#         now_first = nums[0]
#         now_third = nums[0]
#         for indx in range(1,len(nums)) :
#             print(now_first, now_third)
#             if nums[indx] >= now_third :
#                 # 更新 now_third
#                 now_third = nums[indx]
#             elif nums[indx] < now_first :
#                 # 把 now_first now_third 儲存
#                 if now_first < now_third :
#                     first.append(now_first)
#                     third.append(now_third)
#                 now_first = nums[indx]
#                 now_third = nums[indx]
#             elif nums[indx] == now_first :
#                 pass
#             else :
#                 return True

#             # 檢查有沒有在 mem 區間
#             if check_in_his(nums[indx]) :
#                 return True

#         return False

# My v2 
# Runtime: 2128 ms, faster than 5.00% of Python3
# class Solution:
#     def find132pattern(self, nums):
#         # 紀錄所有最好的區間 (如果可以合併就合併)
#         first = []
#         third = []

#         def check_in_his(num):
#             for i in range(len(first)) :
#                 if first[i] < num and num < third[i] :
#                     return True
#             return False

#         indx = 1
#         now_first = nums[0]
#         now_third = nums[0]
#         for indx in range(1,len(nums)) :
#             # print(now_first, now_third)
            
#             if nums[indx] >= now_third :
#                 # 更新 now_third
#                 now_third = nums[indx]
#             elif nums[indx] < now_first :
#                 # 把 now_first now_third 儲存
#                 if now_first < now_third :
#                     # 去除包含的區間 新的區段只有可能包含舊的 不可能某段重疊 -> 不需要用max 
#                     for ii in range(len(first)-1 , -1, -1) :
#                         if now_third > first[ii] :
#                             # print("刪除 : ",first[ii],third[ii])
#                             del(first[ii])
#                             del(third[ii])
#                     # 每次都加新的 
#                     first.append(now_first)
#                     third.append(now_third)
#                 now_first = nums[indx]
#                 now_third = nums[indx]
#             elif nums[indx] == now_first :
#                 pass
#             else :
#                 return True

#             # 檢查有沒有在 mem 區間
#             if check_in_his(nums[indx]) :
#                 return True

#             # print(first, third)

#         return False

# v3 增加了 提早 return 的地方 速度差不多
# Runtime: 2502 ms, faster than 5.00% of Python3
# class Solution:
#     def find132pattern(self, nums):
#         # 紀錄所有最好的區間 (如果可以合併就合併)
#         first = []
#         third = []

#         def check_in_his(num):
#             for i in range(len(first)) :
#                 if first[i] < num and num < third[i] :
#                     return True
#                 # elif num < first[i] : # 如果從後面開始判斷
#                 #     return False
#                 elif num > third[i] :
#                     return False
#             return False

#         indx = 1
#         now_first = nums[0]
#         now_third = nums[0]
#         for indx in range(1,len(nums)) :
#             # print(now_first, now_third)
            
#             if nums[indx] >= now_third :
#                 # 更新 now_third
#                 now_third = nums[indx]
#             elif nums[indx] < now_first :
#                 # 把 now_first now_third 儲存
#                 if now_first < now_third :
#                     # 去除包含的區間 新的區段只有可能包含舊的 不可能某段重疊 -> 不需要用max 
#                     for ii in range(len(first)-1 , -1, -1) :
#                         if now_third > first[ii] :
#                             # print("刪除 : ",first[ii],third[ii])
#                             del(first[ii])
#                             del(third[ii])
#                         else :
#                             break
#                     # 每次都加新的 
#                     first.append(now_first)
#                     third.append(now_third)
#                 now_first = nums[indx]
#                 now_third = nums[indx]
#             elif nums[indx] == now_first :
#                 pass
#             else :
#                 return True

#             # 檢查有沒有在 mem 區間
#             if check_in_his(nums[indx]) :
#                 return True

#             # print(first, third)

#         return False

# given ans Runtime: 434 ms, faster than 61.62% of Python3
# 我剛剛是要找中間的點
# 它反方向來看 先找到有無 儲存second > third 儲存third
# 在判斷有沒有點 在third之下
class Solution:
    def find132pattern(self, nums):
        stack = [] # max stack
        ak = -1000000001  # we want to find a seq ai < ak < aj

        for i in range (len(nums)-1, -1, -1) :
            # 有 ak 代表之前已經找到 上升的點了 所以小於ak就有答案
            if nums[i] < ak : 
                return True
            # 如果 此點 > stack中最大的點
            # 目標是找到 最大的 ak
            while stack and stack[-1] < nums[i] :
                ak = stack.pop()
        
            stack.append(nums[i]) # stack 裡面是存 ak 的候選數字 # 只是由於目前沒有找到比 此數更大的數字

        return False

s = Solution()
# print(s.find132pattern([1,4,0,5,-1]))
# print(s.find132pattern([1,4,0,3,-1]))
# print(s.find132pattern([1,4,-10,-5,-11]))
# print(s.find132pattern([3,1,4,0,5,-1,6,-10,7,-11]))
print(s.find132pattern([42,43,6,12,3,4,6,11,20]))
