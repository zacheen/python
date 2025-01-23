# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import Counter

# my practice again : 55ms Beats5.10% 
# 計算從頭到現在有幾種總和
# 計算 [總和 - k = 前面的總和] 有幾種加總方式
class Solution:
    def subarraySum(self, nums, k):
        cou = Counter()
        cou[0] = 1 # 不用減去前面
        s = 0
        ans = 0
        for n in nums :
            s += n
            ans += cou[s-k]
            cou[s] += 1
        return ans
    
# given ans : using dict is faster : 29ms Beats68.19%
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
        
        for num in nums:
            prefix_sum += num  # Update the running prefix sum
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
            else:
                prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
        return count
s = Solution()
print(s.subarraySum([1,1,1],2))
print(s.subarraySum([3,2,1],3))
print(s.subarraySum([-1,-1,1],0))



