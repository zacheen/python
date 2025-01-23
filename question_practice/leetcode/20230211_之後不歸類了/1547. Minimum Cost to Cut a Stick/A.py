# 1547. Minimum Cost to Cut a Stick
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

from typing import List
import functools

# my 
import bisect
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 最多 100 刀
        # 一定是從中間切最好 (但是如果沒有剛好在中間會出錯)
        cuts.sort()
        print(cuts)
        ans = 0
        def recursive(cuts, start, end) :
            nonlocal ans
            if len(cuts) == 0 :
                return 
            ans += (end - start)
            if len(cuts) == 1 :
                print("cut :", "len==1",cuts[0])
                return
            
            mid = (end + start) / 2
            left = bisect.bisect_right(cuts, mid) - 1
            # print("left :",left, cuts, mid)
            if left+1 >= len(cuts) :
                left = len(cuts) - 1
                recursive(cuts[:left], start, cuts[left])
                return
            elif cuts[left] == mid :
                # 會超出範圍 or 剛好是中間
                pass
            else :
                diff_left = mid - cuts[left]
                diff_right = cuts[left+1] - mid
                # print("diff :",diff_left, diff_right)
                if (diff_left < diff_right) or (diff_left == diff_right and len(cuts) > 2*left):
                    # 切左邊
                    pass
                else :
                    left += 1
            print("cut :", left, cuts[left])
            recursive(cuts[:left], start, cuts[left])
            recursive(cuts[left+1:], cuts[left], end)
            return 

        recursive(cuts, 0, n)

        return ans

# given ans Beats 82.14%
# 真的一刀一刀看怎麼切最好
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        A = [0] + sorted(cuts) + [n]

        @functools.lru_cache(None)
        def dp(i, j):
            if j - i <= 1:
                return 0

            return min(A[j] - A[i] + dp(i, k) + dp(k, j) for k in range(i + 1, j))

        return dp(0, len(A) - 1)
  
s = Solution()
# print(s.minCost(n = 7, cuts = [1,3,4,5]))
# print(s.minCost(n = 9, cuts = [5,6,1,4,2]))
print(s.minCost(n = 20, cuts = [1,14,18,6,17,8,10,4,13,16,7]))



