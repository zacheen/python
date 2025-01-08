# 1408. String Matching in an Array
# https://leetcode.com/problems/string-matching-in-an-array/description

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x : len(x), reverse = True)
        # print(words)

        stack = []
        ans = []
        for w in words :
            not_ans = True
            for s in stack :
                if w in s :
                    ans.append(w)
                    not_ans = False
                    break
            if not_ans :
                stack.append(w)
        # print(stack)
        return ans

s = Solution()
print("ans :",s.stringMatching()) # 



