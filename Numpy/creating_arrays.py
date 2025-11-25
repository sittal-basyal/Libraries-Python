import numpy as np

#o print version
print(np.__version__)

array1=np.array([1,2,3,4,5])
#to print type
print(type(array1))
#to print array
print(array1)

a=np.array(1)
b=np.array([1,2])
c=np.array([[1,2],[3,4]])
#to ind the dimension
print(a.ndim,b.ndim,c.ndim,sep="\n")


d=np.array([1,2,7,8,9],ndmin=5)
print(d)
print(d.ndim)

#Remember there is ndmin:to set the dimension and ndim: to get the dimension

a1_zeros = np.zeros((3, 3))
a2_ones = np.ones((2, 4))
a3_range = np.arange(0, 10, 2)

print(a1_zeros)
print(a2_ones)
print(a3_range)