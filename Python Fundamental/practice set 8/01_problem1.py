f = open("d:\Python\Python Fundamental\practice set 8\poems.txt",'r')

content = f.read()

if("twinkle" in content):
  print("The word twinkle is present on the poems file")
else:
  print("The word twinkle is not present on the poems file")

f.close()