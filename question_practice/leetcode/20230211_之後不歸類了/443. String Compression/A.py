# my Beats 100%
class Solution(object):
    def compress(self, chars):
        self.write_indx = 0
        def change_ori(s):
            for c in s :
                chars[self.write_indx] = c
                self.write_indx += 1

        now_char = chars[0]
        count = 0
        for i in range(len(chars)) : 
            if chars[i] == now_char :
                count += 1
            else :
                change_ori(now_char)
                if count != 1 :
                    change_ori(str(count))
                now_char = chars[i]
                count = 1
        change_ori(now_char)
        if count != 1 :
            change_ori(str(count))
        return self.write_indx

# given ans
# 是先把後面一樣的字母 while 計數
    # 這樣就不用像我一樣 for 迴圈完了 還要處理還在 mem 裡面的東西

s = Solution()
in_list = ["a","a","b","b","c","c","c"]
ret_len = s.compress(in_list)
print(in_list[:ret_len])
in_list = ["a"]
ret_len = s.compress(in_list)
print(in_list[:ret_len])
in_list = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ret_len = s.compress(in_list)
print(in_list[:ret_len])



