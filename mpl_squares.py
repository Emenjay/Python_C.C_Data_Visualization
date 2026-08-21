# plotting a simple line graph

import matplotlib.pyplot as plt
# pyplot module - contains functions that help generate charts and plots

squares = [1, 4, 9, 16, 25]

# Subplots() function generates one or more plots in the same figure
# Variable fig represents the entire figure, which is the collection of plots that are generated
# Variable ax represents an Axes object, which is the whole plot area that contains the x-axis
# and y-axis together, plus your data
fig, ax = plt.subplots()

# plot() method plots the data given
# plotted data - the actual line/points/bars drawn on the chart
ax.plot(squares)

# opens matplotlib's viewer and displays the plot
plt.show()