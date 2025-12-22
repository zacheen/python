# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

from typing import List
from math import inf

# my 0ms
class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack_rev = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pour(self) :
        if not self.stack_rev :
            while self.stack :
                self.stack_rev.append(self.stack.pop())

    def pop(self) -> int:
        self.pour()
        return self.stack_rev.pop()

    def peek(self) -> int:
        self.pour()
        last = self.stack_rev.pop()
        self.stack_rev.append(last)
        return last

    def empty(self) -> bool:
        return not (self.stack_rev or self.stack)


