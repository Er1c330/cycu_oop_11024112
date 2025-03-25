import requests
from bs4 import BeautifulSoup
import re

def get_bus_route_stops(url):
    try:
        # 發送HTTP請求
        response = requests.get(url)
        response.raise_for_status()  # 檢查請求是否成功
        
        # 解析HTML內容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到去程的表格 (通常第一個表格是去程)
        outbound_table = soup.find('table', {'class': 'outbound'})
        if not outbound_table:
            # 如果沒有明確的outbound類別，嘗試找第一個表格
            tables = soup.find_all('table', limit=2)
            if len(tables) >= 1:
                outbound_table = tables[0]
            else:
                return None
        
        # 提取站牌資訊
        stops = []
        rows = outbound_table.find_all('tr')
        for row in rows[1:]:  # 跳過表頭
            cells = row.find_all('td')
            if len(cells) >= 2:
                stop_name = cells[0].get_text(strip=True)
                stop_address = cells[1].get_text(strip=True)
                stops.append({
                    'name': stop_name,
                    'address': stop_address
                })
        
        return stops
    
    except Exception as e:
        print(f"爬取資料時發生錯誤: {e}")
        return None

def search_stop_position(stops, query):
    # 搜尋站牌位置
    results = []
    for idx, stop in enumerate(stops, 1):
        if query.lower() in stop['name'].lower():
            results.append({
                'sequence': idx,
                'name': stop['name'],
                'address': stop['address']
            })
    return results

def main():
    url = "https://pda5284.gov.taipei/MQS/route.jsp?rid=10417"
    
    # 獲取公車路線站牌資訊
    stops = get_bus_route_stops(url)
    if not stops:
        print("無法獲取公車路線資訊")
        return
    
    print(f"成功獲取 {len(stops)} 個去程站牌資訊")
    
    # 使用者查詢介面
    while True:
        print("\n請輸入要查詢的站牌名稱 (輸入 'exit' 結束):")
        query = input().strip()
        
        if query.lower() == 'exit':
            break
        
        if not query:
            continue
        
        # 搜尋站牌
        results = search_stop_position(stops, query)
        
        if not results:
            print(f"找不到包含 '{query}' 的站牌")
        else:
            print(f"找到 {len(results)} 個結果:")
            for result in results:
                print(f"第 {result['sequence']} 站: {result['name']} - {result['address']}")

if __name__ == "__main__":
    main()