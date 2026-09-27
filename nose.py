from random import randint
print('hello, world :)')
for i in range(5):
  r = randint(1,10) - randint(1, 10)
  if not r == 0:
    r = r * -1
  print(r)
