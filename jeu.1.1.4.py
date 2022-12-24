###################################### IMPORTS ######################################
from random import *

#################################### Menu ######################################
liste_jeu=["Menu","Morpion","Chenes contre Sapins","Puissance Quatre"]
mode="Menu"

def menu():
    '''
        Menu principal
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
    ''' 
        Fonction principale
        NB : "ccs_" (pour Chenes Contre Sapins) devant chaque appelations pour ne pas poser de problemes avec les autres jeux
    '''
    global mode
    global ccs_fin                                  # Variable qui permet de déterminer quand la partie est finie (si end=True --> Fin de partie)
    ccs_fin=False
    ccs_regle_du_jeu(input('Voulez-vous prendre connaissance des regles du Chene Contre Sapin ? Si oui tapez "O" \n'))
    ccs_quadrillage(int(input("Choisissez le nombre de colonnes du quadrillage : ")),int(input("Choisissez le nombre de lignes du quadrillage : ")))           # Creation d''un tableau
    ccs_jeu()
    assert ccs_fin==True
    print(f"\n------- Le Joueur {ccs_tour_joueur} gagne, Bien Joue !! -------\n")
    if input('"Voulez-vous revenir au menu principal ? Tapez "O" pour validez, ou ENTER pour arreter : ')=="O":
        mode="Menu"
        menu()                                      # Quand le jeu est fini, on peut revenir au menu avec tous les jeux

# ------------------------------------------------
def ccs_regle_du_jeu(ccs_choix):
    '''
        Affiche les regles du jeu
        Entree : Le choix saisi par l'utilisateur ("O" pour afficher, n'immporte quoi d'autre pour passer)
    '''
    if ccs_choix=="O":                              # Si l'utilisateur a saisi "O", on affiche les regles
        print("Le Chene Contre Sapin se joue a deux, au debut de la partie chaque joueur plante une jeune pousse dans un terrain (tableau), ces deux pousses doivent être adjacentes. Le but du jeu est de propager son espece. Un joueur gagne lorsque les pousses sont entourees par son espece d'arbre. L'entourage est considere comme effectif lorsque tous les arbres de l'espece composent une forme continue englobant les deux pousses. Tous les arbres doivent être adjacents les uns aux autres, un arbre de l'espece concurrente brisant la continuite de la forme englobante peut être saute si il est bien ajdacent a un autre arbre de la bonne espece. Si plusireurs arbres ajdacents de l'espece concurrente brisent la continuite de la forme englobante de l'autre espece, ceux ci ne pourront pas etre sautes.")
        input("\nPressez enter pour continuer")

# ------------------------------------------------
def ccs_quadrillage(nb_colonnes,nb_lignes):
    '''
        Creation et affichage d'un quadrillage (tableau a deux dimensions) 
        Entree : Nombre de lignes et de colonnes (choisi par l'utilisateur)
    '''
    global ccs_case
    ccs_case=[["-" for _ in range(nb_colonnes)] for _ in range(nb_lignes)]  # Creation d'un tableau deux dimensions (appele quadrillage)
    [print(ccs_case[i]) for i in range(nb_lignes)]                          # Affichage du quadrillage

# ------------------------------------------------
def ccs_jeu():
    '''
        Fonction secondaire, fonctionnement et execution du jeu
    '''
    global ccs_pion,ccs_position_souche,ccs_fin,ccs_tour_joueur
    #ccs_joueur={1:"joueur1",2:"joueur2"}
    ccs_pion={0:"*",1:"X",2:"O"}                        # Dictionnaire faisant correspondre son pion (caractere) au numero du joueur 
    ccs_changer_tour={1:2,2:1}                          # Permet de faire alterner les tours entre les joueurs
    ccs_tour_joueur=1                                   # le joueur 1 commence"
    
    ccs_position_souche=[(1,1),(1,2)]                   # Position par défaut des jeunes pousses
    print("Veuillez placer deux jeunes pousses d'arbre adjacentes :")
    [ccs_tour(t,True) for t in range(1,3)]              # 2 permiers tours : les joueurs placent les 2 jeunes pousses

    while not ccs_fin:                                  # Boucle qui s'execute juqusqu'à le fin du jeu, chaque repetition correspond a 1 tour
        ccs_tour(ccs_tour_joueur,False)                 # 1 tour
        ccs_tour_joueur=ccs_changer_tour[ccs_tour_joueur] # On change de joueur pour le prochain tour
        ccs_fin_partie()                 # Verifie si la partie est finie


def ccs_tour(ccs_tour_joueur,ccs_premiertour):
    '''
        Correspond a 1 tour
        Entree : quel joueur joue a ce tour et si c'est le premier tour (au premier tour les jeunes poussent sont placées)
    '''
    print(f"\nC'est au tour du Joueur {ccs_tour_joueur}") 

    #ccs_entree_ligne,ccs_entree_colonne=int(input("ligne : "))-1,int(input("colonne : "))-1
    ccs_position_pion=(int(input("ligne : "))-1,int(input("colonne : "))-1) # tuple(LIGNE,COLONNE) qui définit la position du pion a inserer dans le quadrillage
    if ccs_case[ccs_position_pion[0]][ccs_position_pion[1]] != "-":         # Sl'emplacement dans le quadrillage est deja prit par un pion : 
        print("\nVeuillez saisir un emplacement vide !")                    
        ccs_tour(ccs_tour_joueur,ccs_premiertour)                           # On recommence le tour avec le meme joueur
        return
    
    if ccs_premiertour:                                 # Si c'est le premier tour (celui ou on place les jeunes pousses)
        if ccs_tour_joueur==1:                          
            ccs_position_souche[0]=ccs_position_pion    # Si c'est le premier joueur, on enregistre la position de sa jeune pousse dans un tableau specifique
        if ccs_tour_joueur==2:
            if not ((abs(ccs_position_souche[0][0]-ccs_position_pion[0])==1 and (ccs_position_souche[0][1]-ccs_position_pion[1])==0) ^ ((ccs_position_souche[0][0]-ccs_position_pion[0])==0 and abs(ccs_position_souche[0][1]-ccs_position_pion[1])==1)):
                                                        # Si le deuxieme jeune pousse placee n'est pas adjacente a la premiere :
                print("La deuxieme jeune pousse n'est pas adjacente a la premiere !")
                ccs_tour(ccs_tour_joueur,ccs_premiertour) # On relance le tour avec le meme joueur pour qu'il la replace 
                return
            ccs_position_souche[1]=ccs_position_pion    # On enregistre la position valide de la deuxieme jeune pousse dans le tableau specifique 
        ccs_placer_pion(ccs_position_pion,ccs_pion[0])  # On place le pion (attention, ccs_pion[0] car c'est le premier tour, donc ce n'est pas un pion banal, c'est la jeune pousse)
    else:
        ccs_placer_pion(ccs_position_pion,ccs_pion[ccs_tour_joueur]) # Si ce n'est pas le premier tour, on place un pion banal
    [print(ligne) for ligne in ccs_case]                # Affichage du quadrillage (tableau)

def ccs_placer_pion(ccs_position_pion,ccs_pion_joueur):
    '''
        Entree : Position du pion --> tuple(LIGNE,COLONNE), Type de pion --> caractere '''
    ccs_case[ccs_position_pion[0]][ccs_position_pion[1]]=ccs_pion_joueur # Raplacage du tiret de la case vide par le caractere

def ccs_fin_partie():
    '''
        Determine si la partie est finie. Si oui on redefinit la variable ccs_fin=True
        NB : Le jeu de Chene Contre Sapin est produit de notre invention, la determination par analyse qui se fait 
        assez facilement visuellement est cependant plus complexe a coder et serait assez long. Nous avons donc convenu que l'analyse se ferait par l'utilisateur
    '''
    global ccs_fin
    if input('La partie est-elle finie ? Tapez "O" pour validez, sinon pressez ENTER : ')=="O":
        ccs_fin=True
    

# ------------------------------------------ Morpion ------------------------------------------



# ---------------------------------------------------------------------------------------------
menu()