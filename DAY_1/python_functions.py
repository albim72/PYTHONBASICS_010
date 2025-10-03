"""
We will describe a group of function
We will show different aspects of using functions in Python
???
"""

#simple function without arguments
def greeting():
    print("Welcome to the world of Python !")

#function with one agrument()
def square(x):
    return x**2

#function with 2 parameters
def add(x,y):
    return x+2*y

#function with a default value
def user_greeting(name,lang="en"):
    if lang=="en":
        print(f"Welcome to the world of Python {name}!")
    elif lang=="pl":
        print(f"Witaj w świecie Pythona {name}!")
    elif lang=="fr":
        print(f"Bienvenue au monde de Python {name}!")
    else:
        print(f"??????????? {name}!")

#function returning multiple values
def divide(a,b):
    """
    returns (imteger quotient,remainder) for integers a and b
    :param a: int
    :param b: int
    :return: divmod(a,b)
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return divmod(a,b)

#function with the list of argument
def average(values):
    if not values:
        raise ValueError("no values provided")
    return sum(values)/len(values)

#anonymous function (lambda)
cube = lambda x: x**3 + 2*x**2 - 10*x + 1

if __name__ == '__main__':
    print("______ greeting() _____")
    greeting()
    greeting()
    greeting()

    print("______ square(y) _____")
    print(square(5))
    print(square(11))

    print("______ add(x,y) _____")
    print(add(5,2))
    print(add(11,2))

    print("______ user_greeting('name') _____")
    user_greeting("John")
    user_greeting("Henio","pl")
    user_greeting("Paul","fr")
    user_greeting("Yoko","jpn")

    print("______ divide(a,b) _____")
    quotient,remainder = divide(10,3)
    print(f"quotient={quotient} remainder={remainder}")

    # quotient, remainder = divide(10, 0)
    # print(f"quotient={quotient} remainder={remainder}")

    print("______ average(values) _____")
    print(average([1,2,3,4,5]))
    print(average([45,378,9,3,98,64,38,94,2]))
    # print(average([]))

    print("______ cube(x) _____")
    print(cube(2))
    print(cube(3))
    print(cube(8))


