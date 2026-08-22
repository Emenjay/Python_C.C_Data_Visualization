import matplotlib.pyplot as plt

x_vals = (1, 2, 3, 4, 5)
y_vals = (1, 4, 9, 16, 25)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# scatter - allows you to plot individual points

# -- single point --
# ax.scatter(2, 4, s=200) # (2, 4) x, y of single point. s = size of dot

# -- series of points --
ax.scatter(x_vals, y_vals, s=100)

# set chart title and label axes
ax.set_title("Square numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()