import shutil # 刪除測試檔案用

# 創建測試檔案
import os
dir_path = r"D:\test_dir"+"\\"
inside_dir = r"inside_dir"+"\\"
file_name_list = ["file.txt", "file_2.txt", "file_3.txt", "4.txt", "not_txt.tif", ]
os.mkdir(dir_path)
os.mkdir(dir_path + "this_is_folder.txt")
for file_name in file_name_list :
    fw = open(dir_path + file_name, "w")
    fw.close()
os.mkdir(dir_path+inside_dir)
fw = open(dir_path + inside_dir + "inside_file.txt", "w")
fw.close()

# |-- test_dir
# |   |-- file.txt
# |   |-- file_2.txt
# |   |-- file_3.txt
# |   |-- 4.txt
# |   |-- not_txt.tif
# |   |-- inside_dir
# |   |   -- inside_file.txt
# |   |-- this_is_folder.txt

## 方法一 glob.glob ##############################################################################
from glob import glob
# 要注意的是只要符合的檔案或資料夾就會算是答案
# 例如資料夾 但資料夾名稱是 "test.txt" 這樣也會算是結果 
find_pattern = dir_path + "*.txt" # 找出全部的 txt 檔
print("find_pattern : "+find_pattern)
find_result = glob(find_pattern)
# recursive 的參數並不是
# 印出target當下資料夾裡所有的 .txt檔 路徑 
# 注意!! 
#   沒有印出 .tif 的結果
#   也沒有印出target資料夾裡面的資料夾的檔案 (只能找到當下目錄的結果)
for indx, each_result_path in enumerate(find_result) :
    print("glob.glob result " + str(indx) + " : " + each_result_path)
####################################################################################

## 方法二 os.walk ##############################################################################
import os
# 壞處是結果 我們要自己判斷 符不符合我們要的格式
find_result = os.walk(dir_path, topdown=True, )
# 印出target資料夾底下的所有資料夾以及檔案
count_indx = 0
# dirPath : 這行啟始路徑
# dirNames : 一個 list，裡面包含了 dirPath 下所有的資料夾名稱
# fileNames : 一個 list，包含了 dirPath 下所有的檔案名稱
for dirPath, dirNames, fileNames in find_result :
    print("os.walk folder result " + str(count_indx) + " : " + dirPath)
    count_indx += 1
    for f in fileNames:
        print("os.walk file result " + str(count_indx) + " : " + os.path.join(dirPath, f))
        count_indx += 1
####################################################################################
input() # 等待
# 清除測試檔案
shutil.rmtree(dir_path)