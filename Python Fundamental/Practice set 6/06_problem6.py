num = int(input("Enter a number to calculate factorial: "))
fact = 1

if (num < 0):
  print("Factorial does not support negative number.")
elif (num == 0):
  print("Factorial of 0 is 1.")
else:
  for i in range(1, num + 1):
    fact = fact * i;

print("Factorial is =",fact)


