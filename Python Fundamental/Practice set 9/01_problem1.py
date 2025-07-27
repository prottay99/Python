class Programmer:
  company = "Microsoft"

  def __init__(self,name,salary,language):
    self.name = name
    self.salary = salary
    self.language = language
    

harry = Programmer("Harry",60000,"python")
print(harry.name,harry.language,harry.salary,harry.company)

akash = Programmer("akash",50000,"javascript")
print(akash.name,akash.language,akash.salary,akash.company)

marllo = Programmer("marllo",50000,"java")
print(marllo.name,marllo.language,marllo.salary,marllo.company)
