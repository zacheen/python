# My Runtime: 100 ms, faster than 68.59% of Python3 
class Solution:
    def isPowerOfThree(self, n: int):
        if n == 0 :
            return False
        
        if n == 1 :
            return True
        
        mul = 3
        times = 1
        cache = {1:3}
        
        while True :
            double = mul*mul
            times = times * 2
            cache[times] = double
            if double >= n :
                break
            else :
                mul = double
  
        # print(cache)
        # print(mul, times)

        if mul == n :
            return True

        alltimes = list(cache.keys())[::-1]
        for i in alltimes :
            # print(i, cache[i])
            res = mul * cache[i]

            if res <= n :
                mul = res
                if res == n :
                    return True
                
        return False

        
s = Solution()
print(s.isPowerOfThree(6))