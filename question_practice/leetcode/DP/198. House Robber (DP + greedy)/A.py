# My Runtime: 50 ms, faster than 38.57% of Python3
# class Solution:
#     def rob(self, nums):
        
#         # 從最後一個位置到現在位置 最多的可能拿多少錢
#         cache = {}
#         houseNum = len(nums)
#         cache[houseNum-1] = nums[houseNum-1]
#         if houseNum > 1 :
#             cache[houseNum-2] = nums[houseNum-2]
#         else :
#             return nums[0]
        

#         def search(pos): 
#             # print(cache)
#             his = cache.get(pos, None)
#             if his != None :
#                 # print("有找到紀錄")
#                 return his
            

#             maxCanRob = 0
#             for i in range(pos+2,houseNum) :
#                 # print("search(i) i :",i)
#                 canrob = nums[pos] + search(i)
#                 if canrob > maxCanRob :
#                     maxCanRob = canrob

#             # print("寫紀錄 pos,maxCanRob",pos,maxCanRob)
#             cache[pos] = maxCanRob
#             return maxCanRob
            
#         # 這個不能再和進去嗎?
#         from_first = search(0)
#         from_second = search(1)
#         return max(from_first, from_second)

# given ans
# 又拆成更小的問題 (就看前面兩個點的總和哪個比較高 決定要從哪裡走)
class Solution:
    def rob(self, nums):
        prev1 = 0  # dp[i - 1] # 一個點之前最好的結果
        prev2 = 0  # dp[i - 2] # 兩個點之前最好的結果

        for num in nums:
            dp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = dp
            print(prev1, prev2)

        return prev1


s = Solution()
# print(s.rob([1,2,3]))
# print(s.rob([1,1,1,2,7,9,3,1]))
# print(s.rob([100,90,80,100,70,60,100,110]))
print(s.rob([100,1,2,100,3,4,100,5]))
# print(s.rob([0,0,0,0,0,0,0,0,0]))
# print(s.rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))