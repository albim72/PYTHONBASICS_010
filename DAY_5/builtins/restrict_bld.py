import builtins

real_open = builtins.open

def real_only_open(file,mode="r",*args,**kwargs):
    if any(flag in mode for flag in ("w","a","+")):
        raise PermissionError("Only read allowed")
    return real_open(file,mode,*args,**kwargs)

builtins.open = real_only_open

try:
    with open("demo.txt","w") as f:
        f.write("Nope!")

except PermissionError as e:
    print(e)

