import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the cleaned dataset."""
    df = pd.read_csv(file_path)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['Price']
    return df

def invoices_per_country(df: pd.DataFrame) -> pd.Series:
    """Returns the number of invoices per country."""
    return df.groupby('Country')['Invoice'].nunique().sort_values(ascending=False)

def revenue_per_country(df: pd.DataFrame) -> pd.Series:
    """Returns the total revenue per country."""
    return df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

def revenue_per_customer(df: pd.DataFrame) -> pd.Series:
    """Returns the total revenue per customer."""
    return df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False)

def quantity_sold_per_customer(df: pd.DataFrame) -> pd.Series:
    """Returns the total quantity of products sold per customer."""
    return df.groupby('Customer ID')['Quantity'].sum().sort_values(ascending=False)

def most_sold_products(df: pd.DataFrame) -> pd.Series:
    """Returns the most sold products."""
    return df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)

def revenue_per_product(df: pd.DataFrame) -> pd.Series:
    """Returns the total revenue per product."""
    return df.groupby('Description')['Revenue'].sum().sort_values(ascending=False)

def revenue_over_time(df: pd.DataFrame, freq: str):
    """Plots revenue over a specified time frequency."""
    df.set_index('InvoiceDate', inplace=True)
    revenue = df.groupby(pd.Grouper(freq=freq))['Revenue'].sum()
    revenue.plot(kind='line', title=f'Revenue Over Time ({freq})')
    plt.show()

def top_products_uk(df: pd.DataFrame):
    """Plots the top 10 most sold products in the UK."""
    top_products = df[df['Country'] == 'United Kingdom'].groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    top_products.plot(kind='bar', title='Top 10 Most Sold Products in the UK')
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.show()

def main():
    """Main function to execute the script."""
    input_path = 'cleaned_data_online_retail_II.csv'
    df = load_data(input_path)
    
    print("Invoices per Country:\n", invoices_per_country(df).head(10))
    print("\nRevenue per Country:\n", revenue_per_country(df).head(10))
    print("\nRevenue per Customer:\n", revenue_per_customer(df).head(10))
    print("\nQuantity Sold per Customer:\n", quantity_sold_per_customer(df).head(10))
    print("\nMost Sold Products:\n", most_sold_products(df).head(10))
    print("\nRevenue per Product:\n", revenue_per_product(df).head(10))
    
    revenue_over_time(df, 'ME')
    top_products_uk(df)
    
if __name__ == "__main__":
    main()
