import pandas as pd
import numpy as np
from scipy.stats import chi2

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the co-occurrence matrix from a CSV file."""
    df = pd.read_csv(file_path, index_col=0)
    np.fill_diagonal(df.values, 0)  # Remove self-correlation
    return df

def min_significant_count(total_sales: int, row_sum: int, col_sum: int, alpha: float = 0.05) -> float:
    """Calculates the minimum observed frequency required for statistical significance."""
    chi2_critical = chi2.ppf(1 - alpha, df=1)
    expected = (row_sum * col_sum) / total_sales
    min_O = expected + (chi2_critical * expected) ** 0.5
    return min_O

def filter_significant_pairs(df: pd.DataFrame, total_sales: int, alpha: float = 0.05) -> pd.DataFrame:
    """Identifies statistically significant product pairs based on chi-square criteria."""
    significant_pairs = []
    products = df.index
    
    for i, product1 in enumerate(products):
        for product2 in products[i + 1:]:
            observed = df.at[product1, product2]
            row_sum = df.loc[product1].sum()
            col_sum = df[product2].sum()
            min_count = min_significant_count(total_sales, row_sum, col_sum, alpha)
            
            if observed >= min_count:
                significant_pairs.append((product1, product2, observed))
    
    return pd.DataFrame(significant_pairs, columns=['Product 1', 'Product 2', 'Observed']).sort_values(by='Observed', ascending=False)

def save_results(df: pd.DataFrame, output_path: str):
    """Saves the significant product pairs to a CSV file."""
    df.to_csv(output_path, index=False)

def main():
    """Main function to execute the script."""
    input_path = 'co_basket.csv'
    output_path = 'significant_pairs.csv'
    total_sales = 18046  # Adjust based on dataset
    
    df = load_data(input_path)
    significant_pairs_df = filter_significant_pairs(df, total_sales)
    save_results(significant_pairs_df, output_path)
    
if __name__ == "__main__":
    main()
