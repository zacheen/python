# given ans
# Runtime: 2896 ms, faster than 95.86% of Python3
class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        # 喊出的第一個數字就能超過 desiredTotal
        if (maxChoosableInteger >= desiredTotal) : 
            return True
        
        # 判斷 maxChoosableInteger 總數加起來能不能到 desiredTotal
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) :
            return False

        def canWin(total, used, m) :
            get_mem = m.get(used, None)
            if get_mem != None :
                return get_mem

            for i in range(maxChoosableInteger) :
                cur = (1 << i)
                # cur & used 是判斷 這個位置有沒有用過
                if (cur & used) == 0 : 
                    # i + 1 是因為 0 的位置 是紀錄數字 1 有沒有用過
                    # total <= i + 1 : 代表加總已經超過 desiredTotal
                    # 因為 cur 用過了 所以遞迴的時候 要記錄此位置用過 -> cur | used
                    if (total <= i + 1 or not canWin(total - (i + 1), cur | used, m)) :
                        m[used] = True
                        return True

            m[used] = False
            return False
        
        m = {}
        return canWin(desiredTotal, 0, m)
        

s = Solution()
print(s.canIWin(maxChoosableInteger = 10, desiredTotal = 11))
print(s.canIWin(maxChoosableInteger = 10, desiredTotal = 0))
print(s.canIWin(maxChoosableInteger = 10, desiredTotal = 1))