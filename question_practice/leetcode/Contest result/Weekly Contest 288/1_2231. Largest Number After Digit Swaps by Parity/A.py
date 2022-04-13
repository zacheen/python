# my v2
class Solution:
    def largestInteger(self, num):
        odd = []
        even = []
        place = []
        while num > 0 :
            if num % 2 == 0 :
                even.insert(0, num % 10)
                place.insert(0, 0)
            else :
                odd.insert(0, num % 10)
                place.insert(0, 1)
            num = num // 10
            
        odd.sort()
        even.sort()
        ans = 0
        for p in place :
            if p == 0 :
                ans = ans*10 + even.pop()
            else :
                ans = ans*10 + odd.pop()
        return ans

# my v1 在比賽期間找不到 BUG
# 最後改比較優雅的寫法
# 最後找到問題在 if now > max_num and int(now)%2 == mod :
    # 那時候打錯打成 if now > "find_num" and int(now)%2 == mod :
# class Solution:
#     def largestInteger(self, num):
#         n = list(str(num))

#         def find_max(start, find_num) :
#             # print("in find_max,", find_num)
#             mod = int(find_num)%2 
#             max_num = find_num
#             max_indx = -1
#             for i in range(start, len(n)) :
#                 now = n[i]
#                 # print(i, now, find_num, int(now)%2)
#                 if now > max_num and int(now)%2 == mod :
#                     max_num = now
#                     max_indx = i
#             return max_num, max_indx
        
#         for indx in range(len(n)) :
#             # print("into find_max,", n[indx])
#             max_num, max_indx = find_max(indx, n[indx])
#             if max_indx != -1 :
#                 n[max_indx], n[indx] = n[indx], n[max_indx]
#             # print(indx, n, n[indx])
    
#         return int("".join(n))

# given ans 跟 my v2 的方法差不多

s = Solution()
print(s.largestInteger(1234)) # 3412
print(s.largestInteger(65875)) # 87655
print(s.largestInteger(3159)) # 9531

