# 3582. Generate Tag for Video Caption
# https://leetcode.com/problems/generate-tag-for-video-caption

from typing import List
from math import inf

# my 0ms
class Solution:
    def generateTag(self, caption: str) -> str:
        ans  = ["#"]
        first_word = True
        for word in caption.split(" ") :
            if word == "" : continue
            if first_word : 
                ans.append(word.lower())
                first_word = False
            else :
                ans.append(word[0].upper())
                ans.append(word[1:].lower())
        return "".join(ans)[:100]

s = Solution()
print("ans :",s.generateTag("Leetcode daily streak achieved")) # "#leetcodeDailyStreakAchieved"
print("ans :",s.generateTag("can I Go There")) # "#canIGoThere"
print("ans :",s.generateTag("hhhhhhhhhhhhhhhhh")) # '#hhhhhhhhhhhhhhhhh'
print("ans :",s.generateTag(" ff")) # "#ff"



