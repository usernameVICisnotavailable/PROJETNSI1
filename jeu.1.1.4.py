###################################### IMPORTS ######################################
from random import *



def def_mode(valeur):
    '''Change la valeur de mode pour la définir comme celle du menu'''
    global mode # comme la valeur du mode va etre modifie
    
    mode=valeur


def test_mode(valeur):
    '''Test qui renvoit true ou False si la valeur de mode est la meme
que celle qui est demandee'''
    
    return mode==valeur


def test_def_mode_jeu_str():
    '''associe une valeur à mode en fonction de la si
la valeur d'entree_jeu est dans la liste des jeux'''
    global mode
    
    if entree_jeu in liste_jeu: # si le jeu entrée est dans la liste de jeux
        def_mode(entree_jeu) # le nom du jeu devient le mode

    
def menu():
    '''Menu principale dans lequel on choisit le jeu auquel on va jouer'''
    assert test_mode("Menu") #vérifie qu'on est bien en mode menu
    global mode, entree_jeu # comme la valeur du mode va etre modifie. Attention si on oublie entree_jeu, ça ne marche pas car cette valeur est utlisé dans les autres fonctions (je ne comprends pas bien)
    
    print("Menu :\nJeux disponibles :")
    #affiche tout les jeux disponibles :
    for jeu in liste_jeu:
        print(f"- {jeu}")

    #Change le mode en fonction du texte entree
    while test_mode("Menu"):
        #les joueurs entre le jeu auquel il veulent jouer :
        entree_jeu=str(input("Ecrivez le jeux auquel vous voulez jouer comme écrit ci-dessus : "))
        #Si le nom est valide, on change de mode, sinon on redemande
        test_def_mode_jeu_str()
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



liste_jeu=["Morpion"]
mode="Menu"
menu()

# ------------------------------------------ Morpion ------------------------------------------
