try:
  number = int(input("Enter a number: "))
  print("The number is:",number)

except:
  print("This is a value error! Please enter a number.")

print("Done")


# try:
#   a = int(input("Enter a number: "))
#   b = int(input("Enter a number: "))
#   print("The division of a and b:", (a / b))

# except ZeroDivisionError:
#   print("the value of b does not 0")


# except TypeError:
#   print("the value of a and b is integer")

# except:
#   print("Error!!")