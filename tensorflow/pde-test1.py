import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

N = 500
u_init = np.zeros([N,N], dtype=np.float32)

for n in range(40):
    a, b = np.random.randint(0, N, 2)
    u_init[a, b] = np.random.uniform()

#plt.imshow(u_init.eval())
#plt.show()
