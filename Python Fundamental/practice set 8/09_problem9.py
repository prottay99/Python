with open("d:/Python/Python Fundamental/practice set 8/this.txt", "r") as f:
  content1 = f.read()

with open("d:/Python/Python Fundamental/practice set 8/this_copy.txt", "r") as f:
  content2 = f.read()

if(content1 == content2):
  print("Yes, this is identical and matches the content of another file.")

else:
  print("No, this is not identical and matches the content of another file.")
  