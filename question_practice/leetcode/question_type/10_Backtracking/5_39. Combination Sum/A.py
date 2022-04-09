# my Runtime: 97 ms, faster than 65.76% of Python3
class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def rec(indx, remain, mem):
            if remain < 0:
                return 
            elif remain == 0:
                ans.append(mem)
                return 
            
            for ind, i in enumerate(candidates[indx:]):
                rec(indx+ind, remain-i, mem+[i])
                
        rec(0, target, [])
        return ans

# given ans
# 我每次 recursive 都是創建一個新的空間 (就不用再pop)
# given ans 通常都是用同一個空間
# 各有優缺點八
# class Solution:
#     def combinationSum(self, candidates, target):
#         ans = []

#         def dfs(s, target, path):
#             if target < 0:
#                 return
#             if target == 0:
#                 ans.append(path.copy())
#                 return

#             for i in range(s, len(candidates)):
#                 path.append(candidates[i])
#                 dfs(i, target - candidates[i], path)
#                 path.pop()

#         candidates.sort()
#         dfs(0, target, [])
#         return ans

s = Solution()
print(s.combinationSum(candidates = [2,3,5], target = 8))
print(s.combinationSum(candidates = [2,3,6,7], target = 7))


