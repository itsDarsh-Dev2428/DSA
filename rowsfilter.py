import pandas as pd


data = {
    "Name": ["Aditya", "Sham", "Dirham", "Gajni", "guula"],
    "Age": [10,23,43,22,21],
    "Salary": [10000, 23223, 23000, 2111, 3231,],
    "Performance_Score": [45, 242, 23,1,2]

}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] >  22000]
print("Employees have salary greater than 5000: ")
print(high_salary)

filtered = df[(df['Age'] > 30) & (df["Salary"]> 22000)]
print("Employe having age above 21 and salary above 22000",filtered)

filtered_or = df[(df["Age"] < 10) | (df["Performance_Score"] > 62  )]
print("This employees have niche skills in their core area")
print(filtered_or)
