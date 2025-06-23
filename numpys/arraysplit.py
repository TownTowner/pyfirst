import numpy as np

# array_split : Split an array into multiple sub-arrays of equal or
#                near-equal size. Does not raise an exception if an equal division cannot be made.
# hsplit : Split array into multiple sub-arrays horizontally (column-wise).
# vsplit : Split array into multiple sub-arrays vertically (row wise).
# dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).
# concatenate : Join a sequence of arrays along an existing axis.
# stack : Join a sequence of arrays along a new axis.
# hstack : Stack arrays in sequence horizontally (column wise).
# vstack : Stack arrays in sequence vertically (row wise).
# dstack : Stack arrays in sequence depth wise (along third dimension).

arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = np.array_split(arr, 3)
print(
    f"array_split:{newarr = }"
)  # 输出：[array([1, 2, 3]), array([4, 5]), array([6, 7])]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(
    f"array_split 2-D array:{newarr = }"
)  # 输出：[array([[1, 2], [3, 4], [5, 6]]), array([[ 7,  8], [ 9, 10]]), array([[11, 12]])]

arr = np.array(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
)
newarr = np.array_split(arr, 3, axis=1)
print(
    f"array_split 2-D axis=1 array:{newarr = }"
)  # [array([[ 1],[ 4],[ 7],[10],[13],[16]]), array([[ 2],[ 5],[ 8],[11],[14],[17]]), array([[ 3],[ 6],[ 9],[12],[15],[18]])]
# equals to:
# newarr = np.hsplit(arr, 3)


# indices_or_sections : int or 1-D array
#     If indices_or_sections is an integer, N, the array will be divided into N equal arrays along axis.
# If such a split is not possible, an error is raised.
#     If indices_or_sections is a 1-D array of sorted integers, the entries indicate where along axis the array is split.
# For example, [2, 3] would, for axis=0, result in
#       ary[:2]
#       ary[2:3]
#       ary[3:]

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.split(arr, 3)
print(
    f"split can divide:{newarr = }"
)  # 输出：[array([1, 2]), array([3, 4]), array([5, 6])]


arr = np.array([1, 2, 3, 4, 5, 6, 7])
try:
    # raise error: ValueError: array split does not result in an equal division
    newarr = np.split(arr, 3)
    print(
        f"split cannot divide:{newarr = }"
    )  # 输出：[array([1, 2]), array([3, 4]), array([5, 6]), array([7])]
except ValueError as e:
    print(f"split cannot divide ValueError: {e}")

arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = np.split(arr, [2, 4])
print(
    f"split 1-D array:{newarr = }"
)  # 输出：[array([1, 2]), array([3, 4]), array([5, 6, 7])]

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr = np.hsplit(arr, 3)
print(
    f"hsplit:{arr = }"
)  # 输出：[array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]
