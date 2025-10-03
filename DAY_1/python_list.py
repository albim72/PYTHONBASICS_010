#list creating
# CTRL + D  duplication of code block/line
# CTRL + / - quick commentary of block code/line or uncomment

# [] - list
from statistics import stdev

students = ["Ann","Johns","Leon","Tomas","John","Juan","Clare","Maria","John","Ann","Tomas","John"]
marks = [4,4,4,5,2,2,4,3,5]
homog = [5.3,12,"Warsaw",True]

print(students)
print(type(students))
print(len(students)) #length

print(students[0])
print(students[4])
print(students[-1])
print(students[-3])
print(students[1:5])
print(students[3:])
print(students[:5])

#add elements to list
students.append("Kate")
students.append("Maria")
students.append("John")

print(students)

#adding element to concrete index ... 4

students.insert(4,"Martin")
print(students)

#removing elements from list

students.remove("John")
print(students)

while "John" in students:
    students.remove("John")

print(students)


if "Olaf" in students:
    students.remove("Olaf")
else:
    print("Olaf not found")

print(students)

#how to remove student with index 3?
del students[3]
print(students)

delete = students.pop(5)
print(delete)
print(students)

#iteration by list
for ind,var in enumerate(students): #loop for returned pair(index, value)
    print(ind,var)

#list comprehension

squares = [var**2 for var in range(1,11)]
print(squares)

even = [x for x in marks if x%2==0]

#sort of elements
#safty sorting
print(sorted(students)) #not muting indexes

students.sort()
print(students)

#multidimensional arrays
tab = [
    ["Maria",5],
    ["John",4],
    ["Esther",5],
    ["Robert",3],
    ["Nadia",4]
]

print(tab)
for name,mark in tab:
    print(f"{name} has mark {mark}")
print(f"highest mark: {max(marks)}")
print(f"lowest mark: {min(marks)}")
print(f"average mark: {sum(marks)/len(marks)}")
print(f"standard dev: {stdev(marks)}")
