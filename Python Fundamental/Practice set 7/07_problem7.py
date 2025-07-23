def check(l,w):
  for item in l:
    if w in item:
      l.remove(item)

l = ["jhon","marllo","marry","david"]

check(l,"harry")

print(l)