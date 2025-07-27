class Circle:
    def __init__(self, radius):
        self._radius = radius  # private by convention

    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

# Usage
c = Circle(5)
print(c.area)     # 78.54 (acts like an attribute, not a method)
c.radius = 10     # Sets new radius
print(c.area)     # 314.16
