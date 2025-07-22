mark1 = int(input("Enter first subject mark: "))
mark2 = int(input("Enter second subject mark: "))
mark3 = int(input("Enter third subject mark: "))


total_mark_percentage = (mark1 + mark2 + mark3) / 3

if(total_mark_percentage >= 40 and mark1>=33 and mark2>=33 and mark3>=33):
  print('pass')

else:
  print("fail")