import pandas as pd
my_series=[5,7,8,9,10]
my_var=pd.Series(my_series)
print(my_var)
my_index=['a','b','c','d','e']
my_var2=pd.Series(my_series,index=my_index)
print(my_var2)

#key_balue pairs
data={'a':5,'b':7,'c':8,'d':9,'e':10}
my_var3=pd.Series(data)
print(my_var3)


print(my_var3['c'])
# print(my_var3[2])


print(my_var3.index)
print(my_var3.values)
print(my_var3.dtype)
print(my_var3.shape)



