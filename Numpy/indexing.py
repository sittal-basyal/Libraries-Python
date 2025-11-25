import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]])

# print the element 6
print(arr[0][1][2])  #This is known as chain indexing

print(arr[0,1,2])   #This is called multidimensional indexing which is faster than chain indexing 

print(arr.ndim)

arr = np.array([-1,10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# Integer array indexing
indices = np.array([1, 3, 5])
print ("Integer array indexing:", arr[indices])




array2=np.array([[['A','B','C'],['D','E','F']],
                 [['G','H','I'],['J','K','L']]])
print(array2.ndim)
word=array2[0,0,0]+array2[0,1,0]*2
print(word)

#negative indexing

print(arr[-1,-2,-3])
'''
[[7, 8, 9], [10, 11, 12]]
[7, 8, 9]
7
'''
