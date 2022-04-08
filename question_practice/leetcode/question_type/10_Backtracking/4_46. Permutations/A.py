# my Runtime: 40 ms, faster than 93.08% of Python3
class Solution:
    def permute(self, nums):
        ans = []
        
        def rec(mem, remain):
            if len(remain) == 0:
                ans.append(mem)
                return 
            
            for indx, num in enumerate(remain):
                if indx == len(remain)-1 :
                    rec(mem+[num], remain[:indx])
                else :
                    rec(mem+[num], remain[:indx]+remain[indx+1:])
          
        rec([], nums)
        return ans

# given ans
# 是用 used 記錄此位置有沒有用過
# 退回來的時候 再改成沒有用過
# class Solution:
#     def permute(self, nums):
#         ans = []
#         used = [False] * len(nums)

#         def dfs(path):
#             if len(path) == len(nums):
#                 ans.append(path.copy())
#                 return

#             for i, num in enumerate(nums):
#                 if used[i]:
#                     continue
#                 used[i] = True
#                 path.append(num)
#                 dfs(path)
#                 path.pop()
#                 used[i] = False

#         dfs([])
#         return ans

s = Solution()
print(s.permute(nums = [1,2,3]))



