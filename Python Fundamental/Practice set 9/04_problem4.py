
class Calculator:
  def __init__(self,n):
    self.n = n

  def square(self):
    print(f"Square of {self.n} is {self.n ** 2}")

  def cube(self):
    print(f"Cube of {self.n} is {self.n ** 3}")

  def squareRoot(self):
    print(f"Square root of {self.n} is {self.n ** 1/2}")
  
  @staticmethod                       # decorator
  def greet():
    print("Hello there!")


a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareRoot()