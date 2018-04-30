import csv

csv_reader = csv.reader(open("E0.csv", "rt"), delimiter=",")
csv_rows = list()
csv_attr_dict = dict()
# iterate and extract data
for row in csv_reader:
    print(row)
    csv_rows.append(row)
import pandas as pd

df = pd.read_csv("E0.csv", sep=",")
print(df)
