# Example
# Increase the maximum number of rows to display the entire DataFrame:

# import pandas as pd
# df = pd.read_csv("Tickets.csv")
# print(df) 

# Output:
# 0         5979998  24/11/2025 14:40                      Newly user not able to login  ...  Severity III               NaN                 NaN
# 1         1733069  22/11/2025 12:01                       unable to verify from HLARA  ...  Severity III               NaN                 NaN
# 2         5637921  19/11/2025 17:56                             BIRT/GIFT enhancement  ...  Severity III               NaN      Sumesh Pradhan
# 3         3056703  19/11/2025 17:52                             BIRT/GIFT enhancement  ...  Severity III               NaN                 NaN
# 4         7863963  19/11/2025 17:51                             BIRT/GIFT enhancement  ...  Severity III               NaN                 NaN
# ..            ...               ...                                               ...  ...           ...               ...                 ...
# 95        4784908   6/11/2025 11:39                      Issue While Performing HLARA  ...   Severity II               NaN           Leki Dema
# 96        2229016   6/11/2025 11:25                      Issue While Performing HLARA  ...           NaN               NaN                 NaN
# 97        6780415   5/11/2025 16:14  Backdated transaction issue for a particular acc  ...  Severity III  10/11/2025 10:28  Neera Devi Acharya
# 98        3023157   5/11/2025 11:27                 LASPAY PAYMENT VERIFICATION ISSUE  ...    Severity I               NaN           Leki Dema
# 99        9430577   4/11/2025 12:44                                        FIWEB DOWN  ...    Severity I   4/11/2025 15:32  Neera Devi Acharya




import pandas as pd
pd.options.display.max_rows=9999
df=pd.read_csv("Tickets.csv")
print(df)


# Note:
# It displays the full rows indexing form 0 to 99 for 100 records and header at top without indexing

#     Ticket Number      Date Created                                            Subject  ...      SLA Plan       Closed Date      Agent Assigned
# 0         5979998  24/11/2025 14:40                       Newly user not able to login  ...  Severity III               NaN                 NaN
# 1         1733069  22/11/2025 12:01                        unable to verify from HLARA  ...  Severity III               NaN                 NaN
# 2         5637921  19/11/2025 17:56                              BIRT/GIFT enhancement  ...  Severity III               NaN      Sumesh Pradhan
# 3         3056703  19/11/2025 17:52                              BIRT/GIFT enhancement  ...  Severity III               NaN                 NaN
# 4         7863963  19/11/2025 17:51                              BIRT/GIFT enhancement  ...  Severity III               NaN                 NaN
# 5         8901553  19/11/2025 17:50        

# All records shown like above



# Note:
# CHATGPT:
# hightes limit to set the max_rows value
# pandas.options.display.max_rows has no hard-coded highest limit — you can set it to any integer value or None.
# ✔ Official Behavior
# max_rows accepts:
# Any positive integer (1, 1000, 1000000, etc.)

# None → means no limit



# Example:
# pd.set_option('display.max_rows', 10_000_000)

# Pandas will accept it.
# ⚠ Practical Limit
# Even though there is no maximum, the real-world limit is:


# Your system RAM,


# Your terminal or Jupyter environment’s ability to render massive output.


# If you set too large a number and print a huge DataFrame, it may:


# Freeze your notebook/IDE,


# Flood the output,


# Crash the session.


# 🔥 Unlimited Output
# pd.set_option('display.max_rows', None)

# 📌 Summary
# SettingMeaning1000, 1e6, etc.Pandas allows any large integerNoneInfinite displayTrue limitDepends on your system and output environment
# So the highest limit is only restricted by your system, not pandas itself.