import requests
import concurrent.futures

base_url = "http://r0k.us/graphics/kodak/kodak/kodim"
download_url = "./data/imgs/kodims"


def download_image(num):
    num_str = f"{num:02d}"
    url = f"{base_url}{num_str}.png"
    filename = f"{download_url}/kodim{num_str}.png"

    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"成功下载: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"下载失败 {filename}: {e}")


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 创建1-24的任务列表
    executor.map(download_image, range(1, 25))
