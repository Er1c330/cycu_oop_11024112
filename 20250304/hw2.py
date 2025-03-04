def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# Predefined numbers
num1 = 56
num2 = 98

# Using the iterative version of Euclidean Algorithm
print(f"The greatest common divisor (iterative) of {num1} and {num2} is: {gcd_iterative(num1, num2)}")

# Using the recursive version of Euclidean Algorithm
print(f"The greatest common divisor (recursive) of {num1} and {num2} is: {gcd_recursive(num1, num2)}")
