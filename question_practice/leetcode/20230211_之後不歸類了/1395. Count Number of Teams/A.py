# 1395. Count Number of Teams
# https://leetcode.com/problems/count-number-of-teams

from typing import List
import functools

# my 1674ms Beats5.04%
class Solution:
    def numTeams(self, rating):
        @functools.lru_cache(None)
        def count_comb(last_pos, increase, amount):
            if amount == 0 :
                return 1
            total_comb = 0
            for i in range(last_pos+1, len(rating)) :
                if increase :
                    if last_pos == -1 or rating[i] > rating[last_pos] :
                        total_comb += count_comb(i, increase, amount-1)
                else : 
                    if last_pos == -1 or rating[i] < rating[last_pos] :
                        total_comb += count_comb(i, increase, amount-1)
            return total_comb
        return count_comb(-1, True, 3) + count_comb(-1, False, 3)

# given ans
# 498ms Beats53.30%
# 取中間 計算左右兩邊比中間大跟小的數量 最後相乘
# 這是因為剛好 3 個才有特別快的算法
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(1, len(rating) - 1):
            # Calculate soldiers on the left with less//greater ratings.
            leftLess = 0
            leftGreater = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    leftLess += 1
                elif rating[j] > rating[i]:
                    leftGreater += 1
            # Calculate soldiers on the right with less//greater ratings.
            rightLess = 0
            rightGreater = 0
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    rightLess += 1
                elif rating[j] > rating[i]:
                    rightGreater += 1
            ans += leftLess * rightGreater + leftGreater * rightLess
        return ans
    
s = Solution()
print(s.numTeams(rating = [2,5,3,4,1]))
print(s.numTeams(rating = [2,1,3]))
print(s.numTeams(rating = [1,2,3,4]))
