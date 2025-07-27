class Employee:
  def greet(self):
    print("Hello")
  def show(self):
    print("This is base class")

class Programer(Employee):
  def greet(self):
    print("Good Day")
  def pr(self):
    print("This is derived class")

e = Employee()
# e.show()
# e.pr()    # this is base class
e.greet()

p = Programer()
p.pr()
p.show()    # this is derived class that's why we can use methods and attributes of base classs
p.greet()