import pandas as pd

data = {
    "Name": ["Aditya", "Sham", "Dirham", "Gajni", "guula"],
    "Age": [10,23,43,22,21],
    "Salary": [10000, 23223, 23000, 2111, 3231,],
    "Performance_Score": [45, 242, 23,1,2]
}
dp = pd.DataFrame(data)
print(dp)

# dp.drop(columns = ["Salary"], inplace=True)

""" 
For multiples 
"""
dp.drop(columns = ["Salary", "Age","Name"], inplace=True)
print(dp)
