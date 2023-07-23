from readchar import readkey, key
import os

nombre = input('Hola! Cual es tu nombre?: ')
print('Que tal', nombre+'?','Bienvenido a nuestro laberinto!\nHaz tu mejor esfuerzo para salir!',sep=" " )

#funcion para limpiar la pantalla
def clear_p(k,c1):
  if k == 'n' or c1>=50:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(c1)

#funcion para crear el laberinto
def lab(f):
  text = open(f)
  lb = list()
  for line in text:
    line = line.rstrip()
    lb.append(list(line))
  lb[-2].append('#')
  lb[-1].append('#')
  return lb

f='export-dcode-2023-07-23-20-31-21.txt'
lb=lab(f)
for i in lb:
  print(f'{i}')

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

