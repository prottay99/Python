
# def printPattern(n):
#   for i in range(0, n):
#     print("*" * (n-i),end="")
#     print(" " * i,end="")
#     print("")

# n = int(input("Enter n: "))

# printPattern(n)


def pattern(x):
  if x == 0:
    return
  print("*" * x)
  pattern(x-1)

pattern(3)