def calculateSum(n):
  if n == 1:
    return 1
  return n + calculateSum(n - 1)
    

n = int(input("Enter a integer number: "))

totalSum = calculateSum(n)

print(f"The sum of {n} natural number is {totalSum}")