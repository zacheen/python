# my 
# fail 3 次
    # 第一次 : 質數計算 range 有誤 (沒有加上 -1)
    # 第二次 : 質數不包含 1
    # 第三次 : 質數計算 range 有誤 (num//2 + 1 -> num//2)
from typing import List
import functools
def check_prime(num) :
    if num == 1 :
        return False
    for i in range(num//2, 1, -1) :
        if num % i == 0 :
            return False
    return True

# given ans
# 計算質數優化
import math 
def check_prime(num) :
    if num == 1 :
        return False
    for i in range(2,int(math.sqrt(num)+1)) :
        if num % i == 0 :
            return False
    return True

# print(check_prime(841))
# print(check_prime(503))

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        edge_len = len(nums)
        all_diagonals = set()
        for i in range(edge_len) :
            all_diagonals.add(nums[i][i])
            all_diagonals.add(nums[i][edge_len-i-1])
        
        all_diagonals = list(all_diagonals)
        all_diagonals.sort(reverse = True)
        # print(all_diagonals)
        
        for num in all_diagonals :
            if check_prime(num) :
                return num
        return 0



s = Solution()
# print(s.diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))
# print(s.diagonalPrime([[1,2,3],[5,17,7],[9,11,10]]))
# print(s.diagonalPrime([[1,2,3,1],[5,17,7,1],[9,11,10,1],[1,1,1,1]]))



