# Load library
import pandas as pd


# create URL
url = 'https://tinyurl.com/titanic-csv'

# Load data as a dataframe
dataframe = pd.read_csv(url)

# Show first 5 rows
print(dataframe.head(5))
