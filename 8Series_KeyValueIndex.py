import pandas as pd
ds={"day1":200,"day2":499,"day3":345}
dser=pd.Series(ds,index=["day1","day2"])
print(dser)

# Output:
# day1    200
# day2    499
# dtype: int64

# import pandas as pd
# ds={"day1":"hello","day2":"hi","day3":"bye"}
# dser=pd.Series(ds,index=["day1","day3"])
# print(dser)

# Output:
# day1    hello
# day3      bye
# dtype: object