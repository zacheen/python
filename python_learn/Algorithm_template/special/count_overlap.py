# count_overlap
    # st +1 , en -1
    # 根據 accumulate 的結果，判斷有多少個區間重疊

from itertools import accumulate
## <template> ######################################
# shift_mem = [0]*(len(nums)+1)
# for st,en,di in shifts :
#     shift_mem[st] += di
#     shift_mem[en+1] -= di

# return [OP for n, sh_cou in zip(nums, accumulate(shift_mem))]
## <template end> ######################################

# classic
# 2381. Shifting Letters II
# https://leetcode.com/problems/shifting-letters-ii/description
from functools import cache
# my 43ms Beats98.83%
class Solution:
    def shiftingLetters(self, s, shifts):
        shift_mem = [0]*(len(s)+1)
        for st,en,di in shifts :
            if di : # di == 1
                shift_mem[st] += 1
                shift_mem[en+1] -= 1
            else : # di == 0
                shift_mem[st] -= 1
                shift_mem[en+1] += 1
        
        adjust = ord("a")
        @cache
        def op(c, sh_cou):
            return chr(((ord(c)-adjust) + sh_cou)%26 + adjust)
        return "".join(op(c, sh_cou%26) for c, sh_cou in zip(s, accumulate(shift_mem)))

s = Solution()
print("ans :",s.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])) # "ace"
print("ans :",s.shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]])) # "catz"



