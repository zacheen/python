# 2523. Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range

from typing import List
from math import inf
import math
from itertools import pairwise
from collections import deque

# my : 343ms Beats62.50%
    # using template : generating all the factors
MAX = 10 ** 6 + 1
fac = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        fac[j].append(i)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [n for n in range(left, right+1) if len(fac[n]) == 2]
        if len(primes) < 2 :
            return [-1,-1]
        ans = None
        min_diff = inf
        for n1,n2 in pairwise(primes) :
            if (diff := n2-n1) < min_diff :
                min_diff = diff
                ans = [n1,n2]
        return ans

# given ans : 0~5ms
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime
    
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):  # check odd numbers only
        if n % i == 0:
            return False
    return True
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        q = deque([])
        diff = inf
        pair = [-1,-1]
        for i in range(left,right+1):
            if isPrime(i): 
                q.append(i)
            if len(q)>=2:
                if (d:=q[1]-q[0]) <diff:
                    pair=[q[0],q[1]]
                    diff=d
                    if diff<=2: return pair
                q.popleft()
        return pair

s = Solution()
print("ans :",s.closestPrimes(10,19)) # [11, 13]
print("ans :",s.closestPrimes(4,6)) # [-1, -1]



