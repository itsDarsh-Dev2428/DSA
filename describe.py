#step sample data frame

import pandas as pd

data = {
    "Name": ["Aditya", "Sham", "Dirham", "Gajni", "guula"],
    "Age": [10,23,43,22,21],
    "Salary": [10000, 23223, 23000, 2111, 3231,],
    "Performance Score": [45, 242, 23,1,2]

}

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Descriptive Statstics")
print(df.describe())