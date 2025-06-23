# 类似SQL:
# select city,max(temperature) from city_weather groupby city;
# groupby：先对数据分组，然后在每个分组上应用聚合函数、转换函数
# 本次演示：
# 一、分组使用聚合函数做数据统计
# 二、遍历groupby的结果理解执行流程
# 三、实例分组探索天气数据

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

# warnings.filterwarnings("ignore")  # 忽略警告
mpl.rcParams["font.family"] = "SimHei"  # 显示中文

# 1.分组使用聚合函数做数据统计
df = pd.DataFrame(
    {
        "city": [
            "beijing",
            "beijing",
            "beijing",
            "shanghai",
            "shanghai",
            "shanghai",
            "shenzhen",
            "shenzhen",
            "shenzhen",
        ],
        "grade": ["A", "B", "B", "A", "C", "C", "A", "B", "C"],
        "temperature": [20, 20, 30, 40, 20, 20, 30, 20, 30],
        "humidity": np.random.randint(100, 900, 9),
        "wind_speed": np.random.randint(10, 90, 9),
    }
)

print(df)

# sum,min,max,mean,count
print(df.groupby("city").sum(numeric_only=True))  # 按城市分组，求和
print(df.groupby("city").mean(numeric_only=True))  # 按城市分组，求平均值
print(df.groupby(["city", "grade"]).mean(numeric_only=True))  # 按城市分组，求平均值
print(
    df.groupby(["city", "grade"], as_index=False).mean(numeric_only=True)
)  # 按城市分组，求平均值

# agg
print(
    df.groupby("city").agg({"temperature": "mean", "humidity": "sum"})
)  # 按城市分组，求平均值
# agg 不支持 numberic_only参数，需要手动选择数字列
# print(
#     df.groupby("city").agg([np.sum, np.mean, np.std])
# )  # 按城市分组，求平均值
# 方法1：手动选择数字列
numeric_cols = df.select_dtypes(include=["number"]).columns
agg_funcs = [np.sum, np.mean, np.std]
print(df.groupby("city")[numeric_cols].agg(agg_funcs))

# 方法2：对每个聚合函数单独指定列
print(
    df.groupby("city").agg(
        {
            "temperature": agg_funcs,
            "humidity": agg_funcs,
            "wind_speed": agg_funcs,
        }
    )
)
print(
    df.groupby(["city", "grade"], as_index=False).agg(
        {"temperature": "mean", "humidity": "sum", "wind_speed": "max"}
    )
)  # 按城市分组，求平均值
# print(df.groupby("city").max())  # 按城市分组，求最大值
# print(df.groupby("city").min())  # 按城市分组，求最小值
# print(df.groupby("city").count())  # 按城市分组，计数

for name, g in df.groupby("city"):  # 按城市分组，遍历
    print(name)  # 城市名称
    print(g)  # 城市对应的DataFrame
    print("*" * 100)  # 分隔符，方便查看

g_s = df.groupby(["city", "grade"])
for name, g in g_s:  # 按城市、分级分组，遍历
    print(name)  # 元组
    print(g)  # 元组对应的DataFrame
    print("*" * 100)  # 分隔符，方便查看

# 分组后再取数据
g_s_bb = g_s.get_group(("beijing", "B"))
print(g_s_bb)
print(type(g_s_bb))  # <class 'pandas.core.frame.DataFrame'>

g_s_bb_g = g_s["grade"]
print(g_s_bb_g)
print(type(g_s_bb_g))  # <class 'pandas.core.groupby.generic.SeriesGroupBy'>

for name, group in g_s_bb_g:
    print(name)  # ('beijing','A')
    print(group)  # 0 A
    print(type(group))  # <class 'pandas.core.series.Series'>
    print("*" * 100)  # 分隔符，方便查看

df["temperature"].plot()
# plt.show()  # 显示折线图 , 跳出窗口

ct = df.groupby("city")["temperature"]
print(ct)  # <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001D843119A90>
ct.plot()  # 按城市分组，绘制折线图
plt.show()  # 显示折线图, 跳出窗口
