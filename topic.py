"""
1- How big is your dataset
2- what are the names of columns

shape and columns
"""

import pandas as pd

data = {
    "Name": ["Aditya", "Sham", "Dirham", "Gajni", "guula"],
    "Age": [10,23,43,22,21],
    "Salary": [10000, 23223, 23000, 2111, 3231,],
    "Performance Score": [45, 242, 23,1,2]

}

df = pd.DataFrame(data)
print(df)
print(f"Shape:{df.shape}")
print(f"Column : {df.columns}")

