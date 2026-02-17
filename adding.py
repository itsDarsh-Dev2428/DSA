import pandas as pd

data = {
    "Name": ["Aditya", "Sham", "Dirham", "Gajni", "guula"],
    "Age": [10,23,43,22,21],
    "Salary": [10000, 23223, 23000, 2111, 3231,],
    "Performance_Score": [45, 242, 23,1,2]
}
dp = pd.DataFrame(data)
# print(dp)

dp["Bonus"] = dp["Salary"] * 0.1                    
# print(dp

dp.insert(0, "Employee ID", [10,20,30,40,50])
# print(dp)
dp.insert(5, "Applicants", ("Darsh", "Aditya", "Harsh", "Devansh", "Aadi"))
print(dp)
