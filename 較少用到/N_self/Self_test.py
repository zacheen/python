# 為了測試 class 的 self 到底由什麼意義

# class DOG() : 
#     remain_food = 10  # static 變數 
    
#     def __init__(self,ss) : 
#         self.flower = ss
#         self.full = False
#         self.pocket = None

#     def eat(self) :
#         DOG.remain_food = DOG.remain_food-1
#         self.full = True

#         # x = 1

#     def bark() :
#         print("旺")


# # var = FKNN_only_var() 
# # print(var.func)

# # ff = var.func

# # print(ff(1))
# # print(var.func(1))


# # print(FKNN_only_var.func2(1))

# # print(FKNN_only_var.var5)

# dog1 = DOG("花狗")
# dog2 = DOG("白狗")

# print(DOG.remain_food)
# print(dog1.full)
# print(dog2.full)

# dog1.eat()


# print(DOG.remain_food)
# print(dog1.full)
# print(dog2.full)

# dog2.eat()


# print(DOG.remain_food)
# print(dog1.full)
# print(dog2.full)


#--------------------------------------------------------------------------------------------------------

# remain_food = 10

# class DOG() : 
#     def __init__(self,ss) : 
#         self.flower = ss
#         self.full = False
#         self.pocket = None

#     def eat(self) :
#         global remain_food
#         remain_food = remain_food-1
#         self.full = True

#         # x = 1

#     def bark() :
#         print("旺")


# var = FKNN_only_var() 
# print(var.func)

# ff = var.func

# print(ff(1))
# print(var.func(1))


# print(FKNN_only_var.func2(1))

# print(FKNN_only_var.var5)

# dog1 = DOG("花狗")
# dog2 = DOG("白狗")

# print(remain_food)
# print(dog1.full)
# print(dog2.full)

# dog1.eat()


# print(remain_food)
# print(dog1.full)
# print(dog2.full)

# dog2.eat()


# print(remain_food)
# print(dog1.full)
# print(dog2.full)

#=================================================================
#global

# var = 1

# def change():
#     global var2
#     var2 = 2
#     print(var2)

# # def change2():
# #     var = 2
# #     print(var)


# print(var)
# change()
# print(var)

# print(var2)

#---------------------------------------------------
#global2

# var = [1,2]

# def change():
#     # global var
#     var2 = var
#     var2.append(3)
#     print(var2)


# print(var)
# change()
# print(var)

#---------------------------------------------------
#for local

# x = 1

# for i in range(5) :
#     del(y)
#     y = 2

# print(x)
# print(y)

#---------------------------------------------------

# def func(x):
#     print(x)

# func(1)
#---------------------------------------------------
# def func(x, y):
#     print(x,y)

# func(1,2)

# #---------------------------------------------------
# def func(x, y = 2):
#     print(x,y)

# func(1)
# func(1,9)

# #---------------------------------------------------
# def func(x = 2, y):
#     print(x,y)

# func(1)

# #---------------------------------------------------
# def func(x, y = 2, z = 2):
#     print(x,y,z)

# func(1)
# func(1,3)
# func(1,3,3)

# #---------------------------------------------------
# def func(x, y = 2, z):
#     print(x,y,z)

# func(1,3)
# #---------------------------------------------------
# A = 2
# x = "a"
# y = "b"
# z = "c"

# if A == 1 :
#     print(x)
#     print("1")
# if A == 2 :
#     print(y)
#     print("1")
# if A == 3:
#     print(z)
#     print("1")

# if A == 1 :
#     print(x)
#     print("1")
# if A == 2 :
#     print(y)
#     print("1")
# if A == 3:
#     print(z)
#     print("1")

# if A == 1 :
#     print(x)
#     print("1")
# if A == 2 :
#     print(y)
#     print("1")
# if A == 3:
#     print(z)
#     print("1")

#---------------------------------------------------
# A = 2
# x = "a"
# y = "b"
# z = "c"
# def func(A,x,y,z) :
#     if A == 1 :
#         print(x)
#         print("1")
#     if A == 2 :
#         print(y)
#         print("1")
#     if A == 3:
#         print(z)
#         print("1")

# func(A,x,y,z)
# func(A,x,y,z)
# func(A,x,y,z)

#--------------------------------------------------------
# A = 2
# x = "a"
# y = "b"
# z = "c"
# def func_x(x) :
#     print(x)
#     print("1")
# def func_y(y) :
#     print(y)
#     print("1")
# def func_z(z) :
#     print(z)
#     print("1")

# if A == 1 :  
#     func_x(x)
# elif A == 2 :  
#     func_y(y)
# elif A == 2 :  
#     func_z(z)

# #--------------------------------------------------------
# A = 2
# x = "a"
# y = "b"
# z = "c"
# def func(x) :
#     print(x)
#     print("1")

# if A == 1 :  
#     func(x)
# elif A == 2 :  
#     func(y)
# elif A == 3 :  
#     func(z)

# if A == 1 :  
#     func(x)
# elif A == 2 :  
#     func(y)
# elif A == 3 :  
#     func(z)

# if A == 1 :  
#     func(x)
# elif A == 2 :  
#     func(y)
# elif A == 3 :  
#     func(z)

# #-------------------------------------------------------------
# A = 2
# x = "a"
# y = "b"
# z = "c"
# def func(x) :
#     print(x)
#     print("1")

# def func2(A, x, y, z) : 
#     if A == 1 :  
#         func(x)
#     elif A == 2 :  
#         func(y)
#     elif A == 3 :  
#         func(z)
#     # else :
#     #     func("error")

# func2(A, x, y, z)
# func2(A, x, y, z)
# func2(A, x, y, z)
