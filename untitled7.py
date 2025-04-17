import pandas as pd

file_path = "/mnt/data/hci_crime_752_pl_co_re_ca_2000-2013_21oct15-ada.xlsx"
xls = pd.ExcelFile("/content/hci_crime_752_pl_co_re_ca_2000-2013_21oct15-ada.xlsx")

sheet_names = xls.sheet_names
sheet_names

violent_crime_df = pd.read_excel(xls, sheet_name='ViolentCrime')

violent_crime_df.head()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

xls = pd.ExcelFile("hci_crime_752_pl_co_re_ca_2000-2013_21oct15-ada.xlsx")
violent_crime_df = pd.read_excel(xls, sheet_name='ViolentCrime')

filtered_df = violent_crime_df[['reportyear', 'geoname', 'rate']].dropna(subset=['rate'])

state_data = filtered_df[filtered_df['geoname'] == 'California']

sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.lineplot(data=state_data, x='reportyear', y='rate', marker='o')
plt.title("Trend of Violent Crime Rate in California (2000–2013)")
plt.xlabel("Year")
plt.ylabel("Violent Crime Rate per 1,000")
plt.tight_layout()
plt.show()


race_data = filtered_df[filtered_df['geoname'] == 'California']

race_avg = race_data.groupby('race_eth_name')['rate'].mean().reset_index()

race_avg = race_avg.sort_values(by='rate', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(data=race_avg, x='rate', y='race_eth_name', palette='viridis')
plt.title("Average Violent Crime Rate by Race/Ethnic Group in California (2000–2013)")
plt.xlabel("Average Violent Crime Rate per 1,000")
plt.ylabel("Race/Ethnic Group")
plt.tight_layout()
plt.show()


race_data = filtered_df[filtered_df['geoname'] == 'California']
race_avg = race_data.groupby('race_eth_name')['rate'].mean().reset_index()
race_avg = race_avg.sort_values(by='rate', ascending=False)


plt.figure(figsize=(10, 6))
sns.barplot(data=race_avg, x='rate', y='race_eth_name', palette='viridis')
plt.title("Average Violent Crime Rate by Race/Ethnic Group in California (2000–2013)")
plt.xlabel("Average Violent Crime Rate per 1,000")
plt.ylabel("Race/Ethnic Group")
plt.tight_layout()
plt.show()

county_data = filtered_df[~filtered_df['geoname'].isin(['California'])]

top_counties = county_data['geoname'].value_counts().head(10).index
subset = county_data[county_data['geoname'].isin(top_counties)]


plt.figure(figsize=(12, 6))
sns.boxplot(data=subset, x='geoname', y='rate', palette='coolwarm')
plt.xticks(rotation=45)
plt.title("Violent Crime Rate Distribution Across Top Counties (Outlier Detection)")
plt.xlabel("County")
plt.ylabel("Violent Crime Rate per 1,000")
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

corr_data = filtered_df.dropna(subset=['rate', 'denominator'])

plt.figure(figsize=(10, 6))
sns.scatterplot(data=corr_data, x='denominator', y='rate', hue='geoname', legend=False)
plt.title("Correlation Between Population and Violent Crime Rate")
plt.xlabel("Population")
plt.ylabel("Violent Crime Rate per 1,000")
plt.tight_layout()
plt.show()

correlation, p_value = pearsonr(corr_data['denominator'], corr_data['rate'])
print(f"Pearson Correlation: {correlation:.3f} (p-value: {p_value:.3e})")


summary_stats = filtered_df['rate'].describe()
print("Summary Statistics for Violent Crime Rates (Entire Dataset):\n")
print(summary_stats)

import seaborn as sns
import matplotlib.pyplot as plt


corr_df = filtered_df[['rate', 'denominator', 'reportyear']].dropna()

corr_matrix = corr_df.corr()


plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.show()