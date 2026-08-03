import numpy as np
product = ['fruits','vegetables','cereal','dairy','eggs','snacks','beverages','coffee','tea','spices']

# array[index]
# array [start:stop:step size]

product_np_array = np.array(product)

print(product_np_array)
print(type(product_np_array))
print(product_np_array.dtype)
print(product_np_array.shape)

print(product_np_array[1])
print(product_np_array[-1])

print(product_np_array[:5])

print(product_np_array[5::2])
