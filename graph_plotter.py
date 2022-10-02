from matplotlib import pyplot as plt

x = [1, 2, 3, 5]
y = [2, 3, 4, 6]

plt.plot(x, y, color='green', linestyle='dashed')
plt.xlabel("x axis")
plt.ylabel('y axis')
plt.title("This is demo graph")
plt.show()