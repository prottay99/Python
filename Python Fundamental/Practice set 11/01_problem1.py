try:  
  with open("d:/Python/Python Fundamental/Practice set 11/1.txt",'r') as f:
    print(f.read())

except Exception as e:
  print(e)

try:
  with open("d:/Python/Python Fundamental/Practice set 11/2.txt",'r') as f:
    print(f.read())

except Exception as e:
  print(e)

try:
  with open("d:/Python/Python Fundamental/Practice set 11/3.txt",'r') as f:
    print(f.read())

except Exception as e:
  print(e)


print("Done")