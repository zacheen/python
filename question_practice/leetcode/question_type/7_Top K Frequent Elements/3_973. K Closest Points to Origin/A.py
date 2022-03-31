import heapq
# my  Runtime: 1024 ms, faster than 57.65% of Python3
# class Solution:
#     def kClosest(self, points, k):
#         def dest(x, y):
#             return x*x + y*y
        
#         dis_list = [ ( dest(point[0],point[1]), point ) for point in points]
#         # print(dis_list)
        
#         heapify(dis_list)
#         # print(dis_list)
        
#         return [ p[1] for p in heapq.nsmallest(k, dis_list) ]

# given ans
# 可能是因為 heap 比較小 所以比較快 Runtime: 844 ms, faster than 86.88% of Python3
# 我是用內建的function
# 他是自己實作了 找N個最近的
    # 距離全部加負號 這樣minheap 就會變maxheap
    # 當數量超過了 每次都取出最遠的項目
    # 剩下的就是答案
class Solution:
    def kClosest(self, points, k):
        maxHeap = []

        for x, y in points:
            heapq.heappush(maxHeap, (- x * x - y * y, [x, y]))
            # print("add :",maxHeap)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                # print("pop :",maxHeap)

        return [pair[1] for pair in maxHeap]

s = Solution()
print(s.kClosest([[-2,1],[-2,2],[-2,3],[-2,4],[-2,5],[-2,6],[-2,7],[-1,1],[-1,2],[-1,3],[-1,4],[-1,5],[-1,6],[-1,7]], 10))



