# My v3 受其他人啟發 : mem 是存已經有幾個了  (吐了 好噁心的演算法)
# Runtime: 484 ms, faster than 56.66% of Python3  
class Solution:
    def getFolderNames(self, names):
        mem = {}
        
        for i, each_name in enumerate(names) :
            count = mem.get(each_name , 0)
            print(each_name,count)
            if count != 0 :
                while True :
                    this_name = each_name+ "(" + str(count) + ")"
                    if this_name not in mem :
                        # 這裡需要注意 他同時增加了兩個 key 分別給 本名 跟 本名(count)
                        mem[each_name] = count
                        mem[this_name] = 1
                        names[i] = this_name
                        break
                    count = count + 1

            else :
                mem[each_name] = 1

        return names

# my v2 改用 replace 還是 Time Limit Exceeded
# class Solution:
#     def getFolderNames(self, names):
#         mem = {}
        
#         for i, each_name in enumerate(names) :
#             # 判斷正長長度
#             before = mem.get(each_name , None)
#             if before == None :
#                 mem[each_name] = True
#                 continue

#             # 加上括號
#             count = 0
#             endStr = "(@)"
#             while True :
#                 # print("each_name :",each_name)
#                 pass_name = each_name + endStr.replace("@", str(count+1))
#                 before = mem.get(pass_name , None)
#                 if before == None :
#                     mem[pass_name] = True
#                     names[i] = pass_name
#                     break
#                 count = count + 1

#         return names

# # My v1 Time Limit Exceeded
# class Solution:
#     def getFolderNames(self, names):
#         mem = {}
        
#         for i, each_name in enumerate(names) :
#             count = 1
#             this_name = each_name
#             while True :
#                 # print("each_name :",e。ach_name)
#                 before = mem.get(each_name , None)

#                 if before == None :
#                     mem[each_name] = True
#                     names[i] = each_name
#                     break
#                 else :
#                     each_name = this_name + "(" + str(count) + ")"
#                 count = count + 1

#         return names

s = Solution()
print(s.getFolderNames(["gta","gta", 'gta(1)', 'gta', 'gta(2)']))
# print("my :",s.getFolderNames(["d(2)(4)","n","y","q(3)","q(3)","p(2)","o","k(4)","x(1)","m(1)","a(2)","z","p(2)(3)","d","g","t","n","z(3)","a","d(2)","b","t","m","r(1)(2)","k","c","p(2)(1)","c","l(1)","l","b","u","o","h(2)","p(3)(3)","d","o","c","c","v","a","g","j","m","g(4)","h","b(2)","r(3)","e","b(1)","f(4)","i","m","r","m","w(3)(4)","p","a","g","b","s","r","b(1)","f","k","q","p"]))
# print("ans:",["d(2)(4)","n","y","q(3)","q(3)(1)","p(2)","o","k(4)","x(1)","m(1)","a(2)","z","p(2)(3)","d","g","t","n(1)","z(3)","a","d(2)","b","t(1)","m","r(1)(2)","k","c","p(2)(1)","c(1)","l(1)","l","b(1)","u","o(1)","h(2)","p(3)(3)","d(1)","o(2)","c(2)","c(3)","v","a(1)","g(1)","j","m(2)","g(4)","h","b(2)","r(3)","e","b(1)(1)","f(4)","i","m(3)","r","m(4)","w(3)(4)","p","a(3)","g(2)","b(3)","s","r(1)","b(2)(2)","f","k(1)","q","p(1)"])
# print(s.getFolderNames(["p(2)","q","k","q(2)","m","z","b","c(4)(3)","o","v","l(1)(1)","w","u","k(1)(1)","n(1)","l","s(1)","i(1)","p","n","q","e","s(3)","i","k","e(2)(1)","j","h","r","x(2)(1)","b","q","i(1)","s","e","d","x(4)","u","k","r(2)","a","l(1)","n(4)","w","a(2)","u(1)(3)","l","u","o","u","w","f","c","t","l","o","e","z","o","k","m","h","r(1)(1)","h","f(3)","o(4)","s","j","h","b","f","u","d(4)","o","x(1)(4)","c","j(3)","g","k","n","d","d","x","s(3)","z","d","f","u","j","g(2)(1)","f(2)","r(1)","t(4)(2)","x(2)(4)","t","m","k","a","d(2)(1)","v","y","l","j","l(4)","i(4)(4)","y","j(1)(3)","x(3)(3)","u(3)","i","g","t","y(3)","s","g","m","j(1)","k(3)","l(3)","e(4)","x(1)(2)","u(2)","w(4)(2)","d(3)","e","w","q","u","j","n","f","h","p","u(2)(3)","a","y","r(2)(2)","x(2)(1)","i(4)","k","i","c","f","y(2)(4)","s","s","m","l","x(4)(4)","c","m(2)","e","u(2)(3)","t(1)","z(3)","a(4)(1)","v(2)","a","n","c","g","v(1)","n","h(2)","x(3)","n","g","o","o","w","q(2)","p","h","a","z(1)(1)","n(2)","a","u","a","a","v","i","z","t","b(4)(2)","b(4)(2)","x","h","n","w","n","r","a(2)(1)","a","w(4)","a","z(4)(3)","d","r(2)","e","g(1)(1)","g","b","z(2)","f","r","o","m(1)","w","o","l(3)(1)","h(3)","b(4)","n(1)(3)","o(3)(2)","p","j","f","n","o","f(2)(4)","g","t","w(2)","y","f","p","y","z(4)(2)","u","n","r(4)(3)","z","r","v(4)(4)","y(4)(3)","x(2)(1)","v","d","r","y","d(3)(2)","f","u(2)","r","v","h(2)","p","g(4)","i","j(4)(4)","c(1)","t","u","m","z","r(1)(1)","a","g(3)(3)","c(3)(3)","d(4)(1)","x","x","u","p","j(4)(1)","b(3)(3)","u(3)(4)","m","e","e(4)","q(2)(3)","d","x","w(1)","p","o","p(1)","z(1)","d(3)(2)","k","h","x(4)","g","c","x(2)","k","c(3)","k(4)(3)","m","j","r","a(4)","v(4)(4)","h","n","k(4)(1)","m","d","w(2)","m(1)(4)","i","n","x","e","v","f","o","s","r","d","m","o","z","e","p","o","o","h(3)","z","z","v","t","a","b(1)","c","b","e(4)(1)","w","t(4)","b","q","x","u(1)(2)","p","c(1)","g","u","a(1)(3)","o","a(2)","t(1)","f","t","j","z","g(1)(4)","x","a","j","v","h","h","f","f","d","d(2)(1)","g(2)(3)","y(1)(2)","u","w","p(3)(1)","a","t","k(3)(2)","r(4)","c(2)","r","u","y","u","z(2)","p(4)","n","u(4)","e","i","p","j(3)(1)","x","h","j(1)","s","y(4)","b(3)","q","u(2)(1)","h","d","n","o(3)","t(1)","y(2)","h","e","v","y(1)(2)","c","s","i","d(3)","i","t","i(4)","t","e(2)(3)","t","m(1)(2)","g","o(3)(2)","a","a(2)","b(2)","q","p","z","h","d","n","j","l","a(4)(3)","e","t(2)","a","z","m(3)","r(2)","f(3)","h(4)(2)","l","t(4)(1)","i","c","g","a","a","o(1)","k(4)","c(2)(1)","v","a","d(1)(4)","c(3)(4)","g","m","n","e","t","e(2)(2)","o","d","d","u(1)(1)","g(4)","w","b","l(3)","k(3)","e(2)","h","w","w","j(4)(3)","j","x","w","i","r","a(2)(4)","b","l","i","v(2)(3)","d","t","s(3)","x(1)","m","j","m","g(3)","w","h","o(1)","s(2)(1)","p","h","m","h","w","v(4)","f(4)(2)","k(3)(2)","o","y","t","a(4)(3)","p","y","k","r(4)(4)","n","a","v","c","l(1)","x(2)","p","x","h","d","x(4)","z","e","j(1)","t","y","o","g(3)","w(4)(3)","i","d(3)(2)","e","k","x","u","o(1)(4)","g","d","p","w(1)(1)","y(3)","a","o","z","o(1)","k","d(4)","z(4)(3)","y","i","o(4)(2)","o(4)(3)","k","a(4)(3)","u(1)","r","b","n(4)(3)","o","y","n","n(3)(2)","l","p","q","g","g","a(1)","k","x","y","y(3)(2)","r","d","b","l(3)","o","r(3)","x","v","r","s","o(2)","a","p","q(4)(1)","w(4)(2)","t","h(2)","i(4)","s(4)(2)","i","g","q","f","h","c","t","t(3)(1)","o","i","f","e","o(2)","f","s","z","s(2)","z","s","g","u","s","w","n","l","t","k(4)","a","r","q","w(1)(3)","q(4)","p","d","g(4)","f","f(3)","g","i(3)","b","g(3)","u","g","f","h","u(3)","l","m","l","c(1)","x(3)(2)","g","u","u(1)","j(3)(4)","u(4)(4)","h(2)","q","l","u(2)","u(2)","c","z(4)","f","q","q","r(3)(3)","e","z","m","u","k(2)(4)","s","x","g","c","u(3)","z","c","e","w(1)(3)","s(1)(2)","o","w","n","k(2)(4)","n","a","d","z","m","m","r(1)","o(2)","l(2)","l","g","m(4)(4)","z","t","w","i(4)","s","p","x","m","k","x","u","b","d(3)","u","z","o","o(3)","j","e","n","z(3)(4)","h","q","g","n","c","o","u","c","r","y","s","d(2)","d(2)(1)","z(1)(4)","n","i(1)","q","v","j","w","q","q","l","t","o","h","l","o","e","p","v","b","c","w","a","i","b(1)","d","z(3)","e","n","l","x(1)(1)","v","e(2)(3)","q(2)(2)","m","x","d","i","a","k","v(3)","y","w","h","t","v(2)","z","k","i","m","f","z","c","i(1)","i","x(4)","p","r(1)(3)","e","t(1)","v","f","h(4)","h","d","p","a","r","a(1)","e","f(4)","r","t(3)(3)","j","p","m","f(1)(2)","g","t","w","q(3)(2)","b(3)","o","q","m","n","u","i","o(4)","n","p(1)","g(3)","z","l","i(4)(2)","m(4)(1)","p","w","s(1)","j","v(1)","r(4)(3)","h","w(3)(4)","b(2)(4)","y","e","h(4)","n","n","z","a(1)","a","a","r","p","n","l","l","k","h","k","z","b","r","u","k","m","s(3)","l","p","y","j(4)(1)","o(1)(1)","e(2)(3)","p","d","e","l","v","h(3)","f","p","o(2)(4)","a(1)(3)","q(4)(1)","y(2)(4)","z(2)(1)","x(2)(4)","t","q(3)","m","w","h","m","m","u","s","i(3)(2)","l","h","a","d","w","v","s","e(2)","s","t","d","k","g","r(3)","j","i","j","k","w","u","z","q","h","t","n(3)","m(1)","x(4)(1)","r","s","d","i(1)","r","a","k(2)(1)","h(4)(2)","f","s","h","d(4)(4)","c","j(1)","a(2)(2)","f","h","o(2)(4)","p(2)","w","k(2)(2)","u(2)","t","b(4)(1)","b","d","h","z","i","m(3)","d","a(4)(4)","l","m","a(4)(3)","a(3)(3)","j","w","r","h(1)(3)","y","x(3)","g","v(3)(4)","c(1)(1)","w","s","c(4)","w","v","f","x(4)(4)","n","s","i","r(1)","e","h","g","r","y","i","z","n","o","d(4)(4)","w","h","z","g(3)(3)","j","l","z(3)(1)","s","p","d(3)(4)","x","n","j","v(2)(2)","v","f","f","s","n","w(3)(4)","d","g","e","p(1)(1)","l","m","h","e","j","f(4)(3)","e","d","l","u(3)","k","n","z","w(3)","r","y","n","e(3)","q(4)","a","c","s(2)(1)","c(3)","m","m(1)(3)","j(2)(3)","s","u","h","o","k","c","w","u(4)","s(1)","o","f(2)","c(2)","s(1)","j(4)","e","h","l(3)(4)","v","k(4)","u","m","m","b(3)(3)","k","o","y(1)","x(1)","v","j","k(3)","x","z","f","e","g","p","g","r","e","x","o","t","w","n(4)(1)","w","g","f(1)(1)","u","v(3)","m","y","h(1)","l","c","x","x","b","j(4)","c","f","k","w","l(4)","o","f(1)(4)","w","m(1)(1)","e(1)(3)","j(4)","s","l(3)(2)","v","x(3)(3)","p","n","y(2)","d","q","w","k","y(1)(4)","a","r(2)","s","j","i","q","a(4)","z(2)","u","a(2)","t","q","n","w","u","c","z(2)(1)","p(3)(4)","o(3)(4)","a(3)(1)","j(4)(1)","b","s","z","m(2)(4)","v","t","c","f(2)","j","f(1)(1)","d","g(2)(2)","q","r(1)","m(2)","e","n(2)(3)","u","v","m","a(2)(2)","v","r(4)","q(1)","z","n(2)(1)","t(3)","z","f","k","r(1)(3)","a","k(2)(1)","n","k(2)(1)","a(1)(1)","e","e","w","b(2)(1)","x(2)(3)","x","r(4)(2)","j","n","a","u","h(1)(3)","z","h(3)","k(3)(2)","y","g(2)","j","x(3)(3)","i","o","c","d(2)(4)","y(2)(1)","h(2)(2)","z(4)(3)","z","i(2)","j","v(1)(2)","e","o(1)(2)","g(4)(1)","t","t","t(4)(2)","k","f","y(4)(2)","t","o","m","m","z(4)(1)","i(3)","l(4)","y(4)(2)","s(4)(1)","l(1)(1)","g","v(1)","x","g(3)(4)","l(2)","c(2)","y","g","d","p","b","r(3)(1)","q(1)","c","u","t","b","i","o(2)","u","p","u(2)","k","o(4)(2)","p(2)","w(2)(3)","j(4)","b","e","j","m(4)","p","d","r(3)","i","l(4)(1)","j","g","h","n","v","n","s","i","t(2)","k(1)(4)","b","o","n","o","d(3)","r(2)(4)","i(1)","l","g","k","d","s(3)","b","f","h(3)","y","s","y","a(3)","h","v(2)","u","w(3)(3)","e","z","w","d","y","d","y(4)","s(4)","o(4)","j(2)(4)","v(1)","j","i(2)","k(1)","u","l","t(3)(3)","i(2)","w","c(2)(1)","c(3)","q","w","m","k(4)","b","s","a","o(2)","o(4)","a","u(2)","u","t","p","q","z(4)","n(2)","w(2)","u","k","h","a","x","q","a(2)","r(1)","p(3)(1)","x","v","u(2)","k","j(4)(2)","v","o(4)(3)","b","z","v","g(4)","o","u(2)","w(3)","p(2)","u","g","v","y","t","u","x","s(3)(4)","r(4)","a","y(3)(1)","j","x","t","o","e","x","j(1)","e(4)(3)","e(1)","f","d","z","j","u","h","d","u","f","p","c","c","x(3)","p","y","n","j(2)(3)","m","n(3)(3)"]))