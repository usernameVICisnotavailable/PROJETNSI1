print(len("ඞ"))
def sous_test_aligne(x,y,tuple_alignement,deltax,deltay):
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
