import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distribution(mu, sigma):
    try:
        # 定義 x 軸範圍
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        # 計算 PDF 值
        y = norm.pdf(x, mu, sigma)
        
        # 繪製圖形
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'μ={mu}, σ={sigma}')
        plt.title('Normal Distribution (PDF)')
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        plt.legend()
        plt.grid(True)
        
        # 儲存圖檔
        plt.savefig('normal_pdf.jpg')
        plt.close()
        print("圖檔已儲存為 normal_pdf.jpg")
    except Exception as e:
        print(f"發生錯誤: {e}", file=sys.stderr)

# 範例呼叫
if __name__ == "__main__":
    try:
        print("開始繪製常態分布圖...")
        plot_normal_distribution(mu=0, sigma=1.0)
        print("程式執行完成！")
    except ModuleNotFoundError as e:
        print(f"模組未安裝: {e}. 請確認是否已安裝必要模組，例如 numpy、matplotlib、scipy。", file=sys.stderr)
    except Exception as e:
        print(f"發生未預期的錯誤: {e}", file=sys.stderr)