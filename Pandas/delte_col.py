import pandas as pd
my_df=pd.read_csv("sample_data.csv")

# print(my_df.drop('rating',axis=1,inplace=False))
# print(my_df)

#if inplace=True pemanent delete hunxa
#if inplace=False pemanent delete hudaina
#axis=1 means column
#axis=0 means row   
#inplace=False means original data change hudaina
#inplace=True means original data change hunxa  
#drop means delete

# print(my_df.drop(2,axis=0))
print(my_df.loc[[2,5],'product'])
