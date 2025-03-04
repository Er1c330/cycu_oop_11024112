def absolute_value_correct(x):
    if x < 0:
        return -x
    else:
        return x  # x >= 0 的情況都涵蓋了

print(absolute_value_correct(0))  # 應該輸出 0
