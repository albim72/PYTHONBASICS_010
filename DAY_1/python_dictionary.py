books = {
        "978-245-252-0024-0": "Pride and Prejudice",
        "978-245-252-0024-1": "Moby-dick",
        "978-245-252-0024-2": "Great Expectations",
        "978-245-252-0024-3": "Hobbit",
}

print(books)
print(books["978-245-252-0024-0"])

books["978-245-252-0024-8"] = "Jane Eyre"
print(books)

print("_______________ BOOKS _________________")
for k,v in books.items():
    print(f"{k} : {v}")

#checking if a key exsits
print(f"\nDo we have -> 978-245-252-0024-1 ?? { '978-245-252-0024-1' in books }")
print(f"\nDo we have -> 978-245-111-0024-1 ?? { '978-245-111-0024-1' in books }")
