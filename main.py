from Objeto_laberinto import laberinto, juego
from readchar import readkey, key
import os
import random

def main():
    nombre = input('Hola! Cual es tu nombre?: ')
    while True:
        print('Que tal', nombre+'?','Bienvenido a nuestro laberinto!\nHaz tu mejor esfuerzo para salir!\nPresiona enter para empezar',sep=" " )
        saludo = readkey()
        if saludo == key.ENTER:
            break
        else:
            continue
    map_r = random.choice(os.listdir('maps/'))
    f = f"maps/{map_r}"
    lab = juego(f)
    nuevo = 1
    while True:
        if nuevo == 1:
            map_r = random.choice(os.listdir('maps/'))
            f = f"maps/{map_r}"
            lab = juego(f)
        else:
            pass
        lab.dibujar()
        tecla = readkey()
        ganador = lab.mover(tecla,nombre)
        if ganador:
            lab.dibujar()
            nuevo = 1
            continue
        else:
            nuevo = 0
        if tecla == key.ENTER:
            salir = input('Deseas salir del juego?[y/n]:')
            if salir == 'y':
                break
            else:
                continue
        
if __name__ == '__main__':
    main()
