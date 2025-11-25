import numpy as np
import pandas as pd
stuff={
    'Corporation':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
    'Person':['Sam ','Charlie ','Amy ','Vanessa ','Carl ','Sarah '],
    'Sales':[200,120,340,124,243,350]
}

mydata=pd.DataFrame(stuff)

print(mydata)
print(mydata.groupby('Corporation').sum())

