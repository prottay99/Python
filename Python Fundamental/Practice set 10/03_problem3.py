class Employee:
  salary = 234
  increment = 20

  @property
  def salaryAfterIncrement(self):
    return (self.salary + self.salary * (self.increment/100))
  
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self,salary):
    self.increment = ((salary / self.salary) - 1) * 100


e = Employee()
# print("Salary after increment",e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print("Increment rate",round(e.increment))