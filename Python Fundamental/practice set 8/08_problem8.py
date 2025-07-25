with open("d:/Python/Python Fundamental/practice set 8/this.txt", "r") as f:
  content = f.read()

with open("d:/Python/Python Fundamental/practice set 8/this_copy.txt", "w") as f:
  f.write(content)