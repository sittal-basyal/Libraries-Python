import pandas as pd
my_df=pd.read_csv("sample_data.csv")
my_df["header"]=["Person1","Person2","Person3","Person4","Person5","Person6"]
my_df.set_index('header',inplace=True)
# print(my_df.reset_index(inplace=True))
print(my_df)