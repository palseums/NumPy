# np.where(logical test,value if true, value if false)

import numpy as np

inventory_array = [12,102,18,0,0]

inventory_np_array = np.array(inventory_array)

print(inventory_np_array)

product_array = ['fruits','vegetables','cereal','dairy','eggs']

product_np_array = np.array(product_array)

print(np.where(inventory_np_array <= 0, "out of stock","In stock"))

print(np.where(inventory_np_array <= 0, "out of stock",product_np_array))



