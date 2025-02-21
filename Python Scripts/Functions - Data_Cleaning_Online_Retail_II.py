import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the dataset from an Excel file."""
    return pd.read_excel(file_path)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and preprocesses the dataset."""
    # Convert data types
    df['StockCode'] = df['StockCode'].astype(str)
    df['Invoice'] = df['Invoice'].astype(str)
    
    # Remove rows with missing Customer ID
    invoice_to_remove = df[df['Customer ID'].isnull()]['Invoice'].unique()
    df = df[~df['Invoice'].isin(invoice_to_remove)]
    
    # Remove negative or zero Quantity (except for cancellations starting with 'C')
    negative_quantity_invoices = df[(df['Quantity'] <= 0) & (~df['Invoice'].str.startswith('C'))]['Invoice'].unique()
    df = df[~df['Invoice'].isin(negative_quantity_invoices)]
    
    # Correct negative or zero prices using mode of valid prices
    wrong_price_products = df[df['Price'] <= 0]['StockCode'].unique()
    for product in wrong_price_products:
        correct_price = df.loc[(df['StockCode'] == product) & (df['Price'] > 0), 'Price'].mode()
        if not correct_price.empty:
            df.loc[(df['StockCode'] == product) & (df['Price'] <= 0), 'Price'] = correct_price[0]
    
    # Remove extremely low prices (<= 0.001)
    low_price_invoices = df[df['Price'] <= 0.001]['Invoice'].unique()
    df = df[~df['Invoice'].isin(low_price_invoices)]
    
    # Remove rows with unwanted descriptions
    unwanted_descriptions = ['Adjustment by', 'POSTAGE', 'Manual']
    df = df[~df['Description'].str.contains('|'.join(unwanted_descriptions), na=False)]
    
    return df

def save_cleaned_data(df: pd.DataFrame, output_path: str):
    """Saves the cleaned dataset to a CSV file."""
    df.to_csv(output_path, index=False)


def main():
    """Main function to execute the script."""
    file_path = 'online_retail_II.xlsx'  # Adjust the path if needed
    output_path = 'cleaned_data_online_retail_II.csv'
    
    df = load_data(file_path)
    df_cleaned = preprocess_data(df)
    save_cleaned_data(df_cleaned, output_path)

    
if __name__ == "__main__":
    main()
