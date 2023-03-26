# my Beats 41.25% 且 記憶體用很多
# from collections import defaultdict
# class Solution:
#     def largestDivisibleSubset(self, nums):
#         nums.sort()

#         link_mem = defaultdict(list)

#         for i in range(1,len(nums)) :
#             for j in range(i) :
#                 if nums[i] % nums[j] == 0 :
#                     link_mem[nums[i]].append(nums[j])
#         # print(link_mem)

#         @cache
#         def dfs(n):
#             max_len = 1 # 自己一點
#             max_path = [n]
#             for next_n in link_mem[n] :
#                 ret_len, ret_path = dfs(next_n)
#                 ret_len += 1
#                 if ret_len > max_len :
#                     max_len = ret_len
#                     max_path = ret_path + [n]
#             return max_len, max_path

#         max_len = 0
#         max_path = []
#         for n in nums :
#             ret_len, ret_path = dfs(n)
#             if ret_len > max_len :
#                 max_len = ret_len
#                 max_path = ret_path

#         return max_path

# given ans
# 我是用 recursive 的寫法
# 但他是用 DP 的寫法 (比較省記憶體)
class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        ans = []
        count = [1] * n
        prevIndex = [-1] * n
        maxCount = 0
        index = -1

        nums.sort()

        for i, num in enumerate(nums):
            for j in reversed(range(i)):
                if num % nums[j] == 0 and count[i] < count[j] + 1:
                    count[i] = count[j] + 1
                    prevIndex[i] = j
            # 這個是為了下面的組合出原本的路徑
            if count[i] > maxCount:
                maxCount = count[i]
                index = i

        while index != -1:
            ans.append(nums[index])
            index = prevIndex[index]

        return ans

s = Solution()
print(s.largestDivisibleSubset(nums = [1,2,3]))
print(s.largestDivisibleSubset(nums = [1,2,4,8]))
print(s.largestDivisibleSubset(nums = [1,2,3,4,6,12]))



