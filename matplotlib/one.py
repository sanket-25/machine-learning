import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y, color="green", label="Revenue")

plt.title("Scatter Plot Example")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid(True)

plt.show()