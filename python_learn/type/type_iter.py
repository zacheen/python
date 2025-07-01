
# Iterator iterator

ll = [1,2,3]

# init
list_iter = iter(ll)
# print(dir(list_iter))

# next 取出第一個項目 同時iterator只到下一個項目
print("next : ",next(list_iter))
print("next : ",next(list_iter))

# hasNext 沒有 Python 的 iter 沒有 hasNext
# 所以終止有兩種方法
# # 方法1 使用 default_value
def next_default(list_iter) :
    default_value = None
    ret = next(list_iter, None)
    if ret != None :
        print(ret)
    else :
        print("stop")
next_default(list_iter)
next_default(list_iter)
# # 方法2 使用 try catch
# def next_try(list_iter) :
#     try :
#         print(next(list_iter))
#     except StopIteration :
#         print("stop")
# next_try(list_iter)
# next_try(list_iter)

## 較少用到的方法 ################################
# <跳過 找過的位置>
t = iter("".join(c+str(i) for i,c in enumerate("abccabcdcc")))
for i in range(5) :
    print(i, "c" in t) # 在現在 t 指到的位置後面還有沒有 "3"
    print("now_i",next(t))
