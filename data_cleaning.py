import pandas as pd
import csv
df = pd.read_csv("total_stars.csv")
del(df["Unnamed: 0"])
del(df["Unnamed: 0.1"])
del(df['Luminosity'])
df.to_csv("final_data.csv",index=False)