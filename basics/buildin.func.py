# exec

exec("print('exec:Hello, World!')")  # 执行字符串中的代码

# eval

x = 10
y = eval("x + 5")  # 计算字符串中的表达式
print("eval:", y)  # 输出 15


# open

file = open("data/example.txt", "r")  # 打开文件
content = file.read()  # 读取文件内容
print("open:", content)  # 输出文件内容
file.close()  # 关闭文件


# sorted

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  # 定义一个整数列表
sorted_numbers = sorted(numbers)  # 对列表进行排序
print("sorted:", sorted_numbers)  # 输出排序后的列表


# sum
numbers = [1, 2, 3, 4, 5]  # 定义一个整数列表
total = sum(numbers)  # 计算列表中所有元素的总和
print("sum:", total)  # 输出总和

# divmod
quotient, remainder = divmod(10, 3)  # 计算商和余数
print(f"divmod: {quotient = }, {remainder = }")  # 输出商和余数

# filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 定义一个整数列表
even_numbers = filter(lambda x: x % 2 == 0, numbers)  # 过滤出偶数
print(f"filter:", list(even_numbers))  # 输出偶数列表

# partial
from functools import partial
from typing import override


def multiply(x, y):
    return x * y


multiply_by_2 = partial(multiply, 2)  # 创建一个新函数，固定第一个参数为 2
result = multiply_by_2(3)  # 调用新函数，第二个参数为 3
print("partial:", result)  # 输出 6

# permutations,combinations_with_replacement,combinations
from itertools import permutations, combinations_with_replacement, combinations

items = ["A", "B", "C"]  # 定义一个列表
perms = permutations(items)  # 生成所有可能的排列
for perm in perms:  # 遍历所有排列
    print("permutations:", perm)  # 输出排列


str_comb_reps = combinations_with_replacement(
    items, 2
)  # 生成所有可能的组合，允许重复元素
for comb in str_comb_reps:  # 遍历所有组合
    print("combinations_with_replacement:", comb)  # 输出组合

str_combs = combinations(items, 2)  # 生成所有可能的组合，不允许重复元素
for comb in str_combs:  # 遍历所有组合
    print("combinations:", comb)  # 输出组合

# filedialog
# from tkinter import filedialog, Tk  # 导入 filedialog 和 Tkinter 模块
# file_path = filedialog.askopenfilename()  # 弹出文件选择对话框，选择一个文件
# print("filedialog:", file_path)  # 输出选择的文件路径

print(f"{" a bc  ".strip() = }")


class Cmd:
    def __init__(self, id=0, name="", val=""):
        self.id = id
        self.name = name
        self.val = val

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            val=data.get("val", ""),
        )

    @override
    def __repr__(self) -> str:
        return f"Cmd(id={self.id}, name={self.name}, val={self.val})"


cmd = Cmd()
ins = cmd.from_dict(dict(zip(["id", "name", "val"], [1, "tom", "val", "other"])))
print(f"{ins = }")
