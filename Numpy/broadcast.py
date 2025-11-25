#To broad cast eaither must be of same dim or one should be of dim 1
import numpy as np
array1=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,2,3,4],
                 [5,6,7,8]])
array2=np.array([[1],
                 [2],
                 [3],
                 [4]])
print(array1.shape)
print(array2.shape)

print(array1*array2)