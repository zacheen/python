# cc3d 2D 3D 都可以做
import cc3d
import numpy as np

init_arr = [
 [0, 2, 2, 1, 0, 0, 2, 0], \
 [0, 2, 2, 1, 1, 2, 0, 0], \
 [2, 1, 0, 1, 2, 1, 1, 0], \
 [2, 1, 1, 1, 1, 1, 2, 1], \
 [0, 2, 0, 0, 0, 1, 0, 1], \
 [2, 0, 1, 0, 0, 1, 0, 2], \
 [2, 0, 2, 2, 2, 1, 1, 0], \
 [1, 2, 1, 0, 0, 2, 0, 1]]

array = np.array(init_arr)
# array = np.random.randint(0,3,(8,8))
print(array)

# 2D 4, 8 通
# 3D 6, 18, 26 通
tar_connectivity = 4
# 同樣的 Label 如果有相連就不會動，如果沒有相連會變成新的 label
connected_array = cc3d.connected_components(array, connectivity = tar_connectivity)
print(connected_array)
print(np.count_nonzero(np.where(connected_array==3)))

# 分開全部的 Object
# 照理來說是可以直接用拉，但是怕 mask 的結果跟 connected_components 有些規則不同，導致結果錯誤
analyze_result = cc3d.statistics(connected_array)
index = 2
print('邊界位置 : ' + str(analyze_result['bounding_boxes'][index]))
print('中心位置' + str(analyze_result['centroids'][index]))
print('體積' + str(analyze_result['voxel_counts'][index]))