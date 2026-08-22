import matplotlib.pyplot as plt

x_vals = range(1, 1001)
y_vals = [x**2 for x in x_vals]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# scatter - allows you to plot individual points

# -- single point --
# ax.scatter(2, 4, s=200) # (2, 4) x, y of single point. s = size of dot

# -- series of points --
ax.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, s=10)
# pass 'color' argument for color

# colormap - sequence of color in gradient, used to emphasize patterns in data
# example: c=y_vals, cmap=plt.cm.Blues (put as argument to scatter)

# set chart title and label axes
ax.set_title("Square numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)

# set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain') # keep plain notation and not use scientific notation

plt.show()

# to save the plot to a file, use this instead of show()
# plt.savefig()
# 1st arg is name, 2nd arg trims extra whitespace from the plot(omit for extra whitespace

# summary: this section includes intro to scatter, calculating data automatically,
# with mostly similar customizations to plot().