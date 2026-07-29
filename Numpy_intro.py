# numpy arrays are fixed size containers of items that are 
# efficient than python lists or tuples for data processing

# They only store a single data type ( mixed data types are stored as a string)
# They can be one dimensional or multi dimensional
# Array elements can be modified but the array size cannot change

import numpy as np

sales = [0,5,10,15,20]

sales_array = np.array(sales)

# The sales input can be python array or tuples
print(type(sales_array))
print(sales_array)


# NumPy arrays have these key properties
# 1) ndim => The number of dimensions in the array
# 2) shape => The size of the array for each dimension
# 3) size => the total number of elements in the array
# 4) dtype => the data type of the elements in the array

print(sales_array.ndim)
print(sales_array.shape)
print(sales_array.size)
print(sales_array.dtype)