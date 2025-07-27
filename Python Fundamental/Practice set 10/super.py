class Parent:
  def __init__(self):
    print("This is Based class constructor")
  
  def greet(self):
    print("Hello everyone")

class Child(Parent):
  def __init__(self):
    super().__init__()
    print("This is derived class constructor")
  def show(self):
    super().greet()
    print("This is child class")
  
c = Child()
c.show()
