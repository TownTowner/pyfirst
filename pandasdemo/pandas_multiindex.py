# 分层索引Multilndex?
# ·分层索引：在一个轴向上拥有多个索引层级，可以表达更高维度数据的形式；
# ·可以更方便的进行数据筛选，如果有序则性能更好；
# ·groupby等操作的结果，如果是多KEY，结果是分层索引，需要会使用
# ·一般不需要自己创建分层索引(Multilndex有构造函数但一般不用）
# 演示数据：百度、阿里巴巴、爱奇艺、京东四家公司的10天股票数据
# 数据来自：英为财经
# https://cn.investing.com/
# 本次演示提纲：
# 一、Series的分层索引Multilndex
# 二、Series有多层索引怎样筛选数据？
# 三、DataFrame的多层索引Multilndex
# 四、DataFrame有多层索引怎样筛选数据？

import pandas as pd
import numpy as np

# 一、Series的分层索引Multilndex
df = pd.read_excel("data/stuck.xlsx")
print(df.shape)
print(df.head())
print(df["公司"].unique())  # 查看公司名称
print(df.index)  # 查看索引
print(df.columns)  # 查看列名
print(df.dtypes)  # 查看数据类型
print(df.info())  # 查看数据信息

se_corp_date = df.groupby(["公司", "日期"])["收盘"].mean()
print(se_corp_date)
print(type(se_corp_date))  # 查看类型 Series
print(se_corp_date.index)  # 查看索引 MultiIndex

print(se_corp_date.unstack())  # 分层索引转普通索引
# 日期    2023-07-10  2023-07-11  2023-07-12
# 公司
# BABA       90.56       91.79       94.00
# BIDU      142.95      143.33      148.83
# IQ          5.12        5.23        5.70
# JD         35.95       36.02       37.41
print(se_corp_date.unstack().stack())  # 普通索引转分层索引 same as se_corp_date

print(se_corp_date.reset_index())  # 分层索引转普通索引
#       公司         日期      收盘
# 0   BABA 2023-07-10   90.56
# 1   BABA 2023-07-11   91.79
# 2   BABA 2023-07-12   94.00
# 3   BIDU 2023-07-10  142.95
# 4   BIDU 2023-07-11  143.33
# 5   BIDU 2023-07-12  148.83
# 6     IQ 2023-07-10    5.12
# 7     IQ 2023-07-11    5.23
# 8     IQ 2023-07-12    5.70
# 9     JD 2023-07-10   35.95
# 10    JD 2023-07-11   36.02
# 11    JD 2023-07-12   37.41
print(
    se_corp_date.reset_index().set_index(["公司", "日期"])
)  # 普通索引转分层索引 same as se_corp_date

print("二：" + "*" * 100)

# 二、Series有多层索引怎样筛选数据？
print(se_corp_date)  # 分层索引
print(se_corp_date["BABA"])  # 筛选BABA
print(se_corp_date.loc["BABA"])  # 筛选BABA same as se_corp_date["BABA"]
print(se_corp_date["BABA", "2023-07-10"])  # 筛选BABA的2023-07-10
print(se_corp_date.loc["BABA", "2023-07-10"])  # 筛选BABA的2023-07-10
print(se_corp_date[:, "2023-07-10"])  # 筛选2023-07-10
print(
    se_corp_date.loc[:, "2023-07-10"]
)  # 筛选2023-07-10 same as se_corp_date[:, "2023-07-10"]

print("三：" + "*" * 100)

# 三、DataFrame的多层索引Multilndex
df.set_index(["公司", "日期"], inplace=True)  # 分层索引
print(df)
print(type(df))  # 查看类型 DataFrame
print(df.index)  # 查看索引 MultiIndex
print(df.sort_index())  # 排序

print("四：" + "*" * 100)

# 四、DataFrame有多层索引怎样筛选数据？
# 【重要知识】在选择数据时：
# ·元组（key1,key2)代表筛选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD，key2=2019-10-02
# ·列表[key1,key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key1=JD，key2=BIDU

print(df)  # 分层索引
print(df.loc["BABA"])  # 筛选BABA
print(df.loc["BABA", "2023-07-10"])  # 筛选BABA的2023-07-10
# print(
#     df.loc["BABA", "2023-07-10", "收盘"]
# )  # pandas.errors.IndexingError: Too many indexers
print(df.loc[("BABA", "2023-07-10"), "收盘"])  # 筛选BABA的2023-07-10
print(df.loc[("BABA", "2023-07-10"), :])  # 筛选BABA的2023-07-10

# print(df.loc["BABA", "JD"])  # KeyError: 'JD'
print(df.loc[["BABA", "JD"]])  # 筛选BABA和JD
print(df.loc[["BABA", "JD"], :])  # 筛选BABA和JD, same as last line
# print(df.loc[(["BABA", "JD"], "2023-07-10")])  # error:KeyError: '2023-07-10'
print(df.loc[(["BABA", "JD"], "2023-07-10"), :])  # 筛选BABA和JD的2023-07-10
print(
    df.loc[("BABA", ["2023-07-10", "2023-07-11"]), :]
)  # 筛选BABA的2023-07-10，2023-07-01
print(
    df.loc[(["BABA", "JD"], "2023-07-10"), "收盘"]
)  # 筛选BABA和JD的2023-07-10的收盘价
print(
    df.loc[(["BABA", "JD"], ["2023-07-10", "2023-07-11"]), :]
)  # 筛选BABA的2023-07-10，2023-07-01
print(df.loc[(slice(None), "2023-07-10"), :])  # 筛选2023-07-10
print(df.loc[:, "2023-07-10", :])  # 筛选2023-07-10, no 日期 column

print(
    df.loc[(slice(None), ["2023-07-10", "2023-07-11"]), :]
)  # 筛选2023-07-10和2023-07-11
print(
    df.loc[:, ["2023-07-10", "2023-07-11"], :]
)  # 筛选2023-07-10和2023-07-11, same as last line
