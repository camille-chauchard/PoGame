import pygame

from constants import *
from screen import create_screen, update_screen
from world import create_world

inventaire=[]
sol=["vase","épée","lampe","sac à dos", "stylo", "livre","flûte"]
#il faut les mettre chacun dans une case de world ces objets. Comment ?
alive=True
running=True

#while True: la fonction while empêche le programme de bien fonctionner
def prendre (objet):
    index_1=sol.index(str(objet))
    del sol[index_1]
    inventaire.append(objet)
    return ('Votre inventaire est composé de',inventaire,'Sur le sol, il y a : ',sol)
def poser (objets):
    index_2=inventaire.index(str(objet))
    del inventaire[index_2]
    sol.append(objet)
    return ('Votre inventaire est composé de',inventaire,'Sur le sol, il y a : ',sol)
def quitter():
    alive=False
        

    
    

    

        
        
        