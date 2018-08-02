# Load library
import pandas as pd


# create URL
url = 'https://tinyurl.com/titanic-csv'

# Load data as a dataframe
dataframe = pd.read_csv(url)

# Show first 5 rows
print(dataframe.head(5))

#Show dimensions
print('dataframe: ',dataframe.shape)

#Show statistics
print('Statistics: ',dataframe.describe())

# Select first row
print(dataframe.iloc[0])

# Select first three
print(dataframe.iloc[1:4])

# Show top two rows where column 'sex' is 'female'
print(dataframe[dataframe['Sex']=='female'].head(5))

# Rename column, show two rows
dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2)
print(dataframe)

# Calculate statistics
print('Max:',dataframe['Age'].max())
print('Min:',dataframe['Age'].min())
print('Mean:',dataframe['Age'].mean())
print('Sum:',dataframe['Age'].sum())
print('Count:',dataframe['Age'].count())

# Select unique values
print('Unique values:',dataframe['Sex'].unique())

# Show unique counts
print(dataframe['Sex'].value_counts())