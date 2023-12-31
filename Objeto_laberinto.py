from readchar import readkey, key
import os

class laberinto:
    def __init__(self, archivo):
        self.archivo = archivo
        with open(self.archivo) as f:
            texto = f.readlines()
            test = [linea.rstrip() for linea in texto]
            self.lb = list(map(list,test[1:]))
        self.lb[-2][-1]='#'
        self.lb[-1][-1]='#'
        self.lb[0][0]='#'
        self.lb[1][0]='#'
        self.lb[-1][-2]= "\U0001F34C"
        self.px = 0
        self.py = 1
        self.p_a = [0,1]
    def dibujar(self):
        self.lb[self.px][self.py] = "\U0001F412"
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in self.lb:
            print(" ".join(i))

class juego (laberinto):
    def mover(self,tecla,nombre):
        self.lb[self.px][self.py] = "\U0001F412"
        self.tecla = tecla
        if not (0 <= self.py <= len(self.lb[0]) and 0 <= self.px <= len(self.lb)):
            return self.p_a[0], self.p_a[1]
        if self.tecla == key.RIGHT:
            self.py += 1
            self.p_a[1] = self.py-1
            self.p_a[0] = self.px
        elif self.tecla == key.DOWN:
            self.px += 1
            self.p_a[1] = self.py
            self.p_a[0] = self.px-1
        elif self.tecla == key.LEFT:
            self.py -= 1
            self.p_a[1] = self.py+1
            self.p_a[0] = self.px
        elif self.tecla == key.UP:
            self.px -= 1
            self.p_a[1] = self.py
            self.p_a[0] = self.px+1
        if self.px==(len(self.lb)-1) and self.py==(len(self.lb[0])-2):
            self.lb[self.p_a[0]][self.p_a[1]]='.'
            print('Gracias por ayudar a Mako!! {} lograste completar el laberinto!!\nPresiona cualquier tecla para continuar y buscar mas bananas'.format(nombre))
            readkey()
            return True
        else:
            self.lb[self.p_a[0]][self.p_a[1]]='.' 
        if self.lb[self.px][self.py] == '#':
            self.px, self.py = self.p_a 
            return False

