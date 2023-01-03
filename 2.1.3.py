###################################### IMPORTS ######################################
from random import *

#################################### Menu ######################################
liste_jeu=["Morpion","Chenes contre Sapins","Puissance Quatre"]
mode="Menu"
pions=["",""]

def menu():
    '''
        Menu principale
    '''
    assert mode=="Menu"
        
    menu_choisir_pions()
    menu_affichage()
    menu_choisir_jeu()
    print(f"Vous avez choisi de jouer a {mode} : \n")


def menu_affichage():
    '''
        Liste les jeux disponibles (dans liste_jeu)
    '''
    print("Menu :\nJeux disponibles :")
    #Affichage de la liste des jeux disponibles ainsi que leur indice augmenté de 1
    for indice in range(len(liste_jeu)):
        print(f" - {indice+1} {liste_jeu[indice]}")

def menu_choisir_pions():
    global pions
    # on demande tant que les pions sont : inchages, identiques ou trop longs
    while pions==["",""] or pions[0]==pions[1] or len(pions[0])!=1 or len(pions[1])!=1 or "_" in pions:
        pions=[]
        #On demande un pion pour chaque joueur.
        for numero_joueur in range(2):
            pions.append(str(input(f"Joueur {numero_joueur+1}, veuillez renseigner votre caractère de pion :")))

def menu_choisir_jeu():
    '''
        Entree : jeu entree via l'input
        Change le mode en fonction du texte entre
    '''
    global mode, entree_jeu 

    while mode=="Menu":
        # les utilisateurs entrent le jeu auquel ils veulent jouer :
        entree_jeu = int(input("Ecrivez le numéro correspondant au mode choisi : \n"))

        # si l'indice du jeu entrée est valide
        if 0<entree_jeu<=len(liste_jeu):                                
            # le nom du jeu devient le mode. 
            # On met -1 car les numéros affichés était +1
            mode=liste_jeu[entree_jeu-1] 
        
        #Si le numéro est invalide on recommence.
        else:
            print(f"\nNuméro Invalide.")


# ------------------------------------ Fonction réutilisable partout ------------------------------

def grille_vide(nb_colonnes,nb_ligne):
    '''
    renvoit un tableau vide avec le nombre de colones et de lignes renseigne qui sont indiqués
    '''
    assert nb_colonnes<=26
    
    #1er : ligne du haut avec les lettres de l'alphabet
    grille_tempo=[[alphabet[i] for i in range(nb_colonnes+1)]] #+1 car il y a un trou au début 
    
    #ensuitement : les autres lignes
    for i in range(1,nb_ligne+1): #on commence à 1 car le trou a déjà été posé et +1 car tout est donc déclalé
        #numéro de ligne puis un espace si besoin, proportioné à la longueur du plus grand numero de ligne
        grille_tempo.append([str(i)+" "*(len(str(nb_ligne))-len(str(i)))])
        #le reste de la ligne, vide
        grille_tempo[i].extend(["_" for _ in range(nb_colonnes)])
        
    return grille_tempo

def afficher_grille(liste_grille):
    '''
    Affiche de belle maniere le tableau genere par la fonction grille_vide
    '''
    for ligne in liste_grille:
        for valeur in ligne:
            print(f"{valeur}|", end="")
        print("")    

def victoire(grillage, tuple_alignement):
    '''
    Teste si les pions sont alignes obliquement
    '''

    #on parcours tout les points de la grillage
    for indice_colone in range(1,len(grillage[0])):
        for indice_ligne in range(1,len(grillage)):
            #a partir de chaque point on tire une diagonale montante et descendante puis on regarde si suffisament de pions y sont alignes
            for delta_x, delta_y in ((0,1),(1,1),(1,-1),(1,0)):
                if sous_test_aligne(grillage,indice_colone,indice_ligne,tuple_alignement,delta_x,delta_y) :
                    #si des points sont alignes, on renvoit True
                    return True
    #si le test finit, on renvoit False
    return False

def sous_test_aligne(grillage,x,y,tuple_alignement,deltax,deltay):
    '''
    tire des traits tel que donne par delta x et y a partir du point de coordonnees x et y. Renvoie True si l'alignement renseigne (entrez un tuple ou une liste) est rencontre
    '''
    compteur_aligne=0
    #tant que les x et les y sont dans la grillage
    while 0<x<len(grillage[0]) and len(grillage)>y>0:
        #a chaque fois que le pion est rencontre on augmente le compteur de 1
        if grillage[y][x]==tuple_alignement[compteur_aligne]:
            compteur_aligne+=1
            #si l'alignement fixe est atteint True
            if compteur_aligne==len(tuple_alignement):
                return True
        #si le pion rencontre n'est pas celui qu'on recherche le compteur retombe a 0
        else:
            compteur_aligne=0
        #on change de coordonees suivant une diagonale descendante
        x+=deltax
        y+=deltay
        #si le test finit, on renvoit False
    return False

        
# ------------------------------------ Puissance-Quatre ------------------------------------

from random import *

def puissance_quatre():
    global alphabet, grille, mode,joueur,pions,jeu_en_cours
    '''
    Permet de jouer au puissance quatre à deux joueurs
    '''

    #création d'une liste comportant toutes les lettres de l'alphabet avec un espace proportionel à la place que prendront les caractères des numéros de ligne au début
    #la liste sera utilisé dans la fonction afficher_grille et jouer_pion_puissance_4
    alphabet=[" "*len(str(6)),"A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #cree une grille vide de 9 sur 6
    grille=grille_vide(7,6)
    #designe aléatoirement le joueur qui commence
    joueur=randint(0,1)
    #indique que le jeu est en cours
    jeu_en_cours=True

    accueil_puissance_4()

    jeu_puissance_4()
    

def accueil_puissance_4():
    global pions
    print("Vous avez choisi de jouer au Puissance 4.\n\
\nLe puissance 4 se joue à deux joueurs dans un quardilage de 6 lignes sur 7 colones.\
\nCommencer une partie de puissance 4 :\n\
Pour commencer une partie de puissance 4, on désigne le premier joueur.\n\
Celui-ci met un de ses jetons de couleur dans l’une des colonnes de son choix.\n\
L3e jeton tombe alors en bas de la colonne.\n\n\
Le deuxième joueur insère à son tour son jeton, de l’autre couleur dans la colonne de son choix.\n\
Et ainsi de suite jusqu’à obtenir une rangée de 4 jetons de même couleur.\n\n\
Comment gagner une partie de puissance 4 :\n\
Pour gagner une partie de puissance 4, il suffit d’être le premier à aligner 4 jetons\n\
de sa couleur horizontalement,verticalement et diagonalement.\n\
Si lors d’une partie, tous les jetons sont joués sans\n\
qu’il y est d’alignement de jetons, la partie est déclaré nulle.")



def jeu_puissance_4():
    global jeu_en_cours,pion_joueur,pions,joueur,mode
    while jeu_en_cours:
        afficher_grille(grille)
        
        #Associe un pion en fonction du joueur
        pion_joueur=pions[joueur]
            
        #Demande a jouer
        print(f"C'est au joueur {joueur+1} de joueur \nSon pion est : {pion_joueur}")
        # joue
        jouer_pion_puissance_4(input("Entrez une colone : "),pion_joueur)
        
        #change de joueur si la colone est valide ou redemande a jouer
        if colone_valide:
            joueur=(joueur+1)%len(pions)
        else:
            print("Veuillez renseigner une colone valide.")
        for i in range(len(pions)):
            if victoire(grille,[pions[i] for _ in range(4)]):
                afficher_grille(grille)
                print(f"Le joueur {i+1} remporte la victoire.\nFélicitation à toi !\nRetour au menu principal…")
                jeu_en_cours=False
                mode="Menu"

        '''on parcours la grille de ligne en ligne et de bas en haut, 
        si la ligne du haut (en dessous des lettres de colones) est pleine
        c'est qu'il y a egalite puisque personne n'a gagne.'''
        if not "_" in grille[1]:
            afficher_grille(grille)
            print("Egalite !\n\
La grille est remplie et personne n'a gagne.\n\
Remarquez, une egalite n'est-elle pas preferable a la defaite ?")
            jeu_en_cours=False
            mode="Menu"

def jouer_pion_puissance_4(colone,caractère_joueur):
    '''
    Pose le pion renseigne en bas de la colone renseigne dans la liste de nom grille. Donne aussi la valeur True ou False à la variable colone_valide 
    '''
    global grille, colone_valide

    colone=colone.upper()
    
    #Si la valeur est correct
    if colone in grille[0]:
        #on associe un indice a la lettre renseigne
        index_colone=alphabet.index(colone)

        #on parcourt la colone de bas en haut
        for ligne in range(len(grille)-1,0,-1): #de la fin au debut sans la ligne des lettres de colones
            #des qu'on rencontre un "_" on place le pion
            if grille[ligne][index_colone]=="_":
                grille[ligne][index_colone]=caractère_joueur
                colone_valide=True
                break
    else:
        colone_valide=False


# ------------------------------------ Chene contre sapin ------------------------------------
# VLP :
##################################### Chenes contre Sapins #####################################

def chene_contre_sapin():
    ''' 
        Fonction principale
        NB : "ccs_" (pour Chenes Contre Sapins) devant chaque appelations pour ne pas poser de problemes avec les autres jeux
    '''
    global mode
    global ccs_fin                                  # Variable qui permet de determiner quand la partie est finie (si end=True --> Fin de partie)
    ccs_fin=False
    ccs_regle_du_jeu(input('Voulez-vous prendre connaissance des regles du Chene Contre Sapin ? Si oui tapez "O" \n'))
    global ccs_nb_lignes,ccs_nb_colonnes
    ccs_nb_lignes,ccs_nb_colonnes=ccs_entree("Choisissez le nombre de lignes du quadrillage : ",int,"Vous devez saisir un nomre entier : "),ccs_entree("Choisissez le nombre de colonnes du quadrillage : ",int,"Vous devez saisir un nomre entier : ")
    #ccs_quadrillage(int(input("Choisissez le nombre de colonnes du quadrillage : ")),int(input("Choisissez le nombre de lignes du quadrillage : ")))           # Creation d''un tableau
    ccs_quadrillage(ccs_nb_lignes,ccs_nb_colonnes)
    ccs_jeu()
    assert ccs_fin==True
    ccs_gagnant=ccs_entree(f"\n------- Le Joueur {ccs_tour_joueur} a-t-il bien gagne ? (O/N) -------\n","majuscule","Veuillez saisir O pour OUI ou N pour NON : ",('O','N'))
    if ccs_gagnant=='O':
        print(f"\n------- Bien joue a toi Joueur {ccs_tour_joueur} !! -------\n")
    elif ccs_gagnant=='N':                          # Le dernier joueur qui a joue peut avoir donne la victoire a son edversaire par sotise
        print(f"\n------- Joueur {ccs_tour_joueur}, tu es nul, c'est impardonnable ! -------\n")
    if input('"Voulez-vous revenir au menu principal ? Tapez "O" pour validez, ou ENTER pour arreter : ')=="O":
        mode="Menu"
        menu()                                      # Quand le jeu est fini, on peut revenir au menu avec tous les jeux

# ------------------------------------------------
def ccs_entree(message,expectation,erreur="Veuillez saisir une valeur valide : ",autorises=None):
    '''
        Verifie que la valeur entree respecte la demande :
        Entree: message : Demande textuelle a afficher (dans l'input)
                expectation : int/majuscule : type de valeur attendue, elle sont referencees dans le dictionnaire ccs_caracteres
                erreur : message d'erreur supplementaire (facultatif)
                (mini,maxi):expectation=int : valeur minimale et maximale accepetee de la valeur (facultatif)
                            expectation=lettre/majuscule ...etc : tuple de toutes les lettres acceptees
        Sortie : la valeur verifiee saisie par l'utilisateur
    '''
    ccs_caracteres={int:{"nom":"un nombre entier","min":ord('0'),"max":ord('9')},"majuscule":{"nom":"une majuscule","min":ord('A'),"max":ord('Z')}}   # Capacite d'etendre ccs_entree a la verification de la saisie de lettres avec ord()
    if expectation in list(ccs_caracteres.keys()):                      # La fonction peut-elle geree la verification de ce type de ccs_caracteres ?
        if expectation==int:                                            # La valeur demandee est un entier
            while True:
                ccs_question = input(message)
                for i in range(len(ccs_question)):                      # Pour tous les caracteres de la valeur saisie
                    if ord(ccs_question[i]) < ccs_caracteres[expectation]["min"] or ord(ccs_question[i]) > ccs_caracteres[expectation]["max"]:              # print(erreur) car ce n'est pas un caractere
                        print(erreur)
                        break
                    elif autorises!=None and (int(ccs_question)<int(autorises[0]) or int(ccs_question)>int(autorises[1])):                                   # Trop grand ou trop petit
                        print(erreur,'cheeeeeeeeeeeeeeeeeeeeeeeeeh')
                        break
                    if len(ccs_question)==i+1:                          # On est arrive jusqu'a la fin du mo sans erreur, donc c'est bon
                        return expectation(ccs_question)
        
        if expectation=="majuscule":                                     # La valeur attendue est une lettre majuscule
            while True:
                ccs_question = input(message)
                if ccs_question in autorises:                            # On s'assure qu'elle est dans la liste des majuscules autorisees
                    return ccs_question
                else:
                    print(erreur)
    else:
        return input(expectation)                                       # Par defaut sans verification 

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
def ccs_quadrillage(nb_lignes,nb_colonnes):
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
    global ccs_pion,ccs_position_souche,ccs_fin,ccs_tour_joueur,ccs_nb_tour
    #ccs_joueur={1:"joueur1",2:"joueur2"}
    ccs_pion={0:"*",1:pions[0],2:pions[1]}                        # Dictionnaire faisant correspondre son pion (caractere) au numero du joueur 
    ccs_changer_tour={1:2,2:1}                          # Permet de faire alterner les tours entre les joueurs
    ccs_tour_joueur=1                                   # le joueur 1 commence"
    ccs_nb_tour=0                                       # Compteur du nombre de tours (le placement des jeunes pousses ne compte pas dedans)
    
    ccs_position_souche=[(1,1),(1,2)]                   # Position par defaut des jeunes pousses
    print("Veuillez placer deux jeunes pousses d'arbre adjacentes :")
    [ccs_tour(t,True) for t in range(1,3)]              # 2 permiers tours : les joueurs placent les 2 jeunes pousses

    while not ccs_fin:                                  # Boucle qui s'execute juqusqu'a le fin du jeu, chaque repetition correspond a 1 tour
        ccs_nb_tour+=1
        ccs_tour(ccs_tour_joueur,False)                 # 1 tour
        ccs_tour_joueur=ccs_changer_tour[ccs_tour_joueur] # On change de joueur pour le prochain tour
        ccs_fin_partie()                 # Verifie si la partie est finie


def ccs_tour(ccs_tour_joueur,ccs_premiertour):
    '''
        Correspond a 1 tour
        Entree : quel joueur joue a ce tour et si c'est le premier tour (au premier tour les jeunes poussent sont placees)
    '''
    print(f"\nC'est au tour du Joueur {ccs_tour_joueur}") 

    #ccs_entree_ligne,ccs_entree_colonne=int(input("ligne : "))-1,int(input("colonne : "))-1
    #ccs_position_pion=(int(input("ligne : "))-1,int(input("colonne : "))-1) # tuple(LIGNE,COLONNE) qui definit la position du pion a inserer dans le quadrillage
    ccs_position_pion=(ccs_entree("ligne : ",int,"Veuillez saisir un nombre entier rentrant dans le tableau : ",(1,ccs_nb_lignes))-1,ccs_entree("colonne : ",int,"Veuillez saisir un nombre entier rentrant dans le tableau : ",(1,ccs_nb_colonnes))-1)
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
    if ccs_nb_tour>9:
        if input('La partie est-elle finie ? Tapez "O" pour validez, sinon pressez ENTER : ')=="O":
            ccs_fin=True
    



# ------------------------------------------ Morpion ------------------------------------------
def morpion():
    global joueur, pions, jeu_en_cours, grille, alphabet
    
    #création d'une liste comportant toutes les lettres de l'alphabet avec un espace proportionel à la place que prendront les caractères des numéros de ligne au début
    #la liste sera utilisé dans la fonction afficher_grille, case_colonne et case_ligne 
    alphabet=[" "*len(str(6)),"A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    #Créer une grille de 3 sur 3
    grille = grille_vide(3,3)
    
    #Désigne un joueur aléatoirement qui commencera 
    joueur = randint(0,1)
    
    #Désigne les pions que vont avoir les joueurs
    pions = ["O","X"]
    
    #Indique si le jeu est en cours
    jeu_en_cours = True
    
    jeu_morpion()
    

def jeu_morpion():
    global pions, joueur, pion_du_joueur, jeu_en_cours, mode
    while jeu_en_cours:
        afficher_grille(grille)
        
        #Associe un pion à un joueur
        pion_du_joueur = pions[joueur]
    
        #Demande au joueur de jouer
        print(f"C'est au joueur {joueur} de commencer \nLe pion qu'il l'appartient est le {pion_du_joueur}")

        #Permet au joueur de jouer
        case_colonne = input("Entrez le numéro d'une case de la colonne")
        case_ligne = input("Entrez le numéro d'une case de la ligne")

        #Donne la position du pion jouer
        print("Vous avez joué la case ("+colonne_pose_pion+","+ligne_pose_pion+")")
        
        #Vérifie la colonne de la case
        if colone_valide:
            joueur=(joueur+1)%len(pions)
        else:
            print("Veuillez renseigner une colone valide.")
        
        #Vérifie la ligne de la case
        if ligne_valide:
            joueur=(joueur+1)%len(pions)
        else:
            print("Veuillez renseigner une ligne valide.")

        #Vérifie si 3 pions identiques sont collés
        for i in range(len(pions)):
            if test_victoire(grille,pions[i],3):
                print(f"Le joueur {i} remporte la victoire.")
                jeu_en_cours=False
                mode="Menu"
                
def case_colonne(colonne, caractere_joueur):
    """
    Vérifie si la case est libre ou non
    """
    global grille, colonne_valide

    colonne=colonne.upper()
    
    #Si la valeur est correct
    if colonne in grille[0]:
        #on associe un indice a la lettre renseigne
        index_colone=alphabet.index(colonne)

        #On parcourt la colone de bas en haut
        for ligne in range(len(grille)-1,0,-1): #De la fin au debut sans la ligne des lettres de colonnes
            #des qu'on rencontre un "_" on place le pion
            if grille[ligne][index_colonne]=="_":
                grille[ligne][index_colonne]=caractere_joueur
                colonne_valide=True
                break
    else:
        colonne_valide=False

def case_ligne(ligne):
    """
    Vérifie si la case est libre ou non
    """
    if[grille][ligne] == "_":
        return True
    return False    


# ---------------------------------------------------------------------------------------------
while 1==1:
    if mode=="Menu":
        menu()
    '''if mode=="Morpion"
        morpion()'''
    if mode=="Chenes contre Sapins":
        chene_contre_sapin()
    if mode=="Puissance Quatre":
        puissance_quatre()