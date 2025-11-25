import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([1,3,4])

lists=[1,2,3]
print(lists)
print(arr1*arr2)

arr3=np.array([[1,2,3],
      [4,5,6],
      [7,8,9]
      ])

#get dimesnions
print(arr1.ndim)
print(arr3.ndim)

#row , column
print(arr3.shape)

#datatype
print(arr2.dtype)

#no of elements
print(arr3.size)
