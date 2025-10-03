
# Task: Python Collections — Library System

# You will work with Python’s main collections: list, tuple, set, dictionary, frozenset.
# Your goal is to build a small “library system” step by step.


raw_titles = [
    "Dune", "Foundation", "Dune", "Neuromancer",
    "Snow Crash", "Foundation", "Hyperion", "Dune"
]

isbn_author_pairs = [
    ("9780441013593", "Frank Herbert"),
    ("9780553293357", "Isaac Asimov"),
    ("9780441569595", "William Gibson"),
    ("9780553380958", "Dan Simmons")
]

loaned_titles = {"Neuromancer", "Hyperion"}

# 1) Remove duplicates
unique_titles = set(raw_titles)
print("Unique titles (set):", unique_titles)
print("Count:", len(unique_titles))

# Bonus: keep order
unique_titles_ordered = list(dict.fromkeys(raw_titles))
print("Unique ordered (list):", unique_titles_ordered)

# 2) Create dictionary ISBN -> Author
authors_by_isbn = dict(isbn_author_pairs)
print("\nAuthors by ISBN:", authors_by_isbn)
print("All ISBNs:", list(authors_by_isbn.keys()))

# 3) Build catalog (list of dicts)
catalog = []
for idx, title in enumerate(unique_titles_ordered, start=1):
    record = {
        "title": title,
        "isbn": f"ISBN-{idx:03d}",  # fake placeholder
        "available": title not in loaned_titles
    }
    catalog.append(record)

print("\nCatalog preview:", catalog[:3])

# 4) Extra challenge: frozenset
available_snapshot = frozenset(
    rec["title"] for rec in catalog if rec["available"]
)
print("\nAvailable snapshot (frozenset):", available_snapshot)

# Trying to add will raise an error:
# available_snapshot.add("New Book")
try:
    available_snapshot.add("New Book")
except AttributeError as e:
    print("\nError:", e)
