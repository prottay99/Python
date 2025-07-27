class Test:
  a = 5  # class attribute 

obj = Test()
print(obj.a)
obj.a = 0   # instance attribute which is preference above class attributes
print(obj.a)
print(Test.a)