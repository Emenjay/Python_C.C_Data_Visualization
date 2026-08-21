# plotting a simple line graph

import matplotlib.pyplot as plt
# pyplot module - contains functions that help generate charts and plots

squares = [1, 4, 9, 16, 25]
# when given a single sequence of numbers, plot() assumes the first data point
# corresponds to an x-value of 0, which is wrong in this case, to correct:

input_values = [1, 2, 3, 4, 5]
# with this plot() has the input(x) and output(y) values used to calculate the squares

# use built-in style
plt.style.use('Solarize_Light2')

# Subplots() function generates one or more plots in the same figure
# Variable fig represents the entire figure, which is the collection of plots that are generated
# Variable ax represents an Axes object, which is the whole plot area that contains the x-axis
# and y-axis together, plus your data
fig, ax = plt.subplots()

# plot() method plots the data given
# plotted data - the actual line/points/bars drawn on the chart
ax.plot(input_values, squares, linewidth=3) # linewidth - line thickness

# set chart title and label axes
ax.set_title("Square numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# ax.set_yticks([1, 4, 9, 16, 25]) sets specfic tick marks, but is not evenly spaced which is bad practice and not scalable


# set size of tick_labels
# tick - the small markers along the axes of a plot that denote specific data points and help readers locate coordinates
ax.tick_params(labelsize=14)


# annotate relevant data points
for x, y in zip(input_values, squares): # zip pairs each x with its matching y, to loop through every point to stick a label on it
    ax.annotate(
        f'{y}',                        # the text to show
        (x, y),                        # the point to label

        # the labels will be put on top of the line itself, making it hard to read, to solve, offset the label

        textcoords="offset points",    # offset is in pickles, not data units
        xytext=(0, 10),                # move label 10 pixels up
        ha='center'                    # horizontal alignment: centered above point
    )

# opens matplotlib's viewer and displays the plot
plt.show()

# for built-in styles
# 'plt.style.available' in terminal(start python interpreter)

# or

# print(plt.style.available)