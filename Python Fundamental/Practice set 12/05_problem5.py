from functools import reduce

l = [11,8,35,75,69,152,95,13,512,177]

def max(a,b):
  if (a > b):
    return a
  return b


a = reduce(max,l)

print(f"Maximum number of list is {a}")