import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the correlation dataset from a CSV file."""
    return pd.read_csv(file_path)

def compute_semantic_similarity(df: pd.DataFrame) -> pd.DataFrame:
    """Computes semantic similarity between product descriptions using embeddings."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    df['Embedding1'] = df['Description1'].apply(lambda x: model.encode(x))
    df['Embedding2'] = df['Description2'].apply(lambda x: model.encode(x))
    
    df['SemanticSimilarity'] = df.apply(
        lambda row: cosine_similarity([row['Embedding1']], [row['Embedding2']])[0][0], axis=1
    )
    
    return df

def identify_non_obvious_pairs(df: pd.DataFrame, high_corr: float = 0.7, low_sim: float = 0.4) -> pd.DataFrame:
    """Identifies product pairs with high correlation but low semantic similarity."""
    return df[(df['Correlation'] > high_corr) & (df['SemanticSimilarity'] < low_sim)]

def plot_correlation_vs_similarity(df: pd.DataFrame):
    """Plots correlation against semantic similarity."""
    plt.scatter(df['Correlation'], df['SemanticSimilarity'])
    plt.xlabel('Correlation')
    plt.ylabel('Semantic Similarity')
    plt.title('Correlation vs. Semantic Similarity')
    plt.show()

def save_results(df: pd.DataFrame, output_path: str):
    """Saves the results to a CSV file."""
    df.to_csv(output_path, index=False)

def main():
    """Main function to execute the script."""
    input_path = 'dataFrameWithDescriptionsAndCorrelation.csv'
    output_path = 'non_obvious_pairs.csv'
    
    df = load_data(input_path)
    df = compute_semantic_similarity(df)
    non_obvious_pairs = identify_non_obvious_pairs(df)
    save_results(non_obvious_pairs, output_path)
    plot_correlation_vs_similarity(df)
    
if __name__ == "__main__":
    main()
