from collections import Counter

# my v1 Runtime: 334 ms, faster than 5.07% of Python3
# class Solution:
#     def combinationSum2(self, candidates, target):
#         count = Counter(candidates)
#         count_key = list(count.keys())
#         count_key.sort()
#         # print(count_key)
        
#         ans = []
#         def rec(indx, mem, remain, target):
#             if target < 0:
#                 return 
#             elif target == 0:
#                 ans.append(mem)
#                 return 
            
#             for ind in range(indx, len(count_key)):
#                 now_num = count_key[ind]
#                 if remain[now_num] > 0 :
#                     pass_in_c = remain.copy()
#                     pass_in_c[now_num] -= 1
#                     rec(ind, mem+[now_num], pass_in_c, target-now_num)
          
#         rec(0, [], count, target)
#         return ans


# v1 太慢了
# my v2 試著用同一個空間
# 改 Counter  Runtime: 108 156
# 再改list    Runtime: 129 112 96
# final version : Runtime: 70 ms, faster than 78.69% of Python3
class Solution:
    def combinationSum2(self, candidates, target):
        count = Counter(candidates)
        count_key = list(count.keys())
        # count_key.sort() # 發現keys不用sort
        
        ans = []
        def rec(indx, mem, remain, target):
            if target < 0:
                return 
            elif target == 0:
                ans.append(mem.copy())
                return 
            
            for ind in range(indx, len(count_key)):
                now_num = count_key[ind]
                if remain[now_num] > 0 :
                    remain[now_num] -= 1
                    mem.append(now_num)
                    rec(ind, mem, remain, target-now_num)
                    remain[now_num] += 1
                    mem.pop()
          
        rec(0, [], count, target)
        return ans

# given ans
# 有用到 sort 應該會比較慢


s = Solution()
print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))


