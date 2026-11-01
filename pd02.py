import pandas as pd

url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"

titanic = pd.read_csv(url)

survivor = titanic[titanic["Survived"] == True]
pClass_Survivor = titanic[(titanic["Pclass"] == 1) & (titanic["Survived"] == True)]
print(pClass_Survivor.head(10))