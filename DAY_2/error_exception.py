try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Program execution completed.")

# print(8*number)
