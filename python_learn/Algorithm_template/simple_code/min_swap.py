# minimum swaps to make the list ordered
def min_swaps(nums, key):
    n = len(nums)
    # order[i] : 位置 i 應該要換到哪個新位置
    order = sorted(range(n), key = lambda i: key(nums[i]))
    swaps = 0
    for current_idx, target_idx in enumerate(order):
        while current_idx != target_idx:
            order[target_idx], target_idx = target_idx, order[target_idx]
            swaps += 1
    return swaps

# 3551. Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/
class Solution:
    def minSwaps(self, nums):
        def cal_val(n) :
            ret = 0
            while n :
                ret += n%10
                n //= 10
            return ret
        return min_swaps(nums, lambda x: (cal_val(x), x))
