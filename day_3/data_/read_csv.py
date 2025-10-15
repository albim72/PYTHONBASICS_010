import csv

filename = "data.csv"
data = []

with open(filename,newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['score'] = float(row['score'])
        data.append(row)


print("Pierwsze 5 wierszy:")
print(data[:5])

category_scores = {}
category_counts = {}

for row in data:
    category = row['category']
    score = row['score']
    if category in category_scores:
        category_scores[category] += score
        category_counts[category] += 1
    else:
        category_scores[category] = score
        category_counts[category] = 1

#obliczanie średnich
average_scores = {category:category_scores[category]/category_counts[category] for category in category_scores}
print(f'sredni wynik: {average_scores}')
