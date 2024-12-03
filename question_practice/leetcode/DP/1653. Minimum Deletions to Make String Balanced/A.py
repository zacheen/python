# 1653. Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

from typing import List
import functools

# my 
# 在這個地方當分界需要改幾個字
class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a_amount = 0
        for c in s :
            if c == "a" :
                total_a_amount += 1
        total_b_amount = len(s) - total_a_amount
        now_a_count = 0
        min_ans = len(s) 
        for indx, c in enumerate(s) :
            # indx 是轉折位置
            # , a開頭(到目前為止b有幾個 + 後面a有幾個)
            # min_ans = min(min_ans, 
            #               (indx-now_a_count)+(total_a_amount-now_a_count), 
            #             #   (now_a_count) + (total_b_amount-(indx-now_a_count)) # 我以為可以b開頭
            #               )
            min_ans = min(min_ans, indx+total_a_amount-now_a_count)
            if c == "a" :
                now_a_count += 2 #1
        # 全a 跟 全b
        return min(min_ans, total_a_amount, total_b_amount)
            

# given ans
class Solution:
    # Same as 926. Flip String to Monotone Increasing
    def minimumDeletions(self, s: str) -> int:
        dp = 0  # the number of characters to be deleted to make subso far balanced
        countB = 0
        for c in s:
            if c == 'a':
                # 1. Delete 'a'.
                # 2. Keep 'a' and delete the previous 'b's.
                dp = min(dp + 1, countB)
                # 之前最好的解答(遇到a就要多改一個,遇到b不用更新) , 目前要改幾個b
            else:
                countB += 1
            print(dp + 1, countB)

        return dp

s = Solution()
# print(s.minimumDeletions("aababbab"))
print(s.minimumDeletions("bbaaaaabb"))
# print(s.minimumDeletions("aabbaababbababaabbbaabbbbaababababbabbbababbabbaabaaabbbbbbaaabbbbabaababbaaabbbbaaabababbbaaa"))



