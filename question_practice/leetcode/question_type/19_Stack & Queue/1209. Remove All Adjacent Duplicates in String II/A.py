from collections import deque
# my Runtime: 119 ms, faster than 81.56% of Python3
class Solution:
    def removeDuplicates(self, s, k):
        stack = deque()
        for c in s :
            if len(stack) > 0 and c == stack[-1][0] :
                stack[-1][1] += 1
                if stack[-1][1] == k :
                    stack.pop()
            else :
                stack.append([c,1])  
            # print(stack)
        return "".join([c*n for c , n in stack])

# given ans 完全一樣!

s = Solution()
print(s.removeDuplicates(s = "abcd", k = 2)) # "abcd"
print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3)) # "aa"

