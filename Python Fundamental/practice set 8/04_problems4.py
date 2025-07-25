word = 'donkey'

with open("d:/Python/Python Fundamental/practice set 8/passage.txt", "r") as f:
  content = f.read()

newContent = content.replace(word,"######")

with open("d:/Python/Python Fundamental/practice set 8/passage.txt", "w") as f:
  f.write(newContent)
