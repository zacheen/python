# "Z-algorithm" "longest common prefix"
# 可以用較快的速度找到每個位置的'自己的'prefix長度
# 詳細教學 : https://www.youtube.com/watch?v=2EqYY0c--QI

# 詳解
# return[i] 是起始為 i 的最大長度prefix
def lcp(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i+1, z[i-z_box_l])
                # z_box_r-i+1  : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
        while i + same_len < len_arr and arr[same_len] == arr[i+same_len]:
            # 這裡順序不能錯
            z_box_l = i
            z_box_r = i + same_len
            same_len += 1
        z[i] = same_len
    return z
        
print(lcp("abababzabababab"))
print(lcp("aabab")) # 第三個a的 prefix 其實只有1
print(lcp("aaabaab"))
print(lcp([1,1,1,2,1,1,2]))

# 雙層
def lcp_2D(arr) :
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

# # print(lcp_2D([1,1,1,2,1,1,2]))