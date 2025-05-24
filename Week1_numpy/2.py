import numpy as np
cb= np.indices((8, 8)).sum(axis=0) % 2
print(cb)
