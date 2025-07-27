class TwoDVector:
  def __init__(self,i,j):
    self.i = i
    self.j = j
  
  def show(self):
    print(f"2D vector: {self.i}i + {self.j}j")
  
class ThreeDVector(TwoDVector):
  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k = k

  def show(self):
    print(f"3D vector: {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(4,2)
a.show()
b = ThreeDVector(5,3,7)
b.show()