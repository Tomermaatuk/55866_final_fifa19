import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Reading csv
data_file = 'fifa19.csv'
fifa = pd.read_csv(data_file, encoding='utf-8')

## Deleting irrelevant columns
columns = ['Photo', 'Flag', 'Club Logo', 'Special', 'Work Rate', 'Real Face', 'Jersey Number', 'Loaned From']
fifa.drop(columns, inplace=True, axis=1)
# print(fifa.head())

## Checking if and in which columns there are NaN values and how many total NaN's in the data
# print(fifa.isnull().any())
# print(fifa.isnull().sum().sum())

##Changing NaN in 'Release Clause' to 'No Release Clause' (there is a meaning to no existing release clause within itself)
fifa['Release Clause'].fillna('No Release Clause', inplace=True)

## Adding a column of the difference between overall and potential
fifa['Non Realized Poten'] = fifa['Potential'] - fifa['Overall']
# print(fifa['Non Realized Poten'].sort_values(ascending=False).head(n=20))

########## TRYING TO CHANGE LS INTO THE SUM - SUCCEEDED IN CHANGING TO LIST OF INT BUT NOT THEIR SUM
fifa["LS"] = fifa["LS"].str.split("+", expand = False)
fifa['LS'] = fifa['LS'].apply(pd.to_numeric)

test = fifa.iloc[1]['LS']
new = int(sum(test))
# test = new
df12 = fifa.set_value(1,'LS',new)
print(fifa['LS'].head())



# print('PRINTING WHAT IS IN THE LS COLUMN IN ROW 1, whata what', fifa.iloc[1]['LS'])







## Delete ???? rows which are missing many values, according to NaN in 'preferred foot' & 'position' 'Club' columns
fifa_1 = fifa.dropna(subset=['Preferred Foot', 'Position', 'Club'])
# print(fifa_1.isnull().any())
# print(fifa_1.isnull().sum().sum())

#Checking the type of data in column LS
# print(fifa_1.LS.dtype)

# csv_write = fifa.to_csv('fifa19_2.csv')


# #Create Correlation df
# corr = got.corr()
# #Plot figsize
# fig, ax = plt.subplots(figsize=(10, 10))
# #Generate Color Map
# colormap = sns.diverging_palette(220, 10, as_cmap=True)
# #Generate Heat Map, allow annotations and place floats in map
# sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
# #Apply xticks
# plt.xticks(range(len(corr.columns)), corr.columns);
# #Apply yticks
# plt.yticks(range(len(corr.columns)), corr.columns)

# plt.show()