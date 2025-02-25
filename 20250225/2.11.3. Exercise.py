import math

# Part 1: Calculate the volume of a sphere
radius = 5  # radius in centimeters
volume = (4/3) * math.pi * radius**3  # volume in cubic centimeters
print("Volume of the sphere:", volume, "cubic centimeters")

# Part 2: Verify the trigonometric identity (cos(x))^2 + (sin(x))^2 = 1
x = 42  # angle in degrees
x_radians = math.radians(x)  # convert to radians
result = math.cos(x_radians)**2 + math.sin(x_radians)**2
print("Does (cos(x))^2 + (sin(x))^2 = 1", result)

# Part 3: Calculate e^2 in three ways
e_exp = math.e**2  # using the ** operator
e_pow = math.pow(math.e, 2)  # using math.pow
e_exp_func = math.exp(2)  # using math.exp

print("e^2 using **:", e_exp)
print("e^2 using math.pow:", e_pow)
print("e^2 using math.exp:", e_exp_func)
