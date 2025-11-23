# Create Labels
# With the index argument, you can name your own labels.

# Create your own label

# With the index argument ,you can name your labels.

import pandas as pd
a=[10,20,30]
myvar=pd.Series(a,index=['X','Y','Z'])
print(myvar)

# Output:
# X    10
# Y    20
# Z    30
# dtype: int64

# import pandas as pd
# a=[10,'Test',30]
# myvar=pd.Series(a,index=['X','Y','Z'])
# print(myvar)

# Output:
# X      10
# Y    Test
# Z      30
# dtype: object


# When you have created labels, you can access an item by referring to the label.

print(myvar['Y'])