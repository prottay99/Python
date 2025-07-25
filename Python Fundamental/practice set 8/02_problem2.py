import random

def game():
  print("You are playing the game...")
  score = random.randint(1,60)
  #fetch the high score result
  with open("d:\Python\Python Fundamental\practice set 8\highscore.txt",'r') as f:
    hiscore = f.read()
    if(hiscore != ""):
      hiscore = int(hiscore)
    else:
      hiscore = 0

    print(f"Your score: {score}")
    if(score > hiscore):
      with open("d:\Python\Python Fundamental\practice set 8\highscore.txt",'w') as f:
        f.write(str(score))
    
    return score

game()