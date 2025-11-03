code = 'print("This is a test")'
exec(code)

#dynamic variables

for i in range(3):
    exec(f"x{i} = {i}**2")

print(x0,x1,x2)
