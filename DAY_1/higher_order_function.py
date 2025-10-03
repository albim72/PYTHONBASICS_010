"""
Example of Higher-Order Functions in Python
A higher-order function is a function that can take other functions as arguments
or return a function as a result.
"""

# Example 1: Function taking another function as argument
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

# Example 2: Function returning another function
def power_function(exp):
    def power(x):
        return x ** exp
    return power

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Original numbers:", nums)

    # Using lambda as operation
    squared = apply_operation(nums, lambda x: x**2)
    print("Squared:", squared)

    # Using predefined function as operation
    doubled = apply_operation(nums, lambda x: x*2)
    print("Doubled:", doubled)

    # Function returning another function
    cube = power_function(3)
    print("Cube of 4:", cube(4))

    fourth_power = power_function(4)
    print("4 to the power of 4:", fourth_power(4))
