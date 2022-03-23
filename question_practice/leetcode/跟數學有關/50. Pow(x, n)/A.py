# My
class Solution:
    def myPow(self, x, n):
        if n == 0 :
            return 1
        
        cache = {}
        
        def breakDown(x, n):
            print(n)
            if n == 1 :
                return x
            
            mulans = cache.get(n, False)
            if mulans == False :
                # 先判斷餘數
                remain = n % 2
                if remain == 0:
                    small_mul = breakDown(x , n // 2)
                    small_mul=small_mul*small_mul
                    cache[n] = small_mul
                    return small_mul
                else :
                    small_mul = breakDown(x , n // 2)
                    small_mul=small_mul*small_mul
                    cache[n-1] = small_mul
                    small_mul = small_mul * x
                    cache[n] = small_mul
                    return small_mul
            else :
                return mulans
        
        if n < 0:
            x = 1 / x
            n = -n
        return breakDown(x, n)


# given solution
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             x = 1 / x
#             n = -n
#         res = 1
#         while n > 0:
#             if n % 2:
#                 res = res*x
#             n = n // 2 
#             x = x*x
#         return res

s = Solution()
print(s.myPow(2.00000, 7))
print(s.myPow(2.00000, -3))