from readchar import readkey, key

nombre = input('Hola! Cual es tu nombre?: ')
print('Que tal', nombre+'?','Bienvenido al juego.',sep=" " )

while True:
  k = readkey()
  print(k)
  if k == key.UP:
    break

