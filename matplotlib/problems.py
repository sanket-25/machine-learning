import matplotlib.pyplot as plt
import random as r

age = []

for i in range(0, 100):
    age.append(r.randint(0, 100))

print(age)

plt.hist(age)

plt.show()