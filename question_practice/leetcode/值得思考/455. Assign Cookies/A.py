# My Runtime: 181 ms, faster than 77.35% of Python3
# 那時候我的目標是想要 找到 max content 其實不用
# 不過這個想法比較值觀拉
class Solution:
    def findContentChildren(self, g, s):
        g.sort(reverse = True)
        s.sort(reverse = True)
        # print(s)
        
        cookie_pointer = 0
        child_pointer = 0
        count = 0 
        total_content = 0
        while child_pointer < len(g) and cookie_pointer < len(s) :
            # print(child_pointer, cookie_pointer)
            # print(s[cookie_pointer] , g[child_pointer])
            if s[cookie_pointer] >= g[child_pointer] :
                total_content += g[count]
                count += 1
                cookie_pointer += 1
                child_pointer += 1
            else :
                child_pointer += 1
        print("total_content :",total_content)      
                
        return count

# given ans 為什麼 count++ 就是答案 ?
# class Solution:
#     def findContentChildren(self, g, s):
#         g.sort()
#         s.sort()
        
#         count = 0
#         # total_content = 0
#         for cookie_pointer in range(len(s)) :
#             if count >= len(g) :
#                 break
#             if s[cookie_pointer] >= g[count] :
#                 # total_content += g[count]
#                 count += 1
#         # print("total_content :",total_content)        
#         return count

# 思考 
# 1345
# 1245
# 最後分配 1 -> 1, 4 -> 3, 5 -> 4, 
# 最後分配 1 -> 1, 4 -> 4, 5 -> 5, 
# 這個時候這兩種分配方法的效益都是一樣的
# 因為滿足的人數一樣
# 所以解法才這麼簡單
# 如果 加起來 滿足感最大 就不一樣了

s = Solution()
print(s.findContentChildren([1,3,4,5],[1,2,4,5]))

