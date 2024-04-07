class Sphere:
    def __init__(self, rad=None, x=None, y=None, z=None):
        if rad is None and x is None and y is None and z is None:
            self.rad = 1
            self.x = 0
            self.y = 0
            self.z = 0
            return
        elif rad is not None and x is None and y is None and z is None:
            self.rad = rad
            self.x = 0
            self.y = 0
            self.z = 0
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

    def addition(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multi(self, value1, value2):
        return value1 * value2

    def division(self, value1, value2):
        if value2 == 0:
            raise ZeroDivisionError("Деление на 0 недопустимо")
        return value1 / value2

math = Math()
print(math.multi(1,2))
print(math.division(5,1))
print(math.addition(3,10))
print(math.subtract(5,4))