# My 
from collections import Counter
class Solution:
    def numSplits(self, s: str):
        countLeft = Counter(s)
        countRight = Counter()
        ansCount = 0
        for eachWord in s :
            countLeft[eachWord] -= 1
            countRight[eachWord] += 1
            
            # 這裡是移除沒有剩餘數量的key
            if countLeft[eachWord] == 0 :
                del(countLeft[eachWord])
            
            # v1 #########################################
            if len(countLeft) == len(countRight) :
                ansCount += 1
            # # 沒有註解之前 Runtime: 282 ms, faster than 39.06% of Python3
            # # 註解之後     Runtime: 212 ms, faster than 67.39%
            # # 三小... 好像是因為創建新的變數 很耗時間 ??
            # # elif len(countLeft) < len(countRight) :
            # #     break

            # v2 好像也沒有比較快 #########################################
            # lenL = len(countLeft)
            # lenR = len(countRight)
            # if lenL == lenR :
            #     ansCount += 1
            # elif lenL < lenR :
            #     break
            ###############################################################
                
        return ansCount

s = Solution()
print(s.numSplits("aacaba"))