import numpy as np
product = ['fruits','vegetables','cereal','dairy','eggs','snacks','beverages','coffee','tea','spices']

# array[row index,column index]
# array [start:stop:step size,start:stop:step size]

product_np_array = np.array(product)
product_np_2d_array = product_np_array.reshape(2,5)

print(product_np_2d_array)

print(product_np_2d_array.shape)

print(product_np_2d_array[1,2])

# All rows, column from 2 to end
print(product_np_2d_array[:,2:])


# First row to end, All column
print(product_np_2d_array[1:,:])