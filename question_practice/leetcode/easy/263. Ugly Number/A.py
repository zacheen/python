class Solution:
    def isUgly(self, n):

        # # My v1 Runtime: 48 ms, faster than 47.48% of Python3
        # if n <= 0 :
        #     return False
        
        # factors = [15,10,6,5,3,2] # 因為我不知道 testcase 所以我不知道哪一種比較快
        # # factors = [5,3,2]
        # nowFactor = 30
        # factorCount = 0

        # while n > 1 :
        #     # print(n)
        #     if n % nowFactor == 0 :
        #         n = n // nowFactor
        #     else :
        #         if factorCount == 6:
        #         # if factorCount == 3:
        #             return False
                
        #         nowFactor = factors[factorCount]
        #         factorCount = factorCount + 1

        # return True

        # My v2 換成 for 每個 factor 
        # 36 ms, faster than 79.43% of Python3 
        # 可見一開始架構很重要 而且程式碼看起來更整潔
        if n <= 0 :
            return False

        factors = [30,15,10,6,5,3,2] # 因為我不知道 testcase 所以我不知道哪一種比較快
        for factor in factors:
            while n % factor == 0 :
                n = n // factor

        if n == 1 :
            return True
        else :
            return False


s = Solution()
print(s.isUgly(6))
print(s.isUgly(1))
print(s.isUgly(14))
print(s.isUgly(60))

