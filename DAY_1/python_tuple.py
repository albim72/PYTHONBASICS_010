numbers = (7,12,3,68,90,12,3,1,56,7,8,9,12,3,1,3,57,8,0)
print(numbers)
print(type(numbers))

print(numbers[1])
print(numbers[2:6])

print(numbers.count(3))
print(numbers.index(3))

reservation = [(1,5),(2,6),(3,7),(4,8),(5,9),(6,10)]

print(reservation)

#show - is this place(2,4) free
m = (2,4)
k = (2,6)
if k in reservation:
    print("This place is taken")
else:
    print("This place is free")

# numbers.remove(12)
# print(numbers)

nblist = list(numbers)
print(nblist)

nblist[2:4] = [101,45,67,90,102]
print(nblist)

numbers = tuple(nblist)
print(numbers)

s = "Impressive"
print(s)
print(type(s))
print(s[0])
print(s[1:5])
print(s[-1])
print(s[:6])

print(s[::-1])

print(numbers)
print(numbers[2:9:2])

imp = list(s)
print(imp)
print(type(imp))

imp.append("!")
print(imp)

imp_o = "".join(imp)
print(imp_o)

