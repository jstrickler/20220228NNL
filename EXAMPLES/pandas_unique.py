import pandas as pd

df = pd.read_excel('../DATA/presidents.xlsx', sheet_name='US Presidents',
                  na_values='NA()')
df.index = range(1,len(df)+1)

# print(df.head())
parties = df['Party affiliation'].value_counts()
print(parties)
# parties.plot(kind='bar')
print()
print(df['State of Birth'].value_counts())

