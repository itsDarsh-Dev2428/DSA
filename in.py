import pandas as pd

#to check the data type you can use "info()" function

data = { 
    "Name": ["Darsh",  "Harsh", "Aditya"],
    "Age": [15, 14, 16],
    "City":["Pune", "Mumbai","Nashik"]
}

df = pd.DataFrame(data)

print("Displaying the info of data set")
print(df.info())
