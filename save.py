import pandas as pd
import openpyxl as workbook

data = { 
    "Name": ["Darsh",  "Harsh", "Aditya"],
    "Age": [15, 14, 16],
    "City":["Pune", "Mumbai","Nashik"]
}

df = pd.DataFrame(data)
print(df)

df.to_excel("data.xlsx", index=False)



#if you don't want index, you can pass False statement in index for saving, use to_csv, FOR DATAframing use DataFrame

