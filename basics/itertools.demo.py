import itertools

# 示例：使用 itertools 中的函数

# bached 函数将一个可迭代对象分割成指定大小的批次
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
batches = list(itertools.batched(numbers, 3))  # 将 numbers 分割成大小为 3 的批次
print(batches)  # 输出：[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

# chain 函数将多个可迭代对象连接成一个
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, [10, 11, 12]]
combined = list(
    itertools.chain(numbers1, numbers2, numbers3)
)  # 将 numbers1、numbers2 和 numbers3 连接成一个可迭代对象
print(f"chain = {combined}")  # 输出：[1, 2, 3, 4, 5, 6, 7, [ 10, 11, 12]

# compress 函数根据选择器序列选择可迭代对象中的元素
data = [1, 2, 3, 4, 5]
selectors = [True, False, True, False, True]
selected = list(
    itertools.compress(data, selectors)
)  # 根据选择器序列选择可迭代对象中的元素
print(selected)  # 输出：[1, 3, 5]

# count 函数生成一个无限的计数器
counter = itertools.count(start=1, step=2)  # 从 1 开始，每次加 2
print(next(counter))  # 输出：1
print(next(counter))  # 输出：3
print(next(counter))  # 输出：5

# cycle 函数将一个可迭代对象循环生成
colors = ["red", "green", "blue"]
cycled_colors = itertools.cycle(colors)  # 将 colors 循环生成
print(next(cycled_colors))  # 输出：red
print(next(cycled_colors))  # 输出：green
print(next(cycled_colors))  # 输出：blue
print(next(cycled_colors))  # 输出：red，再次循环生成

# dropwhile 函数从可迭代对象中删除满足条件的元素，直到遇到不满足条件的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(
    itertools.dropwhile(lambda x: x < 5, numbers)
)  # 删除小于 5 的元素
print(filtered_numbers)  # 输出：[5, 6, 7, 8, 9, 10]

# filterfalse 函数从可迭代对象中删除满足条件的元素，直到遇到不满足条件的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(
    itertools.filterfalse(lambda x: x < 5, numbers)
)  # 删除小于 5 的元素
print(filtered_numbers)  # 输出：[5, 6, 7, 8, 9, 10]

# groupby 函数将可迭代对象中的元素按照指定的键进行分组
data = [("A", 1), ("B", 2), ("A", 3), ("B", 4), ("A", 5)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])  # 按照第一个元素进行分组
for key, group in grouped_data:
    print(key, list(group))  # 输出：A [(A, 1), (A, 3), (A, 5)] B [(B, 2), (B, 4)]

# islice 函数从可迭代对象中选择指定范围内的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_numbers = list(itertools.islice(numbers, 2, 5))  # 选择索引为 2 到 4 的元素
print(sliced_numbers)  # 输出：[3, 4, 5]

# zip_longest 函数将多个可迭代对象中的元素配对
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6, 7, 8]
zipped_numbers = list(
    itertools.zip_longest(numbers1, numbers2)  # , fillvalue="default"
)  # 将 numbers1 和 numbers2 中的元素配对
print(
    zipped_numbers
)  # 输出：[(1, 4), (2, 5), (3, 6), (None, 7), (None, 8)] # 输出：[(1, 4), (2, 5), (3, 6), ('default', 7), ('default', 8)]

# product 函数生成多个可迭代对象的笛卡尔积
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]
product = list(
    itertools.product(numbers1, numbers2, numbers3)
)  # 生成 numbers1、numbers2 和 numbers3 的笛卡尔积
print(f"{product = }")

# starmap 函数将可迭代对象中的元素作为参数传递给函数
numbers = [(1, 2), (3, 4), (5,6)]

squared_numbers = list(
    itertools.starmap(lambda x, y: x**y, numbers)
)  # 将 numbers 中的元素作为参数传递给 lambda 函数
print(squared_numbers)  # 输出：[1, 4, 9, 16, 25]

# takewhile 函数从可迭代对象中选择满足条件的元素，直到遇到不满足条件的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(
    itertools.takewhile(lambda x: x < 5, numbers)
)  # 选择小于 5 的元素
print(filtered_numbers)  # 输出：[1, 2, 3, 4]
