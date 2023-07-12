import matplotlib.pyplot as plt
import random

random.seed(42)
x = [random.random() for _ in range(50)]
y = [random.random() for _ in range(50)]
colors = [random.random() for _ in range(50)]
sizes = [random.random() for _ in range(50)]
plt.scatter(x, y, c = colors, s = sizes, marker = "o")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.grid(True)
plt.show()
