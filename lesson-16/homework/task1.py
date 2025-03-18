import pandas as pd
import sqlite3
import json

with sqlite3.connect('chinook.db') as con:
    df1 = pd.read_sql_query("SELECT * FROM customers", con)

print(df1.head(10))

df2 = pd.read_json('iris.json')
print("Shape: ", df2.shape)
print(df2.columns.tolist())

df2.columns = [x.lower() for x in df2.columns]
df2_new = df2[["sepal_length", "sepal_width"]]

mean_values = df2.mean()
median_values = df2.median()
std_values = df2.std()

df3 = pd.read_excel('titanic.xlsx')
print(df3.head())

df3_filtered = df3[df3["Age"]>30]
gender_counts = df3["Sex"].value_counts()
print(gender_counts)

min_age = df3["Age"].min()
max_age = df3["Age"].max()
sum_age = df3["Age"].sum()

df4 = pd.read_parquet('flights.parquet')
print(df4.info())

df5 = pd.read_csv('moive.csv')
df5.sample(10)

df5_filtered = df5[df5["duration"] > 120]
df5_filtered.sort_values(by="director_facebook_likes", inplace=True)
