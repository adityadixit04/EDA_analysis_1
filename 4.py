import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Frame, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

root = Tk()
root.title("Population Data Visualizations")

def create_histogram():
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(population_2020['2020'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribution of Population in 2020')
    ax.set_xlabel('Population')
    ax.set_ylabel('Frequency')
    
    canvas = FigureCanvasTkAgg(fig, master=frame_histogram)
    canvas.draw()
    canvas.get_tk_widget().pack()

def create_bar_chart_region():
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=population_2020, x='Region', y='2020', estimator=sum, ci=None, ax=ax)
    ax.set_title('Total Population in 2020 by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Population')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_bar_region)
    canvas.draw()
    canvas.get_tk_widget().pack()

def create_bar_chart_income():
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=population_2020, x='IncomeGroup', y='2020', estimator=sum, ci=None, ax=ax)
    ax.set_title('Total Population in 2020 by Income Group')
    ax.set_xlabel('Income Group')
    ax.set_ylabel('Total Population')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_bar_income)
    canvas.draw()
    canvas.get_tk_widget().pack()

frame_histogram = Frame(root)
frame_histogram.pack(side="top", fill="both", expand=True)

frame_bar_region = Frame(root)
frame_bar_region.pack(side="top", fill="both", expand=True)

frame_bar_income = Frame(root)
frame_bar_income.pack(side="top", fill="both", expand=True)

Button(root, text="Show Histogram", command=create_histogram).pack()
Button(root, text="Show Bar Chart by Region", command=create_bar_chart_region).pack()
Button(root, text="Show Bar Chart by Income Group", command=create_bar_chart_income).pack()

root.mainloop()
