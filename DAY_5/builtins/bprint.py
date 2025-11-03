import builtins,time

original_print = builtins.print

def logged_print(*args,**kwargs):
    ts = time.strftime('%H:%M:%S')
    original_print(f'[{ts}]',*args,**kwargs)

builtins.print = logged_print
print('Hello World')
print('Builtins can be patches safety')

builtins.print = original_print
print('Back to normal')

print(dir(builtins))
