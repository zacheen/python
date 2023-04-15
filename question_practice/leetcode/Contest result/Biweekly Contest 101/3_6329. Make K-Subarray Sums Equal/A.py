# my (fail)
class Solution:
    def makeSubKSumEqual(self, arr, k):
        # 比賽的時候沒想到
        # 如果可以整除的話 k 個數字循環，要不然全部的數字都要相同
            # 證明
            # a1+b1+c1 = b1+c1+a2
            # 所以一定 a1 == a2
            # 同理 b1 == b2，所以 
        # 從 given ans 找到邏輯 Bug
            # a1, b1, c1, d1, a2, b2 長度4
            # -> a1 = a2
                # -> b1 = b2
            # -> c1 = a1
                # -> d1 = b1
            # 整理
            # a1 = a2 = c1
            # b1 = b2 = d1
            # 所以應該是最大公因數一個循環即可
                # 但我不知道要怎麼證明這樣是對的
                # 如果不能證明就應該要用下面的方法，就是用最基本的邏輯去解決
        
        def get_dist(l):
            l.sort()
            mid = l[len(l)//2]
            return sum( abs(mid-n) for n in l)
        
        if len(arr) % k == 0:
            # 數字循環即可
            total = 0
            for modk in range(k) :
                total += get_dist(arr[modk::k])
                print(total)
            return total
        else :
            # 全部的數字相同
            return get_dist(arr)

# given ans 翻譯成 python
class Solution:
    def makeSubKSumEqual(self, arr, k):
        ans = 0
        n = len(arr)
        vis = [False]*n
        for i in range(n):
            if not vis[i] :
                x = []
                j = i
                while not vis[j] :
                    vis[j] = True
                    x.append(arr[j])
                    j = (j+k) % n
                print(x)
                x.sort()
                y = x[len(x)//2]
                for xi in x :
                    ans += abs(xi-y)
        return ans

s = Solution()
# print(s.makeSubKSumEqual(arr = [1,4,1,3], k = 2))
# print(s.makeSubKSumEqual(arr = [2,5,5,7], k = 3))
print(s.makeSubKSumEqual(arr = [6,2,8,5,7,10], k = 4))



