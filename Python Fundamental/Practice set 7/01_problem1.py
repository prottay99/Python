def greatestNumber(a,b,c):
  if(a>b and a>c):
    print("A is greatest")
  elif(a<b and b>c):
    print("B is greatest")
  else:
    print("C is greatest")


greatestNumber(7,9,5)     # B is greatest
greatestNumber(11,9,7)    # A is greatest
greatestNumber(10,7,15)   # C is greatest
