from numpy import int32
import pandas as pd


file_path = "./data/student_score.xlsx"
df = pd.read_excel(file_path, skiprows=5)  # 跳过前5行

# pandas 处理缺失值

# print(df.isnull())
# 0         True  False  False  False
# 1         True   True  False  False
# 2         True   True  False  False
# 3         True   True   True   True
# 输出某一列是否有缺失值，True表示有缺失值，False表示没有缺失值
# print(df["分数"].isnull())
# 0    False
# 1    False
# print(df["分数"].notnull())  # reverse of isnull()
# 0    True
# 1    True

# 1. 删除空列 (axis=columns/1)
df.dropna(
    axis="columns", how="all", inplace=True
)  # 删除所有包含缺失值的行，inplace=True表示直接修改原DataFrame

# 2. 删除空行（axis=index/rows/0）
df.dropna(
    axis="index", how="all", inplace=True
)  # 删除所有包含缺失值的列，inplace=True表示直接修改原DataFrame

# 3. 替换空值为0分
# df.fillna(
#     {"分数": 0}, inplace=True
# )  # 将所有缺失值替换为0，inplace=True表示直接修改原DataFrame
# or
# df["分数"].fillna(
#     0, inplace=True
# )  # 将所有缺失值替换为0，inplace=True表示直接修改原DataFrame
# or
df.loc[:, "分数"] = df["分数"].fillna(
    0
)  # 将所有缺失值替换为0，inplace=True表示直接修改原DataFrame

# 4. 将姓名替换为前值
df.loc[:, "姓名"] = df["姓名"].fillna(
    method="ffill"
)  # 将所有缺失值替换为前值，inplace=True表示直接修改原DataFrame

print(df)

df.to_excel(
    "./data/student_score_processed.xlsx", index=False
)  # 保存到新的Excel文件中，index=False表示不保存行索引
