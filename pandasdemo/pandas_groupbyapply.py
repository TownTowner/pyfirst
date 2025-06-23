import pandas as pd
import numpy as np
from pandas.api.typing import DataFrameGroupBy

df_ratings = pd.read_csv(
    "./data/movie/ratings.dat",
    sep="::",  # 分隔符
    engine="python",  # 告诉pandas使用python的解析器, 若不加，sep="::"会报错，因为pandas默认使用c引擎，c引擎不支持::分隔符
    header=None,  # 没有表头
    names=["user_id", "movie_id", "rating", "timestamp"],
)
print(df_ratings.head())

print("*" * 100)


def ratings_norm(df: pd.DataFrame):
    min = df["rating"].min()
    max = df["rating"].max()
    df["rating_norm"] = df["rating"].apply(lambda x: (x - min) / (max - min))
    return df


# DeprecationWarning: DataFrameGroupBy.apply operated on the grouping columns.
# This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation.
# Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to
# silence this warning.
df_ratings_norm = df_ratings.groupby("user_id").apply(
    ratings_norm
)  # 对每个用户的评分进行归一化，即每个用户的评分减去该用户的评分最小值，再除以该用户的评分最大值减去该用户的评分最小值，得到一个0到1之间的数值，作为该用户的评分归一化值。
print(df_ratings_norm.index)
# MultiIndex(
#     [
#         (1, 0),
#         (1, 1),
#         (1, 2),
#         ...
#         (6040, 1000206),
#         (6040, 1000207),
#         (6040, 1000208),
#     ],
#     names=["user_id", None],
#     length=1000209,
# )
print(df_ratings_norm.head())
#            user_id  movie_id  rating  timestamp  rating_norm
# user_id
# 1       0        1      1193       5  978300760          1.0
#         1        1       661       3  978302109          0.0
#         2        1       914       3  978301968          0.0
#         3        1      3408       4  978300275          0.5
#         4        1      2355       5  978824291          1.0
# # .loc[1] 通过索引直接访问行数据，这里的索引是user_id，即用户ID
print(df_ratings_norm.loc[1])  # 筛选user_id为1的用户的评分归一化值。
#     user_id  movie_id  rating  timestamp  rating_norm
# 0         1      1193       5  978300760          1.0
# 1         1       661       3  978302109          0.0
# 2         1       914       3  978301968          0.0
# 3         1      3408       4  978300275          0.5
# 4         1      2355       5  978824291          1.0
# ...
# 51        1       608       4  978301398          0.5
# 52        1      1246       4  978302091          0.5

df_ratings_norm_noindex = df_ratings.groupby("user_id", as_index=False).apply(
    ratings_norm
)  # 对每个用户的评分进行归一化，即每个用户的评分减去该用户的评分最小值，再除以该用户的评分最大值减去该用户的评分最小值，得到一个0到1之间的数值，作为该用户的评分归一化值。
print(df_ratings_norm_noindex.index)
# MultiIndex(
#     [
#         (0, 0),
#         (0, 1),
#         (0, 2),
#         ...
#         (6039, 1000206),
#         (6039, 1000207),
#         (6039, 1000208),
#     ],
#     length=1000209,
# )

print(df_ratings_norm_noindex.head())
# 注意默认索引值0
#      user_id  movie_id  rating  timestamp  rating_norm
# 0 0        1      1193       5  978300760          1.0
#   1        1       661       3  978302109          0.0
#   2        1       914       3  978301968          0.0
#   3        1      3408       4  978300275          0.5
#   4        1      2355       5  978824291          1.0
# # .loc[1] 通过索引直接访问行数据，这里的索引是默认索引，即0,1,2...
print(df_ratings_norm_noindex.loc[1])  # 筛选默认索引值为1的用户(即用户ID为2)。
# 这里可以看出user_id为1的用户为53个，因为groupby已经默认sort了，可以在上一步head(54)查看
#      user_id  movie_id  rating  timestamp  rating_norm
# 53         2      1357       5  978298709         1.00
# 54         2      3068       4  978299000         0.75
# 55         2      1537       4  978299620         0.75
# 56         2       647       3  978299351         0.50
# 57         2      2194       4  978299297         0.75
# ..       ...       ...     ...        ...          ...
# 177        2       356       5  978299686         1.00
# 178        2      1245       2  978299200         0.25
# 179        2      1246       5  978299418         1.00
# 180        2      3893       1  978299535         0.00
# 181        2      1247       5  978298652         1.00

df_ratings_norm_nogrpk = df_ratings.groupby("user_id", group_keys=False).apply(
    ratings_norm
)  # 对每个用户的评分进行归一化，即每个用户的评分减去该用户的评分最小值，再除以该用户的评分最大值减去该用户的评分最小值，得到一个0到1之间的数值，作为该用户的评分归一化值。
print(df_ratings_norm_nogrpk.index)
# Index([      0,       1,       2,       3,       4,       5,       6,       7,
#              8,       9,
#        ...
#        1000199, 1000200, 1000201, 1000202, 1000203, 1000204, 1000205, 1000206,
#        1000207, 1000208],
#       dtype='int64', length=1000209)
print(df_ratings_norm_nogrpk.head())
# 这里就可以看出结果集没有分组，因为group_keys=False
#    user_id  movie_id  rating  timestamp  rating_norm
# 0        1      1193       5  978300760          1.0
# 1        1       661       3  978302109          0.0
# 2        1       914       3  978301968          0.0
# 3        1      3408       4  978300275          0.5
# 4        1      2355       5  978824291          1.0
print(df_ratings_norm_nogrpk.loc[1])  # 筛选默认索引值为1的行。
# 因为没有分组，结果集中是原始的行，所以这里的索引是原始的索引，即0,1,2...，索引值为1的行是原始的第2行，即user_id为1的第2行
# user_id                1.0
# movie_id             661.0
# rating                 3.0
# timestamp      978302109.0
# rating_norm            0.0
# Name: 1, dtype: float64

# `group_keys`和`as_index`在pandas的groupby操作中有相似之处但也有重要区别：
# 1. **as_index参数**：
# - 控制分组键是否成为结果DataFrame的索引
# - `as_index=False`时，分组键会保留为普通列而不是索引
# - 主要用于聚合操作后的结果
# 2. **group_keys参数**：
# - 控制在使用apply方法时是否将分组键添加到结果索引中
# - `group_keys=False`会避免创建多级索引
# - 主要用于分组后应用函数时的索引处理
# 主要区别：
# - `as_index`影响的是groupby后的聚合结果
# - `group_keys`影响的是groupby后apply操作的结果索引结构

# print(
#     df_ratings_norm[df_ratings_norm["user_id"] == 1]
# )  # same as df_ratings_norm.loc[1](.grouby("user_id"),即as_index=True,group_keys=True)

print("*" * 100)


# select top N
def rating_norm_topN(df: pd.DataFrame):
    # return df.sort_values(by="rating_norm", ascending=False)[-10]
    return df.sort_values(by="rating_norm", ascending=False).head(10)


# df_ratings.apply(rating_norm_topN) # DataFrame.apply

df_ratings_norm_top_n_noindex = (
    df_ratings.groupby("user_id", as_index=False)
    .apply(ratings_norm)  # DataFrameGroupBy.apply
    .groupby("user_id")
    .apply(rating_norm_topN)
)  # 对每个用户的评分归一化值进行排序，取前10个评分归一化值最大的电影作为该用户的推荐电影。

print(df_ratings_norm_top_n_noindex.index)
# MultiIndex(
#     [
#         (1, 0, 0),
#         (1, 0, 4),
#         (1, 0, 10),
#         ...
#         (6040, 6039, 999887),
#         (6040, 6039, 1000170),
#         (6040, 6039, 1000154),
#     ],
#     names=["user_id", None, None],
#     length=60400,
# )
print(df_ratings_norm_top_n_noindex.head(20))
#               user_id  movie_id  rating  timestamp  rating_norm
# user_id
# 1       0 0          1      1193       5  978300760          1.0
#           4          1      2355       5  978824291          1.0
#           10         1       595       5  978824268          1.0
#           7          1      2804       5  978300719          1.0
#           6          1      1287       5  978302039          1.0
#           18         1      3105       5  978301713          1.0
#           14         1      1035       5  978301753          1.0
#           40         1         1       5  978824268          1.0
#           41         1      1961       5  978301590          1.0
#           36         1      1836       5  978300172          1.0
# 2       1 53         2      1357       5  978298709          1.0
#           59         2      2268       5  978299297          1.0
#           63         2      3468       5  978298542          1.0
#           68         2      3578       5  978298958          1.0
#           81         2      2236       5  978299220          1.0
#           85         2      1259       5  978298841          1.0
#           79         2      1610       5  978299809          1.0
#           88         2      1293       5  978298261          1.0
#           115        2       480       5  978299809          1.0
#           102        2      1945       5  978298458          1.0

print("*" * 100)


df_ratings_norm_top_n_nogrpk = (
    df_ratings.groupby("user_id", group_keys=False)
    .apply(ratings_norm)  # DataFrameGroupBy.apply
    .groupby("user_id")
    .apply(rating_norm_topN)
)  # 对每个用户的评分归一化值进行排序，取前10个评分归一化值最大的电影作为该用户的推荐电影。
print(df_ratings_norm_top_n_nogrpk.index)
# MultiIndex(
#     [
#         (1, 0),
#         (1, 4),
#         (1, 10),
#         ...
#         (6040, 999887),
#         (6040, 1000170),
#         (6040, 1000154),
#     ],
#     names=["user_id", None],
#     length=60400,
# )
print(df_ratings_norm_top_n_nogrpk.head(20))
#              user_id  movie_id  rating  timestamp  rating_norm
# user_id
# 1       0          1      1193       5  978300760          1.0
#         4          1      2355       5  978824291          1.0
#         10         1       595       5  978824268          1.0
#         7          1      2804       5  978300719          1.0
#         6          1      1287       5  978302039          1.0
#         18         1      3105       5  978301713          1.0
#         14         1      1035       5  978301753          1.0
#         40         1         1       5  978824268          1.0
#         41         1      1961       5  978301590          1.0
#         36         1      1836       5  978300172          1.0
# 2       53         2      1357       5  978298709          1.0
#         59         2      2268       5  978299297          1.0
#         63         2      3468       5  978298542          1.0
#         68         2      3578       5  978298958          1.0
#         81         2      2236       5  978299220          1.0
#         85         2      1259       5  978298841          1.0
#         79         2      1610       5  978299809          1.0
#         88         2      1293       5  978298261          1.0
#         115        2       480       5  978299809          1.0
#         102        2      1945       5  978298458          1.0

print("*" * 100)

# same result
df_ratings_norm_top_n_rstindex = (
    df_ratings.groupby("user_id")
    .apply(ratings_norm)  # DataFrameGroupBy.apply
    .reset_index(drop=True)
    .groupby("user_id")
    .apply(rating_norm_topN)
)  # 对每个用户的评分归一化值进行排序，取前10个评分归一化值最大的电影作为该用户的推荐电影。
print(df_ratings_norm_top_n_rstindex.index)
# MultiIndex(
#     [
#         (1, 0),
#         (1, 4),
#         (1, 10),
#         ...
#         (6040, 999887),
#         (6040, 1000170),
#         (6040, 1000154),
#     ],
#     names=["user_id", None],
#     length=60400,
# )
print(df_ratings_norm_top_n_rstindex.head(20))
#              user_id  movie_id  rating  timestamp  rating_norm
# user_id
# 1       0          1      1193       5  978300760          1.0
#         4          1      2355       5  978824291          1.0
#         10         1       595       5  978824268          1.0
#         7          1      2804       5  978300719          1.0
#         6          1      1287       5  978302039          1.0
#         18         1      3105       5  978301713          1.0
#         14         1      1035       5  978301753          1.0
#         40         1         1       5  978824268          1.0
#         41         1      1961       5  978301590          1.0
#         36         1      1836       5  978300172          1.0
# 2       53         2      1357       5  978298709          1.0
#         59         2      2268       5  978299297          1.0
#         63         2      3468       5  978298542          1.0
#         68         2      3578       5  978298958          1.0
#         81         2      2236       5  978299220          1.0
#         85         2      1259       5  978298841          1.0
#         79         2      1610       5  978299809          1.0
#         88         2      1293       5  978298261          1.0
#         115        2       480       5  978299809          1.0
#         102        2      1945       5  978298458          1.0
