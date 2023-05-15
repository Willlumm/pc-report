import pandas as pd

df = pd.read_excel("./input/rcr.xlsx", skiprows=12)
dates = pd.to_datetime(df["Week End"], format="%m/%d/%Y")
df.to_csv(f"./historic/{dates.min().date()}_to_{dates.max().date()}", index=False)