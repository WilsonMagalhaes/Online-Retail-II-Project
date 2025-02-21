# -*- coding: utf-8 -*-


import pandas as pd
df = pd.read_csv('/content/cleaned_data_online_retail_II.csv')

df.head()

df.info()

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#Invoices per country
df.groupby('Country')['Invoice'].nunique().sort_values(ascending=False)

#Most revenue per country
df['Revenue'] = df['Quantity'] * df['Price']
df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

#Revenue per customer
df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False)

#Quantity of products sold per customer
df.groupby('Customer ID')['Quantity'].sum().sort_values(ascending=False)

#Most invoices per customer
df.groupby('Customer ID')['Invoice'].nunique().sort_values(ascending=False)

#Most expensive invoices
df.groupby('Invoice')['Revenue'].sum().sort_values(ascending=False)

#Products most sold
df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)

#Revenue per product
df.groupby('Description')['Revenue'].sum().sort_values(ascending=False)

#Most sold products in the United Kingdom
df[df['Country']=='United Kingdom'].groupby('Description')['Quantity'].sum().sort_values(ascending=False)

#Countries with the most customers
df.groupby('Country')['Customer ID'].nunique().sort_values(ascending=False)

df.set_index('InvoiceDate', inplace=True)

df.head()

#See all the possible frequencies
#https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

#Total revenue per calendar day
df.groupby(pd.Grouper(freq='D'))['Revenue'].sum().sort_values(ascending=False)

#Total revenue per week
df.groupby(pd.Grouper(freq='W'))['Revenue'].sum().sort_values(ascending=False)

#Total revenue per semi month (1st to 15th)
df.groupby(pd.Grouper(freq='SMS'))['Revenue'].sum().sort_values(ascending=False)

#Total revenue per month end
df.groupby(pd.Grouper(freq='ME'))['Revenue'].sum().sort_values(ascending=False)

#Total revenue per quarter end
df.groupby(pd.Grouper(freq='QE'))['Revenue'].sum().sort_values(ascending=False)

#Total revenue per year end
df.groupby(pd.Grouper(freq='YE'))['Revenue'].sum().sort_values(ascending=False)

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

meDF = df.groupby(pd.Grouper(freq='ME'))['Revenue'].sum().sort_values(ascending=False).head(10)
meDF = meDF.reset_index()
meDF['InvoiceDate'] = meDF['InvoiceDate'].dt.strftime('%b-%Y')
meDF.head()
ax = meDF.plot(x='InvoiceDate', y='Revenue', kind='bar')
plt.xticks(rotation=45)
plt.ylim(0, meDF['Revenue'].max() * 1.1) #Multiply for 1.1 so the chart goes higher then the max valueu of the revenue (Y axis)
plt.xlabel('Month end')
plt.ylabel('Revenue')
plt.title('Top 10 total revenue per month end')
formatter = FuncFormatter(lambda x, _: f'{x:,.0f}') #Change the Y axis range from 0 to 1 with scientific notation (1eX) to the real values
ax.yaxis.set_major_formatter(formatter)
plt.show()

ax = df.groupby(pd.Grouper(freq='D'))['Revenue'].sum().plot(kind='line')

ax = df.groupby(pd.Grouper(freq='SMS'))['Revenue'].sum().plot(kind='line')

ax = df.groupby(pd.Grouper(freq='ME'))['Revenue'].sum().plot(kind='line')

ax = df[df['Country']=='United Kingdom'].groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10).plot(x='Description', y='Revenue', kind='bar')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.title('Top 10 most sold products in the UK')
plt.show()