import numpy as np
import random
import matplotlib.pyplot as plt
x = int(input('input size: '))
C_N = range(x)
matrix = np.zeros((x, x))
ch = random.randint(0, 1)
for i in range(x):
    for j in range(x):
        if (i + j) % 2 != ch:
            matrix [i][j] = 1
mas = matrix.copy()
plt.clf()
plt.imshow(matrix)
plt.draw()
plt.show()
plt.gcf().canvas.flush_events()
print(plt.ioff())