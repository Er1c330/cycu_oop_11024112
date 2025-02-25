# 1. 17 = n?
# 這會產生 SyntaxError，因為賦值運算符 (=) 只能將值賦給變數，而不是將值賦給一個常數。
# Uncomment the line below to see the error:
# 17 = n  # SyntaxError: cannot assign to literal

# 2. x = y = 1
# 這是合法的，它將 1 同時賦值給 x 和 y
x = y = 1
print(f"x = {x}, y = {y}")  # Output: x = 1, y = 1

# 3. 在 Python 語句末尾加上分號
# 在 Python 中，分號是可選的，但它不會改變語句的執行結果。它只是用來分隔同一行中的多個語句。
print("Hello")  # 這個語句結尾的分號可以存在，也不影響執行
print("World");  # Output: World (這樣做也是合法的，但分號在 Python 中不必要)

# 4. 在語句末尾加上句點
# 在語句結尾加句點會導致 SyntaxError，因為句點在 Python 中不是語法的一部分。
# Uncomment the line below to see the error:
# print("Hello.")  # SyntaxError: invalid syntax (This will raise an error)

# 5. 拼寫錯誤，導入錯誤的模塊名稱
# 嘗試導入錯誤名稱的模塊會導致 ImportError。
# Uncomment the line below to see the error:
# import maath  # ImportError: No module named 'maath'
