import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file1 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"
df1 = pd.read_csv(file1, skiprows=4) 
df1 = df1.drop(columns=['Unnamed: 68'])
df1 = df1.dropna(subset=['Country Name', 'Country Code'])

for col in df1.columns[4:]:
    df1[col] = pd.to_numeric(df1[col], errors='coerce')

df1[df1.columns[4:]] = df1[df1.columns[4:]].interpolate(axis=1)

population_2020 = df1[['Country Name', '2020']].dropna()

plt.figure(figsize=(12, 6))
sns.histplot(population_2020['2020'], bins=30, kde=True)
plt.title('Distribution of Population in 2020')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()
