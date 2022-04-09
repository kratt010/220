import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return 4 / 3 * math.pi * self.radius * self.radius * self.radius
