import numpy as np

print(np.__version__)
print("this is the first python script")

a = 10
print(a)
print(type(a))

a = "hello"
print(a)
print(type(a))

a = 11.34
print(a)
print(type(a))

x = 7
y = 12

print(x + y)

d:float = 8.9
print(d)
print(type(d))

d = "one"
print(d)
print(type(d))

_info = "information" #variable - protected
print(_info)
_spec_ = "desc" #protected - special - variable

__priv = "private" #private variable

#You do not use reservate names: __init__, __repr__, __call__ etc.

u = "6.7"
print(u*12)

# print(int(u)*12)
print(eval(u)*12)
