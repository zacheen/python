# https://massivealgorithms.blogspot.com/2019/01/leetcode-923-3sum-with-multiplicity.html
# 有很多種方法 結果好像列舉最快

from collections import Counter

# my Runtime: 158 ms, faster than 50.00% of Python3
# 可以重複使用的 如果可以就不要用counter解題 會變得很複雜 (O)
class Solution:
    def threeSumMulti(self, arr, target):
        global ans
        ans = 0

        count = Counter(arr)
        dist_list = list(count.keys())
        dist_list.sort()

        mod_num = 10**9 + 7
        def add_ans(num):
            global ans
            ans = (ans+num)%mod_num
        
        def recur(start, cou, remain, mem) :
            # 要優化要合併到 for i in range(start+1, len(dist_list)):
            if start >= len(dist_list) :
                return
            if cou == 1 :
                # print("final :",remain, mem)
                if mem[-1] > remain :
                    # 代表重複算過了
                    return
                # print("pass :",remain, mem, count[remain])
                if mem[0] == mem[1] and mem[1] == remain :
                    add_ans(((count[mem[0]])*(count[mem[1]]-1)*(count[remain]-2))//6)
                elif mem[0] == mem[1]:
                    add_ans(((count[mem[0]])*(count[mem[1]]-1))//2*(count[remain]))
                elif mem[1] == remain:
                    add_ans((count[mem[0]])*((count[mem[1]])*(count[remain]-1))//2)
                else :
                    add_ans((count[mem[0]])*(count[mem[1]])*(count[remain]))
            else :
                for i in range(start, len(dist_list)):
                    now = dist_list[i]
                    recur(i, cou-1, remain-now, mem+[now])

        recur(0, 3, target, [])
        return ans

# # given ans
# # 結果 given ans 也是列舉了每一種例外狀況...
# 一開始我以為List有sort 但沒有 所以這樣應該比較快
    # for i, x in count.items():
    #     for j, y in count.items():
# class Solution:
#     def threeSumMulti(self, A, target):
#         kMod = int(1e9) + 7
#         ans = 0
#         count = Counter(A)

#         for i, x in count.items():
#             for j, y in count.items():
#                 k = target - i - j
#                 if k not in count:
#                     continue
#                 if i == j and j == k:
#                     ans = (ans + x * (x - 1) * (x - 2) // 6) % kMod
#                 elif i == j and j != k:
#                     ans = (ans + x * (x - 1) // 2 * count[k]) % kMod
#                 elif i < j and j < k:
#                     ans = (ans + x * y * count[k]) % kMod

#         return ans % kMod

# given ans 每次加入一個項目
# 一開始有想到 只是不知道怎麼實現
# 有辦法實現 不過很慢 9500 ms
# 但是是個想法
# class Solution:
#     def threeSumMulti(self, A, target):
#         c = Counter()

#         ans = 0
#         mod = 1000000007
#         for i, num in enumerate(A) :
#             # 找出加入的這個數字 搭配有多少組合
#             ans = (ans + c[target - num]) % mod

#             # 加入這個數字有可能的搭配
#             for j in range(0, i):
#                 c[A[j]+num] += 1
#         return ans

s = Solution()
# print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
print(s.threeSumMulti([1,1,2,2,2,2], 5))
# print(s.threeSumMulti([3,3,1], 7))

