# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

df = pd.read_csv('/content/co_basket.csv')

df.head()

df.columns[1:]

df.set_index(df.columns[1:], inplace=True)

df

df.drop(columns=['Description'], inplace=True)

df

np.fill_diagonal(df.values, 0)

df

from scipy.stats import chi2

# Function to calculate the minimum observed frequency
def min_significant_count(total_sales, row_sum, col_sum, alpha=0.05):
    # Critical value for chi-square at given alpha (df=1)
    chi2_critical = chi2.ppf(1 - alpha, df=1)

    # Expected frequency
    expected = (row_sum * col_sum) / total_sales

    # Solve for minimum observed count (O) using chi2 = (O - E)^2 / E
    min_O = expected + (chi2_critical * expected) ** 0.5
    return min_O

# Example inputs
total_sales = 18046
row_sum = 22   # Total sales involving Product 1
col_sum = 95   # Total sales involving Product 2

# Calculate the minimum observed count for significance
min_count = min_significant_count(total_sales, row_sum, col_sum)
print(f"Minimum observed count for significance: {min_count:.2f}")

# Apply the filter to your DataFrame
def filter_significant_pairs(df, total_sales, alpha=0.05):
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

    return significant_pairs

# Get significant pairs
significant_pairs = filter_significant_pairs(df, total_sales=18046)
print(significant_pairs)
# significant_pairsDF = pd.DataFrame(significant_pairs, columns=['Product 1', 'Product 2', 'Observed'])

significant_pairsDF = pd.DataFrame(significant_pairs, columns=['Product 1', 'Product 2', 'Observed'])

significant_pairsDF.sort_values(by='Observed', ascending=False)

significant_pairsDF.sort_values(by='Observed', ascending=False).to_csv('significant_pairs.csv')