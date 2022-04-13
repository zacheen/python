# My Time Limit Exceeded
# class Solution:
#     def smallestStringWithSwaps(self, s, pairs):
#         each_set = []
        
#         # 找連在一起的位置
#         for each_link in pairs :
#             set_find_indx = None
#             first_not_find = True
#             second_not_find = True
#             for indx, this_set in enumerate(each_set)  :
#                 # print("indx, this_set",indx, this_set)
#                 if first_not_find and (each_link[0] in this_set) :
#                     first_not_find = False
#                     if set_find_indx != None :
#                         # print("merge : ", set_find_indx, indx)
#                         each_set[set_find_indx] = this_set | each_set[set_find_indx]
#                         del(each_set[indx])
#                         break
#                     else :    
#                         # print("find one : ", indx, each_link[1])
#                         set_find_indx = indx
#                         this_set.add(each_link[1])
                
#                 # 這裡要用 elif 因為上面已經 把 第二個加到 那個set裡面 
#                 # 所以如果沒有 el 會直接進到 merge (each_link[1] in this_set 一定會是True)
#                 elif second_not_find and (each_link[1] in this_set) :
#                     second_not_find = False
#                     if set_find_indx != None :
#                         # print("merge : ", set_find_indx, indx)
#                         each_set[set_find_indx] = this_set | each_set[set_find_indx]
#                         del(each_set[indx])
#                         break
#                     else :    
#                         # print("find one : ", indx, each_link[0])
#                         set_find_indx = indx
#                         this_set.add(each_link[0])

#             if first_not_find and second_not_find :
#                 each_set.append({each_link[0], each_link[1]})

#             # print(each_set)

#         print(each_set)
#         s = list(s)
#         for this_set in each_set :
#             this_set_char = []
#             this_set_indx = list(this_set)
#             print(this_set_indx)
#             this_set_indx.sort()

#             # 抓出全部字母
#             for ind in this_set_indx :
#                 this_set_char.append(s[ind])

#             this_set_char.sort()
#             print(this_set_char)

#             # 把整理好的順序放回 s
#             for ind1, ind2 in enumerate(this_set_indx) :
#                 s[ind2] = this_set_char[ind1]

#         return "".join(s)

#------------------------------------------------------------------
# given ans Runtime: 1034 ms, faster than 45.56% of Python3
# 1034 ms, 1278 ms, 1347 ms
# 隨然這樣的確 在分類set的確是order(N) 
# 但是find是order(N^2)ㄟ ??
#   for N : order(N) 
#       find源頭 應該也是 order(N) 
#   搭配起來就是 order(N^2)
# 這樣真的比較快嗎 ?  事實上就是比較快...
# class UF:
#     def __init__(self, n: int):
#         self.id = list(range(n))

#     def union(self, u: int, v: int):
#         self.id[self.find(u)] = self.find(v)
#         print(self.id)

#     # 最終會找到源頭 (那個從來沒動過的點)
#     def find(self, u: int):
#         if self.id[u] != u:
#             self.id[u] = self.find(self.id[u])
#         return self.id[u]

# class Solution:
#     def smallestStringWithSwaps(self, s, pairs):
#         ans = ''
#         uf = UF(len(s))

#         # 第一次的 union (把每個位置連結)
#         # 只要跟原本的位置有變動的 就代表跟那個位置的同一個set的 (就是沒變過數字的那一個set)
#         for p, q in pairs:
#             uf.union(p, q)

#         # My 優化
#         # 其實 union 之後的每一次 find 結果都是固定的
#         # 因此這裡其實可以加個 mem
#         # 優化後 : Runtime: 829 ms 和 994 ms 和 1661 ms (樣本數不夠大 時間差距很大)
#         # Runtime: 829 ms, faster than 71.53% of Python3
#         # mem_find = {}
#         # def get_cache(i):
#         #     ret = mem_find.get(i, None) 
#         #     if ret == None :
#         #         real_find = uf.find(i)
#         #         mem_find[i] = real_find
#         #         return real_find
#         #     else :
#         #         return ret

#         # 第二次的 union (把有聯結的位置相對應的字全部找出來 加到源頭的set(用find找源頭)中)
#         from collections import defaultdict
#         map = defaultdict(list)
#         for i in range(len(s)):
#             map[uf.find(i)].append(s[i])
#             # map[get_cache(i)].append(s[i])
        
#         print("map1 : ",map)

#         # 把各個set的字 從大排到小 (可能 pop 比較方便)
#         for key in map.keys():
#             map[key].sort(reverse=True)

#         # 根據位置對應的set取出一個字組合
#         for i in range(len(s)):
#             ans += map[uf.find(i)].pop()
#             # ans += map[get_cache(i)].pop()
#         return ans

#------------------------------------------------------------------
# given ans 2 邏輯一樣只是沒有用 class
class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        p = list(range(n))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            p[p2] = p1

        for a, b in pairs:
            union(a, b)

        res = [[] for _ in range(n)]
        for i in range(len(s)):
            fa = find(i)
            res[fa].append((s[i], i))

        ans = [''] * n

        for e in res:
            idx = [i[1] for i in e]
            chars = sorted([i[0] for i in e])
            for i, j in enumerate(idx):
                ans[j] = chars[i]

        # print(p)
        # print(res)
        return ''.join(ans)
                    
s = Solution()
print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
# print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
