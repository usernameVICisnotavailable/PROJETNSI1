def test_morpion():
    ''' renvoie True ou False selon la valeur de la chaîne de caractère entrée_jeu'''
    return entrée_jeu=="Morpion"

def def_mode_morpion():
    global mode
    mode=1
    
def menu():
    print("Menu :\n Jeux disponibles : \n-Morpion")
    entrée_jeu=input("Ecrivez le jeux auquel vous voulez jouer comme écrit ci-dessus.")
    if testMorpion():
        

