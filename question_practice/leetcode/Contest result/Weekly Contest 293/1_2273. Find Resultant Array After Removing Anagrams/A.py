# my 
# class Solution:
#     def removeAnagrams(self, words):
#         c_list = [Counter(w) for w in words]
        
#         del_indx = []
#         for i in range(len(words)-1) :
#             if c_list[i] == c_list[i+1]:
#                 del_indx.append(i+1)
                    
#         for i in reversed(del_indx) :
#             del(words[i])
#         return words

# Count是O(N) 但比較有沒有全部一樣又是O(N) -> O(N^2)
# sort雖然是O(NlogN) 但比較字串只需要O(1)  -> O(NlogN)
# 而且比較多個 還可以hash

# given ans
class Solution:
    def removeAnagrams(self, words):
        prev = None
        res = []
        for word in words: 
            word_sort = sorted(word)
            if prev != word_sort :
                prev = word_sort
                res.append(word)
        return res
        
# 我一開始以為是只要符合條件的就要刪除 結果只需要刪除相鄰的
#         c_list = [Counter(w) for w in words]
#         del_indx = set()
#         for i in range(len(words)) :
#             for j in range(i+1, len(words)) :
#                 if c_list[i] == c_list[j]:
#                     del_indx.add(j)
                    
#         del_indx = list(del_indx)
#         del_indx.sort(reverse = True)
#         for i in del_indx :
#             del(words[i])
#         return words

s = Solution()
print(s.removeAnagrams())



