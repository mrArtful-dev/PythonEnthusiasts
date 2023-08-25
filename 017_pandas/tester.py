import pandas as pd

df = pd.read_csv('csv_files/test.csv')
print(df)

df.to_excel('out.xlsx')
