import random

n = random.randint(1,100)
a = -1;
guess = 1

while (a != n):
  a = int(input("Enter a number between 1 to 100: "))
  if(a>n):
    print("Lower number please")
    guess += 1
  elif(a<n):
    print("Higher number please")
    guess += 1

print(f"You have guesses the number {n} correctly in {guess} attemps")