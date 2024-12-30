# 3403. Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/

from typing import List
import functools

# my 15ms Beats100.00%
# Fail 1 : only consider max_len cases
# Fail 2 : forgot the case : numFriends == 1
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # 只要 N>1 就可以有長度為 1 的字串
        if numFriends == 1 :
            return word
        max_ans = ""
        str_len = len(word)-numFriends+1
        for start_i in range(len(word)):
            max_ans = max(max_ans, word[start_i : start_i+str_len])
        return max_ans
        
# given ans
# same

s = Solution()
print("ans :",s.answerString("aann", 3)) # 
print("ans :",s.answerString("gh", 1)) # 



