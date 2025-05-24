import numpy as np
a=np.random.randint(0, 100, (5, 5))
b=np.concatenate([
    a[0],                
    a[1:-1, 0],          
    a[-1],               
    a[1:-1, -1]          
])
print("Original Array:\n", a)
print("\nBorder Elements:\n", b)
