# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

# Return the first value of the Series:


import pandas as pd
a=[10,20,30]
myvar=pd.Series(a)
print(myvar[10])

# Output: 
# 10


# print(myvar[10])