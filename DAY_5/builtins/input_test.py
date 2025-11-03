import builtins

real_input = builtins.input

def fake_input(prompt=""):
    print(prompt + "[auto-answer]")
    return "42"

builtins.input = fake_input

answer = input("What is meaning of life? ")
print("You said: ", answer)

builtins.input = real_input
