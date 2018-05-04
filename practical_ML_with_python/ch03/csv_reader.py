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

# identify missing values
print("Columns with Missing Values::", df.columns[df.isnull().any()].tolist())
print("Number of rows with Missing Values::", len(pd.isnull(df).any(1).nonzero()[0].tolist()))
print("Sample Indices with missing data::", pd.isnull(df).any(1).nonzero()[0].tolist()[0:5])

# summary
print("General Stats::")
print(df.info())
print("Summary Stats::")
print(df.describe())


def cleanup_column_names(df, rename_dict={}, do_inplace=True):
    """This function renames columns of a pandas dataframe
    It converts column names to snake case if rename_dict is not passed.
    Args:
    rename_dict (dict): keys represent old column names and values point to
    newer ones
    do_inplace (bool): flag to update existing dataframe or return a new one
    Returns:
    pandas dataframe if do_inplace is set to False, None otherwise
    """
    if not rename_dict:
        return df.rename(columns={col: col.lower().replace(' ', '_')
                                  for col in df.columns.values.tolist()},
                         inplace=do_inplace)
    else:
        return df.rename(columns=rename_dict, inplace=do_inplace)


cleanup_column_names(df, {"Div": "Division"})
print(df)

# With pandas, we can vertically slice (select a subset of columns) in a variety of ways. pandas
# provides different ways to suit different scenarios as we shall see in the following snippet.

print("Using Column Index::")
print(df.Division.values)

# Yet there are times when we would need to get attributes
# based on their data types alone.
print("UsingColumnDataType::")
print(df.select_dtypes(include=['float64']).values[:, 0])

# There may be
# requirements to horizontally splitting a dataframe as well. To work with a subset of rows, pandas provides
# ways as outlined in the following snippet.
print("Select Specific row indices::")
print(df.iloc[[10, 100, 20]])
print("Excluding Specific Row indices::")
print(df.drop([0, 24, 51], axis=0).head())
print("Subsetting based on logical condition(s)::")
print(df[df.HTAG > 0].head())
print("Subsetting based on offset from top (bottom)::")
print(df[100:].head())

# Typecasting
# Typecasting or converting data into appropriate data types, is an important part of cleanup and wrangling in
# general
df["Date"] = pd.to_datetime(df.Date)
print("To Date time", df.head())

import numpy as np

# using map to dummy encode
type_map = {'H': 0, 'D': 1, 'A': 2, np.NAN: -1}
df['ENCODED_HTR'] = df.HTR.map(type_map)
print("HEAD *******", df.head())
