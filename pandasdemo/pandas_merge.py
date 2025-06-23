# pandas merge
from numpy import int32
import pandas as pd

# Pandas的Merge，相当于Sql的Join，将不同的表按key关联到一个表
# merge的语法：
# pd.merge(left, right, how=inner', on=None, left_on=None, right_on=None, lef_index=False, right_index=False, sort=True, suffixes=(_x','y), copy=True,
# indicator=False, validate=None)
# ·left，right:要merge的dataframe或者有name的Series
# ·how：join类型，“eft,，'right'，'outer'，"inner'
# ·on：join的key，lef和right都需要有这个key
# ·left_on:left的df或者series的key
# ·right _on: right的df或者seires的key
# ·left_index，right_index：使用index而不是普通的column做join
# ·suffixes：两个元素的后缀，如果列有重名列，自动添加后缀，默认是(_x，'y")
# 文档地址: https://pandas.pydata.org/pandas-docs/stable/reference/ap/pandas.DataFrame.merge.html
# 本次讲解提纲：
# 1.电影数据集的join实例
# 2.理解merge时一对一、一对多、多对多的数量对齐关系
# 3.理解left join、right join、inner join、outer join的区别
# 4.如果出现非Key的字段重名怎么办

# 电影评分数据集
# 是推荐系统研究的很好的数据集
# 位于本代码目录：./datas/movie
# 包含三个文件：
# 1.用户对电影的评分数据ratings.dat
# 2.用户本身的信息数据users.dat
# 3.电影本身的数据movies.dat
# 可以关联三个表，得到一个完整的大表
# 数据集官方地址：https://grouplens.org/datasets/movielens/

rating_file_path = "./data/movie/ratings.dat"
user_file_path = "./data/movie/users.dat"
movie_file_path = "./data/movie/movies.dat"

df_ratings = pd.read_csv(
    rating_file_path,
    sep="::",  # 分隔符
    engine="python",  # 告诉pandas使用python的解析器, 若不加，sep="::"会报错，因为pandas默认使用c引擎，c引擎不支持::分隔符
    header=None,  # 没有表头
    names=["user_id", "movie_id", "rating", "timestamp"],
)
df_users = pd.read_csv(
    user_file_path,
    sep="::",  # 分隔符
    engine="python",  # 告诉pandas使用python的解析器, 若不加，sep="::"会报错，因为pandas默认使用c引擎，c引擎不支持::分隔符
    header=None,  # 没有表头
    names=["user_id", "gender", "age", "occupation", "zip_code"],
)
df_movies = pd.read_csv(
    movie_file_path,
    sep="::",  # 分隔符
    engine="python",  # 告诉pandas使用python的解析器, 若不加，sep="::"会报错，因为pandas默认使用c引擎，c引擎不支持::分隔符
    header=None,  # 没有表头
    names=["movie_id", "title", "genres"],  # movie id, title, 题材
    encoding="utf-8",  # 编码
)

print(df_ratings.head())
print(df_users.head())
print(df_movies.head())

df_ratings_users = pd.merge(
    df_ratings, df_users, on="user_id", how="inner"
)  # 合并两个表，on="user_id"表示以user_id为键，how="inner"表示取交集，即只保留两个表中都有的行，即只保留用户信息和评分信息
print(df_ratings_users.head())

df_ratings_users_movies = pd.merge(
    df_ratings_users, df_movies, on="movie_id", how="inner"
)  # 合并两个表，on="movie_id"表示以movie_id为键，how="inner"表示取交集，即只保留两个表中都有的行，即只保留用户信息、评分信息和电影信息
print(df_ratings_users_movies.head())

# left join, right join, outer join, inner join
# left join: 左连接，保留左表的所有行，右表的行根据左表的键进行匹配，若右表没有匹配的行，则对应行的值为NaN
# right join: 右连接，保留右表的所有行，左表的行根据右表的键进行匹配，若左表没有匹配的行，则对应行的值为NaN
# outer join: 外连接，保留左右表的所有行，若左右表没有匹配的行，则对应行的值为NaN
# inner join: 内连接，保留左右表的所有行，若左右表没有匹配的行，则不保留该行
# 默认为inner join，即取交集，即只保留两个表中都有的行，即只保留用户信息、评分信息和电影信息

df_left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
df_right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K4", "K5"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
print(df_left)
print(df_right)
df_left_join = pd.merge(
    df_left, df_right, on="key", how="left"
)  # 左连接，保留左表的所有行，右表的行根据左表的键进行匹配，若右表没有匹配的行，则对应行的值为NaN
print(df_left_join)

df_right_join = pd.merge(
    df_left, df_right, on="key", how="right"
)  # 右连接，保留右表的所有行，左表的行根据右表的键进行匹配，若左表没有匹配的行，则对应行的值为NaN
print(df_right_join)

df_inner_join = pd.merge(
    df_left, df_right, on="key", how="inner"
)  # 内连接，保留左右表的所有行，若左右表没有匹配的行，则不保留该行
print(df_inner_join)

df_outer_join = pd.merge(
    df_left, df_right, on="key", how="outer"
)  # 外连接，保留左右表的所有行，若左右表没有匹配的行，则对应行的值为NaN
print(df_outer_join)

# 产生笛卡尔积的结果集(4*4=16行)，（不要设置 on="key"）
df_cross_join = pd.merge(df_left, df_right, how="cross")
# 交叉连接，
print(df_cross_join)
