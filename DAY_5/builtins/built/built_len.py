import builtins

true_len = builtins.len
def traced_len(obj):
    result = true_len(obj)
    print(f"[TRACE] len({type(obj).__name__}) -> {result}")
    return result

builtins.len = traced_len

data = [1,2,3,4,5]
text = "Python"
print(len(data))
print(len(text))

builtins.len = true_len
print(len(data))
print(len(text))
