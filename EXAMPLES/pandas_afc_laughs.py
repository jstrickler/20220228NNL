import pandas as pd

URL = "https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Laughs"

df_list = pd.read_html(URL)

df  = df_list[1]
print(df.head())
print(df[df.loc[:,'Directors(s)'] == 'Robert Altman'])

movies_by_director = df_list[1].value_counts("Director(s)")

def afc_sort(row):
    last_name = row[0].split(',')[0].split()[-1]
    return -row[1], last_name

for director, count in sorted(movies_by_director.items(), key=afc_sort):
    print(f"{director:30.30s} {count:2d}")

