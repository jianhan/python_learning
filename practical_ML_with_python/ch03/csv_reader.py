import csv

csv_reader = csv.reader(open("E0.csv", "rt"), delimiter=",")
csv_rows = list()
csv_attr_dict = dict()
# iterate and extract data
for row in csv_reader:
    print(row)
    csv_rows.append(row)
import pandas as pd

# For the majority of this section and subsequent ones, we will be relying on pandas and its utilities to
# perform the required tasks. The following snippet provides the details on row counts, attribute counts,
# and details.

df = pd.read_csv("E0.csv", sep=",")
print("Number of rows::", df.shape[0])
print("Number of columns::", df.shape[1])
print("Column Names::", df.columns.values.tolist())
print("Column Data Types::\n", df.dtypes)
