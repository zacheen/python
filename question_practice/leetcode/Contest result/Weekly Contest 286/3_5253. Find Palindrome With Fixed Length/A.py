class Solution:
    def kthPalindrome(self, queries, intLength):
        ans = []
        if intLength % 2 == 0 :
            add_num = 0
            for i in range((intLength // 2)-1) :
                add_num = add_num*10 + 9
            
            for each_num in queries :
                pal = str(each_num + add_num)
                if len(pal) > (intLength // 2) :
                    ans.append(-1)
                else :
                    ans.append(int(pal + str(pal[::-1])))
        else :
            add_num = 0
            for i in range((intLength // 2)) :
                add_num = add_num*10 + 9
            
            for each_num in queries :
                pal = str(each_num + add_num)
                if len(pal) > ((intLength // 2)+1) :
                    ans.append(-1)
                else :
                    ans.append(int(pal + str(pal[-2::-1])))  # 不知道為什麼是 -2
        return ans

# given ans 
# if intLength % 2 == 0 :  可以最後再判斷  這樣code就不會這麼長
# 其他邏輯差不多 只是各自實現的方法不一樣
# class Solution:
#     def kthPalindrome(self, queries, intLength):
#         res = []
#         for i in queries:
#             n = (intLength+1)//2
#             if 9*10**(n-1) < i:
#                 res.append(-1)
#             else:
#                 first = (10**(n-1)-1) + i
#                 f = str(first)
#                 if intLength&1:
#                     res.append(int(f+f[:-1][::-1]))
#                 else:
#                     res.append(int(f+f[::-1]))
#         return res

s = Solution()
print(s.kthPalindrome(queries = [1,2,3,4,5,90,91], intLength = 3))
print(s.kthPalindrome(queries = [2,4,6,90,91], intLength = 4))
