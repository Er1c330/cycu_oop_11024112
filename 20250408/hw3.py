import requests
from bs4 import BeautifulSoup
import csv

def fetch_bus_route_data(route_id, output_file='bus_route.csv'):
    """
    從臺北市公開網站抓取指定公車路線的站點資料，並儲存為 CSV 格式。

    Parameters:
        route_id (str): 公車代碼，例如 '0100000A00'。
        output_file (str): 輸出的 CSV 檔案名稱，預設為 'bus_route.csv'。
    """
    # 定義目標 URL
    url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # 發送 GET 請求
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 檢查 HTTP 請求是否成功

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # 提取站點資料（根據 HTML 結構調整選擇器）
        stops = []
        stop_elements = soup.find_all("div", class_="stop-info")  # 假設站點資訊在 class="stop-info" 的 div 中

        if not stop_elements:
            print("未找到任何站點資料，請檢查 HTML 結構或公車代碼是否正確。")
            return

        for stop_element in stop_elements:
            print(stop_element.prettify())  # 打印每個站點的 HTML 結構，幫助調試

            arrival_info = stop_element.find("span", class_="arrival-time").text.strip() if stop_element.find("span", class_="arrival-time") else "未知"
            stop_number = stop_element.find("span", class_="stop-number").text.strip() if stop_element.find("span", class_="stop-number") else "未知"
            stop_name = stop_element.find("span", class_="stop-name").text.strip() if stop_element.find("span", class_="stop-name") else "未知"
            stop_id = stop_element.find("span", class_="stop-id").text.strip() if stop_element.find("span", class_="stop-id") else "未知"
            latitude = stop_element.find("span", class_="latitude").text.strip() if stop_element.find("span", class_="latitude") else "未知"
            longitude = stop_element.find("span", class_="longitude").text.strip() if stop_element.find("span", class_="longitude") else "未知"

            stops.append([arrival_info, stop_number, stop_name, stop_id, latitude, longitude])

        # 開啟 CSV 檔案進行寫入
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 寫入標題列
            writer.writerow(["arrival_info", "stop_number", "stop_name", "stop_id", "latitude", "longitude"])
            # 寫入每個站點的資料
            writer.writerows(stops)

        print(f"公車路線資料已成功儲存至 {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"無法取得資料，請檢查網路連線或公車代碼是否正確。錯誤訊息：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")

# 主程式
if __name__ == "__main__":
    route_id = input("請輸入公車代碼（例如 '0100000A00'）：")
    fetch_bus_route_data(route_id)