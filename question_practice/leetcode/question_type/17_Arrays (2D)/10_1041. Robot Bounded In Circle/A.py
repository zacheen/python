# my Runtime: 47 ms, faster than 38.51% of Python3
# class Solution:
#     def isRobotBounded(self, instructions):
#         # 循環的情況
#         c = Counter(instructions)
#         # print(c["R"] , c["L"], (c["R"]-c["L"])%4)
#         if (c["R"]-c["L"])%4 != 0 :
#             return True
        
#         # 一次就會回到原本的位置
#         x = 0
#         y = 0
#         direction = 0 # 
#         direct_list = [0,1,0,-1,0]
        
#         for instr in instructions :
#             if instr == "G" :
#                 x += direct_list[direction]
#                 y += direct_list[direction+1]
#             elif instr == "R" :
#                 direction += 1
#                 if direction == 4 :
#                     direction = 0
#             else :
#                 direction -= 1
#                 if direction == -1 :
#                     direction = 3
        
#         if x == 0 and y == 0 :
#             return True
#         return False

# given ans
# 概念一樣 只是寫的非常優雅
class Solution:
    def isRobotBounded(self, instructions):
        x = 0
        y = 0
        d = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == 'G':
                x += directions[d][0]
                y += directions[d][1]
            elif instruction == 'L':
                d = (d + 3) % 4
            else:
                d = (d + 1) % 4

        return (x, y) == (0, 0) or d > 0

s = Solution()
print(s.isRobotBounded("GLRLLGLL")) # True
print(s.isRobotBounded("GGLLGG")) # True
print(s.isRobotBounded("GL")) # True
print(s.isRobotBounded("GG")) # false



