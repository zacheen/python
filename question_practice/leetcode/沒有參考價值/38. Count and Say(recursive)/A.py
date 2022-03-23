# My
# Runtime: 58 ms, faster than 64.17% of Python3 online submissions for Count and Say.
# Memory Usage: 13.9 MB, less than 82.05% of Python3 online submissions for Count and Say.
class Solution:
    def countAndSay(self, n):
        if n == 1 :
            return "1"
        else :
            ret = self.countAndSay(n-1)
            # print(n,ret)
            retStr = ""
            count = 0
            lastWord = ""
            for eachWord in ret :
                # print("<"+eachWord+">"+"<"+lastWord+">")
                if eachWord == lastWord :
                    count = count + 1
                else :
                    if lastWord == "" :
                        lastWord = eachWord
                        count = 1
                        continue
                    retStr = retStr + str(count) + lastWord
                    lastWord = eachWord
                    count = 1
                # print(eachWord, "<",retStr,">",)
            retStr = retStr + str(count) + lastWord
            
            return retStr

s = Solution()
print(s.countAndSay(5))