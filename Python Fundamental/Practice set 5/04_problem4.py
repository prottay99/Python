userName = input("Enter username: ")

if(len(userName) < 10 and len(userName) != 0):
  print("username less than 10")

elif(len(userName) == 0):
  print('username not be null')

else:
  print("username not less than 10")