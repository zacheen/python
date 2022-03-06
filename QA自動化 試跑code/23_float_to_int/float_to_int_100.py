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
        print("ori : " + str_float)
        print("return : " + str(turn_int))
        return turn_int
    elif str_float[dot_place+1]=="9" and str_float[dot_place+2]=="9" :
        turn_int = int(float_num) + 1
        print("ori : " + str_float)
        print("return : " + str(turn_int))
        return turn_int
    else :
        # really is a float number
        print("error !!!!!!!!!!!!!!!  this number really is a float number")
        turn_int = int(float_num)
        print("ori : " + str_float)
        print("return : " + str(turn_int))
        return turn_int

str_n = "641740.7"
print(float_to_int_100(str_n))

# with open("D:\\python_code\\23_float_to_int\\temp.txt", "w", encoding='UTF-8') as temp_f :
#     for x in range(10) :
#         for y in range(10) :
#             test_str = str_n + str(x) + str(y)
#             temp_f.write(test_str + "  change to : " + str(float_to_int_100(test_str) ) + "  straight change : " + str(int(float(test_str)*100)) + "\n" )
