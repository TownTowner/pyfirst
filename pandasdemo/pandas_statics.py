import pandas as pd

# 数据统计
# 1. 汇总类统计函数
file_path = "./data/weather_beijing_2024.xlsx"
df = pd.read_excel(file_path)

print(df.describe())  # 输出数据的基本统计信息
print(df["high_temp(℃)"].mean())  # 输出最高气温的平均值
print(df["high_temp(℃)"].max())  # 输出最高气温的最大值
print(df["low_temp(℃)"].min())  # 输出最低气温的最小值
# print(df["weather"].value_counts())  # 输出天气情况的计数

# 2. 唯一值类统计函数
print(df["weather"].unique())  # 输出天气情况的唯一值
print(df["weather"].nunique())  # 输出天气情况的唯一值个数量

# 3. 协方差和相关系数
print(df[["high_temp(℃)", "low_temp(℃)"]].cov())  # 输出最高气温和最低气温的协方差
print(df[["high_temp(℃)", "low_temp(℃)"]].corr())  # 输出最高气温和最低气温的相关系数

# print(df.head())  # 输出前几行数据
