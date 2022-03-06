# # break
# for x in range(4) :
#     if x == 3 :
#         break
#     print(x)

# # ------------------------------------ 
# # break 只會 break 一層
# for x in range(4) :
#     for y in range(3):
#         if x == 2 :
#             break
#         print(x)
#     print("AAAAAA")

# # ------------------------------------ 
# # break 邏輯
# for x in range(5) :
#     for y in range(5):
#         if x == y :
#             break
#         print(x,end="")
#     print("")

# # ------------------------------------ 
# # break 邏輯
# x_in = 8   # 如果 x_in = 4 或 6 或 8 呢?
# y_in = 3   # 如果 y_in = 3 或 5 或 7 或 9 呢?
# for x in range(x_in) :  
#     for y in range(y_in):
#         if x == y :
#             break
#         print(x,end="")
#     print("")

# # ------------------------------------
# # continue
# for x in range(4) :
#     if x == 3 :
#         continue
#     print(x)

# # ------------------------------------ 
# # continue 也只會 continue 一層
# for x in range(4) :
#     for y in range(3) :
#         if x == 2 :
#             continue
#         print(x)
#     print("AAAAAA")
#------------------------------------ 
















