# 有點像 generator
    # 條件
    # 有 def __len__(self):
    # 有 def __getitem__(self, idx):
# 不過 
    # 可以重複呼叫 
    # 且可以跳著呼叫
    # 也可以有重複的項目

class DataLoader():
    def __init__(self, file_list, file_reader):
        self.file_list = file_list
        self.file_reader = file_reader
        
    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        return self.file_reader(self.file_list[idx])
    
# 用讀取 txt 當範例
class FileReader():
    def __init__(self, order, file_name):
        self.order = order
        self.file_name = file_name
        
    def __len__(self):
        return len(self.order)

    def __getitem__(self, idx):
        with open(self.file_name, "r") as f:
            f.seek((self.order[idx]-1)*8, 0)
            return f.readline()

fileReader = FileReader([3,2,5,1,4,1], r".\python_learn\big_project\DataLoader_demo.txt")
print(fileReader[0], end = "")
print(fileReader[0], end = "") # 可以重複呼叫 
print(fileReader[2], end = "") # 且可以跳著呼叫
print("print for each")
list(print(txt, end = "") for txt in fileReader)