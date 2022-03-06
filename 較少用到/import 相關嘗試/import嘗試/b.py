print("import b")

var1 = 456
# from a import var1
# import a
# # a.var1 = 20

def g_():
    global var1
    var1 = 10

if __name__ == '__main__' :
    print("789")
    g_()
    # print(a.var1)

print("10")