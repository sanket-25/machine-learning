import numpy as np
import matplotlib.pyplot as plt
import random as r

x = []
y = []

for i in range(0, 100):
    a = r.randint(0, 10)
    b = r.randint(0, 10)

    c = a + b
    x.append([a, b])
    y.append(c)



for i in range(0, 100):
    print(x[i])
    print(y[i])


plt.scatter(x[0], x[1], y)

plt.show()