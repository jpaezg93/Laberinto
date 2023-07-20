from readchar import readkey, key
import os

nombre = input('Hola! Cual es tu nombre?: ')
print('Que tal', nombre+'?','Bienvenido a nuestro laberinto!\nHaz tu mejor esfuerzo para salir!',sep=" " )

def clear_p(k,c1):
  if k == 'n' or c1>=50:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(c1)

c1=0
while True:
  k = readkey()
  c1+=1
  print(k)
  if k == key.ENTER:
    break
  if c1<50:
    clear_p(k,c1)
    continue
  elif c1>=50:
    clear_p(k, c1)
    c1=0
