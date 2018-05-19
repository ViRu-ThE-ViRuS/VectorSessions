import numpy as np

doo = np.array([], dtype=int)
for i in np.arange(1, 11):
	foo = np.array([np.arange(i, 11 * i, i)])
	doo = np.append(doo, foo)
doo = doo.reshape(10, 10)
print(doo)
