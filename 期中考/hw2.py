from datetime import datetime

# 🔹 使用者輸入一個日期時間
input_str = input("請輸入日期時間（格式：YYYY-MM-DD HH:MM:SS）：")
input_dt = datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")

# 🔹 現在系統時間
now_dt = datetime.now()

# 🔹 計算星期幾（1=週一, 7=週日）
weekday_num = input_dt.isoweekday()
weekday_str = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'][weekday_num - 1]

# 🔹 該日期為當年第幾天
day_of_year = input_dt.timetuple().tm_yday

# 🔹 計算從輸入日期到現在的太陽日（含小數）
delta = now_dt - input_dt
elapsed_solar_days = delta.total_seconds() / 86400  # 一天有 86400 秒

# ✅ 顯示結果
print("\n📅 結果資訊：")
print(f"🔹 您輸入的日期是：{weekday_str}")
print(f"🔹 是該年第 {day_of_year} 天")
print(f"🔹 從該時刻至現在（{now_dt.strftime('%Y-%m-%d %H:%M:%S')}）")
print(f"   共經過了 {elapsed_solar_days:.5f} 個太陽日")
