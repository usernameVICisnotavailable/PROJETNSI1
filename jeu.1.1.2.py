
def def_mode_morpion():
    '''Change la valeur de mode pour la définir comme celle du morpion : 1'''
    global mode # comme la valeur du mode va etre modifie
    mode=1

def def_mode_menu():
    '''Change la valeur de mode pour la définir comme celle du menu'''
    global mode # comme la valeur du mode va etre modifie
    mode=0

def test_mode_morpion():
    '''Test qui renvoit true ou False selon
la valeur de mode (mode=1 veut dire qu'on est en mode morpion)'''
    return mode==1

def test_mode_menu():
    '''Test qui renvoit true ou False selon
la valeur de mode (mode=0 veut dire qu'on est en mode menu)'''
    return mode==0
    
def menu():
    assert test_mode_menu() #vérifie qu'on est bien en mode menu
    global mode
    print("Menu :\n Jeux disponibles : \n-Morpion")
    while test_mode_menu():
        entree_jeu=str(input("Ecrivez le jeux auquel vous voulez jouer comme écrit ci-dessus."))
        if entree_jeu=="Morpion":
            def_mode_morpion()
        else:
            print("Veuillez renseignez un jeu existant.")

mode=0
menu()
