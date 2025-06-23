# 抓取某网页数据
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, PageElement
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# 1. 抓取网页数据
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all("div", class_="item")

# 2. 解析网页数据
movie_list = []
for movie in movies:
    if not isinstance(movie, Tag):
        continue
    titleEle = movie.find("span", class_="title")
    title = titleEle.text if titleEle else ""
    ratingEle = movie.find("span", class_="rating_num")
    rating = ratingEle.text if ratingEle else ""
    movie_list.append({"title": title, "rating": rating})

# 3. 保存数据到xlsx文件
df = pd.DataFrame(movie_list)
df.to_excel("./data/douban_movietop250.xlsx", index=False)
print("数据已保存到movie.xlsx文件中")
