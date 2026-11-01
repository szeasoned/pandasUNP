import pandas as pd
from pathlib import Path

path = Path.home() / "OneDrive" / "Documents" / "Data Sets"

df = pd.read_csv(path / "students.csv")

"""
print(df.head(5)) # display first 5 students
print(df.tail(5)) # display last 5 students

print(f"ROWS:", df.shape[0]) # display the number of rows
print(f"COLUMN:", df.shape[1]) # display the number of columns
print(df.dtypes) # check the data type of ALL columns
print(df["student_id"].dtype) #check the data type of column student_id

grade = df["grade"] # get only the grade column
lowest_grade = grade.min() # get lowest in grade column
highest_grade = grade.max() # get highest in grade column
average_grade = grade.mean() # get average in grade column 

df["scholarship"] = df["scholarship"].map({'Yes': 1, 'No': 0}) # count how many have scholarship
count_is_scholar = df["scholarship"]

student_per_city = (df["city"] == "Vigan").sum() # count how many student per city
count_course = df["course"].nunique() # count unique course/s
unique_course= df["course"].unique() # list unique course/s

standings = (df["grade"] >= 75) # check if grade is greater than or equals to 75
df.insert(11, "Standings", standings) # insert 'Standings' column at the end
passed = df["Standings"].map({True: "Passed", False: "Failed"}) # check if failed or passed

"""
