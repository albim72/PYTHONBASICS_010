import csv
from pathlib import Path

rows = [
    {"title":"The Ultra Runner's ABC","author":"Scott Jurek","price":104},
    {"title":"Deep Learning","author":"Ian GoodFellow","price":133},
]

csv_path = Path("data/books.csv")

#write csv with header
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "author", "price"])
    writer.writeheader()
    writer.writerows(rows)

#READ CSV

with open(csv_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    loaded = list(reader)

print("__________ loaded CSV ___________")
for r in loaded:
    print(r["title"], r["author"], r["price"])
