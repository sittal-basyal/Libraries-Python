import numpy as np
a=np.array([[1,2,45,77],
   [5,7,36,4],
   [11,58,69,71]
   ])
'''print(np.zeros((3,2)))

print(np.ones(5))

# np.full(dim,number)
print(np.full((2,2),99))
print(np.full(a.shape,5))
print("\n")

print(np.random.rand(4,2))'''

#5 samma ko random integer samma
# print(np.random.randint(2,5,size=(3,3)))

# print(np.random.random_sample(a.shape))

a=np.array([[1,2,45],
   [5,7,36],
   [11,58,69]
   ])
print(np.repeat(a,3,axis=1))
'''
yesle a ko harek row ma janxa , harek element hai 3 choti repeat garxa 
'''
print(np.repeat(a,3,axis=0))
'''
yesle a ko harek row lai 3 choti repeat garera dinxa 
'''
#axis
