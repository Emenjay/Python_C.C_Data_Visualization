import matplotlib.pyplot as plt

# determine x and y values
x_vals = range(1, 5001)
y_vals = [x**3 for x in x_vals]

fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Cube numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=14)

# ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')


plt.show()


# plot data
