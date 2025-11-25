import pandas as pd
my_df=pd.read_csv("dog_data.csv")
# print(my_df=='Brown')
print(my_df[my_df=='BROWN'][['Color','Breed']])
print(my_df[(my_df['Color']=='BROWN') & (my_df['Breed']=='COCKAPOO')])