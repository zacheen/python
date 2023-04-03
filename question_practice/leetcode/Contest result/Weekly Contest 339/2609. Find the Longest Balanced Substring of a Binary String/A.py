# 因為 s 都太短了，所以速度的差距都不明顯
# my Beats 88.89%
class Solution:
    def findTheLongestBalancedSubstring(self, s):   
        start_indx = 0
        while True :
            if start_indx == len(s) :
                return 0
            if s[start_indx] == '0' :
                break
            start_indx += 1
        
        count = []
        now_c = '0'
        now_count = 0
        for c in s[start_indx:] :
            if c == now_c :
                now_count += 1
            else :
                count.append(now_count)
                now_c = c
                now_count = 1
        count.append(now_count)
        # print(count)
        
        ans = 0
        for i in range(len(count)//2) :
            indx = i*2
            ans = max(ans, min(count[indx], count[indx+1])*2)
        return ans

# given ans 改寫 Beats 100%
class Solution:
    def findTheLongestBalancedSubstring(self, s): 
        zero_count = 0
        one_count = 0
        max_ans = 0
        for c in s :
            if c == "0" :
                if one_count != 0 :
                    # 1 變成 0 的時候
                    max_ans = max(min(zero_count, one_count), max_ans)
                    zero_count = 0
                    one_count = 0
                zero_count += 1
            else :
                one_count += 1
                # 可以放這裡 但是比較慢
                # max_ans = max(min(zero_count, one_count), max_ans)
        max_ans = max(min(zero_count, one_count), max_ans)
        return max_ans*2
    
# 其他
    # 紀錄轉換點 s[i-1] != s[i]
    
s = Solution()
print(s.findTheLongestBalancedSubstring("01000111"))
print(s.findTheLongestBalancedSubstring("00111"))
print(s.findTheLongestBalancedSubstring("111"))
print(s.findTheLongestBalancedSubstring("00"))



