# fertility-rate-correlations-python
Python scripts for parsing and analyzing data related to three global indices: HDI, TFR, and GII

This repository contains Python scripts for parsing and analyzing data related to three global indices: the Human Development Index (HDI), Total Fertility Rate (TFR), and Gender Inequality Index (GII).

The data is parsed using regular expressions from raw strings and stored in JSON format. Then, the data from these three indices is loaded into Pandas dataframes and merged based on the 'country' column. Finally, a correlation matrix is calculated to identify potential relationships between these indices.

The main findings indicate strong negative relationships between HDI and both TFR and GII, and a positive correlation between TFR and GII. This analysis provides interesting insights into global development trends and highlights the close relationship between human development, fertility rates, and gender inequality.

Please note that this is a preliminary analysis and correlation does not imply causation. More robust statistical analysis would be required to determine causal relationships.

## ChatGPT Analysis

```
Correlation matrix:
                 hdi       tfr  gii_value
hdi        1.000000 -0.864450  -0.940867
tfr       -0.864450  1.000000   0.809357
gii_value -0.940867  0.809357   1.000000
```

_Can you explain what this means?_

### Response

Sure, the matrix you're seeing is called a correlation matrix, and it gives you the pairwise correlations of all the columns in the DataFrame. Each cell in the table shows the correlation between two variables.

The correlation coefficient ranges from -1 to 1.

A correlation coefficient of 1 means that for every positive increase in one variable, there is a positive increase of a fixed proportion in the other. For example, shoe sizes go up in (almost) perfect correlation with foot length.

A correlation coefficient of -1 means that for every positive increase in one variable, there is a negative decrease of a fixed proportion in the other. For example, the amount of time it takes to run a mile decreases in correlation with the increase in one's fitness level.

Zero means that for every increase, there isn’t a positive or negative increase. The two just aren’t related.

In your result:

The correlation between hdi and tfr is approximately -0.86, indicating a strong negative relationship. This suggests that as the Human Development Index (HDI) increases, the Total Fertility Rate (TFR) tends to decrease.

The correlation between hdi and gii_value is approximately -0.94, which is also a strong negative relationship. This implies that as the Human Development Index (HDI) increases, the Gender Inequality Index (GII) tends to decrease. This makes sense as higher development is often associated with lower gender inequality.

The correlation between tfr and gii_value is approximately 0.81, indicating a strong positive relationship. This suggests that higher Total Fertility Rates (TFR) are associated with higher Gender Inequality Index (GII) values, i.e., higher gender inequality.

Remember, correlation does not imply causation. These are just relationships between variables, and it doesn't mean that changing one variable will change another. It might be that both variables are being affected by other factors, or the correlation could be a coincidence. More robust statistical analysis would be required to determine causal relationships.

![Womens Fertility Drops when they have more rights](https://github.com/Red-Satori/fertility-rate-correlations-python/assets/117653020/c30b425c-5aff-4218-9a33-73ff14de0846)
