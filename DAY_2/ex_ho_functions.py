# Part 2: Higher-order function — takes another function as a parameter

def apply_and_show(func, value):
    """Apply a given function to a value and display the result."""
    result = func(value)
    print(f"Applying function {func.__name__} to {value} gives {result}")
    return result


# Reuse our previous function
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (9/5) * celsius + 32


# --- Interactive part ---

# Ask the user for input
celsius_str = input("Enter temperature in Celsius: ")

# Convert input to float
celsius_value = float(celsius_str)

# Use higher-order function to apply conversion
apply_and_show(celsius_to_fahrenheit, celsius_value)


# Bonus example: another simple function
def double(x):
    """Return double the value."""
    return x * 2


# Ask for another input for the second test
number_str = input("Enter a number to double: ")
number_value = float(number_str)

# Apply the higher-order function again
apply_and_show(double, number_value)
