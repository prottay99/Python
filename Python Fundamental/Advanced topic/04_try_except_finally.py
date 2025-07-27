def show():
  try:
    number = int(input("Enter a number: "))
    print("The number is:",number)
    return

  except:
    print("Error!!!")
    return

  finally:
    print("This is finally clause")


show()