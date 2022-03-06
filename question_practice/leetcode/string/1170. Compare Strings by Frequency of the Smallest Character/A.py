class Solution:
    def numSmallerByFrequency(self, queries, words):
        from collections import Counter
        def f(s) :
            cou = Counter(s)
            minNum = 0
            minWord = "zz"
            for eachword, co in cou.items() :
                # print(eachword, co)
                if eachword < minWord :
                    minWord = eachword
                    minNum = co
            return minNum
        
        words_f = []
        for eachwords in words :
            words_f.append(f(eachwords))

        # ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
        # print(words_f)
        words_f.sort(reverse=True)
        # print(words_f)

        ans = []
        for eachqueries in queries :
            thisF = f(eachqueries)
            
            count = 0
            for word_f in words_f :
                if thisF < word_f :
                    count = count + 1
                else :
                    break
            # print("thisF count:",thisF,count)
            ans.append(count)

        return ans

# 值得學習的 coding 方式 (雖然計算 answer 沒有優化)
# 但 queries_count = [s.count(min(s)) for s in queries] 很不錯 而且這個應該比較快
# def string_freq(queries, words):
#     queries_count = [s.count(min(s)) for s in queries]
#     word_count = [w.count(min(w)) for w in words]
#     answer = [sum(q < w for w in word_count) for q in queries_count]

s = Solution()
# print(s.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
# print(s.numSmallerByFrequency( queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))
print(s.numSmallerByFrequency( queries = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"], words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]))



