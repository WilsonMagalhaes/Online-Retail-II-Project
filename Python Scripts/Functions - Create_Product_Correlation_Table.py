import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path)

def create_basket_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Creates a basket matrix indicating product purchases per invoice."""
    basket = df.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0)
    basket = (basket > 0).astype(int)
    return basket

def compute_co_occurrence(basket: pd.DataFrame) -> pd.DataFrame:
    """Computes product co-occurrence matrix."""
    return basket.T.dot(basket)

def normalize_co_occurrence(co_basket: pd.DataFrame) -> pd.DataFrame:
    """Normalizes the co-occurrence matrix using product frequencies."""
    diagonal = np.diag(co_basket)
    norm = np.sqrt(diagonal)
    co_basket[co_basket < 50] = 0  # Apply threshold
    np.fill_diagonal(co_basket.values, 0)  # Remove self-correlation
    normalised = co_basket / norm[:, None] / norm[:, None]
    return normalised

def create_correlation_dataframe(normalised: pd.DataFrame) -> pd.DataFrame:
    """Creates a DataFrame with product correlations."""
    stacked_normalized = normalised.stack().sort_values(ascending=False)
    df_correlation = pd.DataFrame({
        'Description1': stacked_normalized.index.get_level_values(0),
        'Description2': stacked_normalized.index.get_level_values(1),
        'Correlation': stacked_normalized.values
    })
    return df_correlation[df_correlation['Correlation'] > 0]

def save_results(df: pd.DataFrame, output_path: str):
    """Saves the correlation data to a CSV file."""
    df.to_csv(output_path, index=False)

def main():
    """Main function to execute the script."""
    input_path = 'cleaned_data_online_retail_II.csv'
    output_path = 'dataFrameWithDescriptionsAndCorrelation.csv'
    
    df = load_data(input_path)
    basket = create_basket_matrix(df)
    co_basket = compute_co_occurrence(basket)
    normalised = normalize_co_occurrence(co_basket)
    df_correlation = create_correlation_dataframe(normalised)
    save_results(df_correlation, output_path)
    
if __name__ == "__main__":
    main()
