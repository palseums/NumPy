import numpy as np

#ones(rows,col)

np_one = np.ones((4,2),dtype=int)
print(np_one)

#zeros(rows,col)

np_zeros = np.zeros((4,3),dtype=int)
print(np_zeros)

np_arange = np.arange(10)
print(np_arange)

np_linspace = np.linspace(0,100,7)
print(np_linspace)
print(np_linspace.shape)

#arange(start,stop)
# reshape( rows,column)
np_reshape = np.arange(1,31)
print(np_reshape)
print(np_reshape.shape)
print(np_reshape.reshape(6,5))


