# check whether the function works well
# 
# 

def str_to_list (in_list) :
    # print(in_list)
    in_list = in_list.strip()
    in_list = in_list.replace("\'","")
    return in_list.split(", ")

def list_have_50 (this_list) :
    for numbers in range(5) :
        if int(this_list[numbers]) == 50 :
            return True
    return False

read_full_dst = "D:\\dont_move\\num_text.txt"
read_50_dst = "D:\\dont_move\\have_50.txt"

with open(read_full_dst, "r") as read_full_dst_f :
    with open(read_50_dst, "r") as read_50_dst_f :

        while(True) :
            may_have_50_str = read_full_dst_f.readline()

            if may_have_50_str.strip() == "" :
                print("nothing wrong  successfully end")
                break

            if list_have_50(str_to_list(may_have_50_str)) :
                have_50_str = read_50_dst_f.readline()
                if may_have_50_str == have_50_str :
                    print("both have it")
                else :
                    print("ERROR num_text.txt have 50 but have_50.txt didn't have it")
                    break
            