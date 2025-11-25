import numpy as np
import pandas as pd

stuff={"A":[1,2,56,4,5],"B":[np.nan,7,np.nan,np.nan,np.nan]}
mydata=pd.DataFrame(stuff)
# print(mydata)

# mydata.dropna(inplace=True)
# print(mydata)

# print(mydata.dropna(thresh=2,axis=1))
# print(mydata)

mydata.fillna(value=int(99),inplace=True)
print(mydata)