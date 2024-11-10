from king22.clean import Clean2022
from king23.clean import Clean2023
from king24.clean import Clean2024

Cleaner2022 = Clean2022()
dels_2022 = Cleaner2022.clean_del()
advs_2022 = Cleaner2022.clean_adv()

Cleaner2023 = Clean2023()
dels_2023 = Cleaner2023.clean_del()
advs_2023 = Cleaner2023.clean_adv()

Cleaner2024 = Clean2024()
dels_2024 = Cleaner2024.clean_del()
advs_2024 = Cleaner2024.clean_adv()

schools1 = advs_2022['School'].unique()
schools2 = advs_2023['School'].unique()
schools3 = advs_2024['School'].unique()

set1 = set(schools1)
set2 = set(schools2)
set3 = set(schools3)
common_schools = set1 & set2 & set3
# Filter datasets to include only schools present in all datasets
df1_common = advs_2022[advs_2022['School'].isin(common_schools)]
df2_common = advs_2023[advs_2023['School'].isin(common_schools)]
df3_common = advs_2024[advs_2024['School'].isin(common_schools)]

df1_common, df2_common, df3_common
df_merged = df1_common.merge(df2_common, on='School', suffixes=(' 2022', ' 2023'))
df_merged = df_merged.merge(df3_common, on='School')
df_merged.rename(columns={'Num. of Dels': 'Num. of Dels 2024'}, inplace=True)

# print(df_merged)
# Calculate changes in participation
df_merged['change_year1_to_year2'] = df_merged['Num. of Dels 2023'] - df_merged['Num. of Dels 2022']
df_merged['change_year2_to_year3'] = df_merged['Num. of Dels 2024'] - df_merged['Num. of Dels 2023']

# Calculate percentage changes if needed
df_merged['percent_change_year1_to_year2'] = (df_merged['change_year1_to_year2'] / df_merged['Num. of Dels 2022']) * 100
df_merged['percent_change_year2_to_year3'] = (df_merged['change_year2_to_year3'] / df_merged['Num. of Dels 2023']) * 100

# View the trends
# print(df_merged[['School', 'change_year1_to_year2', 'change_year2_to_year3', 
                #  'percent_change_year1_to_year2', 'percent_change_year2_to_year3']])

# Total delegates in each year
total_year1 = df_merged['Num. of Dels 2022'].sum()
total_year2 = df_merged['Num. of Dels 2023'].sum()
total_year3 = df_merged['Num. of Dels 2024'].sum()

total_year1, total_year2, total_year3

# Calculate overall percentage change across the years
overall_change_year1_to_year2 = (total_year2 - total_year1) / total_year1 * 100
overall_change_year2_to_year3 = (total_year3 - total_year2) / total_year2 * 100

# print(f"Overall change 2022 to 2023: {overall_change_year1_to_year2:.2f}%")
# print(f"Overall change 2023 to 2024: {overall_change_year2_to_year3:.2f}%")

# no percent change in dels from these 19 schools that attended all 3 years
# Sort by the largest increase or decrease in participation between Year 1 and Year 3
df_merged['total_change'] = df_merged['Num. of Dels 2024'] - df_merged['Num. of Dels 2022']
df_merged.sort_values(by='total_change', ascending=False, inplace=True)

# View the schools with the most growth or decline
# print(df_merged[['School', 'total_change']])
import matplotlib.pyplot as plt

# Plot participation trends for each school
for index, row in df_merged.iterrows():
    plt.plot([1, 2, 3], [row['Num. of Dels 2022'], row['Num. of Dels 2023'], row['Num. of Dels 2024']], label=row['School'])

plt.title('School Participation Trends Over the Years')
plt.xlabel('Year')
# plt.figure(figsize=(15, 10))
plt.ylabel('Number of Delegates')
plt.xticks([1, 2, 3], ['2022', '2023', '2024'])
plt.legend()
plt.show()