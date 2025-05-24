import numpy as np
img= np.random.randint(0, 256, (500, 600), dtype=np.uint8)
h,w =img.shape
start_row=(h - 100) // 2
start_col =(w - 100) // 2
center_region= img[start_row:start_row + 100, start_col:start_col + 100]
print(center_region.shape)
