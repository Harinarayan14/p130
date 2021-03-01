import pandas as pd
import csv
df = pd.read_csv("total_stars.csv")
df.columns
df.drop(["star_name","distance","mass","radius","Luminosity"],axis=1,inplace=True)

final_data=df.dropna()
final_data.reset_index(drop=True,inplace=True)
final_data.to_csv("final_data.csv")
final_data.info()
final_data.describe()
final_data.dtypes
final_data.head(5)
