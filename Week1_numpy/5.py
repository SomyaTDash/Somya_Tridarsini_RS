import numpy as np
arr = np.array([[1, 2],
                [3, 4],
                [1, 2]])
unique_rows = np.unique(arr, axis=0)
print(unique_rows)
