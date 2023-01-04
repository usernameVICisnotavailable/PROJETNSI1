###################################### IMPORTS ######################################
from random import *

#################################### Menu ######################################
liste_jeu=["Tournoi","Morpion","Chenes contre Sapins","Puissance Quatre","La Guerre des Geoliers"]
mode="Menu"
pions=["",""]
tournoi_active=False

def menu():
    '''
        Menu principal
    '''
    assert mode=="Menu"
        
    menu_choisir_pions()
    menu_affichage()
    menu_choisir_jeu()
    print(f"Vous avez choisi de jouer a {mode} : \n")


def menu_affichage():
    '''
        Affiche la liste les jeux disponibles (dans liste_jeu)
    '''
    print("Menu :\nJeux disponibles :")
    #Affichage de la liste des jeux disponibles ainsi que leur indice augmenté de 1
    for indice in range(len(liste_jeu)):
        print(f" - {indice+1} {liste_jeu[indice]}")

def menu_choisir_pions():
    '''
        Permet aux joueurs de choisir leurs pions plutôt que d'avoir X et O par defaut
    '''
    global pions
    # on demande tant que les pions sont : inchages, identiques, "_" ou trop longs
    while pions==["",""] or\
         pions[0]==pions[1] or \
            len(pions[0])!=1 or len(pions[1])!=1 \
                or "_" in pions: #car ce carctere symbolise le vide dans les grilles
        pions=[]
        #On demande un pion pour chaque joueur (2* donc), puis on l'ajoute a la fin de la liste vide
        for numero_joueur in range(2):
            pions.append(str(input(f"Joueur {numero_joueur+1}, veuillez renseigner votre caractère de pion :")))

def menu_choisir_jeu():
    '''
        Entree : jeu entree via l'input
        Change le mode en fonction du texte entre
    '''
    global mode, entree_jeu, tournoi_active, parties
    if tournoi_active:
        print("compteur parties",compteur_parties,"parties", parties)
        #si le nombre de parties fixes est atteint, on affiche les score et le vainque (sauf egalite)
        if compteur_parties==parties:
            if scores[0]>scores[1]:
                print(f"Le joueur 1 gagne !")
            elif scores[0]==scores[1]:
                print("Egalite")
            else:
                print("Le joueur 2 gagne !")
            print(f"Le score était de {scores[0]} a {scores[1]} !")
            #on désactive la mode tournois
            tournoi_active=False
        #le jeu est automatiquement aléatoirement choisi si c'est pas fini
        else:
            mode=liste_jeu[randint(1,len(liste_jeu)-1)]
            
    if not(tournoi_active):
        while mode=="Menu":
            # les utilisateurs entrent le jeu auquel ils veulent jouer :
            entree_jeu = ccs_entree("Ecrivez le numéro correspondant au mode choisi : ",int)

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
        renvoit un tableau vide avec le nombre de colones et de lignes renseigne qui sont indiqués.
        Il contiendra les numeros et les lettres des colones et lignes. Il est ideal de l'afficher avec
        la fonctio, afficher_grille(grille)
    '''
    assert nb_colonnes<=26
    global alphabet
    
    #genere un alphabet avec un espace au debut (case vide)
    alphabet=[" "*len(str(nb_colonnes)),"A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    #1er : ligne du haut avec les lettres de l'alphabet
    grille_tempo=[[alphabet[i] for i in range(nb_colonnes+1)]] #+1 car il y a un trou au début 
    
    #ensuitement : les autres lignes
    for i in range(1,nb_ligne+1):
#on commence à 1             ^^  car la case vide a déjà été posé et +1 car tout est donc déclalé
        #numéro de ligne puis un espace ou non, proportioné à la taille du + grand numero de ligne
        grille_tempo.append([str(i)+" "*(len(str(nb_ligne))-len(str(i)))])
        #le reste de la ligne, vide (c'est la qu'on placera les pions)
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
        Teste si les pions sont alignes dans quel sens que ce soit de la maniere dont ca a ete
        renseigne.
    '''

    #on parcours tout les points de la grillage
    for indice_colone in range(1,len(grillage[0])):
        for indice_ligne in range(1,len(grillage)):
            '''a partir de chaque point on cherche dans tout les sens, cad \, /, - et | si
            on trouve l'alignement renseigne. La fonction utiliser pour cela est sous_test_aligne
            Cette methode provoque plus de calcul que besoin, mais contourner le probleme serait
            sans doute une perte de temps compte tenu des capacites de l'ordinateur'''
            for delta_x, delta_y in ((0,1),(1,1),(1,-1),(1,0)):
                if sous_test_aligne(grillage,indice_colone,indice_ligne,tuple_alignement,delta_x,delta_y) :
                    #si des points sont alignes, on renvoit True
                    return True
    #si le test finit, on renvoit False, on a rien trouve.
    return False

def sous_test_aligne(grillage,x,y,tuple_alignement,deltax,deltay, max = float("inf")):
    '''
    tire des traits tel que donne par delta x et y a partir du point de coordonnees x et y. 
    Renvoie True si l'alignement renseigne (entrez un tuple ou une liste) est rencontre
    on peut definir un max de fois ou l'on fait avance de delta x et y.
    '''
    #compte le nombre de fois ou l'on trouve ce qu'il faut d'affile
    compteur_aligne=0
    #compte le nombre de fois ou l'on augmente de delta x et y
    compteur=0

    #tant que les x et les y sont dans la grillage et que le max n'a pas ete atteint
    while 0<x<len(grillage[0]) and len(grillage)>y>0 and compteur<max:
        #a chaque fois que le pion est rencontre on augmente le compteur de 1
        if grillage[y][x]==tuple_alignement[compteur_aligne]:
            compteur_aligne+=1
            #si l'alignement fixe est atteint True
            if compteur_aligne==len(tuple_alignement):
                return True
        #si le pion rencontre n'est pas celui qu'on recherche le compteur retombe a 0
        else:
            compteur_aligne=0

        #on change de coordonees suivant les delta x et y renseignes
        x+=deltax
        y+=deltay
        compteur+=1
    #si le test finit, on renvoit False, on a rien trouve
    return False

def poser(colone,ligne,pionajouer,grillage):
    '''
    Fonctionne avec les grille de grille_vide
    pose un pion a la colone et a la ligne renseigne du grillage donne.
    Ne fait rien si ce qui est rentre est invalide et donne alors False a la variable valide
    '''
    global valide

    #converti en int le numero de ligne ou lui donne la valeur infini (evitant ainsi les bugs)
    numeral=True
    if isinstance(ligne, str):
        for caractere in ligne:
            numeral= (caractere in (str(i) for i in range(10))) and numeral
        if numeral:
            ligne=int(ligne)
        else:
            ligne=float("inf")

    #met colone en majuscule, quel qu'il soit
    colone=colone.upper()

    #Si la colone est parmis les lettres donnes et que le numero est ni trop grand ni trop petit
    if colone in grillage[0] and 0<ligne<len(grillage):
        #on affecte une valeur numerique a la colone en fonction de sa place dans la 1ere ligne
        colone=grillage[0].index(colone)

        #Si l'emplacement est vide
        if grillage[ligne][colone]=="_":
            #on pose le pion
            grillage[ligne][colone]=pionajouer
            #cette pose est evidement valide
            valide=True
        else:
            #sinon c'est invalide
            valide=False
    else:
        valide=False
        
def test_victoire_classique(longueur):
    '''
        Test s'il y a alignement de pions identiques de la longeur renseigne
        et si oui, arrete le jeu
    '''
    global compteur_parties,scores
    #Test de victoire pour chacun des pions    
    for i in range(len(pions)):
        if victoire(grille,[pions[i] for _ in range(longueur)]):
            afficher_grille(grille)
            print(f"Le joueur {i+1} dont le pions est {pions[i]} remporte la victoire.\nFélicitation à toi !\nRetour au menu principal…")
            if tournoi_active:
                fin_de_partie_tournois(i)
                input("Entree pour continuer")
                fin_de_partie()

def fin_de_partie():
    '''
        Change les variable de tel sorte que la partie se termine
    '''
    global jeu_en_cours, mode
    jeu_en_cours=False
    mode="Menu"

def test_egalite(list_grille):
    '''
    Test si la grille est plein. Si oui, egalite et fin de partie
    '''
    vide=True
    for ligne in list_grille:
        vide= not "_" in ligne and vide
    if vide:
        print("Egalite !\nRetour au menu principal...")
        fin_de_partie()

def tour_classique(grillage):
    '''
        Pose ou pas les pions etc.
    '''
    global joueur
    #Permet au joueur de jouer
    poser(input(f"C'est au tour du joueur {joueur+1} de jouer.\n Son pion est : {pions[joueur]}.\nVeuillez \
renseigner la lettre de la colone : "),input("Veuillez renseigner le numero de la ligne :"),pions[joueur],grillage)
    
    #Si les coordonnes rentrees sont invalides, on ne change pas de joueur et vice versa
    if valide:
        joueur=(joueur+1)%len(pions)
    else:
        print("Veuillez renseigne des coordonees valides.")
# ------------------------------------ Puissance-Quatre ------------------------------------

from random import *

def puissance_quatre():
    global alphabet, grille, mode,joueur,pions,jeu_en_cours
    '''
    Permet de jouer au puissance quatre à deux joueurs
    '''

    accueil_puissance_4()
    jeu_puissance_4()
    

def accueil_puissance_4():
    '''
        Affiche les regles du jeu
    '''
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
    '''
        Le jeu, simplement.
    '''
    global jeu_en_cours,pions,joueur,mode,grille

    #cree une grille vide de 7 sur 6
    grille=grille_vide(7,6)
    #designe aléatoirement le joueur qui commence
    joueur=randint(0,1)
    #indique que le jeu est en cours
    jeu_en_cours=True

    while jeu_en_cours:
        afficher_grille(grille)
            
        puissance_4_tour()

        test_victoire_classique(4)

        test_egalite_puissance4()


def puissance_4_tour():
    '''
        Effectue un tour de jeu.
    '''
    global joueur

    #Demande a jouer et pose le pion du joueur dont c'est le tour, si c'est valide
    jouer_pion_puissance_4(input(f"C'est au joueur {joueur+1} de joueur \n\
Son pion est : {pions[joueur]}\nEntrez une colone : "),pions[joueur])
    
    #change de joueur si la colone est valide ou redemande a jouer
    if colone_valide:
        joueur=(joueur+1)%len(pions)
    else:
        print("Veuillez renseigner une colone valide.")

def test_egalite_puissance4():
    '''
        Test s'il y a egalite et si oui, arrete le jeu
    '''
    '''on parcours la grille de ligne en ligne et de bas en haut, 
    si la ligne du haut (en dessous des lettres de colones) est pleine
    c'est qu'il y a egalite puisque personne n'a gagne.'''
    if not "_" in grille[1]:
        afficher_grille(grille)
        print("Egalite !\nLa grille est remplie et personne n'a gagne.\n\
Remarquez, une egalite n'est-elle pas preferable a la defaite ?")
        fin_de_partie()

def jouer_pion_puissance_4(colone,caractère_joueur):
    '''
    Pose le pion renseigne en bas de la colone renseigne dans la liste de nom grille.
    Donne aussi la valeur True ou False à la variable colone_valide.
    '''
    global grille, colone_valide

    colone=colone.upper()
    
    #Si la valeur est correct
    if colone in grille[0]:
        #on associe un indice a la lettre renseigne
        index_colone=alphabet.index(colone)

        #on parcourt la colone de bas en haut
        for ligne in range(len(grille)-1,0,-1): #de la fin au debut sans la ligne des lettres de colones
            #des qu'on rencontre un "_" on place le pion et on termine
            if grille[ligne][index_colone]=="_":
                grille[ligne][index_colone]=caractère_joueur
                colone_valide=True
                break
    else:
        colone_valide=False

##################################### Chenes contre Sapins #####################################

def chene_contre_sapin():
    ''' 
        Fonction principale
        NB : "ccs_" (pour Chenes Contre Sapins) devant chaque appelations pour ne pas poser de problemes avec les autres jeux
    '''
    global mode, compteur_parties
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
        if tournoi_active:
            fin_de_partie_tournois(ccs_tour_joueur-1)
            mode="Menu"
            menu()  
    elif ccs_gagnant=='N':                          # Le dernier joueur qui a joue peut avoir donne la victoire a son edversaire par sotise
        print(f"\n------- Joueur {ccs_tour_joueur}, tu es nul, c'est impardonnable ! -------\n")
        if tournoi_active:
            fin_de_partie_tournois(ccs_tour_joueur%2)
            mode="Menu"
            ccs_fin=True 
    if not tournoi_active:
        if input('"Voulez-vous revenir au menu principal ? Tapez "O" pour validez, ou ENTER pour arreter : ')=="O":
            mode="Menu"
            ccs_fin=True                                      # Quand le jeu est fini, on peut revenir au menu avec tous les jeux

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
    global joueur, pions, jeu_en_cours, grille, alphabet,mode
    
    accueil_morpion()

    #création d'une liste comportant toutes les lettres de l'alphabet avec un espace proportionel à la place que prendront les caractères des numéros de ligne au début
    #la liste sera utilisé dans la fonction afficher_grille, case_colonne et case_ligne 
    
    #Créer une grille de 3 sur 3
    grille = grille_vide(3,3)
    
    #Désigne un joueur aléatoirement qui commencera 
    joueur = randint(0,1)
        
    #Indique si le jeu est en cours
    jeu_en_cours = True
    
    while jeu_en_cours:
        afficher_grille(grille)
        
        tour_classique(grille)

        test_victoire_classique(3)

        test_egalite(grille)

    
def accueil_morpion():
    '''
        Bref resume des regles
    '''
    print("Le morpion se joue dans une grille de 3 sur 3. Le but est d'aligner 3 de ses pions. ex:")
    grille=grille_vide(3,3)
    pion_exemple=pions[randint(0,1)]
    for j in ("A","B","C"):
        poser(j,2,pion_exemple,grille)
    afficher_grille(grille)
    input("Entree pour continuer.")



# ------------------------------------------ La Guerre des Geoliers ------------------------------------------
def guerre_des_geoliers():
    accueil_guerre_des_geoliers()
    jeu_guerre_des_geoliers()

def accueil_guerre_des_geoliers():
    '''
        Explique les regles du jeu agremente d'exemples
    '''
    print("La guerre des geoliers se joue dans une grille de 10 sur 10.\n Chaque joueur y\
 joue son pion l'un après l'autre.\nIl y a trois manière de gagner :")

    print(f"1 : entourer un alignement de deux pions adverse par les deux extremites.\n \
Ici, {pions[0]} a gagne.\nCela fonctionne en diagonale, a l'horizontale et a la verticale")
    #affiche l'exemple de ci-dessus :
    grille=grille_vide(10,10)
    #d'apres les coordonees et les pions ci-dessous 
    for i,j in ((1,pions[0]),(2,pions[1]),(3,pions[1]),(4,pions[0])):
        poser("B",i,j,grille)
    afficher_grille(grille)
    input("Entree pour continuer.")

    print(f"2 : Entourer par tout les cotes (pas les angles) un pion adverse. Ici, {pions[0]} a gagne.")
    #de meme un exemple:
    grille=grille_vide(10,10)
    #d'abord tout les pions 0
    for i,j in (("B",2),("A",3),("C",3),("B",4)):
        poser(i,j,pions[0],grille)
    #puis le pion 1
    poser("B",3,pions[1],grille)
    afficher_grille(grille)
    input("Entree pour continuer.")

    print(f"3 : Aligner quatre pions. Ici, {pions[0]} a gagne.")
    #encore un exemple
    grille=grille_vide(10,10)
    for j in range(1,5):
        poser("D",j,pions[0],grille)
    afficher_grille(grille)
    input("Entree pour continuer.")

def jeu_guerre_des_geoliers():
    global mode, compteur_parties, jeu_en_cours, joueur, grille
    jeu_en_cours=True
    joueur=randint(0,1)
    grille=grille_vide(10,10)
    while jeu_en_cours:
        afficher_grille(grille)
        tour_classique(grille)
        test_victoire_guerre_des_geoliers()
        test_egalite(grille)

def entoure_guerre_des_geoliers(encerclant,encercle,grillage):
    '''
    Test si un pion est entoures par les quatre cotes
    '''
    for indice_colone in range(1,len(grillage[0])):
        for indice_ligne in range(1,len(grillage)):
            #a partir de chaque point on tire une diagonale montante et descendante puis on regarde si suffisament de pions y sont alignes
            resultat=True
            for delta_x, delta_y in ((0,1),(0,-1),(1,0),(-1,0)):
                #si des points sont alignes, on renvoit True
                resultat= (resultat and sous_test_aligne(grillage,indice_colone,indice_ligne,(encercle,encerclant),delta_x,delta_y,2))
            if resultat:
                return True
            
    return False

def test_victoire_guerre_des_geoliers():
    '''
        Test s'il y a victoire d'apres les trois possibilites quand c'est fait, fin de partie
    '''

    #pour chancun des pions
    for indice_joueur in range(2):
        # test s'il y a des pions entoures, puis s'il y a des pions alignes en xoox puis, xxxx
        if entoure_guerre_des_geoliers(pions[indice_joueur],pions[(indice_joueur+1)%len(pions)],grille) or\
                victoire(grille,(pions[indice_joueur],pions[(indice_joueur+1)%len(pions)],pions[(indice_joueur+1)%len(pions)],pions[indice_joueur]))\
                or victoire(grille,[pions[indice_joueur] for _ in range(4)]):
            #dans ce cas fin de la partie
            afficher_grille(grille)
            print(f"Le joueur {indice_joueur+1} remporte la victoire.\nFélicitation à toi !\nRetour au menu principal…")
            if tournoi_active:
                fin_de_partie_tournois(indice_joueur)
            fin_de_partie()
# ---------------------------------------------tournois---------------------------------------

def tournois():
    '''
        Tournois en cinq manche.
    '''
    global scores, tournoi_active, mode, parties, compteur_parties
    compteur_parties=0
    tournoi_active=True
    scores=[0,0]
    parties=ccs_entree("Chaque partie remportee raporte 1 points.\n\
Combien de parties voulez-vous jouez ?",int)
    mode="Menu"

def fin_de_partie_tournois(joueur):
    '''
        rajouteun point a qui le doit si on est en tournois
    '''
    global compteur_parties, scores
    if tournoi_active:
        scores[joueur]+=1
        print("Il gagne un point !")
        compteur_parties+=1
        input("Entree pour continuer.")

# ---------------------------------------------------------------------------------------------
while True:
    if mode=="Menu":
        menu()
    if mode=="Tournoi":
        tournois()
    if mode=="Morpion" :
        morpion()
    if mode=="Chenes contre Sapins":
        chene_contre_sapin()
    if mode=="Puissance Quatre":
        puissance_quatre()
    if mode=="La Guerre des Geoliers":
        guerre_des_geoliers()
