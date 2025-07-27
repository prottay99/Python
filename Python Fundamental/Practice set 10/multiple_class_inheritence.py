class Employee:
  def greet(self):
    print("Hello")

class Programer:
  def pr(self):
    print("programer")

class Manager(Employee,Programer):  
  def message(self):
    print('This is a message')

o = Manager()
o.greet()
o.pr()
o.message()