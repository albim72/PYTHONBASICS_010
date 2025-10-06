def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (9/5) * celsius + 32


# --- Main program ---
c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")
