#############################################
# Rule-Based Classification for Estimating Potential Customer Revenue
#############################################

#############################################
# Business Problem
#############################################
# A gaming company wants to create level-based (persona) new customer definitions using some characteristics of their customers and then wants to estimate how much average revenue potential customers could bring to the company based on these new customer definitions.

# For example: Determining how much a 25-year-old male user from Turkey who uses IOS can potentially bring in.

#############################################
# Data Set Story
#############################################
# The Persona.csv dataset contains prices of products sold by an international gaming company and some demographic information of the users who purchased these products. The dataset consists of records generated for each purchase transaction. This means the table is not singularized. In other words, a user with certain demographic characteristics may have made multiple purchases.

# Price: Amount spent by the customer
# Source: Type of device the customer connected with
# Sex: Gender of the customer
# Country: Country of the customer
# Age: Age of the customer

################# Before Application #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# After Application #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJECT TASKS
#############################################

#############################################
# TASK 1: Answer the following questions.
#############################################

# Question 1: Read the persona.csv file and show general information about the dataset.
import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv('Module_1_Data_Science_for_Python_Programming/Part_2_Data_Science_for_Python_Programming/Rule_Based_Classification/persona.csv')
df.head()
df.shape
df.info()

# Question 2: How many unique SOURCES are there? What are their frequencies?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Question 3: How many unique PRICES are there?
df["PRICE"].nunique()

# Question 4: How many sales were made for each PRICE?
df["PRICE"].value_counts()

# Question 5: How many sales were made from each country?
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()

df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count")


# Question 6: How much total revenue was earned from sales in each country?
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="sum")

# Question 7: What are the sales counts for each SOURCE type?
df["SOURCE"].value_counts()

# Question 8: What are the average PRICES for each country?
df.groupby(by=['COUNTRY']).agg({"PRICE": "mean"})

# Question 9: What are the average PRICES for each SOURCE?
df.groupby(by=['SOURCE']).agg({"PRICE": "mean"})

# Question 10: What are the average PRICES for each COUNTRY-SOURCE combination?
df.groupby(by=["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})



#############################################
# TASK 2: What are the average earnings for COUNTRY, SOURCE, SEX, and AGE breakdowns?
#############################################
df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).head()


#############################################
# TASK 3: Sort the output by PRICE.
#############################################
# Apply sort_values method to the output of the previous question on PRICE in descending order to better visualize the output.
# Save the output as agg_df.
agg_df = df.groupby(by=["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()


#############################################
# TASK 4: Convert the index names to variable names.
#############################################
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names.
# Hint: reset_index()
# Save the output as agg_df.
agg_df = agg_df.reset_index()
agg_df.head()


#############################################
# TASK 5: Convert the AGE variable to a categorical variable and add it to agg_df.
#############################################
# Convert the numerical variable AGE to a categorical variable.
# Create intervals in a way that you find convincing.
# For example: '0_18', '19_23', '24_30', '31_40', '41_70'

# Specify where AGE will be divided:
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

# Specify what the naming of the divided points will be:
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

# Divide age:
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()


#############################################
# TASK 6: Define new level-based customers and add them as variables to the dataset.
#############################################
# Define a variable named customers_level_based and add this variable to the dataset.
# Attention!
# After creating the values of customers_level_based with list comp, these values need to be singularized.
# For example, there may be multiple of "USA_ANDROID_MALE_0_18" segment.
# These should be grouped by and the price averages should be taken.


# METHOD 2
agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)


# METHOD 3
agg_df["customers_level_based"] = ['_'.join(i).upper() for i in agg_df.drop(["AGE", "PRICE"], axis=1).values]


# METHOD 1
# Variable names:
agg_df.columns

# How to access observation values?
for row in agg_df.values:
    print(row)

# We want to put the VALUES of COUNTRY, SOURCE, SEX, and age_cat variables SIDE BY SIDE and join them with an underscore.
# We can do this with list comprehension.
# Perform the operation by selecting the observation values needed in the above loop:
[row[0].upper() + "_" + row[1].upper() + "_" + row
