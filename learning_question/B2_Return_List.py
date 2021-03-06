# # List 的回傳 (跟連動的觀念是一樣的)
# # 此區域不需要註解
def ret(argum): # 爬其他資料
    argum.append(4) # 新增資料
    return argum

if __name__ == "__main__":
    pass # 此行也不需要註解

    # # =======================================
    # list return覆寫回去
    # ll = [1,2,3] # 爬完後的資料
    # ll = ret(ll)
    # ll = ret(ll)
    # print(ll)

    # # =======================================
    # # 執行順序 1
    # ll = [1,2,3] # 爬完後的資料
    # ll = ret(ll)
    # print(ret(ll))

    # # ========================================
    # # list 沒有覆寫回去 但因為 list 會連動
    ll = [1,2,3] # 爬完後的資料
    print(ret(ll))
    print(ret(ll))

    # # =============================================
    # # 等同上面 但少印一次
    # ll = [1,2,3] # 爬完後的資料
    # ret(ll)
    # ret(ll)
    # print(ll)

    # # ==============================================
    # # 使用 copy
    # ll = [1,2,3] # 爬完後的資料
    # print(ret(ll.copy()))
    # print(ret(ll.copy()))
    # print(ll)

    # # ==================================================
    # # 
    # ll = [1,2,3] # 爬完後的資料
    # ll = ret(ll.copy())
    # print(ret(ll.copy()))
    # print(ll)

    # # ==================================================
    # # 結論
    # # 如果希望 傳進去的 list 被改動 則要 1. 不用copy 2. 覆寫原變數 
    # ll = [1,2,3]
    # ll = ret(ll)
    # print(ll)

    # # ==================================================
    # # 如果希望 傳進去的 list "不"改動 則要 1. 用copy 2. 不覆寫原變數 
    # ll = [1,2,3]
    # ret(ll.copy())
    # print(ll)