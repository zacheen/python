# my ver1 Memory Limit Exceeded
class Solution:
    def addOperators(self, num, target):
        # j not include, means that mem_i_to_j_possible[i][i] always is []
        mem_i_to_j_possible = [[[] for _ in range(len(num)+1) ] for _ in range(len(num)+1)]
        
        # init mem_i_to_j_possible
        for i in range(len(num)):
            mem_i_to_j_possible[i][i+1].append((int(num[i]), num[i], 0))
                                               # num,        string, type : 
                                               #                     0-just number, 1-have mul , 2 just add
        
        for width in range(1,len(num)) :
            for i in range(len(num)-width):
                for j in range(1,width+1) :
                    for n1, n1_str, n1_type in mem_i_to_j_possible[i][i+j] :
                        for n2, n2_str, n2_type in mem_i_to_j_possible[i+j][i+width+1] :
                            # temp_sum = n1+n2
                            # if temp_sum <= target : # because have - so have to keep
                            #     mem_i_to_j_possible[i][i+width+1].append((temp_sum, str(n1_str)+"+"+str(n2_str), 2))
                            # temp_mul = n1*n2
                            # if temp_mul <= target :
                            #     mem_i_to_j_possible[i][i+width+1].append((temp_mul, str(n1_str)+"*"+str(n2_str), 1))
                            mem_i_to_j_possible[i][i+width+1].append((n1+n2, "("+str(n1_str)+"+"+str(n2_str)+")", 2))
                            mem_i_to_j_possible[i][i+width+1].append((n1-n2, "("+str(n1_str)+"-"+str(n2_str)+")", 2))
                            mul_comb_str = str(n1_str)+"*"+str(n2_str)
                            if ")*" not in mul_comb_str and "*(" not in mul_comb_str :
                                mem_i_to_j_possible[i][i+width+1].append((n1*n2, mul_comb_str, 1))
                            if n1_type == 0 and n2_type == 0 and n1_str[0] != "0":
                                comb_num = n1_str + n2_str
                                mem_i_to_j_possible[i][i+width+1].append((int(comb_num), comb_num, 0))
        # print(mem_i_to_j_possible)
        # print("len(num) :", len(num))
        ans_list = set()
        for res_sum, res_str, res_type in mem_i_to_j_possible[0][len(num)] :
            if res_sum == target :
                ans_list.add(res_str.replace("(","").replace(")",""))
        return list(ans_list)

# ver2
# 測試如果只判斷有沒有結果的時間複雜度 時間複雜度OK 但是這樣變成我要記錄 i到k所有的可能 不可行 
class Solution:
    def addOperators(self, num, target):
        # j not include, means that mem_i_to_j_possible[i][i] always is []
        mem_i_to_j_possible = [[set() for _ in range(len(num)+1) ] for _ in range(len(num)+1)]
        # 紀錄i到j數字為n有可能的字串組合 :  mem_i_to_j_num_str_set[i][j][n] 
        mem_i_to_j_num_str_set = [[{} for _ in range(len(num)+1) ] for _ in range(len(num)+1)]
        # init mem_i_to_j_possible
        for i in range(len(num)):
            # mem_i_to_j_possible[i][i+1].append((int(num[i]), num[i], 0))
            mem_i_to_j_possible[i][i+1].add((int(num[i]), 0))
                                               # num,        string, type : 
                                               #                     0-just number, 1-have mul , 2 just add
            mem_i_to_j_num_str_set[i][i+1]

        for width in range(1,len(num)) :
            for i in range(len(num)-width):
                for j in range(1,width+1) :
                    for n1, n1_type in mem_i_to_j_possible[i][i+j] :
                        for n2, n2_type in mem_i_to_j_possible[i+j][i+width+1] :
                            # 原本想要用數字大小優化 項目數量
                            # temp_sum = n1+n2
                            # if temp_sum <= target : # because have - so have to keep
                            #     mem_i_to_j_possible[i][i+width+1].append((temp_sum, str(n1_str)+"+"+str(n2_str), 2))
                            # temp_mul = n1*n2
                            # if temp_mul <= target :
                            #     mem_i_to_j_possible[i][i+width+1].append((temp_mul, str(n1_str)+"*"+str(n2_str), 1))
                            
                            # mem_i_to_j_possible[i][i+width+1].append((n1+n2, str(n1_str)+"+"+str(n2_str), 2))
                            mem_i_to_j_possible[i][i+width+1].add((n1+n2, 2))
                            mem_i_to_j_possible[i][i+width+1].add((n1-n2, 2))
                            if n1_type != 2 and n2_type != 2 :
                                mem_i_to_j_possible[i][i+width+1].add((n1*n2, 1))
                            if n1_type == 0 and n2_type == 0 and num[i] != "0":
                                comb_num = num[i:i+width+1]
                                mem_i_to_j_possible[i][i+width+1].add((int(comb_num), 0))
        # print(mem_i_to_j_possible)
        # print("len(num) :", len(num))
        ans_list = set()
        for res_sum, res_type in mem_i_to_j_possible[0][len(num)] :
            if res_sum == target :
                ans_list.add("have ans")
        return list(ans_list)

# given ans

s = Solution()

print(s.addOperators(num = "12", target = 3))
print(s.addOperators(num = "12", target = 2))
print(s.addOperators(num = "123", target = 6))
print(s.addOperators(num = "232", target = 8))
print(s.addOperators(num = "2222", target = 8))
print(s.addOperators(num = "3456237490", target = 9191))

print(s.addOperators(num = "105", target = 5))
# 發現沒有括號可以用
# 還可以是兩個數字組合 

