import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distribution(mu, sigma):
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

# 範例呼叫
if __name__ == "__main__":
    plot_normal_distribution(mu=0, sigma=1.0)