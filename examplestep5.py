import pandas as pd


data = {
    "Name": ["Aditya", "Sham", "Dirham", "Gajni", "guula"],
    "Age": [10,23,43,22,21],
    "Salary": [10000, 23223, 23000, 2111, 3231,],
    "Performance Score": [45, 242, 23,1,2]

}

df = pd.DataFrame(data)

print("Sample DataFrame")
print(df)
name = df["Name"]
print(name)

subset = df[['Name',"Age"]]
print("\nsubest with name and salary")
print(subset)