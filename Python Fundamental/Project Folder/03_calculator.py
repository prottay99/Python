"""
calculator
step1 - take input form user
step2- understand what user done
step3 - performs user task
"""

def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mult(a,b):
  return a * b

def div(a,b):
  return a / b

# print statements for user what operation they choose
print("Select an operation: ")
print('"1" for addition')
print('"2" for subtraction')
print('"3" for multiplication')
print('"4" for division')

while True:
  try:
    choice = input("Enter any operation (1 / 2 / 3 / 4) : ")
    if choice in ("1", "2", "3", "4"):
      num1 = float(input("Enter num1: "))
      num2 = float(input("Enter num2: "))

      if choice == '1':
        print(add(num1,num2))
      elif choice == '2':
        print(sub(num1,num2))
      elif choice == '3':
        print(mult(num1,num2))
      elif choice == '4':
        print(div(num1,num2))

    else:
      print("Invalid Choise!!!")

  except:
    print(f"Something went wrong!!")