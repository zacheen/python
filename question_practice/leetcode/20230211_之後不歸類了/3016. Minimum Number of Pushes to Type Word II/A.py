# 3016. Minimum Number of Pushes to Type Word II

from typing import List
import functools

from collections import Counter
# my 142ms Beats85.44%
class Solution:
    def minimumPushes(self, word: str) -> int:
        # print(list(Counter(word).values()))
        word_c = list(Counter(word).values())
        word_c.sort(reverse=True)
        press_c = 0
        press_time = 1
        pos = 0
        for p_time in word_c:
            press_c += press_time*p_time
            pos += 1
            if pos == 8 :
                pos = 0
                press_time += 1
        return press_c

# given ans
# 165ms Beats47.97%, slower becasue in for loop every time have to calculate divide
class Solution:
    # Same as 3014. Minimum Number of Pushes to Type Word I
    def minimumPushes(self, word: str) -> int:
        freqs = sorted(Counter(word).values(), reverse=True)
        return sum(freq * (i // 8 + 1) for i, freq in enumerate(freqs))
    
s = Solution()
print("ans :",s.minimumPushes(word = "abcde"))
print("ans :",s.minimumPushes("xyzxyzxyzxyz"))
print("ans :",s.minimumPushes("aabbccddeeffgghhiiiiii"))



