def twice(func):
    """
    return a new function that calls func twice, this is very simple decorator
    :param func:
    :return:
    """
    def inner(x):
        return func(func(x))
    return inner

def square(x):
    return x**2
square_twice = twice(square)
print(square_twice)
print(square_twice(2))
