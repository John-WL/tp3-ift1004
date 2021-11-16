from random import seed
from tp3.scrabble import Scrabble, charger_partie


##############################################################################
# Programme principal.
# Vous n'avez pas à coder cela. Vous pouvez le modifier pour faire des tests,
# mais remettez votre TP avec la version originale de ce fichier.
##############################################################################


if __name__ == '__main__':
    # Nous fixons ici la valeur du seed, afin de vous aider à avoir 
    # quelque chose de prévisible lors de vos tests.
    seed(42)

    print('*'*80)
    print('{:^80}'.format('Bienvenue dans IFT-1004 Scrabble'))
    print('*'*80)

    choix = ''
    while choix not in ['n', 'o']:
        choix = input('Entrez (n) pour commencer une nouvelle partie \n'
                      'ou (o) pour ouvrir une partie déja existante: ').strip().lower()
    if choix == 'n':
        valide = False
        while not valide:
            try:
                nb_joueurs = int(input('Veuillez entrer le nombre de joueurs (min=2, max=4): '))
                if 2 <= nb_joueurs <= 4:
                    valide = True
            except:
                print('Vous devez entrer un entier.')

        valide = False
        while not valide:
            langue = input('Veuillez sélectionner la langue(français=fr, anglais=en): ')
            if langue in ['en', 'fr']:
                valide = True
            else:
                print("Nous n'avons pas pu détecter la langue.")

        scrabble = Scrabble(nb_joueurs, langue)
        scrabble.jouer()
    else:
        valide = False
        while not valide:
            try:
                fichier = input('Entrez le nom du fichier à ouvrir: ')
                scrabble = charger_partie(fichier)
                valide = True
            except:
                valide = False
        scrabble.jouer()
