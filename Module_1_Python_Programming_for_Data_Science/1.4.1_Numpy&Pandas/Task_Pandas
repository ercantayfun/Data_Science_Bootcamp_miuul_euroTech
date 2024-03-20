##################################################
# Pandas Exercises
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Task 1: Load the Titanic dataset from the Seaborn library.
#########################################
df = sns.load_dataset("titanic")
df.head()
df.shape

#########################################
# Task 2: Find the number of male and female passengers in the Titanic dataset.
#########################################

df["sex"].value_counts()


#########################################
# Task 3: Find the number of unique values for each column.
#########################################

df.nunique()

#########################################
# Task 4: Find the unique values of the 'pclass' variable.
#########################################

df.loc[:,"pclass"].unique()

df["pclass"].unique()

df["pclass"].head()

#########################################
# Task 5: Find the number of unique values for 'pclass' and 'parch' variables.
#########################################

df[["pclass","parch"]].nunique()

#########################################
# Task 6: Check the data type of the 'embarked' variable. Change its type to category. Check its type again.
#########################################

df["embarked"].dtype
str(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
str(df["embarked"].dtype)
df.info()

#########################################
# Task 7: Show all information of passengers whose embarked value is 'C'.
#########################################

df[df["embarked"]=="C"].head(10)

#########################################
# Task 8: Show all information of passengers whose embarked value is not 'S'.
#########################################

df[df["embarked"] != "S"]["embarked"].unique()

df[~(df["embarked"] == "S")]["embarked"].unique()

a = df[df["embarked"] != "S"]
a["embarked"].unique()

#########################################
# Task 9: Show all information of female passengers under the age of 30.
#########################################

df[(df["age"]<30) & (df["sex"]=="female")].head()

#########################################
# Task 10: Show information of passengers whose fare is over 500 or age is over 70.
#########################################

df[(df["fare"] > 500 ) | (df["age"] > 70 )].info()

#########################################
# Task 11: Find the total number of missing values in each column.
#########################################

df.isnull().sum()

#########################################
# Task 12: Drop the 'who' variable from the dataframe.
#########################################

df.drop("who", axis=1, inplace=True)

df = df.drop("who", axis=1)

#########################################
# Task 13: Fill missing values in the 'deck' variable with the most frequent value (mode).
#########################################

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

#########################################
# Task 14: Fill missing values in the 'age' variable with the median of age.
#########################################

df["age"].fillna(df["age"].median(),inplace=True)
df.isnull().sum()

#########################################
# Task 15: Find the sum, count, and mean of the 'survived' variable based on 'pclass' and 'sex'.
#########################################

df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})

#########################################
# Task 16: Write a function that assigns 1 to those under the age of 30 and 0 to those aged 30 and above.
# Create a new variable named 'age_flag' in the Titanic dataset using the function (using apply and lambda structures).
#########################################

def age_30(age):
    if age<30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

#########################################
# Task 17: Define the Tips dataset from the Seaborn library.
#########################################

df = sns.load_dataset("tips")
df.head()
df.shape

#########################################
# Task 18: Find the sum, min, max, and mean of 'total_bill' based on the categories of 'time' (Dinner, Lunch).
#########################################

df.groupby("time").agg({"total_bill": ["sum","min","mean","max"]})

#########################################
# Task 19: Find the sum, min, max, and mean of 'total_bill' based on the categories of 'day' and 'time'.
#########################################

df.groupby(["day","time"]).agg({"total_bill": ["sum","min","mean","max"]})

#########################################
# Task 20: Find the sum, min, max, and mean of 'total_bill' and 'tip' for lunch time and female customers, grouped by 'day'.
#########################################

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"],
                                                                            "Lunch" : lambda x:  x.nunqiue()})

#########################################
# Task 21: What is the average total bill of orders where the size is less than 3 and the total bill is over 10?
#########################################

df.loc[(df["size"] < 3) & (df["total_bill"] >10 ) , "total_bill"].mean() # 17.184965034965035

#########################################
# Task 22: Create a new variable named 'total_bill_tip_sum'. It should represent the total of 'total_bill' and 'tip' for each customer.
#########################################

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

#########################################
# Task 23: Find the mean of 'total_bill' for male and female separately.
# Create a new variable named 'total_bill_flag'. Assign 0 to those below the average and 1 to those equal to or above the average.
# Note: For females, consider the average calculated for females, and for males, consider the average calculated for males.
# Start by writing a function that takes gender and total_bill as parameters. (Include if-else conditions)
#########################################

# Calculating the average total bill for females and males

f_avg = df[df["sex"]=="Female"]["total_bill"].mean() # 18.056896551724133
m_avg = df[df["sex"]=="Male"]["total_bill"].mean() # 20.744076433121016

def func(sex,total_bill):
    if sex=="Female":
        if total_bill < f_avg:
            return 0
        else:
            return 1
    else:
        if total_bill < m_avg:
            return 0
        else:
            return 1

df["total_bill_flag"] = df[["sex","total_bill"]].apply(lambda x: func(x["sex"],x["total_bill"]),axis=1)

#########################################
# Task 24: Observe the number of individuals above and below the average based on the total_bill_flag variable for each gender.
#########################################

df.groupby(["sex", "total_bill_flag"]).agg({"total_bill_flag": "count"})


#########################################
# Task 25: Sort based on the total_bill_tip_sum variable from highest to lowest and assign the top 30 individuals to a new dataframe.
#########################################

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape
