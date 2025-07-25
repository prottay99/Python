with open("d:/Python/Python Fundamental/practice set 8/log.txt", "r") as f:
  content = f.read()

if "python" in content:
  print("Python word is found")

else:
  print("Python word is not found")