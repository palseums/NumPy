# numpy arrays are fixed size containers of items that are 
# efficient than python lists or tuples for data processing

# They only store a single data type ( mixed data types are stored as a string)
# They can be one dimensional or multi dimensional
# Array elements can be modified but the array size cannot change

import numpy as np

sales = [0,5,10,15,20]

sales_array = np.array(sales)
print(sales_array)