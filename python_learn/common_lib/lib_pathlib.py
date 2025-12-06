# This is the first line

from pathlib import Path

# 當下檔案
this_file_path = Path(__file__).resolve()
print(this_file_path)

# 當下檔案的目錄
this_file_dir = Path(__file__).resolve().parent
print(this_file_dir)

cwd_dir = Path.cwd()
print(cwd_dir)

# 確認檔案或目錄存不存在
print(this_file_path.exists())  # T
print(this_file_dir.exists())   # T
# 確認是不是一個資料夾
print(this_file_path.is_dir())  # F
print(this_file_dir.is_dir())   # T
# 確認是不是一個檔案
print(this_file_path.is_file())  # T
print(this_file_dir.is_file())   # F

# 上一層路徑的名稱
print("parent:", this_file_path.parent)
print("parent:", this_file_dir.parent)
# 檔名不含副檔名 或 資料夾最後一層的名稱
print("stem:", this_file_path.stem)
print("stem:", this_file_dir.stem)
# 副檔名
print("suffix:", this_file_path.suffix)
print("suffix:", this_file_dir.suffix)
# name = stem + suffix
print("name:", this_file_path.name)
print("name:", this_file_dir.name)

# 組裝 (會直接加在後面 不管有沒有副檔名)
print("extra_folder:", this_file_path / "extra_folder")
print("extra_folder:", this_file_dir / "extra_folder")

# 只修改副檔名
print("with_suffix:", this_file_path.with_suffix(".txt"))

# 只修改檔案名稱
print("with_stem:", this_file_path.with_stem("new_name"))

# 檔案名稱加長
print("append:", this_file_path.with_stem(this_file_path.stem + "_new"))

with this_file_path.open('r', encoding="utf8") as f: 
    print(f.readline())
