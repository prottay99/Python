class Prarent:
  a = 1

class Childofparent(Prarent):
  b = 2

class Childofchild(Childofparent):
  c = 3

o = Childofchild()
print(o.a)
print(o.b)
print(o.c)
o1 = Childofparent()
print(o1.b)
print(o1.a)


