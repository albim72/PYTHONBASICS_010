import builtins

true_sum = builtins.sum

def surreal_sum(itrable, start=0):
    print("Calculating the meaning of the universe...")
    total = true_sum(itrable, start)
    if total == 42:
        return "You have reached enlightenment!"
    elif total < 0:
        return "This sum has entered the shadow realm!"
    else:
        return f"Your sum is {total}, but meaning is optimal!"

builtins.sum = surreal_sum

numbers = [10,20,33,101]
print(sum(numbers))
print(sum([-5,-36]))
print(sum([40,2]))

builtins.sum = true_sum
print(f"Back to reality: {sum(numbers)}")
