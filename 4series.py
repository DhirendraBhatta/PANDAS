# # Pandas Series:
# A pandas series like a column in a table.
# It is a one dimensional array holding data of any type.

# Eg:Create a simple pandas series from a list
import pandas as pd
a=[10,20,30]
myvar=pd.Series(a)
print(myvar)


# Tested for another column:
# import pandas as pd
# a=[10,20,30]
# b=[40,50,60]
# myvar=pd.Series(a,b)
# print(myvar)

# Output:
# 40    10
# 50    20
# 60    30
# dtype: int64