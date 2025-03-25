import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
file_path = 'ExchangeRate@202503251848.csv'  # 你的 CSV 檔案路徑
df = pd.read_csv(file_path)

# 顯示資料的前幾行來檢查
print(df.head())

# 假設你想繪製 '本行買入' 的匯率 (你可以根據需要更換列名稱)
df_buy = df[df['幣別'] == 'USD']  # 只選取 USD 的資料
df_buy = df_buy[['日期', '本行買入']]  # 只選取 '日期' 和 '本行買入' 兩個欄位

# 確保 '日期' 是日期格式
df_buy['日期'] = pd.to_datetime(df_buy['日期'], format='%Y%m%d')

# 繪製圖表
plt.plot(df_buy['日期'], df_buy['本行買入'], label='本行買入匯率', color='blue')

plt.xlabel('日期')
plt.ylabel('匯率')
plt.title('本行買入匯率隨日期變化')
plt.xticks(rotation=45)  # 讓日期標籤不會重疊
plt.tight_layout()  # 調整圖形以防止標籤被遮擋
plt.legend()

# 顯示圖表
plt.show()
