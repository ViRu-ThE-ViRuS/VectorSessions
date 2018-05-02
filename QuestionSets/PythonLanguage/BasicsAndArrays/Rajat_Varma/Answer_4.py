import numpy as np
x = np.array([], dtype = int)
for i in range(1, 11):
    for j in range(1, 11): 
        x = np.append(x, i*j)

x = x.reshape(10,10)
print(x)
