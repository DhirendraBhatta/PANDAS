# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# Example
# Load a comma separated file (CSV file) into a DataFrame:


import pandas as pd
# df=pd.read_csv("Tickets.csv")

df=pd.read_csv("All Tickets_20251124.csv")
# print(df)
print(df.to_string())

# Tip: use to_string() to print the entire DataFrame.

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:


# Note:self:
# to_string displays all the contents of the table otherwise if only printing the datasets,it will display like .......not showing all data


# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# Example
# Print the DataFrame without the to_string() method:

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df) 

# Records displays like below:
# 1
# 2
# 3
# 4
# 5
# .......
# 196
# 197
# 198
# 199
# 200