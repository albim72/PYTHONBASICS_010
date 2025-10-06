f = open("data.txt", "r",encoding="utf-8")
print(f.read())
f.close()

f = open("data.txt","a",encoding="utf-8")
f.write(
    "\nThis is a new line added to the file."
)
f.close()

f = open("info.txt","w",encoding="utf-8")
f.write(
    "This is a new file created."
)
f.close()
