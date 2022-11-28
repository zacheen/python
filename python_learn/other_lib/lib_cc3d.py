import cc3d
import numpy as np

init_arr = [[0, 2, 2, 1, 0, 0, 2, 0], \
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
connected_array = cc3d.connected_components(array, connectivity = tar_connectivity)
print(connected_array)

print(np.count_nonzero(np.where(connected_array==3)))
