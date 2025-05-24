import numpy as np
img = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)
img[..., [0, 2]] = img[..., [2, 0]]
print(img)
