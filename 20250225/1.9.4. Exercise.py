# Example expressions to check the type of
print("Type of 765:", type(765))  # Integer (int)
print("Type of 2.718:", type(2.718))  # Float (float)
print("Type of '2 pi':", type('2 pi'))  # String (str)
print("Type of abs(-7):", type(abs(-7)))  # Integer (int), because abs returns an integer
print("Type of abs(-7.0):", type(abs(-7.0)))  # Float (float), because abs returns a float for float input
print("Type of abs:", type(abs))  # Function (builtin function)
print("Type of int:", type(int))  # Class (type)
print("Type of type:", type(type))  # Type (builtin type for types)

