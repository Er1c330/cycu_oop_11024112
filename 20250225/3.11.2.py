def print_right(text):
    # Calculate the number of spaces needed to align the last character at the 40th column
    spaces_needed = 40 - len(text)
    
    # Print the text with the calculated number of leading spaces
    print(" " * spaces_needed + text)

# Test the function with example inputs
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
