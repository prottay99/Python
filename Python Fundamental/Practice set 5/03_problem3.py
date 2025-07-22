p1  = "make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"

comment = input("Enter your comment: ")

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
  print("This is a spam message.")

else:
  print("This is not a spam message.")