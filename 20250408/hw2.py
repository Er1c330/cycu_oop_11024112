from datetime import datetime

def calculate_time_info(input_time_str):
    """
    計算輸入時間的星期幾，並計算該時刻至今經過的太陽日數（以浮點數表示）。

    Parameters:
        input_time_str (str): 輸入時間，格式為 'YYYY-MM-DD HH:MM'。

    Returns:
        tuple: 包含該天是星期幾 (str) 和經過的太陽日數 (float)。
    """
    # 定義 Julian 日期的起始點
    JULIAN_START = datetime(4713, 1, 1, 12)  # 公元前 4713 年 1 月 1 日 12:00

    # 將輸入的時間字串轉換為 datetime 物件
    input_time = datetime.strptime(input_time_str, '%Y-%m-%d %H:%M')

    # 計算該天是星期幾
    weekday = input_time.strftime('%A')  # 例如 'Monday', 'Tuesday'

    # 計算輸入時間的 Julian 日期
    julian_date_input = (input_time - JULIAN_START).total_seconds() / 86400.0

    # 計算目前時間的 Julian 日期
    now = datetime.now()
    julian_date_now = (now - JULIAN_START).total_seconds() / 86400.0

    # 計算經過的太陽日數
    elapsed_days = julian_date_now - julian_date_input

    return weekday, elapsed_days

# 讓使用者輸入時間
input_time = input("請輸入時間（格式為 YYYY-MM-DD HH:MM，例如 2020-04-15 20:30）：")
try:
    weekday, elapsed_days = calculate_time_info(input_time)
    print(f"輸入的時間是星期：{weekday}")
    print(f"該時刻至今經過的太陽日數：{elapsed_days:.6f}")
except ValueError:
    print("輸入的時間格式不正確，請使用 YYYY-MM-DD HH:MM 格式。")