import time

server_dst = "D:\\dont_move\\identify_for_import\\member_information.csv"
from_client = "D:\\dont_move\\identify_for_import\\id_result.txt"
# check whether the function works well
# 
# 
def float_to_int_100(float_num):
    if type(float_num) == type("XXX.XXX") :
        float_num = float(float_num)
    elif type(float_num) == type(1.0) :
        pass
    else:
        print("wrong type")
        raise Exception
    
    float_num = float_num*100
    str_float = str(float_num)
    dot_place = str_float.index(".")
    #假設 如果有小數點以下第三位 就是出現 xx.00000001 或 xx.99999999 的情況
    # print(str_float)
    # print(dot_place)
    
    if len(str_float) == dot_place+2:
        return int(float_num)
    elif str_float[dot_place+1]=="0" and str_float[dot_place+2]=="0" :
        turn_int = int(float_num)
        # print("ori : " + str_float)
        # print("return : " + str(turn_int))
        return turn_int
    elif str_float[dot_place+1]=="9" and str_float[dot_place+2]=="9" :
        turn_int = int(float_num) + 1
        # print("ori : " + str_float)
        # print("return : " + str(turn_int))
        return turn_int
    else :
        # really is a float number
        print("error !!!!!!!!!!!!!!!  this number really is a float number")
        turn_int = int(float_num)
        # print("ori : " + str_float)
        # print("return : " + str(turn_int))
        return turn_int

def read_one_from_server(read_server_dst_f) :
    data_from_server = read_server_dst_f.readline()
    data_from_server = data_from_server.split(",")
    print(data_from_server)
    time.sleep(0.5)
    try : 
        server_initial = float_to_int_100(data_from_server[8])
        server_win = float_to_int_100(data_from_server[11])
        return (server_initial, server_win, read_server_dst_f, data_from_server)
    except :
        print("read fail from server func: " + str(data_from_server))
        return read_one_from_server(read_server_dst_f)



def read_one_from_client(read_from_client_f) :
    data_from_client_begin = read_from_client_f.readline()
    data_from_client_begin = data_from_client_begin.split(" , ")
    print(data_from_client_begin)
    data_from_client_end = read_from_client_f.readline()
    data_from_client_end = data_from_client_end.split(" , ")

    try:
        client_initial = int(data_from_client_begin[1])
        client_end = int(data_from_client_end[1])
        client_win = client_end-client_initial

        # time_begin = 

        return (client_initial, client_win, read_from_client_f, data_from_client_end)
    except : 
        print("read fail from client func : " + str(data_from_client_begin))
        return read_one_from_client(read_from_client_f)
    

def compare_num(num1, num2) :
    if num1 == num2 :
        return True
    elif num1 == num2*10 :
        return True
    elif num1 == num2*100 :
        return True
    elif num1*10 == num2 :
        return True
    elif num1*100 == num2 :
        return True
    else :
        # print("return False : " + str(num1) +"  :  "+ str(num2))
        return False

with open(server_dst, "r", encoding='UTF-8') as read_server_dst_f :
    with open(from_client, "r", encoding='UTF-8') as read_from_client_f :
        
        server_initial, server_win, read_server_dst_f, server_all_info = read_one_from_server(read_server_dst_f)
        client_initial, client_win, read_from_client_f, client_all_info = read_one_from_client(read_from_client_f)

        while(True) :
            time.sleep(1)

            if compare_num(server_initial , client_initial) :
                if compare_num(server_win , client_win) :
                    # compare next
                    print(str(client_initial) + " : pass")
                    server_initial, server_win, read_server_dst_f, server_all_info = read_one_from_server(read_server_dst_f)
                    client_initial, client_win, read_from_client_f, client_all_info = read_one_from_client(read_from_client_f)
                    continue
                else :
                    # just win wrong -> show wrong data
                    print("compare cannot match (just win price different)")
                    print("server win : " + str(server_win))
                    print(server_all_info)
                    print("client win : " + str(client_win))
                    print(client_all_info)
                    # compare next
                    server_initial, server_win, read_server_dst_f, server_all_info = read_one_from_server(read_server_dst_f)
                    client_initial, client_win, read_from_client_f, client_all_info = read_one_from_client(read_from_client_f)
                    continue
            else : 
                # initial amount wrong -> maybe miss data
                #                      -> maybe data base wrong or show wrong

                # find if is miss data
                server_initial_next, server_win_next, read_server_dst_f_next, server_all_info_next = read_one_from_server(read_server_dst_f)
                client_initial_next, client_win_next, read_from_client_f_next, client_all_info_next = read_one_from_client(read_from_client_f)

                print(str(server_initial) + "  " + str(client_initial))
                print(str(server_initial) + "  " + str(client_initial_next))
                print(str(server_initial_next) + "  " + str(client_initial))
                print(str(server_initial_next) + "  " + str(client_initial_next))

                if compare_num(server_initial_next , client_initial_next) :
                    # 進這裡通常是辨識的問題
                    # 下一筆一樣 -> 這一筆不一樣
                    print("compare cannot match (just this one)")
                    print("server : " + str(server_all_info))
                    print("client : " + str(client_all_info))
                    
                    # 因為下一筆一樣
                    # 寫回去交給下一輪判斷
                    (server_initial, server_win, read_server_dst_f, server_all_info) = (server_initial_next, server_win_next, read_server_dst_f_next, server_all_info_next)
                    (client_initial, client_win, read_from_client_f, client_all_info) = (client_initial_next, client_win_next, read_from_client_f_next, client_all_info_next)
                    continue
                
                elif compare_num(server_initial , client_initial_next) :
                    # client miss one data
                    print("client miss data : " + str(client_all_info))
                    (client_initial, client_win, read_from_client_f, client_all_info) = (client_initial_next, client_win_next, read_from_client_f_next, client_all_info_next)
                    continue

                elif compare_num(server_initial_next , client_initial) : 
                    # server miss one data
                    print(str(server_initial) + "  " + str(client_initial))
                    print("server miss data : " + str(server_all_info))
                    (server_initial, server_win, read_server_dst_f, server_all_info) = (server_initial_next, server_win_next, read_server_dst_f_next, server_all_info_next)
                    continue

                

                else:
                    print("compare cannot match (some data missing)")
                    # 一直找直到match的那一個
                    # 還沒實作
                    print("server : " + str(server_all_info))
                    print("client : " + str(client_all_info))

                    miss_data_list = []
                    # 先假設通常是client有少
                    # 在 下10筆 找有無相似的

                    find_ans = False

                    for x in range(10) :
                        server_initial_next, server_win_next, read_server_dst_f_next, server_all_info_next = read_one_from_server(read_server_dst_f)
                        
                        if compare_num(client_initial , server_initial_next) : 
                            (server_initial, server_win, read_server_dst_f, server_all_info) = (server_initial_next, server_win_next, read_server_dst_f_next, server_all_info_next)
                            # 會跳到下面cli ser更新成新的資料 再進下一輪比對
                            print("these are missing data")
                            print(miss_data_list)
                            find_ans = True
                            break
                        elif compare_num(client_initial_next , server_initial_next) : 
                            (server_initial, server_win, read_server_dst_f, server_all_info) = (server_initial_next, server_win_next, read_server_dst_f_next, server_all_info_next)
                            (client_initial, client_win, read_from_client_f, client_all_info) = (client_initial_next, client_win_next, read_from_client_f_next, client_all_info_next)
                            # 會跳到下面cli ser更新成新的資料 再進下一輪比對
                            print("these are missing data")
                            print(miss_data_list)
                            find_ans = True
                            break
                        else :
                            miss_data_list.append(server_all_info_next)
                    
                    if find_ans :
                        
                        continue
                    elif find_ans == False :
                        #真的找不到要從哪裡繼續比對
                        break

                

                
