from typing import List
import functools

# commit fail 3次
    # 第一次 : 測試的 Time Limit Exceeded
    # 第二，三次 : 測試不同方法提升速度還是不行，只好開始想 O(n) 的解法，還真的有想到規律

# my v1 I know will Time Limit Exceeded
# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:
#         # 
#         ans_list = [0]*len(nums)
#         for indx_i,num_i in enumerate(nums) :
#             count = 0
#             for indx_j,num_j in enumerate(nums) :
#                 if num_i == num_j :
#                     count += abs(indx_i - indx_j)
#             ans_list[indx_i] = count
#         return ans_list

# my v2 optimize Beats 30.77%
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:  
        same_num = defaultdict(list)
        ans_list = [0]*len(nums)
        for indx_i,num_i in enumerate(nums) :
            same_num[num_i].append(indx_i)
        
        for same_num_indx in same_num.values() :
            now_distance = sum(same_num_indx)
            last_num = 0
            total_len = len(same_num_indx)
            for indx, num in enumerate(same_num_indx) :
                now_distance = now_distance + (num-last_num)*(indx-(total_len-indx))
                ans_list[num] = now_distance
                # print(num, now_distance,(num-last_num),(indx-(total_len-indx)))
                last_num = num
        return ans_list

# given ans Beats 15.38%
    # 比較慢 但是比較不用找規律 且易讀性高
from collections import Counter
class Solution:
    def distance(self, nums: List[int]) -> List[int]:  
        ans = [0]*len(nums)
        
        count_front = Counter()
        sum_mem = Counter()
        # 計算在 i 之前相同項目的 sum(abs()) = indx*前面有幾個項目 - 總和
        for i in range(len(nums)):
            ans[i] = i*count_front[nums[i]] - sum_mem[nums[i]]
            count_front[nums[i]] += 1
            sum_mem[nums[i]]     += i
            # print(ans, count_front, sum_mem)

        count_back = Counter()
        sum_mem = Counter()
        # 再加上 在 i 之後相同項目的 sum(abs()) = 總和 - indx*後面有幾個項目
        for i in range(len(nums)-1,-1,-1):
            ans[i] += sum_mem[nums[i]] - i * count_back[nums[i]]
            count_back[nums[i]] += 1
            sum_mem[nums[i]]    += i

        return ans

s = Solution()
print(s.distance([1,3,1,1,2]))
print(s.distance([0,5,3]))



