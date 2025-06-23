# 抓取某网页数据
from bs4 import BeautifulSoup
from bs4.element import Tag, PageElement
import pandas as pd
import warnings
from playwright.sync_api import sync_playwright

warnings.filterwarnings("ignore")
col_headers = [
    "date",
    "week",
    "high_temp(℃)",
    "low_temp(℃)",
    "weather",
    "wind",
    "air",
]
col_headers_len = len(col_headers)


def getdata(url) -> list:
    weather_list = []

    # 2. 点击某个下拉菜单选项
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("#js_yearVal")  # 等待年份下拉菜单加载完成
        page.click("#js_yearVal")  # 点击年份下拉菜单
        page.click(
            "#js_yearVal+.js_selectDown  a:has-text('2024年')"
        )  # 选择年份下拉菜单选项
        for i in range(1, 13):
            page.click(f"#js_monthVal")  # 点击月份下拉菜单
            page.locator(".history-table").evaluate(
                "node=>node.remove()"
            )  # 删除已存在的表格
            page.click(
                f"#js_monthVal+.js_selectDown a:has-text('{i}月')"
            )  # 选择月份下拉菜单选项

            # 等待加载完成
            page.wait_for_selector(".history-table")

            # soup = BeautifulSoup(page.locator('.history-table').content(), "html.parser")
            mweathers = extract(
                page.locator(".history-table").inner_html()
            )  # soup.find_all("div", class_="item")
            weather_list.extend(mweathers)

    return weather_list


def extract(text: str) -> list:
    soup = BeautifulSoup(text, "html.parser")
    mweathers = soup.find_all("tr")
    mw_list = []
    # 2. 解析网页数据
    for mw in mweathers:
        # 去掉表头
        if not isinstance(mw, Tag) or mw.find("th"):
            continue
        row = {}
        tds = mw.find_all("td")

        for i in range(0, col_headers_len):
            if i == 0:
                row[col_headers[0]] = exec_col(col_headers[0], tds[i].text)
                row[col_headers[1]] = exec_col(col_headers[1], tds[i].text)
            elif i != 1:
                row[col_headers[i]] = exec_col(col_headers[i], tds[i - 1].text)
        mw_list.append(row)
    return mw_list


def exec_col(col: str, text: str) -> str:
    if col == "date":
        # 处理日期格式
        return text.split(" ")[0]
    elif col == "week":
        # 处理日期格式
        return text.split(" ")[1]
    elif col == "high_temp(℃)" or col == "low_temp(℃)":
        # 处理最高气温
        return text.replace("°", "").replace("℃", "")
    else:
        # 处理天气情况
        return text


def save_to_excel(data, filename) -> None:
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"数据已保存到{filename}文件中")


def main() -> None:
    # 1. 抓取网页数据, 网页已死
    url = "https://tianqi.2345.com/wea_history/54511.htm"
    weather_list = getdata(url)
    save_to_excel(weather_list, "./data/weather_beijing_2024.xlsx")


if __name__ == "__main__":
    main()
