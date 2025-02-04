# 3030. Find the Grid of Region Average
# https://leetcode.com/problems/find-the-grid-of-region-average/description/

from typing import List
import functools

from itertools import accumulate, pairwise
# my 
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        len_n1 = len(image)
        len_n2 = len(image[0])

        mem = [[0]*len_n2 for _ in range(len_n1)]
        for n1, l in enumerate(image) :
            l = list(accumulate(l))
            if n1 == 0 :
                mem[0] = l
                continue
            for n2, s in enumerate(l) :
                mem[n1][n2] = s + mem[n1-1][n2]

        def get_total(n1,n2):
            if n1 < 0 or n2 < 0 :
                return 0
            return mem[n1][n2]

        def ave33(n1,n2):
            return (get_total(n1,n2) - get_total(n1-3,n2) - get_total(n1,n2-3) + get_total(n1-3,n2-3)) // 9

        def check_thresh(n1,n2):
            # hor
            for i1 in range(n1-2,n1+1):
                for i2f,i2e in pairwise(list(range(n2-2,n2+1))):
                    if abs(image[i1][i2f] - image[i1][i2e]) > threshold :
                        return False
            # ver
            for i2 in range(n2-2,n2+1):
                for i1f,i1e in pairwise(list(range(n1-2,n1+1))):
                    if abs(image[i1f][i2] - image[i1e][i2]) > threshold :
                        return False
            return True

        ans = [[[0,0] for _ in range(len_n2) ] for __ in range(len_n1)]
        for n1 in range(2, len_n1) :
            for n2 in range(2, len_n2) :
                if check_thresh(n1,n2) :
                    ave = ave33(n1,n2)
                    for i1 in range(n1-2,n1+1):
                        for i2 in range(n2-2,n2+1):
                            ans[i1][i2][0] += ave
                            ans[i1][i2][1] += 1

        # print(ans)
        for n1 in range(len_n1) :
            for n2 in range(len_n2) :
                if ans[n1][n2][1] == 0:
                    ans[n1][n2] = image[n1][n2]
                else :
                    ans[n1][n2] = int(ans[n1][n2][0] / ans[n1][n2][1])
        return ans

# given ans
# they direct sum it, and it is faster...
# because region, which is a 3 x 3, is quite small

s = Solution()
print("ans :",s.resultGrid([[5,6,7,10],[8,9,10,10],[11,12,13,10]], 3)) # 
print("ans :",s.resultGrid([[10,20,30],[15,25,35],[20,30,40],[25,35,45]], 12)) # 
print("ans :",s.resultGrid([[5,6,7],[8,9,10],[11,12,13]], 1)) # 
print("ans :",s.resultGrid([[1,14,9,2],[10,16,13,8],[7,11,12,4]], 13)) # 



