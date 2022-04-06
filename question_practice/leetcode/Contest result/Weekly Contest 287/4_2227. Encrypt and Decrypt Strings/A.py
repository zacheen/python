# my 看起來答案是對的 但Time Limit Exceeded
# class Encrypter:
#     def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
#         self.en_dict = {}
#         self.de_dict = defaultdict(list)
#         self.dictionary = dictionary
        
#         for indx, val in enumerate(keys) :
#             self.en_dict[val] = values[indx]
#             self.de_dict[values[indx]].append(val)

#     def encrypt(self, word1: str):
#         ret = ""
#         for w in word1 :
#             ret = ret + self.en_dict[w]
#         return ret

#     # 這裡應該要memery
#     # memery 從後面到目前這個位置所有的可能性
#     def comb(self, w, now_word):
#         if w == "" :
#             # print(now_word)
#             if now_word in self.dictionary :
#                 self.ret_count += 1
#             return

#         for i in range(1,len(w)+1):
#             for each_poss in self.de_dict[ w[:i] ] :
#                 self.comb(w[i:], now_word+each_poss)
#         return
    
#     def decrypt(self, word2: str):
#         self.ret_count = 0
#         self.comb(word2, "")
#         return self.ret_count

from collections import defaultdict
# given ans
# 這是一個好方法
# 但我感覺有點違背題義 有點像特殊解
# 但大家都好像都這樣做...
class Encrypter:
    def __init__(self, keys, values, dictionary):
        self.d = defaultdict(int)
        self.m = {}
        # 紀錄加解密對應字串
        for i, j in zip(keys, values):
            self.m[i] = j
        
        # 計算各個 dictionary 裡面的字串加密後的結果
        # 並統計 加密後的字串 有幾種經過計算後會變成這個結果
        # (相對應只要尋找結果 就代表其中幾種排列組合在此dictionary中)
        for i in dictionary:
            l = []
            for x in i:
                l.append(self.m[x])
            self.d[''.join(l)] += 1

    def encrypt(self, word1):
        l = []
        for x in word1:
            l.append(self.m[x])
        return ''.join(l)

    def decrypt(self, word2):
        return self.d[word2]


obj = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
for s in ["abcd"] :
    print(s,"after encrypt :",obj.encrypt(s))
for s in ["eizfeiam"] :
    print(s,"after decrypt :",obj.decrypt(s))



