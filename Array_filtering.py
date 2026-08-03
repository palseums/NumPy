import numpy as np

sales = [[0,5,155,0,518],[0,1827,616,317,325]]

sales_np_array = np.array(sales)

print(sales_np_array)

print(sales_np_array != 0)

print(sales_np_array[sales_np_array != 0])   # returns array

print(sales_np_array[(sales_np_array == 616) | (sales_np_array < 100)]) # returns array


print(sales_np_array[(sales_np_array > 100) & (sales_np_array < 500)])

sales1_array = [0,5,155,0,518]

sales1_np_array = np.array(sales1_array)

product_array = ['fruits','vegetables','cereal','dairy','eggs']

product_np_array = np.array(product_array)

print(product_np_array[sales1_np_array > 0])

# modify array values

# sales_np_array[1] = 5
# sales_np_array[sales_np_array == 0] = 5


