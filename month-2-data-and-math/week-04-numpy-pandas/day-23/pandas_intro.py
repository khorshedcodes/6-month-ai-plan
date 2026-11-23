# Day 23: Code Implementation
# Pandas Series, DataFrames, Inspection and Indexing (loc vs iloc)
# Write your implementation here once Stage 1 Q&A is complete.
import pandas as pd 
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

df = pd.read_csv(DATA_DIR/'employees.csv')

print(df.shape)
print(df.info())
print(df.head(3))

custom_list = df.iloc[0:4,0:3]

print(custom_list)
label_list = df.loc[:,["name","salary"]]
print(label_list[:3])

high_earners = df[df["salary"] >= 90000]
print(high_earners[['name',"department","salary"]])

engineering_remote =  df[(df["department"] == "Engineering") & (df["remote"]==True)]

print(engineering_remote["salary"].mean())