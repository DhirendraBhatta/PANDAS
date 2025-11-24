import pandas as pd

dataset={
"vehicle":["car","bike","bus"],
"price":[400000,200000,600000]
}

df=pd.DataFrame(dataset,index=["day1","day2",'day3'])
# print(df)
print(df)
print("")
print(df.loc["day2"])

# Output:
#      vehicle   price
# day1     car  400000
# day2    bike  200000
# day3     bus  600000

