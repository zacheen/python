# try catch

ll = [1,2,3]
try :
    ll.remove(100)
except ValueError :
    print("didnt have this value")
except Exception :
    print("i dont know what wrong happen")
