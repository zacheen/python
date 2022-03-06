import time

read_dst = "D:\\dont_move\\num_text.txt"
write_dst = "D:\\dont_move\\have_50.txt"
# print(read_dst)

def str_to_list (in_list) :
    # print(in_list)
    print("changing")
    in_list = in_list.strip()
    in_list = in_list.replace("\'","")
    return in_list.split(", ")

with open(read_dst, "r") as read_dst_f :
    with open(write_dst, "w") as write_dst_f :
        while(True) :
            read_dst_f_copy = read_dst_f
            each_line = read_dst_f.readline()
            
            if each_line.strip() == "" :
                print("empty")
                read_dst_f = read_dst_f_copy
                time.sleep(5)
                continue
            each_line_list = str_to_list(each_line)

            # print(each_line_list)

            for numbers in range(5) :
                if int(each_line_list[numbers]) == 50 :
                    print(each_line)
                    write_dst_f.write(each_line)
                    write_dst_f.flush()
                    #換下一行
                    break