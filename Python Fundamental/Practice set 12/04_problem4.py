
def divisibleByFive(n):
  if(n%5 == 0):
    return True
  return False

l = [7, 15, 35, 96, 655, 795, 826]

f = list(filter(divisibleByFive,l))

print(f)