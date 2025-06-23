import numpy as np

# 用索引 0 和 2 上的元素创建一个数组:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(f"bool filter:{newarr = }")  # 输出：[41 43]

## 创建数组过滤器
# 从元素值 42 开始过滤:
arr = np.array([41, 42, 43, 44])
filter_arr = []
# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(f"filter adapter:{filter_arr = }")
print(f"bool filter adapter:{newarr = }")  # 输出：[43 44]

## 直接从数组创建过滤器
# 创建一个过滤器数组，该数组返回 [True, False, True, False]:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(f"filter arr adapter:{filter_arr = }")  # 输出：[False False  True  True]
print(f"bool filter arr adapter:{newarr = }")  # 输出：[43 44]
