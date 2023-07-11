import matplotlib.pyplot as plt

products = ["Product 1", "Product 2", "Product 3", "Product 4"]
sales = [320, 240, 450, 520]

plt.bar(products, sales, color = ['red', 'blue', 'green', 'orange'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.legend(['Sales'])
plt.show()

