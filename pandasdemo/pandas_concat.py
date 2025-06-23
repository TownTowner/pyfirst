# 使用场景：
# 批量合并相同格式的Excel、给DataFrame添加行、给DataFrame添加列
# 一句话说明concat语法：
# ·使用某种合并方式(inner/outer)
# ·沿着某个轴向(axis=0/1)
# ·把多个Pandas对象(DataFrame/Series)合并成一个。
# concat语法：pandas.concat(objs,axis=0,join='outer',ignore_index=False)
# ·objs：一个列表，内容可以是DataFrame或者Series，可以混合
# ·axis：默认是0代表按行合并，如果等于1代表按列合并
# ·join：合并的时候索引l的对齐方式，默认是outerjoin，也可以是innerjoin
# ·ignore_index：是否忽略掉原来的数据索引
# append语法:DataFrame.append(other,ignore_index=False)
# append只有按行合并，没有按列合并，相当于concat按行的简写形式
# ·other:单个dataframe、series、dict，或者列表
# ·ignore_index：是否忽略掉原来的数据索引

# pandas concat
from numpy import int32
import pandas as pd
import warnings

warnings.filterwarnings("ignore")  # 忽略警告

# 读取Excel文件
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
        "E": ["E0", "E1", "E2", "E3"],
    }
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
        "F": ["F4", "F5", "F6", "F7"],
    }
)

print(df1)
print(df2)

# 1. 按行合并, default params: axis=0, join="outer", ignore_index=False
df_concat_row_default = pd.concat([df1, df2])
print(df_concat_row_default)

# ignore_index=True, 忽略原来的索引，重新生成索引
df_concat_row = pd.concat([df1, df2], ignore_index=True)
print(df_concat_row)

# join="inner", 合并的时候只保留相同的列，默认是outer
df_concat_row_inner = pd.concat([df1, df2], join="inner")
print(df_concat_row_inner)

# 添加列
s1 = pd.Series(list(range(4)), name="G")
df_concat_col = pd.concat([df1, s1], axis=1)
print(df_concat_col)

# 添加多列
s2 = df1.apply(lambda x: x["A"] + x["B"], axis=1)
s2.name = "AB"
df_concat_col = pd.concat([df1, s1, s2], axis=1)  # df1,s1,s2可以调换顺序
print(df_concat_col)

# append
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list("AB"))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list("AB"))
print(df1)
print(df2)

# append 方法已弃用，推荐使用concat,merge,join
df_append = df1._append(df2, ignore_index=True)
print(df_append)

df_append_concat = pd.concat([df1, df2], ignore_index=True)
print(df_append_concat)
