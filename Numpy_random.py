import numpy as np
rng = np.random.default_rng(616)
print(rng.random(10))

print(rng.integers(0,10,100))

print(rng.normal(50,5,10))