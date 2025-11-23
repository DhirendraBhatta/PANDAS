# import pandas as pd
# ds={
# 'Name':'Sanvi Bhatta',
# 'Age':4,
# 'Gender':'F'
# }

# df=pd.Series(ds)
# print(df)

# Output:
# Name      Sanvi Bhatta
# Age                  4
# Gender               F
# dtype: object


# import pandas as pd
# ds={
# 'Name':['Sanvi',' Bhatta'],
# 'Age':[4,3],
# 'Gender':['F','M']
# }

# df=pd.DataFrame(ds)
# print(df)

# Output:
#       Name  Age Gender
# 0    Sanvi    4      F
# 1   Bhatta    3      M



#Self: If directly provided the value ,then it is default for all the columns,but if in the list and value not matched ,then error for the matching fields.
import pandas as pd
ds={
'Name':['Sanvi',' Bhatta','BHATTA'],
'Age':4,
'Gender':'F'
}

df=pd.DataFrame(ds)
print(df)

# Output:
#       Name  Age Gender
# 0    Sanvi    4      F
# 1   Bhatta    4      F
# 2   BHATTA    4      F

