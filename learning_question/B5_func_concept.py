# function 的用意是為了減少重複的code 方便修改

# def func() :
#     pass

# ret = func()
# print(ret)

#-----------------------------

# i = 1
# i+=1
# print(i)
# i+=1
# print(i)
# i+=1
# print(i)
# i+=1
# print(i)
# i+=1
# print(i)

#-------------------------

# i = 1

# def func():
#     global i
#     i+=1
#     print(i)

# for x in range(3):
#     func()

#--------------------------------

for x in range(10) :

    print(x)
    if x % 2 == 0 :
        if x % 3 == 0 :
            continue
    print("---------------")

#---------------------------------------

