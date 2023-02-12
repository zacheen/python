# my
# Beats 57.93% 
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        #####################################
        # s_count = Counter(secret)
        # g_count = Counter(guess)
        # B = 0
        # for k in s_count.keys():
        #     B += min(g_count[k], s_count[k])
        #####################################
        # 優化 Beats 76.78%
        # s_count = Counter(secret)
        # B = 0
        # for k in s_count.keys():
        #     B += min(guess.count(k), s_count[k])
        #####################################
        # 再簡化 Beats 80.92%
        s_count = Counter(secret)
        B = sum(min(guess.count(k), s_count[k]) for k in s_count.keys())
        #####################################

        A = 0
        for s_word, g_word in zip(secret, guess) :
            if (s_word == g_word) :
                A += 1

        B = B - A

        return str(A) + "A" + str(B) + "B"

# given ans
# 概念是一樣的 但是很簡潔
import operator
class Solution(object):
    def getHint(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        bovine = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, bovine - bulls)

s = Solution()
print(s.getHint(secret = "1807", guess = "7810"))
print(s.getHint(secret = "1123", guess = "0111"))



