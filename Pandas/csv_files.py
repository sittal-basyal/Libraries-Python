import pandas as pd
my_df2=pd.read_csv("sample_data.csv")
# print(my_df2)

#pulling rows
# print(my_df2.loc[0])
# print(my_df2.loc[[0,5]])
# print(my_df2.loc[0:5])

#->my_df2.head() gives first 5 rows
'''print(my_df2.head())
print(my_df2.head(3))'''

# print(my_df2.tail())
# print(my_df2.tail(1))

#get_info


# print(my_df2.info())
# print(my_df2.ndim)
# print(my_df2.shape)
# print(my_df2.dtypes)
# print(my_df2.describe())
# print(my_df2['price'].describe())
# print(my_df2['city'].describe())
# print(my_df2['price'])
print(my_df2.price)


