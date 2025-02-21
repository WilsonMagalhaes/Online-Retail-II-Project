<<<<<<< HEAD
# Online-Retail-II-Project
=======
# Project Overview

This project analyzes customer purchasing behavior using the Online Retail II dataset. It includes data cleaning, co-occurrence analysis, semantic similarity calculations, statistical significance testing, and querying for key business insights. The analysis is conducted through Python scripts, Google Colab notebooks, and Power BI visualizations.

## Folder Structure

### 1. **DataBases**
   - Contains all databases used in this project.
   - Includes the main dataset: [Online Retail II](https://archive.ics.uci.edu/ml/datasets/online+retail+II).
   - Stores additional datasets created during the project.

### 2. **Notebooks**
   - Contains Google Colab notebooks documenting every step of the project.
   - Each notebook includes data transformations, visualizations, and insights.
   - Refer to `Notebooks Explanations.txt` for details on each notebook.

### 3. **Notebooks in py**
   - Stores the Google Colab notebooks converted into `.py` files.
   - Useful for viewing code in text editors or IDEs that do not support `.ipynb` format.

### 4. **Power BI**
   - Contains a `.pbix` file with data visualizations and analyses.
   - Uses Microsoft Power BI Desktop to explore cleaned data.

### 5. **Python Scripts**
   - Includes Python scripts that automate the tasks performed in notebooks.
   - Provides a streamlined approach to running the analysis.
   - Recommended for quick execution, whereas notebooks are better for understanding step-by-step processes.

## Notebooks & Scripts Overview

1. **Data Cleaning (Data_Cleaning_Online_Retail_II)**
   - Loads and cleans the dataset by handling missing values, invalid prices, and unreliable data.
   - Saves cleaned data as `cleaned_data_online_retail_II.csv`.

2. **Co-Occurrence Analysis (Create_Product_Correlation_Table)**
   - Creates a basket matrix (products per invoice) and computes a co-occurrence matrix.
   - Normalizes values to measure product relationships.
   - Saves results in `co_basket.csv`.

3. **Semantic Similarity (Calculate_Semantics_X_Correlation)**
   - Uses Sentence Transformers to compute semantic similarity between product descriptions.
   - Identifies product pairs with high correlation but low semantic similarity.
   - Saves output as `dataFrameWithDescriptionsAndCorrelation.csv`.

4. **Statistical Significance (Statistical_Significance_Test)**
   - Applies Chi-Square tests to filter statistically significant product relationships.
   - Ensures observed relationships are not due to random chance.
   - Saves filtered results as `significant_pairs.csv`.

5. **Query and Analysis (Queries_And_Analysis)**
   - Extracts business insights such as revenue per country, customer, and product.
   - Identifies top-selling products and revenue trends.
   - Generates visualizations to summarize findings.

## Usage
- To explore the step-by-step process, use notebooks in the `Notebooks` folder.
- For a quick execution of the analysis, run scripts from the `Python Scripts` folder.
- To visualize the insights interactively, open the Power BI file in `Power BI` folder.

---
This project leverages statistical methods and machine learning techniques to uncover valuable insights from retail transaction data.
>>>>>>> c85eb4d (Initial commit)
