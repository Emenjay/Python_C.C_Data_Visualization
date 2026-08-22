import matplotlib.pyplot as plt

from random_walk_031 import RandomWalk

# make a random walk

rw = RandomWalk()
rw.fill_walk()

# plot points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_vals, rw.y_vals, s=10)
ax.set_aspect('equal')
plt.show()