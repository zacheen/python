class Solution:
    def isHappy(self, n):
        
        # My Runtime: 36 ms, faster than 86.73% of Python3
        mem = {}
        
        while True :
            newN = 0
            
            while n > 0 :
                lastNum = n % 10
                n = n // 10
                newN = newN + lastNum*lastNum
                
            if newN == 1 :
                return True
                
            roundBefore = mem.get(newN, None)
            if roundBefore != None :
                return False
            else :
                mem[newN] = True
                
            n = newN

        
s = Solution()
print(s.isHappy(19))
print("------------")
print(s.isHappy(2))