words = ['donkey', 'goat', 'fox']


with open("d:/Python/Python Fundamental/practice set 8/passage1.txt", "r") as f:
  content = f.read()

for word in words:
  content = content.replace(word, "#" * len(word))

with open("d:/Python/Python Fundamental/practice set 8/passage1.txt", "w") as f:
  f.write(content)