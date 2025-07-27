# class Calculator:
#   def square(n):
#     print(f"Square of {n} is {n ** 2}")


# a = Calculator.square(4)

class Calculator:
  def __init__(self,n):
    self.n = n

  def square(self):
    print(f"Square of {self.n} is {self.n ** 2}")

  def cube(self):
    print(f"Cube of {self.n} is {self.n ** 3}")

  def squareRoot(self):
    print(f"Square root of {self.n} is {self.n ** 1/2}")


a = Calculator(4)
a.square()
a.cube()
a.squareRoot()

b = Calculator(8)
b.square()
b.cube()
b.squareRoot()

c = Calculator(9)
c.square()
c.cube()
c.squareRoot()