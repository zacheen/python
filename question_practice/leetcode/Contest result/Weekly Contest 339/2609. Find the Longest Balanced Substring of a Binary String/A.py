# my 
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:   
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


s = Solution()
print(s.findTheLongestBalancedSubstring("01000111"))
print(s.findTheLongestBalancedSubstring("00111"))
print(s.findTheLongestBalancedSubstring("111"))
print(s.findTheLongestBalancedSubstring("00"))



