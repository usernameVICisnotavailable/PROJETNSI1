###################################### IMPORTS ######################################
from random import *

#################################### Menu ######################################
    
def menu():
    '''
        Menu principale
    '''
    assert mode=="Menu" #vérifie qu'on est bien en mode menu
        
    menu_affichage()
    menu_choisir_jeu()


def menu_affichage():
    '''
        Liste les jeux disponibles (dans liste_jeu)
    '''
    print("Menu :\nJeux disponibles :")
    for jeu in liste_jeu:
        print(f" - {jeu}")

def menu_choisir_jeu():
    '''
        Entree : jeu entree via l'input
        Change le mode en fonction du texte entre
    '''
    global mode, entree_jeu # comme la valeur du mode va etre modifie. Attention si on oublie entree_jeu, ça ne marche pas car cette valeur est utlisé dans les autres fonctions (je ne comprends pas bien)
    
    while mode=="Menu":
        # les utilisateurs entrent le jeu auquel ils veulent jouer :
        entree_jeu = str(input("Ecrivez le jeux auquel vous voulez jouer comme écrit ci-dessus : "))
        #Si le nom est valide, on change de mode, sinon on redemande
        if entree_jeu in liste_jeu: # si le jeu entrée est dans la liste de jeux
            mode=entree_jeu # le nom du jeu devient le mode
        if mode=="Menu":
            print("\nVeuillez renseigner un jeu valide.")


# ------------------------------------ Puissance-Quatre ------------------------------------

#def puissance_quatre():
    '''
    Permet de jouer au puissance quatre à deux joueurs
    '''

  #  creer_grille(9,6)

   # tour=randint(0,1) # le joueur qui commence est designe aleatoirement



# ------------------------------------ Chene contre sapin ------------------------------------





# ------------------------------------------ Morpion ------------------------------------------

liste_jeu=["Morpion"]
mode="Menu"
menu()