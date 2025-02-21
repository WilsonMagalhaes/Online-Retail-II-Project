# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

df = pd.read_csv('/content/cleaned_data_online_retail_II.csv')


df.nunique()


df.isna().sum()

basket = df.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0)
basket

basket = (basket > 0).astype(int)
basket

basket

co_basket = basket.T.dot(basket)

co_basket

co_basket.to_csv('co_basket.csv')

diagonal = np.diag(co_basket)

diagonal

norm = np.sqrt(diagonal)

norm

co_basketFilter = co_basket < 50
co_basket[co_basketFilter] = 0

co_basket

np.fill_diagonal(co_basket.values, 0)

co_basket


normalised = co_basket / norm[:, None] / norm[:,None]

normalised


stackedNormalized = normalised.stack().sort_values(ascending=False)

stackedNormalized.values

dataFrameWithDescriptionsAndCorrelation = pd.DataFrame({'Description1':stackedNormalized.index.get_level_values(0), 'Description2':stackedNormalized.index.get_level_values(1), 'Correlation': stackedNormalized.values})
dataFrameWithDescriptionsAndCorrelation

filterZeros = dataFrameWithDescriptionsAndCorrelation['Correlation'] == 0
dataFrameWithDescriptionsAndCorrelation[~filterZeros].to_csv('dataFrameWithDescriptionsAndCorrelation.csv', index=False)

dataFrameWithDescriptionsAndCorrelation[~filterZeros]