from pathlib import Path

file_path = Path("data/books.txt")

#WRITE(overwrite)
with open(file_path, "w", encoding="utf-8") as f:
    f.write("The Ultra Runner's ABC | Scott Jurek | 102\n")
    f.write("Deep Learning | Jan Goodfellow | 165\n")

print(f"connection: {f.closed}")

#READ (whole content)
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
print("____________ TXT FILE ___________")
print(content)
