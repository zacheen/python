import pickle

result_count = {1 : "a", 2:{"in" : "裡面"}}

# 寫 object
with open('result_count.pickle', 'wb') as f:
    pickle.dump(result_count, f)

# 讀 object
with open('result_count.pickle', 'rb') as f:
    read_object = pickle.load(f)
    print(read_object)