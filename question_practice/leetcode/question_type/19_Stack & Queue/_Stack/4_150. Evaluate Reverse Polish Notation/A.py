# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List
from math import ceil

# my
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens :
            if t == '+' :
                stack.append(stack.pop() + stack.pop())
            elif t == '-' :
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 - n2)
            elif t == '*' :
                stack.append(stack.pop() * stack.pop())
            elif t == '/' :
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(n1/n2))
                # if (n1 > 0) == (n2 > 0) :
                #     stack.append(n1 // n2)
                # else :
                #     stack.append( ceil(n1/n2) )
            else :
                stack.append(int(t))
            # print(stack)
        return stack[-1]