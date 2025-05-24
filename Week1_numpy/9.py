import numpy as np
a=np.array([])
for i in range(10000):
    a= np.append(a, i)
b=[]
for i in range(10000):
    b.append(i)
b=np.concatenate([np.array(b)])
print("Length using append:",len(a))
print("Length using concatenate:",len(b))
#both give same output