#head() tail()
#head() 5
#tail(n) 5
import pandas as pd

df = pd.read_csv("sales_data_sample.csv")
print("Display first 4 rows of data:")
print(df.head(4))
print("Display last 4 rows of data:")
print(df.tail(4))



