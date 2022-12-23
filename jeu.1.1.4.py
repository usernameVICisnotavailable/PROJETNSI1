###################################### IMPORTS ######################################
from random import *

#################################### Menu ######################################
liste_jeu=["Menu","Morpion","Chenes contre Sapins","Puissance Quatre"]
mode="Menu"

def menu():
    '''
        Menu principale
    '''
    assert mode=="Menu"
        
    menu_affichage()
    menu_choisir_jeu()
    print(f"Vous avez choisi de jouer a {mode} : \n")
    if mode==liste_jeu[1]: # liste_jeu[x] et non pas "NOM_DU_JEU" pour que les noms des jeux puissent être modifiés dans liste_jeu sans causer de problèmes
        pass #rentrer ici (à la place de pass) le nom de la variable principale de votre jeu afin que celui ci soit executé
    elif mode==liste_jeu[2]:
        chene_contre_sapin()
    elif mode==liste_jeu[3]:
        pass #rentrer ici (à la place de pass) le nom de la variable principale de votre jeu afin que celui ci soit executé


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
            print(f"\nVeuillez renseigner un jeu (chiffre de 1 à {len(liste_jeu)-1})") 
    return mode


# ------------------------------------ Puissance-Quatre ------------------------------------

#def puissance_quatre():
    '''
    Permet de jouer au puissance quatre à deux joueurs
    '''

  #  creer_grille(9,6)

   # tour=randint(0,1) # le joueur qui commence est designe aleatoirement



# ------------------------------------ Chene contre sapin ------------------------------------
# VLP :

def chene_contre_sapin():
    global ccs_end
    ccs_end=False
    ccs_quadrillage(5,5)
    ccs_jeu()

def ccs_quadrillage(nb_colonnes,nb_lignes):
    global ccs_case
    ccs_case=[["-" for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
    [print(ccs_case[i]) for i in range(nb_lignes)]

def ccs_jeu():
    global ccs_pion,ccs_position_souche
    #ccs_joueur={1:"joueur1",2:"joueur2"}
    ccs_pion={0:"*",1:"X",2:"O"}
    ccs_changer_tour={1:2,2:1}
    ccs_tour_joueur=1
    ccs_position_souche=[(1,1),(1,2)]
    print("Veuillez placer deux jeunes pousses d'arbre adjacentes :")
    [ccs_tour(t,True) for t in range(1,3)]
    while not ccs_end:
        ccs_tour(ccs_tour_joueur,False)
        ccs_tour_joueur=ccs_changer_tour[ccs_tour_joueur]


def ccs_tour(ccs_tour_joueur,ccs_premiertour):
    print(f"\nC'est au tour du Joueur {ccs_tour_joueur}")
    #ccs_entree_ligne,ccs_entree_colonne=int(input("ligne : "))-1,int(input("colonne : "))-1
    ccs_position_pion=(int(input("ligne : "))-1,int(input("colonne : "))-1)               # tuple(LIGNE,COLONNE)
    if ccs_case[ccs_position_pion[0]][ccs_position_pion[1]] != "-":
        print("\nVeuillez saisir un emplacement vide !")
        ccs_tour(ccs_tour_joueur,ccs_premiertour)
        return
    if ccs_premiertour:
        if ccs_tour_joueur==1:
            ccs_position_souche[0]=ccs_position_pion
        if ccs_tour_joueur==2:
            if not ((abs(ccs_position_souche[0][0]-ccs_position_pion[0])==1 and (ccs_position_souche[0][1]-ccs_position_pion[1])==0) ^ ((ccs_position_souche[0][0]-ccs_position_pion[0])==0 and abs(ccs_position_souche[0][1]-ccs_position_pion[1])==1)):
                print("La deuxieme jeune pousse n'est pas adjacente a la premiere !")
                ccs_tour(ccs_tour_joueur,ccs_premiertour)
                return
            ccs_position_souche[1]=ccs_position_pion
        ccs_placer_pion(ccs_position_pion,ccs_pion[0])
    else:
        ccs_placer_pion(ccs_position_pion,ccs_pion[ccs_tour_joueur])
    [print(ligne) for ligne in ccs_case]

def ccs_placer_pion(ccs_position_pion,ccs_pion_joueur):
    ccs_case[ccs_position_pion[0]][ccs_position_pion[1]]=ccs_pion_joueur



# ------------------------------------------ Morpion ------------------------------------------



# ---------------------------------------------------------------------------------------------
menu()