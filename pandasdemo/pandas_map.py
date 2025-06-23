# 数据转换函数对比：map、apply、applymap:
# 1.map：只用于Series，实现每个值->值的映射；
# 2.apply：Series和Dataframe, 用于Series实现每个值的处理，用于Dataframe实现某个轴的Series的处理；
# 3.(deprecated,use map instead)applymap：只能用于DataFrame，用于处理该DataFrame的每个元素；

import pandas as pd
import numpy as np

# 1.map用于Series值的转换
# 实例：将股票代码英文转换成中文名字
# Series.map(dict) or Series.map(function)均可
df = pd.read_excel("data/stuck.xlsx")
print(df.head())
print(df["公司"].unique())

corp_map_obj = {"bidu": "百度", "iq": "爱奇艺", "jd": "京东", "baba": "阿里巴巴"}

df["公司map"] = df["公司"].str.lower().map(corp_map_obj)
# df["公司map_lbd"] = df["公司"].map(lambda x: corp_map_obj[x.lower()])
# print(df)

# 2. apply用于Series和DataFrame的转换
# series.apply(function)
# df["公司apply"] = df["公司"].apply(lambda x: corp_map_obj[x.lower()])
# print(df)


# dataframe.apply(function)
def corp_map(x: pd.DataFrame):
    return corp_map_obj[x["公司"].lower()]


df["公司df_apply_lbd"] = df.apply(corp_map, axis=1)  # axis=1表示按行处理
print(df)


def apply_multi_cols(d: pd.DataFrame):
    col1, col2 = d["公司"] + "1", d["公司"] + "2"
    return (col1, col2)


df[["公司1", "公司2"]] = df.apply(apply_multi_cols, axis=1, result_type="expand")
print(df.head())

# 3. (deprecated)applymap用于DataFrame的转换,(deprecated,use map instead)
# df.applymap(function)
# df = df.loc[:].applymap(lambda x: x + 1 if pd.api.types.is_number(x) else x)
# print(df)

# 4. assign, 同时添加很多列
# print(df.assign(公司1=df["公司"] + "1", 公司2=df["公司"] + "2"))

# 5. 条件选择
df.loc[df["开盘"] > 50, "isNB"] = True
df.loc[df["开盘"] <= 50, "isNB"] = False
print(df)
