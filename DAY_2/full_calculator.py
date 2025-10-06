# ============================================================
# Day 2 – Individual Exercise: Working with Functions in Python
# ============================================================

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (9/5) * celsius + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (5/9) * (fahrenheit - 32)


def apply_and_show(func, value):
    """Apply a given function to a value and display the result."""
    result = func(value)
    print(f"Applying function {func.__name__} to {value} gives {result}")
    return result


# ============================================================
# MAIN PROGRAM
# ============================================================
if __name__ == "__main__":
    print("Temperature Conversion Tool 🌡️")
    print("--------------------------------")

    # Ask user which conversion they want
    print("Choose conversion type:")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # Celsius → Fahrenheit
        celsius_str = input("Enter temperature in Celsius: ")
        celsius_value = float(celsius_str)
        apply_and_show(celsius_to_fahrenheit, celsius_value)

    elif choice == "2":
        # Fahrenheit → Celsius
        fahrenheit_str = input("Enter temperature in Fahrenheit: ")
        fahrenheit_value = float(fahrenheit_str)
        apply_and_show(fahrenheit_to_celsius, fahrenheit_value)

    else:
        print("Invalid choice. Please restart the program and enter 1 or 2.")
