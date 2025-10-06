#standard libraries imports
#third-party imports
#local application imports

from functools import reduce

students = [
    {"name":"Alice","scores":[80,90,100]},
    {"name":"Bob","scores":[60,70,80]},
    {"name":"Charlie","scores":[90,100,100]},
    {"name":"Dan","scores":[45,33,12]},
    {"name":"Ann","scores":[67,99,45]},
]

#map function, list, lambda
#first parameter of map i function mapping values for every keys form list disctionaries(students)
name_and_avg = list(map(lambda s: (s["name"], sum(s["scores"]) / len(s["scores"])), students))
print(f"name_and_avg: {name_and_avg}")

#filter function - keep only students with average >= 75
#filter(function -> condition,data) -> result -> (name,avg)

passed = list(filter(lambda t: t[1] >= 75, name_and_avg))
print(f"passed: {passed}")

#function sorted with key: sort passed students by average
#sorted will call key(...) to extract the sort from each pair

top_sorted = sorted(passed,
                    key=lambda pair: pair[1],
                    reverse=True)

print(f"top_sorted: {top_sorted}")


#function reduce(function,iterable,initializer)
class_avg = reduce(lambda acc, s: acc + s[1],
                   name_and_avg, 0.0)/len(name_and_avg)

print(f"class_avg: {class_avg:.2f}")

#any/all functions quick checks
#any(...) stops on first True, all(...) stops on first False
any_below_60  = any(map(lambda pair: pair[1] < 60, name_and_avg))
all_above_70  = all(map(lambda pair: pair[1] > 70, name_and_avg))

print(f"any_below_60: {any_below_60}")
print(f"all_above_70: {all_above_70}")
