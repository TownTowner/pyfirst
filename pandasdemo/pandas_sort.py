from numpy import int32
import pandas as pd

weather_file_path = "./data/weather_beijing_2024.xlsx"
df = pd.read_excel(weather_file_path)

# 排序
# dataFrame.sort_values
# df.sort_values(
#     by="high_temp(℃)", ascending=False, inplace=True
# )  # 按照最高气温降序排序，inplace=True表示直接修改原DataFrame
df.sort_values(
    by=["high_temp(℃)", "low_temp(℃)"], ascending=[False, True], inplace=True
)  # 按照最高气温降序排序，inplace=True表示直接修改原DataFrame
print(df.head(10))

# series.sort_values
# low_series = df["low_temp(℃)"].copy()
# low_series.sort_values(
#     ascending=True, inplace=True
# )  # 按照最低气温升序排序，inplace=True表示直接修改原DataFrame
# print(low_series.head(10))
