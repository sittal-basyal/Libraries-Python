import pandas as pd
my_data=pd.read_csv("sample_data.csv")
# print(my_data)
'''print(my_data['product'].count())
print(my_data['product'].value_counts())
print(my_data['product'].value_counts(normalize=True))
print(my_data['product'].value_counts()['Smartphone'])
print(my_data.groupby("city").size())
print(my_data.groupby("city").count())'''
# print(my_data.apply(pd.value_counts))

my_df=pd.read_csv("")
gender=["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"]
my_data["gender"]=gender
print(my_data)  