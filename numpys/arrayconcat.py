import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# 连接,default axis=0
arr = np.concatenate((arr1, arr2))
print(f"concatenate default axis:{ arr = }")  # 输出：[[1 2] [3 4] [5 6] [7 8]]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# 连接
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)  # 输出：[[1 2 5 6] [3 4 7 8]]

arr1 = np.array([[[1, 2], [3, 4]]])
arr2 = np.array([[[5, 6], [7, 8]]])
# 连接
arr = np.concatenate((arr1, arr2), axis=2)
print(arr)  # 输出：[[[1 2 5 6] [3 4 7 8]]]


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# default axis=0
arr = np.stack((arr1, arr2))
print(f"stack default axis:{arr = }")  # 输出：[[1 2 3] [4 5 6]]


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# 使用堆栈函数将两个数组堆叠在一起
arr = np.stack((arr1, arr2), axis=1)
print(f"stack axis=1:{arr = }")  # 输出：[[1 4] [2 5] [3 6]]


arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])
# must be the same shape
arr = np.stack((arr1, arr2), axis=2)

print(f"stack axis=2:{ arr = }")  # 输出：[[[1 4] [2 5] [3 6]]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# 沿行堆叠
arr = np.hstack((arr1, arr2))

print(f"hstack:{arr = }")  # 输出：[1 2 3 4 5 6]

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])
# 沿列堆叠
arr = np.vstack((arr1, arr2))
print(f"vstack:{arr = }")  # 输出：[[1 2 3] [4 5 6]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(f"dstack:{ arr = }")  # 输出：[[[1 4] [2 5] [3 6]]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.column_stack((arr1, arr2))
print(f"column_stack:{arr = }")  # 输出：[[1 4] [2 5] [3 6]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.row_stack((arr1, arr2))
print(f"row_stack:{arr = }")  # 输出：[[1 2 3] [4 5 6]]
