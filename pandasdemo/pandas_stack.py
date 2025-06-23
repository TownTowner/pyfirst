# stack, unstack, pivot
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

# warnings.filterwarnings("ignore")  # 忽略警告
mpl.rcParams["font.family"] = "SimHei"  # 显示中文

# 1. stack
# stack:DataFrame.stack（level=-1，dropna=True)，将column变成index，类似把横放的书籍变成竖放
# level=-1代表多层索引的最内层，可以通过==0、1、2指定多层索引的对应层
rating_file_path = "./data/movie/ratings.dat"

df = pd.read_csv(
    rating_file_path,
    sep="::",  # 分隔符
    engine="python",  # 告诉pandas使用python的解析器, 若不加，sep="::"会报错，因为pandas默认使用c引擎，c引擎不支持::分隔符
    header=None,  # 没有表头
    names=["user_id", "movie_id", "rating", "timestamp"],
)


df["date"] = pd.to_datetime(
    df["timestamp"], unit="s"
)  # 时间戳转换为日期时间格式，单位为秒，即1970-01-01 00:00:00

print(df.head())
print(df.dtypes)

# print(
#     df.groupby([df["date"].dt.month, "rating"])["user_id"].agg("count")
# )  # 按月份和评分分组，统计用户数，agg可以传入多个聚合函数，这里只传入一个

# # same as above
# print(
#     df.groupby([df["date"].dt.month, "rating"])["user_id"].agg("size")
# )  # 按月份和评分分组，统计用户数，agg可以传入多个聚合函数，这里只传入一个

# same as above
df_agg = df.groupby([df["date"].dt.month, "rating"])["user_id"].agg(pv=np.size)
print(df_agg)  # 按月份和评分分组，统计用户数，agg可以传入多个聚合函数，这里只传入一个

# unstack：DataFrame.unstack（level=-1，fill_value=None)，将index变成column，类似把竖放的书籍变成横放
# print(df_agg.unstack())

# df_agg.unstack().plot()  # kind="bar", stacked=True 绘制堆叠柱状图，stacked=True表示堆叠
# plt.show()  # 显示图形

# # FutureWarning: The previous implementation of stack is deprecated and will be removed in a future version of pandas. See the What's New notes for pandas 2.1.0 for details. Specify future_stack=True to adopt the new implementation and silence this warning.
# print(df_agg.unstack().stack(future_stack=True))

# print(df_agg.reset_index().head())

# pivot:DataFrame.pivot（index=None，columns=None，values=None)，指定index、columns、values实现二维透视
# pivot方法相当于对df使用set_index创建分层索引，然后调用unstack
df_pivot = df_agg.reset_index().pivot(index="date", columns="rating", values="pv")
print(df_pivot.head())
df_pivot.plot()  # kind="bar", stacked=True 绘制堆叠柱状图，stacked=True表示堆叠
plt.show()  # 显示图形
