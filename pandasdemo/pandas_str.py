# pandas 字符串处理
from numpy import int32
import pandas as pd

weather_file_path = "./data/weather_beijing_2024.xlsx"
df = pd.read_excel(weather_file_path)

# .str property
# df["weather"] = df["weather"].str.replace("℃", "")
# will throw error: AttributeError: Can only use .str accessor with string values, which use np.object_ dtype in pandas

# startwith
# print(df.get("weather").str.startswith("晴"))
# print(df["weather"].str.startswith("晴"))

# call .str again on the result of the first call
# print(df["weather"].str.startswith("晴").str.replace("晴", "Sunny"))
# print(df["date"].str.replace("-", "").str.slice(0, 6))


def get_chinese_date(df_x):
    year, month, day = df_x["date"].split("-")
    return f"{year}年{month}月{day}日"


df["chinese_date"] = df.apply(get_chinese_date, axis=1)

# regex
# print(df["chinese_date"].str.replace("年", "").str.replace("月", "").str.replace("日", ""))
# print(df["chinese_date"].str.replace(r"(\d{4})年(\d{2})月(\d{2})日", r"\1-\2-\3", regex=True))
print(df["chinese_date"].str.replace("[年月日]", "", regex=True))

print(df.head())
