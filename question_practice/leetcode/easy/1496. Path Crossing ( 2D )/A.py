# My Runtime: 32 ms, faster than 83.30% of Python3 
class Solution:
    def isPathCrossing(self, path: str):
        mem = {(0,0):True}
        
        posX = 0
        posY = 0
        
        direction = {"E":(1,0),"N":(0,1),"W":(-1,0),"S":(0,-1)}
        
        for eachDir in path:
            moveX, moveY = direction[eachDir]

            posX += moveX
            posY += moveY
            
            # print(eachDir, (posX,posY))
            
            key = (posX,posY)
            getres = mem.get(key, None)
            if getres == None :
                mem[key] = True
            else :
                return True

s = Solution()
print(s.isPathCrossing("NESWW"))