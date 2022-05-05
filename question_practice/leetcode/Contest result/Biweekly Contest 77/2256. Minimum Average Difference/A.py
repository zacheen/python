# my 
# class Solution:
#     def minimumAverageDifference(self, nums: List[int]):
#         s = sum(nums)
        
#         now_total = 0
#         mini = math.inf
#         mini_indx = 0
#         for i, n in enumerate(nums) :
#             now_total += n
#             sub = s - now_total
            
#             front = now_total//(i+1)
#             if i == len(nums)-1 :
#                 # print("end:",abs(front))
#                 if front < mini :
#                     mini_indx = i
#                 break
            
#             back = sub//(len(nums)-(i+1))
            
#             # print(abs(front-back))
#             cal = abs(front-back)
#             if cal < mini :
#                 mini = cal
#                 mini_indx = i
            
#         return mini_indx

# given ans 概念一樣
# 但中間判斷有優化
# Runtime: 1092 ms, faster than 84.16% of Python3
class Solution:
    def minimumAverageDifference(self, nums: List[int]):
        s = sum(nums)
        
        now_total = 0
        mini = math.inf
        mini_indx = 0
        for i, n in enumerate(nums) :
            now_total += n
            sub = s - now_total
            
            front = now_total//(i+1)
            # 原本--------------------------
            # if i == len(nums)-1 :
            #     # print("end:",abs(front))
            #     if front < mini :
            #         mini_indx = i
            #     break
            # back = sub//(len(nums)-(i+1))
            # --------------------------

            # 優化--------------------------
            if i == len(nums)-1 :
                back = 0
            else :
                back = sub//(len(nums)-(i+1))
            # --------------------------
            
            # print(abs(front-back))
            cal = abs(front-back)
            if cal < mini :
                mini = cal
                mini_indx = i
            
        return mini_indx






