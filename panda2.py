import pandas as pd
df=pd.read_csv("d://Book1.csv")
ser=pd.Series(df['name'])
print(ser)
