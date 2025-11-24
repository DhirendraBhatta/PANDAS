
# locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.

# Pandas use the loc attribute to return one or more specified row(s)

# Example
# Return row 0:

#refer to the row index:

# import pandas as pd
# data={
#     "calories":[200,300,499,500],
#     "duration":[40,20,50,78],
# }

# df=pd.DataFrame(data)
# print(df)
# print(df.loc[0])
# print(df.loc[3])

# Note:
# If values length mismatched then length mismatch KeyError
# If fetching index with greater size than the length of an array,then KeyError


# Output:
#    calories  duration
# 0       200        40
# 1       300        20
# 2       499        50
# 3       500        78

# calories    200
# duration     40
# Name: 0, dtype: int64

# calories    500
# duration     78
# Name: 3, dtype: int64


# Simulation:
import pandas as pd
data={
    "calories":[200,300,499,500],
    "duration":[40,20,50,78],
    "age":40
}

df=pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[3])