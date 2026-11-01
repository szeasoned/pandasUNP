import pandas as pd

df = pd.DataFrame({
    "Name": [
        "Alexander",
        "Sophia",
        "Benjamin",
        "Isabella",
        "Daniel"
    ],

    "Course": [
        "BSCS",
        "BSIT",
        "BSCS",
        "BSIT",
        "BSCS"
    ]
})

age = pd.Series([19, 20, 18, 21, 19], name="Age")
city = pd.Series(["Vigan", "Laoag", "Bantay", "Caoyan", "Santa"], name="City")
gpa = pd.Series([1.25, 1.50, 1.75, 1.25, 2.00], name="GPA")


df.insert(1, "Age", age)
df.insert(3, "City", city)
df.insert(4, "GPA", gpa)


print(df)