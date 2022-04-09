# 這題可以用 dp mem 解嗎?
# 為什麼可以 為什麼不行

# my Runtime: 36 ms, faster than 80.74% of Python3
# class Solution:
#     def combinationSum3(self, k, n):
#         ans = []
#         def rec(now_num, mem, target):
#             if target < 0 :
#                 return 
#             if len(mem) > k :
#                 return 
#             if target == 0 and len(mem) == k :
#                 ans.append(mem)
                
#             for i in range(now_num, 10):
#                 rec(i+1, mem + [i] , target - i)
                
#         rec(1, [], n)
#         return ans

# v2 Runtime: 28 ms, faster than 97.07% of Python3
class Solution:
    def combinationSum3(self, k, n):
        ans = []
        final_len = k-1
        def rec(now_num, mem, target):
            if len(mem) == final_len :
                if target <= 9 and target >= now_num:
                    ans.append(mem+[target])
            else :
                for i in range(now_num, 10):
                    rec(i+1, mem + [i] , target - i)
                
        rec(1, [], n)
        return ans

# given ans 方法一樣

s = Solution()
print(s.combinationSum3(k = 3, n = 9))  # [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
print(s.combinationSum3(k = 9, n = 45)) # [[1, 2, 3, 4, 5, 6, 7, 8, 9]]


