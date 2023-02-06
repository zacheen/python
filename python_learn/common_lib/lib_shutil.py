import shutil
# 複製檔案用的 lib

import os

def test_copytree():
    dir_path = r"D:\test_dir"+"\\"
    file_name = "file.txt"
    copy_dir_path = r"D:\test_dir_copy"+"\\"
    # 創建測試檔案
    os.mkdir(dir_path)
    fw = open(dir_path + file_name, "w")
    fw.close()
    # 創建了一個資料夾 裡面有放檔案
    # 複製資料夾裡面全部的檔案 到另一個資料夾
    # shutil.copytree 複製前面資料夾底面的檔案 到後面的資料夾裡面 (且後面的資料夾不可預先存在)
    shutil.copytree(dir_path,copy_dir_path)
    input() # 暫停
    # 清除測試檔案
    shutil.rmtree(dir_path)
    shutil.rmtree(copy_dir_path)

def test_copy():
    dir_path = r"D:\test_dir"+"\\"
    file_name = "file.txt"
    copy_dir_path = r"D:\test_dir_copy"+"\\"
    # 創建測試檔案
    os.mkdir(dir_path)
    os.mkdir(copy_dir_path)
    fw = open(dir_path + file_name, "w")
    fw.close()
    # 創建了兩個資料夾 其中一個資料夾裡面有放檔案
    # 從第一個資料夾裡面 複製檔案到 另外一個資料夾
    # shutil.copy 把檔案從前面的路徑 複製到後面的路徑 (只能檔案)
    shutil.copy(dir_path + file_name, copy_dir_path + file_name)
    input() # 暫停
    # 清除測試檔案
    shutil.rmtree(dir_path)
    shutil.rmtree(copy_dir_path)

# 目前不知道 copy 跟 copyfile 的差別
def test_copyfile():
    dir_path = r"D:\test_dir"+"\\"
    file_name = "file.txt"
    copy_dir_path = r"D:\test_dir_copy"+"\\"
    # 創建測試檔案
    os.mkdir(dir_path)
    os.mkdir(copy_dir_path)
    fw = open(dir_path + file_name, "w")
    fw.close()
    # 創建了兩個資料夾 其中一個資料夾裡面有放檔案
    # 從第一個資料夾裡面 複製檔案到 另外一個資料夾
    # shutil.copyfile 把檔案從前面的路徑 複製到後面的路徑 (只能檔案)
    shutil.copyfile(dir_path + file_name, copy_dir_path + file_name)
    input() # 暫停
    # 清除測試檔案
    shutil.rmtree(dir_path)
    
    shutil.rmtree(copy_dir_path)

# # test execute
#---------------
# test_copytree()
# test_copy()
test_copyfile()