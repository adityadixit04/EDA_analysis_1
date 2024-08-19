import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file1 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"
file2 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"
file3 = "D:\\Study\\Intership\\Task 1\\API_SP.POP.TOTL_DS2_en_csv_v2_1021451\Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_1021451.csv"

df1 = pd.read_csv(file1, skiprows=4)  
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

df1 = df1.drop(columns=['Unnamed: 68'])
df1 = df1.dropna(subset=['Country Name', 'Country Code'])

for col in df1.columns[4:]:
    df1[col] = pd.to_numeric(df1[col], errors='coerce')

df1[df1.columns[4:]] = df1[df1.columns[4:]].interpolate(axis=1)


df1 = df1.merge(df2[['Country Code', 'Region', 'IncomeGroup']], on='Country Code', how='left')

population_2020 = df1[['Country Name', '2020', 'Region', 'IncomeGroup']].dropna()

plt.figure(figsize=(12, 6))
sns.histplot(population_2020['2020'], bins=30, kde=True)
plt.title('Distribution of Population in 2020')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(12, 6))
sns.barplot(data=population_2020, x='Region', y='2020', estimator=sum, ci=None)
plt.title('Total Population in 2020 by Region')
plt.xlabel('Region')
plt.ylabel('Total Population')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=population_2020, x='IncomeGroup', y='2020', estimator=sum, ci=None)
plt.title('Total Population in 2020 by Income Group')
plt.xlabel('Income Group')
plt.ylabel('Total Population')
plt.xticks(rotation=45)
plt.show()
