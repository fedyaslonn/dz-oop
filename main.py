import math

class Sphere:
    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4/3 * math.pi * (self.radius ** 3)

    def get_square(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2 < self.radius**2:
            return True
        return False

sphere = Sphere(3, 1, 1, 1)
print(sphere.get_volume())
print(sphere.get_radius())
print(sphere.get_center())
print(sphere.get_square())
sphere.set_radius(5)
print(sphere.get_radius())
print(sphere.is_point_inside(1, 1, 1))