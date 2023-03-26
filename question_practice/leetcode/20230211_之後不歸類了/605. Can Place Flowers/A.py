# my Beats 97.17%
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        flag = 1 
        # 0 : have plent
        # 1 : left side have space
        # 2 : middle have space
        # 3 : right side have space
        for f in flowerbed :
            if f == 0 :
                flag += 1
                if flag == 3 :
                    n -= 1
                    flag = 1
            else :
                flag = 0
        if flag == 2 :
            n -= 1

        return n <= 0

# my v2 提早回傳 Beats 97.90%
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0 :
            return True
        
        flag = 1 
        # 0 : have plent
        # 1 : left side have space
        # 2 : middle have space
        # 3 : right side have space
        for f in flowerbed :
            if f :
                flag = 0
            else :
                flag += 1
                if flag == 3 :
                    n -= 1
                    flag = 1
                    if not n :
                        return True
        if flag == 2 :
            n -= 1

        return n == 0

s = Solution()
print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(s.canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 1))



