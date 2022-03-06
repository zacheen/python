server_dst = "D:\\dont_move\\identify_for_import\\member_information.csv"
rev_dst = "D:\\dont_move\\identify_for_import\\member_information_2.csv"

read_in = []
with open(server_dst, "r", encoding='UTF-8') as read_server_dst_f :
    while(True):
        read = read_server_dst_f.readline()
        if read.strip() == "":
            break
        else :
            read_in.append(read)

with open(rev_dst, "w", encoding='UTF-8') as rev_dst_f :
    file_len = len(read_in)
    
    for x in range(file_len):
        rev_dst_f.write(read_in[file_len-x-1])