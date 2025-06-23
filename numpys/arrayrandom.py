import numpy as np
from numpy import random as nrd
import random as rd

# 生成一个随机数
print(f"{nrd.randint(100) = }")  # 输出：一个随机整数
print(f"{rd.randint(0, 100) = }")  # 输出：一个随机整数

print(f"{ nrd.rand() = }")  # 输出：一个随机浮点数
print(f"{rd.random() = }")  # 输出：一个随机浮点数

# 生成一个随机数组
print(f"{nrd.randint(100, size=(5)) = }")  # 输出：一个包含 5 个随机整数的数组
print(
    f"{[rd.randint(0, 100) for _ in range(5)] = }"
)  # 输出：一个包含 5 个随机整数的数组

print(f"{nrd.rand(5) = }")  # 输出：一个包含 5 个随机浮点数的数组
print(f"{[rd.random() for _ in range(5)] = }")  # 输出：一个包含 5 个随机浮点数的数组

print(f"{nrd.randint(100, size=(3, 5)) = }")  # 输出：一个包含 3 行 5 列的随机整数数组
print(
    f"{[[rd.randint(0, 100) for _ in range(5)] for _ in range(3)] = }"
)  # 输出：一个包含 3 行 5 列的随机整数数组

## 从数组生成随机数
print(f"{nrd.choice([3, 5, 7, 9]) = }")  # 输出：从给定数组中随机选择一个元素
print(f"{rd.choice([3, 5, 7, 9]) = }")  # 输出：从给定数组中随机选择一个元素

print(
    f"{nrd.choice([3, 5, 7, 9], size=(3, 5)) = }"
)  # 输出：从给定数组中随机选择元素，形成一个 3 行 5 列的数组
print(
    f"{[[rd.choice([3, 5, 7, 9]) for _ in range(5)] for _ in range(3)] = }"
)  # 输出：从给定数组中随机选择元素，形成一个 3 行 5 列的数组

## 数据的概率

# 生成一个包含 10 个随机整数的数组，这些整数的概率为 0.1、0.3、0.6、0.0。
# p[] 数组的长度必须与 a[] 数组的长度相同。
# p[] 数组中的每个元素表示 a[] 数组中对应元素的概率。
# p[] 数组中的所有元素的和必须为 1。
# 如果 p[] 数组中的所有元素的和不为 1，则会抛出 ValueError 异常。
# 如果 p[] 数组中的所有元素的和为 1，则会根据 p[] 数组中的概率生成随机数。
print(f"{nrd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10)) = }")
print(f"{[rd.choice([3, 5, 7, 9]) for _ in range(10)] = }")

print(f"{nrd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3,4)) = }")
print(f"{[rd.choice([3, 5, 7, 9]) for _ in range(5) for _ in range(3)] = }")

## shuffle
# 修改原始数组
# 打乱数组的顺序
arr = np.array([1, 2, 3, 4, 5])
nrd.shuffle(arr)
print(f"nrd.shuffle: {arr = }")  # 输出：打乱后的数组
arr = np.array([1, 2, 3, 4, 5])
rd.shuffle(arr)
print(f"rd.shuffle: {arr = }")  # 输出：打乱后的数组

## permutation
# 不修改原始数组
# 生成一个包含 10 个随机整数的数组，这些整数的范围是 0 到 9。
print(f"{nrd.permutation(5) = }")
arr = np.array([1, 2, 3, 4, 5])
print(f"{nrd.permutation(arr) = },{arr = }")  # 输出：一个包含 5 个随机整数的数组

## 正态分布
# 生成一个包含 10 个随机浮点数的数组，这些浮点数的平均值为 0，标准差为 1。
print(f"{nrd.normal(size=(2, 3)) = }")  # 输出：一个包含 2 行 3 列的随机浮点数数组
print(
    f"{nrd.normal(loc=1, scale=2, size=(2, 3)) = }"
)  # 输出：一个包含 2 行 3 列的随机浮点数数组
