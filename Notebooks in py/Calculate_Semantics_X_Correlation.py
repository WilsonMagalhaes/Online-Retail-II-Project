# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 100)

df = pd.read_csv('/content/dataFrameWithDescriptionsAndCorrelation.csv')

from sentence_transformers import SentenceTransformer

# Load a pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Compute embeddings for both descriptions
df['Embedding1'] = df['Description1'].apply(lambda x: model.encode(x))
df['Embedding2'] = df['Description2'].apply(lambda x: model.encode(x))

from sklearn.metrics.pairwise import cosine_similarity

# Calculate similarity
df['SemanticSimilarity'] = df.apply(
    lambda row: cosine_similarity([row['Embedding1']], [row['Embedding2']])[0][0],
    axis=1
)

# Define thresholds for analysis
high_correlation_threshold = 0.7  # Adjust as needed
low_similarity_threshold = 0.4   # Adjust as needed

# Identify pairs with high correlation and low similarity
non_obvious_pairs = df[
    (df['Correlation'] > high_correlation_threshold) &
    (df['SemanticSimilarity'] < low_similarity_threshold)
]

non_obvious_pairs

import matplotlib.pyplot as plt

plt.scatter(df['Correlation'], df['SemanticSimilarity'])
plt.xlabel('Correlation')
plt.ylabel('Semantic Similarity')
plt.title('Correlation vs. Semantic Similarity')
plt.show()