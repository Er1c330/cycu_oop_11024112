from bs4 import BeautifulSoup

def get_bus_arrival_from_file(file_path, stop_name):
    """
    從指定的 HTML 檔案中讀取公車即時到站資訊，並顯示指定車站的到站時間。

    Args:
        file_path (str): HTML 檔案的路徑
        stop_name (str): 車站名稱
    """
    # 讀取 HTML 檔案
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(content, "html.parser")

    # 找到所有公車資訊的表格列
    rows = soup.find_all("tr", class_=["ttego1", "ttego2"])

    # 初始化結果列表
    results = []

    # 遍歷每一列，提取公車資訊
    for row in rows:
        route = row.find("td").text.strip()  # 公車路線名稱
        stop_td = row.find_all("td")[1]  # 站牌名稱
        stop = stop_td.text.strip()
        direction = row.find_all("td")[2].text.strip()  # 去返程
        arrival_td = row.find_all("td")[3]  # 預估到站時間
        arrival_time = arrival_td.text.strip() if arrival_td else "無資料"

        # 如果站牌名稱符合輸入的車站名稱，加入結果
        if stop_name in stop:
            results.append({
                "路線": route,
                "站牌": stop,
                "去返程": direction,
                "預估到站": arrival_time
            })

    # 顯示結果
    if results:
        print(f"車站：{stop_name} 的即時到站資訊：")
        for result in results:
            print(f"路線：{result['路線']}，站牌：{result['站牌']}，去返程：{result['去返程']}，預估到站：{result['預估到站']}")
    else:
        print(f"查無車站：{stop_name} 的即時到站資訊。")

# 主程式
if __name__ == "__main__":
    # 輸入 HTML 檔案路徑和車站名稱
    file_path = "bus_stop_36021.html"  # 替換為您的檔案路徑
    stop_name = input("請輸入車站名稱：")
    get_bus_arrival_from_file(file_path, stop_name)