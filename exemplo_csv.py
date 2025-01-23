import csv

import pandas as pd

path = r".\arquivo.csv"

lista: list = []

with open(path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lista.append(row)


df = pd.DataFrame(lista)
print(df)
