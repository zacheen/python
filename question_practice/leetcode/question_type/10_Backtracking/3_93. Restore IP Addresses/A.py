# my Runtime: 49 ms, faster than 60.24% of Python3
class Solution:
    def restoreIpAddresses(self, s):
        ans = []
        def rec(now_indx, mem):
            if len(mem) == 4:
                if now_indx == len(s) :
                    ans.append(mem)
                return 
            
            if now_indx >= len(s) :
                return
            
            if s[now_indx] == "0" :
                rec(now_indx+1, mem+["0"])
            else :
                for i in range(1,4):
                    new_num = int(s[now_indx : now_indx+i])  # 這裡不用處理長度的問題 python 會處理
                    if new_num <= 255 :
                        rec(now_indx+i, mem+[str(new_num)])    
        
        rec(0, [])
        for i, a in enumerate(ans) :
            ans[i] = ".".join(a)
        return ans

# given ans 概念差不多
# 優化 : 不是加入 list  直接在append的地方先join 之後就不用for 

s = Solution()
print(s.restoreIpAddresses("101023"))



