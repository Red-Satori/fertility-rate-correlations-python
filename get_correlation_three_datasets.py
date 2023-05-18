import json
import pandas as pd

# Load hdi data
with open('hdi_data.json', 'r') as file:
    hdi_data = json.load(file)

# Load tfr data
with open('tfr_data.json', 'r') as file:
    tfr_data = json.load(file)

# Load gii data
with open('gii_data.json', 'r') as file:
    gii_data = json.load(file)

# Convert to pandas DataFrame
hdi_df = pd.DataFrame(hdi_data)
tfr_df = pd.DataFrame(tfr_data)
gii_df = pd.DataFrame(gii_data)

# Merge all dataframes on 'country' column
merged_df = pd.merge(hdi_df, tfr_df, on='country')
merged_df = pd.merge(merged_df, gii_df, on='country')

# Drop rows with missing values in 'hdi', 'tfr', or 'gii_value' columns
merged_df.dropna(subset=['hdi', 'tfr', 'gii_value'], inplace=True)

# Calculate correlation matrix
correlation_matrix = merged_df[['hdi', 'tfr', 'gii_value']].corr()

print(f"Correlation matrix:\n {correlation_matrix}")