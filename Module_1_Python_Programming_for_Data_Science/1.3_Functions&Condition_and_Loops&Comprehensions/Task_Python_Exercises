###############################################
# Python Exercises
###############################################

###############################################
# TASK 1: Examine the types of data structures.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)


l = [1, 2, 3, 4, "String", 3.2, False]
type(l)
# Ordered
# Iterable
# Mutable


d = {"Name": "Jake",
     "Age": [27, 56],
     "Address": "Downtown"}
type(d)
# Mutable
# Iterable
# Unordered
# Keys must be unique


t = ("Machine Learning", "Data Science")
type(t)
# Immutable
# Iterable
# Ordered


s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)
# Mutable
# Unordered + Unique
# Iterable



###############################################
# TASK 2: Convert all letters of the given string to uppercase. Replace commas and periods with spaces, then split the string into words.
###############################################

text = "The goal is to turn data into information, and information into insight."
text.upper().replace(",", " ").replace(".", " ").split()



###############################################
# TASK 3: Perform the following tasks for the given list.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Check the number of elements in the given list.
len(lst)

# Step 2: Call elements at index 0 and 10.
lst[0]
lst[10]

# Step 3: Create a new list from the given list with the elements ["D", "A", "T", "A"].
data_list = lst[0:4]
data_list

# Step 4: Delete the element at index 8.
lst.pop(8)
lst

# Step 5: Add a new element.
lst.append(101)
lst

# Step 6: Add the element "N" back to index 8.
lst.insert(8, "N")
lst


###############################################
# TASK 4: Apply the following steps to the given dictionary structure.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Step 1: Access the key values.
dict.keys()

# Step 2: Access the values.
dict.values()

# Step 3: Update the value of 12 for the key 'Daisy' to 13.
dict.update({"Daisy": ["England", 13]})
dict

dict["Daisy"][1] = 14
dict

# Step 4: Add a new value with the key 'Ahmet' and the value [Turkey, 24].
dict.update({"Ahmet": ["Turkey", 24]})
dict

# Step 5: Remove Antonio from the dictionary.
dict.pop("Antonio")
dict



###############################################
# TASK 5: Write a function that takes a list as an argument, separates the odd and even numbers in the list into different lists, and returns them.
###############################################

l = [2, 13, 18, 93, 22]

def func(lst):

    even_list = []
    odd_list = []

    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


even, odd = func(l)

# List comp. solution.



###############################################
# TASK 6: The list below contains the names of students who succeeded in the engineering and medical faculties.
# The first three students represent the success order of the engineering faculty, while the last three students represent the medical faculty.
# Using enumerate, print student rankings for each faculty.
###############################################

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
for i, x in enumerate(students):
    if i < 3:
        i += 1
        print("Engineering Faculty", i, "th student: ", x)
    else:
        i -= 2
        print("Medical Faculty", i, "th student: ", x)


###############################################
# TASK 7: Three lists are given below, representing the code, credit, and quota information of a course, respectively.
# Print the course information using zip.
###############################################

course_code = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credit = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

for course_code, credit, quota in zip(course_code, credit, quota):
    print(f"The course with code {course_code} has {credit} credits and a quota of {quota} students.")


###############################################
# TASK 8: Two sets are given below.
# If the first set contains the second set, print the common elements; if not, print the difference of the second set from the first set.
###############################################

set1 = set(["data", "python"])
set2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def set_function(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

set_function(set1, set2)
