num = int(input("Enter a number: "))

table = [num * i for i in range(1,11)]

with open("d:/Python/Python Fundamental/Practice set 11/table.txt",'a') as f:
  f.write(f"Table of {num}: {str(table)}\n")
