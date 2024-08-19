import pandas as pd

file1 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"
file2 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"
file3 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"

df1 = pd.read_csv(file1, skiprows=4) 
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)


df1.head(), df2.head(), df3.head()

df1 = df1.drop(columns=['Unnamed: 68'])

missing_values_df1 = df1.isnull().sum()


df1 = df1.dropna(subset=['Country Name', 'Country Code'])

for col in df1.columns[4:]:
    df1[col] = pd.to_numeric(df1[col], errors='coerce')


df1 = df1.interpolate(axis=1)

missing_values_df1_after = df1.isnull().sum()

missing_values_df1, missing_values_df1_after

non_numeric_cols = df1.columns[:4]
numeric_cols = df1.columns[4:]

df1[numeric_cols] = df1[numeric_cols].interpolate(axis=1)

missing_values_df1_after = df1.isnull().sum()

missing_values_df1_after

import matplotlib.pyplot as plt
import seaborn as sns

population_2020 = df1[['Country Name', '2020']].dropna()


plt.figure(figsize=(12, 6))
sns.histplot(population_2020['2020'], bins=30, kde=True)
plt.title('Distribution of Population in 2020')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()
