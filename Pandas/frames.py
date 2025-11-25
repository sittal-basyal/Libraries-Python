import pandas as pd
import numpy as np
from numpy.random import randn

my_data=randn(4,3)
print(my_data)
my_rows=["A","B","C","D"]
my_cols=["Monday","Tuesday","Wednesday"]

my_data=pd.DataFrame(my_data,my_rows,my_cols)
print(my_data)

