def sum(a,b):
  if(b == 0):
    raise ZeroDivisionError("Cannot divided by zero")
  return a / b

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

result = sum(a,b)
print(result)


print("Done")