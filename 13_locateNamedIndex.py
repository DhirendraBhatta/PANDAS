# # Locate Named Indexes
# # Use the named index in the loc attribute to return the specified row(s).

# Example
# Return "day2":

#refer to the named index:
import pandas as pd

dataset={
"vehicle":["car","bike","bus"],
"price":[400000,200000,600000]
}

df=pd.DataFrame(dataset,index=["day1","day2",'day3'])
print(df.loc["day2"])

# Output:
# vehicle      bike
# price      200000
# Name: day2, dtype: object
