# -*- coding: utf-8 -*-


import pandas as pd

df2 = pd.read_excel('/content/online_retail_II.xlsx')

df2.head()

df2.info()

df2.describe()

df2.isnull().sum()

df2.duplicated().sum()

df2['StockCode'] = df2['StockCode'].astype(str)
df2['Invoice'] = df2['Invoice'].astype(str)

df2.isnull().sum()

df2.duplicated().sum()

# df2.drop_duplicates(inplace=True)

# df2.duplicated().sum()

df2.boxplot(column=['Quantity'])

df2.boxplot(column=['Price'])

filterCustomerNull = df2['Customer ID'].isnull()
df2_null = df2[filterCustomerNull]
indexToDeleCust =  df2_null['Customer ID'].index
print(indexToDeleCust)
invoiceToDele =  df2_null['Invoice'].unique()
print(invoiceToDele)
df_filtered = df2[~df2['Invoice'].isin(invoiceToDele)]

df_filtered.isna().sum()

df_filtered.describe()

filter = df_filtered['Quantity'] <= 0
df2_wrong = df_filtered[filter]

all_start_with_C = df2_wrong['Invoice'].str.startswith('C').sum()
print(all_start_with_C)
print(df2_wrong.shape)

filterQuantity = df_filtered['Quantity'] <= 0
df2_wrong = df_filtered[filterQuantity]
invoiceToDeleteQuantity =  df2_wrong['Invoice'].unique()
print(invoiceToDeleteQuantity)
df_filtered2 = df_filtered[~df_filtered['Invoice'].isin(invoiceToDeleteQuantity)]

df_filtered2.describe()

# filterPrice = df_filtered2['Price'] <= 0
# df2_wrongPrice = df_filtered2[filterPrice]
# print(df2_wrongPrice.shape)
# listOfProducts = df2_wrongPrice['StockCode'].unique()
# print(listOfProducts)
# invoiceToDeletePrice =  df2_wrong['Invoice'].unique()
# print(invoiceToDeletePrice)
# df_filtered2.loc[]

# Filter rows where Price <= 0
filterPrice = df_filtered2['Price'] <= 0
df2_wrongPrice = df_filtered2[filterPrice]

# Get unique products with incorrect prices
listOfProducts = df2_wrongPrice['StockCode'].unique()

# Iterate through the list of products with wrong prices
for product in listOfProducts:
    # Find the most common price for this product in rows with correct prices
    correct_price = df_filtered2.loc[(df_filtered2['StockCode'] == product) & (df_filtered2['Price'] > 0), 'Price'].mode()

    if not correct_price.empty:  # If a valid price exists
        # Update the wrong prices in the DataFrame
        df_filtered2.loc[(df_filtered2['StockCode'] == product) & (df_filtered2['Price'] <= 0), 'Price'] = correct_price[0]

# Check the updated DataFrame
df_filtered2

df_filtered2.describe()

df_filtered2.sort_values(by='Price', ascending=False).head(15)

pd.set_option('display.max_rows', 15)

filterPriceDelete = df_filtered2['Price'] <= 0.001
df2_wrongPrice = df_filtered2[filterPriceDelete]
invoiceToDeletePrice =  df2_wrongPrice['Invoice'].unique()
print(invoiceToDeletePrice)
df_filtered3 = df_filtered2[~df_filtered2['Invoice'].isin(invoiceToDeletePrice)]
df_filtered3

df_filtered3.describe()

all_worng_description = ((df_filtered3['Description'].str.contains('Adjustment by')) | (df_filtered3['Description'] == ('POSTAGE')) | (df_filtered3['Description'] == ('Manual')))
wrong_descriptionDF = df_filtered3[all_worng_description]
listOfWrongDescriptionInvoices =  wrong_descriptionDF['Invoice'].unique()
print(listOfWrongDescriptionInvoices)
df_filtered4 = df_filtered3[~df_filtered3['Invoice'].isin(listOfWrongDescriptionInvoices)]
df_filtered4

df_filtered4.head(15)

df_filtered4.sort_values(by='Price', ascending=False).head(15)

df_filtered4.sort_values(by='Price', ascending=True).head(15)

df_filtered4.to_csv('cleaned_data_online_retail_II.csv', index=False)

df_filtered4.plot(x='Price', y='Quantity', kind='scatter')

df_filtered4['Price'].plot(kind='box')

df_filtered4['Quantity'].plot(kind='box')

df_filtered4.sort_values(by='Quantity', ascending=False).head(15)

# filter = df2['Quantity'] <= 0
# df2_wrong = df2[filter]
# indexToDele =  df2_wrong['Quantity'].index
# print(indexToDele)
# df2_wrong.sort_values(by='Quantity')