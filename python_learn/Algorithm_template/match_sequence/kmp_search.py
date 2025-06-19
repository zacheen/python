# kmp_search, Knuth-Morris-Pratt Algorithm, KMP Algorithm
    
# generate Longest Prefix Suffix Table
    # LPST == Longest Prefix Suffix Table == Parital match table == fail table
# 回傳的是 區間arr[:i+1] Prefix 跟 Suffix 最長重複長度 (不包含自己)
    # 也就是如果下一個字不一樣 我可以跳過多少字不比較
def cal_LPST(s): 
    len_s = len(s)
    lps = [0] * len_s
    pref_l = 0
    i = 1
    while i < len_s:
        if s[i] == s[pref_l]: # two pointer are the same word
            pref_l += 1
            lps[i] = pref_l
            i += 1
        else: # two pointer are not the same word
            if pref_l != 0: # find fast forward position
                pref_l = lps[pref_l - 1]
            else: # no fast forward position
                lps[i] = 0
                i += 1
    return lps
# print(cal_LPST("abababzabababab"))

# 回傳 pattern 在 arr 中出現的起始位置 (要全部 pattern 符合)
def kmp_search(arr, pattern):
    if not pattern: # pattern == ""
        return range(len(arr)+1)
    len_p = len(pattern)

    # Precompute the LPS array
    lps = cal_LPST(pattern)
    
    # Search for the pattern in arr
    indices = []
    p_i = 0
    for a_i, a_c in enumerate(arr):
        while p_i > 0 and a_c != pattern[p_i]: # two pointer are not the same word
            p_i = lps[p_i - 1]
        if a_c == pattern[p_i]: # two pointer are the same word
            p_i += 1
            if p_i == len_p: # Match found
                indices.append(a_i-p_i+1) # cal front indx 
                p_i = lps[p_i - 1]
    return indices

# print(kmp_search("aaabaabab", "ab"))
# print(kmp_search("aaabcaababcabcababac", "abc"))
# print(kmp_search("aaabcabababcabcabcabac", "abcab"))

# 回傳 pattern 在 arr 中各個位置 相同prefix的長度
# 查看 "Z-algorithm" 的 prefix_len
