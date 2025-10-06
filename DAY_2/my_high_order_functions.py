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
print(square_twice(3))

#custom filter function
def make_threshold_filter(threshold,key_fn):
    """
    return a predicate that keeps items where key_fn(item) >= threshold
    :param threshold:
    :param key_fn:
    :return:
    """
    def predicate(item):
        return key_fn(item) >= threshold
    return predicate

products = [
    {"name":"Mouse","price":25,"rating":4.3},
    {"name":"Desk","price":199,"rating":4.6},
    {"name":"Chair","price":120,"rating":3.9},
]

price_over_100 = make_threshold_filter(100,lambda item:item["price"])
premium = list(filter(price_over_100,products))
print(f"premium products: {premium}")
