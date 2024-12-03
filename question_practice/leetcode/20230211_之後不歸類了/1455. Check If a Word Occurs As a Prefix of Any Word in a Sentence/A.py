# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

from typing import List
import functools

# my 0ms Beats 100.00%
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        tar_len = len(searchWord)
        for indx, each_word in enumerate(sentence.split(" ")):
            if len(each_word) >= tar_len and each_word[:tar_len] == searchWord :
                return indx+1
        return -1

s = Solution()
print("ans :",s.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
print("ans :",s.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro"))
print("ans :",s.isPrefixOfWord(sentence = "i am tired", searchWord = "you"))
print("ans :",s.isPrefixOfWord(sentence = "i love eating burger", searchWord = "bur"))
print("ans :",s.isPrefixOfWord(sentence = "i love eating burger", searchWord = "urg"))



