# "Z-algorithm" "longest common prefix" "LCP" O(n)
# 可以用較快的速度找到每個位置的'自己的'prefix長度
# 詳細教學 : https://www.youtube.com/watch?v=2EqYY0c--QI
#            https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm

# 詳解
# return[i] 是起始為 i 的最大長度prefix
def LCP(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i, z[i-z_box_l])
                # z_box_r-i    : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
                       # 如果arr還有位置   and r_p 這個位置與 prefix(same_len) 相同
        while (r_p:=i+same_len) < len_arr and arr[same_len] == arr[r_p]:
            same_len += 1
        z[i] = same_len
        if r_p > z_box_r : # 目前 r_p 到更遠的位置 > 更新box
            z_box_l = i
            z_box_r = r_p
    return z
   
# print(LCP("abababzabababab"))
print(LCP("azbazbzaz"))
# print(LCP("aabab")) # 第三個a的 prefix 其實只有1
# print(LCP("aaabaab"))
# print(LCP([1,1,1,2,1,1,2]))

# 回傳 pattern 在 arr 中各個位置 相同prefix的長度
def prefix_len(arr, pattern) :
    concat = pattern + "$" + arr  # 使用 "$" 避免 pattern 影響 arr
    Z = LCP(concat)
    return Z[len(pattern) + 1:]

# classic # 796. Rotate String
# https://leetcode.com/problems/rotate-string/description/

# 雙層 (以各自位置為開頭 做lcp)
    # ret[以i為開頭][位置j] 的 prefix 有多長
def LCP_2D(arr) :
    len_num = len(arr)
    z = [[0]*len_num for _ in range(len_num)]
    for n1, this_z in enumerate(z):
        z_box_l = z_box_r = n1
        for n2 in range(n1+1, len_num):
            same_len = 0
            if n2 <= z_box_r :
                same_len = min(z_box_r-n2+1, this_z[n2-z_box_l])
            while n2 + same_len < len_num and arr[n1+same_len] == arr[n2+same_len]:
                # 這裡順序不能錯
                z_box_l = n2
                z_box_r = n2 + same_len
                same_len += 1
            this_z[n2] = same_len
    return z
# print(LCP_2D([1,1,1,2,1,1,2]))

# 如果要全部位置的 lcp, 要用 dp 會比較快
# 2430. Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/description/
def LCP_all(arr) :
    len_n = len(arr)
    lcp = [[0]*(len_n+1) for _ in range(len_n+1)]
    for i in range(len_n-1,-1,-1):
        for j in range(i + 1, len_n):
            if arr[i] == arr[j]:
                lcp[i][j] = lcp[i + 1][j + 1] + 1
    return lcp

test_s = "aaabaab"
ret = LCP_all(test_s)
for i, LCP_all_lcp in enumerate(ret) :
    LCP_all_lcp.pop() # 移除防止 index out of bound 的 0
    LCP_func = LCP(test_s[i:])
    LCP_func = [0]*i + LCP_func
    print(i, LCP_all_lcp)
    print(i, LCP_func)
    if LCP_all_lcp != LCP_func :
        print("not same")