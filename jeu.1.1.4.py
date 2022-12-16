###################################### IMPORTS ######################################
from random import *

#################################### Menu ######################################
liste_jeu=["Menu","Morpion","Chene contre Sapin","Puissance Quatre"]
mode="Menu"

def menu():
    '''
        Menu principale
    '''
    assert mode=="Menu"
        
    menu_affichage()
    print(f"Vous avez choisi de jouer a {menu_choisir_jeu()} : \n")


def menu_affichage():
    '''
        Liste les jeux disponibles (dans liste_jeu)
    '''
    print("Menu :\nJeux disponibles :")
    compteur=0
    for jeu in liste_jeu:
        print(f" - {compteur} : {jeu}")
        compteur+=1

def menu_choisir_jeu():
    '''
        Entree : jeu entree via l'input
        Change le mode en fonction du texte entre
    '''
    global mode, entree_jeu 

    while mode=="Menu":
        # les utilisateurs entrent le jeu auquel ils veulent jouer :
        entree_jeu = int(input("Ecrivez le numéro correspondant au mode choisi : \n"))
        #entree_jeu = str(input("Ecrivez le jeux auquel vous voulez jouer comme écrit ci-dessus : "))
        #if entree_jeu in liste_jeu:                         # si le jeu entrée est dans la liste de jeux
        if entree_jeu <= len(liste_jeu) and entree_jeu >= 0:
            mode=liste_jeu[entree_jeu]                                 # le nom du jeu devient le mode
        if mode=="Menu":                                    # On redemmande le mode
            print("\nVeuillez renseigner un jeu valide.")
    return mode


# ------------------------------------ Puissance-Quatre ------------------------------------

#def puissance_quatre():
    '''
    Permet de jouer au puissance quatre à deux joueurs
    '''

  #  creer_grille(9,6)

   # tour=randint(0,1) # le joueur qui commence est designe aleatoirement



# ------------------------------------ Chene contre sapin ------------------------------------





# ------------------------------------------ Morpion ------------------------------------------



# ---------------------------------------------------------------------------------------------
menu()