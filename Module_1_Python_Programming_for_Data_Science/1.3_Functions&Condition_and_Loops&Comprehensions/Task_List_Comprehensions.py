##################################################
# List Comprehensions
##################################################

# ###############################################
# # TASK 1: Use List Comprehension structure to convert the names of numeric variables in car_crashes data to uppercase and prefix them with NUM.
# ###############################################
#
# # Expected Output
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notes:
# # The names of non-numeric variables should also be capitalized.
# # It should be done with a single list comprehension.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()


["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# ###############################################
# # TASK 2: Use List Comprehension structure to add "FLAG" at the end of the names of variables in car_crashes data that do not contain "no".
# ###############################################
#
# # Notes:
# # All variable names should be capitalized.
# # It should be done with a single list comprehension.
#
# # Expected output:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# ###############################################
# # Task 3: Use List Comprehension structure to select variable names that are DIFFERENT from the given variable names and create a new dataframe.
# ###############################################
#
og_list = ["abbrev", "no_previous"]
#
# # Notes:
# # First, create a new list named new_cols using list comprehension according to the list above.
# # Then, select these variables by df[new_cols] to create a new dataframe named new_df.
#
# # Expected output:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()
