# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/description/

# 題目 : 
    # 從字串中按照順序抽取字母排列，且每個字母都要有
    # 排出最小的字串 "abc" < "acb"

# my practice again : 4ms Beats33.82%
# "if c in stack :" can still be optimized
class Solution:
    def removeDuplicateLetters(self, s) :
        last_indx = {}
        for i,c in enumerate(s):
            last_indx[c] = i
        stack = []
        for i,c in enumerate(s):
            if c in stack :
                continue
            while stack:
                last_stack = stack[-1]
                # print(i,c, last_stack, c < last_stack and last_indx[last_stack] > i)
                if c < last_stack and last_indx[last_stack] > i :
                    stack.pop()
                else :
                    break
            stack.append(c)
        return "".join(stack)

# given ans Beats 87.13%
class Solution:
    def removeDuplicateLetters(self, s) :
        # 紀錄每個重復的字母 最後的位置
        last = {c: i  for i, c in enumerate(s)}
        # print(last)

        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                # 如果 stack 裡面有東西 
                # && 這個字母小於目前stack最尾端的字 
                # && 目前stack最尾端的字母後面還有其他位置可以擺放
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                    # print("remove :",stack)
                seen.add(c)
                stack.append(c)
                # print(stack)
        return ''.join(stack)
        
s = Solution()
print(s.removeDuplicateLetters("cbacdcbc")) # "acdb"
print(s.removeDuplicateLetters("bcacb")) # acb
print(s.removeDuplicateLetters("bcab"))  # bca
print(s.removeDuplicateLetters("abacb")) # abc
