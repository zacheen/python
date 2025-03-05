# actually is a kind of knapsack_01

# classic
# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence
# 1092. Shortest Common Supersequence 
# https://leetcode.com/problems/shortest-common-supersequence

def lcs(str1: str, str2: str) -> str:
    # # 0 finding longest common subsequence length
        # # but optimized to 1D array, and can't backtrack
    # dp = [0]*(len(str2)+1)
    # for c1 in str1 :
    #     new_dp = [0] # 通常可以跳過某個項目用 0, 若不要跳過用 -inf
    #     for j, c2 in enumerate(str2) :
    #         if c1 == c2 :
    #             new_dp.append(dp[j] + 1)
    #         else :
    #             new_dp.append(max(dp[j+1], new_dp[j]))
    #     dp = new_dp
    # return dp[-1] 
    
    # 1 finding longest common subsequence length
    dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
    for i, c1 in enumerate(str1) :
        for j, c2 in enumerate(str2) :
            if c1 == c2 :
                dp[i+1][j+1] = dp[i][j] + 1
            else :
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            # compare all at once
            # dp[i+1][j+1] = max(dp[i][j] + (c1==c2), dp[i][j+1], dp[i+1][j])
    # print( dp[-1][-1] )
    
    # 2 using dp to backtrack actual lcs
    act_lcs = []
    si1, si2 = len(str1)-1, len(str2)-1
    while si1 >= 0 and si2 >= 0:
        if str1[si1] == str2[si2]:
            act_lcs.append(str1[si1])
            si1 -= 1
            si2 -= 1
        elif dp[si1][si2+1] > dp[si1+1][si2]:
            si1 -= 1
        else:
            si2 -= 1
    act_lcs = "".join(reversed(act_lcs))
    # print(act_lcs)

    # 3. generating Shortest Common Supersequence 
    act_scs = []
    si1, si2 = len(str1)-1, len(str2)-1
    while si1 >= 0 and si2 >= 0:
        if str1[si1] == str2[si2]:
            act_scs.append(str1[si1])
            si1 -= 1
            si2 -= 1
        elif dp[si1][si2+1] > dp[si1+1][si2]:
            act_scs.append(str1[si1])
            si1 -= 1
        else:
            act_scs.append(str2[si2])
            si2 -= 1
    act_scs = str1[:si1+1] + str2[:si2+1] + "".join(reversed(act_scs))
    # print(act_scs)

    return dp[-1][-1], act_lcs, act_scs

print(lcs("abcde", "deabc")) # 3, abc, deabcde
print(lcs("abcde", "ace")) # 3, ace, abcde
print(lcs("abac", "cab")) # 2, ab, cabac
print(lcs("abcd", "acbd")) # (3, 'acd', 'abcbd')
print(lcs("acbd", "abcd")) # (3, 'abd', 'acbcd')