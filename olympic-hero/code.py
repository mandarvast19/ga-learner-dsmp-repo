# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))
better_event = data['Better_Event'].value_counts().index[0]
better_event


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries = top_countries[0:-1]
def top_ten(df,col_name):
    country_list=[]
    ten_largest = df.nlargest(10,col_name)
    country_list = ten_largest.iloc[:,0]
    return country_list
top_10_summer = list(top_ten(top_countries,'Total_Summer'))
top_10_winter = list(top_ten(top_countries,'Total_Winter'))
top_10 = list(top_ten(top_countries,'Total_Medals'))
common=[]
s1 = set(top_10_summer)
s2 = set(top_10_winter)
s3 = set(top_10)
set1 = s1.intersection(s2)
final = set1.intersection(s3)
common = list(final)



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot('Country_Name','Total_Summer', kind='bar',figsize=(20,5))
winter_df.plot('Country_Name','Total_Winter', kind='bar',figsize=(20,5))
top_df.plot('Country_Name','Total_Medals', kind='bar',figsize=(20,5))


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
max1 = summer_df.sort_values(by=['Golden_Ratio'],ascending=False)
summer_max_ratio = max1['Golden_Ratio'].iloc[0]
summer_country_gold = max1['Country_Name'].iloc[0]


winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
max1 = winter_df.sort_values(by=['Golden_Ratio'],ascending=False)
winter_max_ratio = max1['Golden_Ratio'].iloc[0]
winter_country_gold = max1['Country_Name'].iloc[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
max1 = top_df.sort_values(by=['Golden_Ratio'],ascending=False)
top_max_ratio = max1['Golden_Ratio'].iloc[0]
top_country_gold = max1['Country_Name'].iloc[0]


# --------------
#Code starts here
data_1 = data.iloc[0:-1]
data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)
data_1_max = data_1.sort_values(by=['Total_Points'],ascending=False)
most_points = data_1_max['Total_Points'].iloc[0]
best_country = data_1_max['Country_Name'].iloc[0]


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


