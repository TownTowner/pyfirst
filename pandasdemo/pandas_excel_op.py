import os
from os.path import isfile
import pandas as pd


work_path = "./data/split_to_merge"
splits_path = f"{work_path}/splits"

if not os.path.exists(splits_path):
    os.makedirs(splits_path)

# 读取Excel文件
df = pd.read_excel(f"{work_path}/data_level.xlsx")
print(df)

row_count = df.shape[0]  # 行数
users = ["A", "B", "C"]
split_count = len(users)  # 分割文件数量
split_size = row_count // split_count + 1  # 每个文件的行数
print(f"split_size: {split_size}")


def split():
    df_subs = []
    for idx, name in enumerate(users):
        start = idx * split_size
        end = min(
            (idx + 1) * split_size, row_count
        )  # 最后一个文件可能会不足split_size行
        df_sub = df.iloc[start:end]  # 取第i个文件的数据
        df_sub.to_excel(
            f"{splits_path}/data_level_{idx}_{name}.xlsx", index=False
        )  # 保存到新的Excel文件中，index=False表示不保存行索引
        df_subs.append(df_sub)  # 保存到列表中


def merge():
    df_subs = []
    for file_name in os.listdir(splits_path):  # 遍历文件夹中的所有文件
        if not os.path.isfile(f"{splits_path}/{file_name}") or not file_name.endswith(
            ".xlsx"
        ):  # 只处理Excel文件
            continue

        username = file_name.replace(".xlsx", "").split("_")[3]  # 取用户名
        df_sub = pd.read_excel(f"{splits_path}/{file_name}")  # 读取第i个文件的数据
        df_sub["username"] = username  # 增加一个列，值为用户名
        df_subs.append(df_sub)  # 保存到列表中:

    df_merge = pd.concat(
        df_subs, ignore_index=True
    )  # 合并所有文件的数据，ignore_index=True表示忽略原来的索引，重新生成索引
    df_merge.to_excel(
        f"{work_path}/data_level_merge.xlsx", index=False
    )  # 保存到新的Excel文件中，index=False表示不保存行索引


# split()
merge()
