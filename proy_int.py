from readchar import readkey, key
import os

nombre = input('Hola! Cual es tu nombre?: ')
print('Que tal', nombre+'?','Bienvenido a nuestro laberinto!\nHaz tu mejor esfuerzo para salir!',sep=" " )

'''
Esta funcion permite leer un archivo de texto(.txt) que contiene un laberinto donde
las paredes estan representadas con el caracter '#' y los corredores por donde puede
pasar el jugador estan representados por el caracter '.'
Ademas agregamos dos caracteres '#'para completar las paredes del laberinto.
Transformamos el archivo de texto en una matriz que permita la navegacion en coordenadas x,y
'''
def lab(f):
  text = open(f)
  lb = list()
  for line in text:
    line = line.rstrip()
    lb.append(list(line))
  lb[-2].append('#')
  lb[-1].append('#')
  return lb

#funcion para limpiar la pantalla e imprimir el laberinto
def vis_lab(laberinto):
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in laberinto:
    print(" ".join(i))

def move(lb, px, py, k, p_a):
  '''
  En esta seccion creamos la dinamica para que el jugador se mueva en el laberinto
  Dependiendo de la tecla que presione el jugador se actualiza la posicion de 'P' en coordenadas x,y
  tambien se guarda las coordenadas de la posicion anterior en p_a
  Args:
    lb: Matrix del laberinto.
    px: Coordenada actual en x.
    py: Coordenada actual en y.
    k: Entrada del teclado.
    p_a: posicion anterior del jugador.
  '''
  if not (0 <= py <= len(lb[0]) and 0 <= px <= len(lb)):
    return p_a[0], p_a[1]
  if k == key.RIGHT:
    py+=1
    p_a[1]=py-1
    p_a[0]=px
  elif k == key.DOWN:
    px+=1
    p_a[1]=py
    p_a[0]=px-1
  elif k == key.LEFT:
    py-=1
    p_a[1]=py+1
    p_a[0]=px
  elif k == key.UP:
    px-=1
    p_a[1]=py
    p_a[0]=px+1
  return px,py

#abrimos el laberinto que guardamos en un archivo txt
f = 'export-dcode-2023-07-23-20-31-21.txt'
lb = lab(f)
#variables que permiten actualizar las posiciones recientes del jugador en el juego
px = 0
py = 0
#guardamos la posicion anterior
p_a = [0,0]
while True:
  #Aca imprimimos el mapa del laberinto  en la posicion inicial donde se encuentra el jugador
  lb[px][py] = 'P'
  vis_lab(lb)
  k = readkey()
  px, py = move(lb,px,py,k,p_a)
  #Actualizamos la posicion anterior con el valor '.' para no dejar un camino de 'P'
  lb[p_a[0]][p_a[1]]='.'
  #agregamos restriccion para las paredes del laberinto. La posicion del jugador no cambia si el jugador se intenta mover hacia donde hay una pared ('#)
  if px==(len(lb)-1) and py==(len(lb[0])-2):
    lb[px][py] = 'P'
    vis_lab(lb)
    print('Lograste resolver el laberinto\nFELICITACIONES!!!')
    break
  if lb[px][py] == '#':
    px, py = p_a
  #esta seccion la utilizamos para salir del juego en caso de que el jugador presione la tecla enter
  if k == key.ENTER:
    salir = input('Deseas salir del juego?[y/n]:')
    if salir=='y':
      break
    else:
      continue


