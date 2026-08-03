import numpy as np

sales = [[0,5,155,0,518],[0,1827,616,317,325]]

sales_np_array = np.array(sales)

print(sales_np_array)

sales_np_array + 2

quantity = sales_np_array[0,:]

print(quantity)

price = sales_np_array[1,:]

print(price)

print(quantity * price)