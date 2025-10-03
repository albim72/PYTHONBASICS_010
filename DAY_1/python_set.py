colors = {"red", "blue", "green","grey","white","black","violet","brown"}

print(colors)
print(colors)
print(colors)
print(type(colors))

colors.add("yellow")
print(colors)

colors.remove("red")
print(colors)

colors.discard("pink")
print(colors)

colors.add("green")
print(colors)

auto1 = ["honda","toyota","nissan","audi","bmw","dogde","jeep","cupra"]
auto2 = ["honda","toyota","nissan","skoda","dacia","peugeot","lincoln"]


#change lists to sets
auto1 = set(auto1)
auto2 = set(auto2)

print(auto1)
print(auto2)

#intersection
print(auto1.intersection(auto2))

#difference
print(auto1.difference(auto2))

#union
print(auto1.union(auto2))

allcars = auto1 | auto2
print(allcars)

forzenallcars = frozenset(allcars)
print(forzenallcars)


