import json
import pandas as pd
from scipy.stats import pearsonr

# Load hdi data
with open('hdi_data.json', 'r') as file:
    hdi_data = json.load(file)

# Load tfr data
with open('tfr_data.json', 'r') as file:
    tfr_data = json.load(file)

# Convert to pandas DataFrame
hdi_df = pd.DataFrame(hdi_data)
tfr_df = pd.DataFrame(tfr_data)

# Merge both dataframes on 'country' column
merged_df = pd.merge(hdi_df, tfr_df, on='country', suffixes=('_hdi', '_tfr'))

# Drop rows with missing values in 'hdi' or 'tfr' columns
merged_df.dropna(subset=['hdi', 'tfr'], inplace=True)

# Calculate Pearson's correlation coefficient
correlation, _ = pearsonr(merged_df['hdi'], merged_df['tfr'])

print(f"Pearson's correlation coefficient between HDI and TFR is: {correlation}")