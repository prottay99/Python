number  = int(input("Enter a number: "))

for i in range(2,number):
  if(number % i) == 0:
    print("This is not a prime number")
    break
else:
  print("This is a prime number")
