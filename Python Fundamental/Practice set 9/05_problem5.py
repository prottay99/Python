import random

class Train:
  def __init__(self,trainNo):
    self.trainNo = trainNo
    
  def book(self,fro,to):
    print(f"Tain no {self.trainNo} is from {fro} to {to}")
  
  def getStatus(self):
    print(f"Train no {self.trainNo} is on time")
    
  def getFare(self,fro ,to):
    print(f"Tain no {self.trainNo} from {fro} to {to} fare is {random.randint(255,1950)}")


a = Train(12335)
a.book("Dhaka","Khulna")
a.getStatus()
a.getFare("Dhaka","Khulna")