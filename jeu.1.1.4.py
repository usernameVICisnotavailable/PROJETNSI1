###################################### IMPORTS ######################################
from random import *


###################################### Menu ######################################
liste_jeu=["Morpion"]
mode="Menu"


def def_mode(valeur):
    '''Change la valeur de mode pour la définir comme celle du menu'''
    global mode # comme la valeur du mode va etre modifie
    
    mode=valeur


def test_mode(valeur):
    '''Test qui renvoit true ou False si la valeur de mode est la meme
que celle qui est demandee'''
    
    return mode==valeur


    
def menu():
    '''
        Menu principale
    '''
    assert test_mode("Menu") #vérifie qu'on est bien en mode menu
    
    global mode, entree_jeu # comme la valeur du mode va etre modifie. Attention si on oublie entree_jeu, ça ne marche pas car cette valeur est utlisé dans les autres fonctions (je ne comprends pas bien)
    

def menu_affichage():
    '''
        Liste les jeux disponibles (dans liste_jeu)
    '''
    print("Menu :\nJeux disponibles :")
    for jeu in liste_jeu:
        print(f" - {jeu}")

def menu_choisir_jeu():
    '''
        Change le mode en fonction du texte entre
    '''
    global entree_jeu, mode
    while mode=="Menu":
        # les utilisateurs entrent le jeu auquel ils veulent jouer :
        entree_jeu = str(input("Ecrivez le jeux auquel vous voulez jouer comme écrit ci-dessus : "))
        #Si le nom est valide, on change de mode, sinon on redemande
        if entree_jeu in liste_jeu: # si le jeu entrée est dans la liste de jeux
            def_mode(entree_jeu) # le nom du jeu devient le mode
        if test_mode("Menu"):
            print("\nVeuillez renseigner un jeu valide.")


# ------------------------------------ Puissance-Quatre ------------------------------------

def puissance_quatre():
    '''
    Permet de jouer au puissance quatre à deux joueurs
    '''

    creer_grille(9,6)

    tour=randint(0,1) # le joueur qui commence est designe aleatoirement



# ------------------------------------ Chene contre sapin ------------------------------------





# ------------------------------------------ Morpion ------------------------------------------
