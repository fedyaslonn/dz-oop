class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        return "tu-tu-doo-doo" if self.elephant >= self.bee else "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant -= value
            self.bee += value
        elif meal == "grass":
            self.bee -= value
            self.elephant += value
        if self.elephant < 0:
            self.elephant = 0
        if self.elephant > 100:
            self.elephant = 100
        if self.bee < 0:
            self.bee = 0
        if self.bee > 100:
            self.bee = 100

    def __str__(self):
        return f"Пчела {self.bee}, Слон {self.elephant}"

beeel = BeeElephant(50,50)
print(beeel.fly())
print(beeel.trumpet())
beeel.eat("grass", 200)
print(beeel)