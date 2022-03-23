# 其實有時候並不需要排序 說不定用hash就可以了

from collections import Counter
from collections import defaultdict
# My Runtime: 56 ms, faster than 75.05% of Python 
class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        count_list = list(count.items())
        # print(count_list)
        count_list.sort(key=lambda x: x[1], reverse=True)
        # print(count_list)
        ans = ""
        for each_word in count_list :
            ans += each_word[0]*each_word[1]
            # for i in range(each_word[1]) :
            #     ans += each_word[0]
        return ans

# given ans
# 雖然比較慢
# 但是值得思考的是 其實有時候並不需要排序 說不定用hash就可以了
# class Solution:
#     def frequencySort(self, s):
#         ans = []
#         bucket = [[] for _ in range(len(s) + 1)]

#         for c, freq in Counter(s).items():
#             bucket[freq].append(c)

#         # print(bucket)
#         for freq in reversed(range(len(bucket))):
#             for c in bucket[freq]:
#                 ans.append(c * freq)

#         return ''.join(ans)

# My 優化 ver
# 可能是因為重複的字母多 所以比較慢 Runtime: 114 ms, faster than 25.71% of Python
# class Solution:
#     def frequencySort(self, s):
#         ans = []
#         bucket = defaultdict(list)

#         for c, freq in Counter(s).items():
#             bucket[freq].append(c)

#         # 這裡使用 len(s) order(s) | 而不是使用 bucket sort之後的key order(key Number)
#         # 如果重複的東西多 那用 sort之後的key 比較好
#         for freq in reversed(range(len(s))):
#             for c in bucket[freq]:
#                 ans.append(c * freq)

#         return ''.join(ans)


s = Solution()
print(s.frequencySort("eeeee"))

