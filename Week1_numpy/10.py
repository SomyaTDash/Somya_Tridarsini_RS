import numpy as np
arr= np.array([1, 2, 3])
new= [4, 5, 6]
for i in new:
    if i % 2 == 0:
        arr=np.append(arr, i)
print(arr)
