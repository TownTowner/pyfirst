import numpy as np

### where
# 查找值为 4 的索引
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(f"where: {x = }")  # 输出：(array([3, 5, 6], dtype=int64),)

### searchsorted
# 查找应在其中插入值 7 的索引:
# 实例解析: 应该在索引 1 上插入数字 7，以保持排序顺序。
# 该方法从左侧开始搜索，并返回第一个索引，其中数字 7 不再大于下一个值。
# 从右侧搜索
#   默认情况下，返回最左边的索引，但是我们可以给定 side='right'，以返回最右边的索引
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(f"searchsorted: {x = }")  # 输出：1
# 从右侧搜索
x = np.searchsorted(arr, 7, side="right")
print(f"searchsorted right: {x = }")  # 输出：2

# 多个值
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(f"searchsorted multiple values: {x = }")  # 输出：[1 2 3]


### sort
# 对数组进行排序
arr = np.array([3, 2, 0, 1])
newarr = np.sort(arr)
print(f"sort: {newarr = }")  # 输出：array([0, 1, 2, 3])
# 对数组进行排序，保留原始数组
arr = np.array([3, 2, 0, 1])
newarr = np.sort(arr, kind="mergesort")  # 合并排序
print(f"sort mergesort: {newarr = }")  # 输出：array([0, 1, 2, 3])

# 2-D 数组
arr = np.array([[3, 2, 4], [5, 0, 1]])
newarr = np.sort(arr)  # 对每一行进行排序
print(f"sort 2-D array: {newarr = }")  # 输出：array([[2, 3, 4], [0, 1, 5]])
# 对每一列进行排序
newarr = np.sort(arr, axis=0)  # 对每一列进行排序
print(f"sort 2-D array axis=0: {newarr = }")  # 输出：array([[3, 0, 1], [5, 2, 4]])
