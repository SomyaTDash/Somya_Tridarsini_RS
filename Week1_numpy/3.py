import numpy as np
m=np.zeros((5, 5), dtype=int)
np.fill_diagonal(m, np.arange(1, 6))
print(m)
