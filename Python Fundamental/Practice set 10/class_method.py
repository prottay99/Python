class Employee:
  company = "Meta"

  @classmethod
  def change_company(cls,new_name):
    cls.company = new_name

print(Employee.company)  # meta

Employee.change_company("Microsoft")

print(Employee.company)   # Microsoft

o = Employee()
print(o.company)