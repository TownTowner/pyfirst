from numpy import int32
import pandas as pd

# Read a CSV file into a DataFrame
# csvpath = "./data/demo.csv"
# ratings = pd.read_csv(csvpath)
# print(ratings.head())  # 输出前几行数据

# print(ratings.shape)  # 输出数据的行数和列数

weather_file_path = "./data/weather_beijing_2024.xlsx"
df = pd.read_excel(weather_file_path)
# print(df.head())  # 输出前几行数据
# print(df.shape)  # 输出数据的行数和列数

# df.loc[:, "high_temp(℃)"] = df["high_temp(℃)"].replace("℃", "").astype(int32)
# df.loc[:, "low_temp(℃)"] = df["low_temp(℃)"].replace("℃", "").astype(int32)

# 新增一列
# 1. 直接赋值
# df.loc[:, "diff_temp(℃)"] = df["high_temp(℃)"] - df["low_temp(℃)"]


# 2. apply
def is_high_or_low_temp(row):
    if row["high_temp(℃)"] > 30:
        return "High"
    elif row["low_temp(℃)"] < 0:
        return "Low"
    else:
        return "Normal"


# df.loc[:, "temp_status"] = df.apply(is_high_or_low_temp, axis=1)
# print(df["temp_status"].value_counts())

# 3. assign -> new instance of DataFrame with new columns
# df = df.assign(
#     high_temp_huashi=lambda x: x["high_temp(℃)"] * 9 / 5 + 32,
#     low_temp_huashi=lambda x: x["low_temp(℃)"] * 9 / 5 + 32,
# )

# 4. loc with condition
# df["temp_status_info"] = ""
# df.loc[df["high_temp(℃)"] - df["low_temp(℃)"] > 10, "temp_status_info"] = "温差大"
# df.loc[df["high_temp(℃)"] - df["low_temp(℃)"] <= 10, "temp_status_info"] = "温差正常"


print(df.head())
