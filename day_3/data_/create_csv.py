#tworzenie pliki csv
import csv

data = [
    {'Name':'Janek','Age':64,'Score':67.8},
    {'Name':'Anna','Age':45,'Score':68},
    {'Name':'Kamil','Age':32,'Score':55.4},
    {'Name':'Nadia','Age':27,'Score':78.9}
]

output_filename = 'outputdata.csv'
with open(output_filename,mode='w',newline='') as csvfile:
    fieldnames = ['Name','Age','Score']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        writer.writerow(row)

print(f"Dane zostały zapisane do pliku {output_filename}")
