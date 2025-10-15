import pandas as pd

data = pd.read_csv('data.csv')
print(data.head())

#średnia wyników
grouped_data = data.groupby('category')['score'].mean()
print(f"sredni wynik dla każdej kategorii:\n")
print(grouped_data)

filtr = data[data['score']>71]
print(f'wyniki score>71:\n {filtr}')

stats = data.describe()
print(stats)
