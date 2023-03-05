
# 這個演算法是用來計算一些很多種可能的組合 
# 但其實可以簡化成 for 每個結束的點 計算這個結束的點 有幾個開始的點符合需求
    # 這樣可以保證計算到每種情況 但情況又不至於太複雜
# 跟 sliding window 的差異是
    # sliding window 是 通常只會移動 l,r 其中一個，然後看範圍符不符合條件
    # possible_sub 是 for 每個點的 l 或 r，然後找另外一個點符合條件的點 
class Solution:
    def countSubarrays(self, nums, minK, maxK):
        ans = 0
        r = -1
        # 紀錄上一個 minK 跟 maxK
        prevMinKIndex = -1
        prevMaxKIndex = -1

        # r 是紀錄最前面可以當開頭的位置
        # l 是紀錄現在的位置
        for now_pos, num in enumerate(nums):
            if num < minK or num > maxK:
                r = now_pos
            if num == minK:
                prevMinKIndex = now_pos
            if num == maxK:
                prevMaxKIndex = now_pos
            # any index k in [j + 1, min(prevMinKIndex, prevMaxKIndex)] can be the
            # start of the subarray s.t. nums[k..i] satisfies the conditions
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - r)
            # min(prevMinKIndex, prevMaxKIndex) : 代表最後面開頭的位置
            # min(prevMinKIndex, prevMaxKIndex) - r : 代表 最後面可以當開頭的位置 - 最前面可以當開頭的位置 = 在尾端為 now_pos 不同開頭位置有幾種組合
            print(num, now_pos, r, prevMinKIndex,prevMaxKIndex, max(0, min(prevMinKIndex, prevMaxKIndex) - r), ans)

        return ans

s = Solution()
# print(s.countSubarrays(nums = [2,1,3,5,2,7,5], minK = 1, maxK = 5))
print(s.countSubarrays(nums = [2,1,3,5,1,2,7,5], minK = 1, maxK = 5))
# print(s.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))