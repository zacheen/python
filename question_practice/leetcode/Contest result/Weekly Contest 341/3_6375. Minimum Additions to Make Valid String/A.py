from typing import List
import functools

# my 
class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        # 開頭一定要補齊 a 最後一定要補齊 c
        last_word = "c"
        word = word + "ab" 
        order = ["a","b","c","a","b","c"]
        for now_c in word :
            last_word_indx = order.index(last_word)
            last_word_indx += 1
            while(True) :
                if order[last_word_indx] == now_c :
                    break
                else :
                    last_word_indx += 1
                    ans += 1
            last_word = now_c
        return ans
            

# given ans

s = Solution()
print(s.addMinimum("b"))
print(s.addMinimum("aaa"))
print(s.addMinimum("abc"))



