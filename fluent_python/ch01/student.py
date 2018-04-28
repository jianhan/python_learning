import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
df = pd.read_csv("./student_records.csv")
print(df)
