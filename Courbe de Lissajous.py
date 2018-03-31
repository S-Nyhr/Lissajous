from tkinter import *
from math import *

def movement():
    "Permet le tracé de courbe de Lissajous"
    global x, y, angle1, angle2, r1, r2, flag                               #Variable global
    
    xp, yp = x, y                                                           #Variable xp et yp qui sont deux variables qui prennent
                                                                            #les anciennes positions de x et y pour le tracé d'une ligne.
    
    x = 200 + r1 * cos(radians(angle1)) + r1 * sin(radians(angle1))         #Cercle x et y, on additione cos(angle) et sin(angle) pour
    y = 200 + r2 * cos(radians(angle2)) + r2 * sin(radians(angle2))         #obtenir les coordonées du point sur le cercle.
                                                                            #Mise à l'échelle avec 200(la moitié du Canvas)
    
    angle1, angle2 = angle1 + vitesse_x, angle2 + vitesse_y                 #Incrémentation des angles pour faire le tour des deux cercles.
    
    can.create_line(xp, yp, x, y, fill="blue")                              #Création du tracé, avec xp et yp pour anciennes positions.

    if flag > 0 :                                                           #Commutateur pour démarrer ou arrêter l'animation.
        fen.after(1, movement)

def stop_it():
    "Arrêt de l'animation"
    global flag    
    flag = 0

def start_it():
    "Démarrage de l'animation"
    global flag
    if flag == 0 :              #Sans cette instruction, nous pourrions lancer plusieurs fois la fonction, car flag > 0
        flag = 1
        movement()

def reset():
    "Reset du Canvas"
    can.delete(ALL)
    

r1, r2 = 125, 125                #Rayon A et Rayon B
angle1, angle2 = 90, 90          #Psi Ψ = Position de x et de y dans un cercle, (cercle parfait = 0, 90 ou l'inverse)

vitesse_x, vitesse_y =  .18, .20              #Vitesses d'éxecution d'un tour complet du cercle x ou y (VARIABLE A MODIFIER POUR OBTENIR UN CHANGEMENT DE LA COURBE)

flag = 0                        #Variable de référence pour démarrer et arrêter l'animation
x, y = 200 + r1, 200 + r2       #Position de x et de y dans le Canvas, mise a l'échelle avec 200 + le rayon

fen = Tk()

can = Canvas(fen, bg="white", width=400, height=400)
can.pack(side=TOP)

Button(fen, text="Bouger", command=movement).pack(side=LEFT)
Button(fen, text="Démarrer", command=start_it).pack(side=LEFT)
Button(fen, text="Arrêter", command=stop_it).pack(side=LEFT)
Button(fen, text="Reset", command=reset).pack(side=RIGHT)
Button(fen, text="Quitter", command=fen.quit).pack(side=RIGHT)

fen.mainloop()

fen.destroy()
