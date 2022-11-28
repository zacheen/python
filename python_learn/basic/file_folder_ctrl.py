import os
import shutil

# 單層資料夾
path_one_folder = r'.\test_folder'
# 如果已經存在會跳錯
if not os.path.isdir(path_one_folder):
    os.mkdir(path_one_folder)

# 多層資料夾
path_multi_folder_outside = r'.\test_folder2'
path_multi_folder_inside = path_multi_folder_outside + r'\test_folder2\test_folder2'
if not os.path.isdir(path_multi_folder_inside):
    os.makedirs(path_multi_folder_inside)

# ...\git\python\python_learn
# 檢查是否創建成功
input()

shutil.rmtree(path_one_folder)
shutil.rmtree(path_multi_folder_outside)

# 這個是刪除檔案 如果是資料夾會出錯
# os.remove(path_one_folder)
# os.remove(path_multi_folder_outside)

