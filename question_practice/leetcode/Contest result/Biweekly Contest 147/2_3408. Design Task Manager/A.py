# 3408. Design Task Manager
# https://leetcode.com/problems/design-task-manager/description/

from typing import List
import functools

# my 2308ms Beats-%
from math import inf
# 3408. Design Task Manager
# https://leetcode.com/problems/design-task-manager/description/

from typing import List
import functools

# my 2308ms Beats-%
from math import inf
def comp_n(node1, node2):
    # print(node1,node2)
    if node1[0] > node2[0]:
        return node1
    elif node1[0] < node2[0]:
        return node2
    else :
        if node1[1] > node2[1]:
            return node1
        else :
            return node2

class SegTree:
    def __init__(self, nums):
        self.n = nums
        # init
        self.tree = [[-inf, -inf, -1]] * 2 * self.n   

    def update(self, index, val):
        index += self.n
        if type(val) == type(0) :
            self.tree[index][0] = val
        else :
            self.tree[index] = val
        while index > 1:
            # update node
            self.tree[index>>1] = comp_n(self.tree[index], self.tree[index^1])
            index >>= 1

    def query(self):
        return self.tree[1]

max_n = 10**5+1
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.mem = SegTree(max_n)
        # self.id_to_user = {}
        for userId, taskId, priority in tasks :
            self.mem.update(taskId, [priority, taskId, userId])
            # self.id_to_user[taskId] = userId
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mem.update(taskId, [priority, taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.mem.update(taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.mem.update(taskId, [-inf, -inf, -1])

    def execTop(self) -> int:
        ret = self.mem.query()
        if ret[0] == -inf :
            return -1
        self.mem.update(ret[1], [-inf, -inf, -1])
        return ret[2]


# given ans 893ms Beats100.00%
# using another map to track taskID : (priority, userID)
# I thought rmv would be O(n^2) (finding item)*(tasks.length)
    # but its faster...
    # because by using map could find its priority > O(logn)
