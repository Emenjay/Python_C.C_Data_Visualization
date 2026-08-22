from random import choice

# randomizations have practical applications in nature, physics, biology, chemistry, economics, etc
# it can represent real-world objects/phenomena, like molecular motion

# will create decisions on where the walk will go
class RandomWalk:

    def __init__(self, num_points=5000):
        "init attributes of a walk"
        self.num_points = num_points

        # walk starts at 0, 0
        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        "calculate all points in a walk"

        # walk till it reaches desired length
        while len(self.x_vals) < self.num_points:
            # decide which direction to go, and how far to go
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

        # calculate new position
        x = self.x_vals[-1] + x_step
        y = self.y_vals[-1] + y_step

        # calculate new position
        self.x_vals.append(x)
        self.y_vals.append(y)

