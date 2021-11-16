import pickle
from pathlib import Path
from random import randint, shuffle

from tp3.joueur import Joueur
from tp3.plateau import Plateau
from tp3.jeton import Jeton


BASE_DIR = Path(__file__).resolve().parent


class Scrabble:
    """
    Classe Scrabble qui implémente aussi une partie de la logique de jeu.

    Attributes:
        dictionnaire (list): Contient tous les mots qui peuvent être joués sur dans cette partie.
                             (afin de savoir si un mot est permis, on va vérifier s'il est dans dictionnaire)
        plateau (Plateau): Un objet de la classe Plateau. On y place des jetons et il nous dit le nombre de points
                           gagnés.
        jetons_libres (list): La liste de tous les jetons dans le sac (instances de la classe Jeton), c'est là que
                              chaque joueur pige des jetons quand il en a besoin.
        joueurs: (list): L'ensemble des joueurs de la partie (instances de la classe Joueur)
        joueur_actif (Joueur): Le joueur qui est en train de jouer le tour en cours. Si aucun joueur alors None.
    """
    def __init__(self, nb_joueurs, langue='fr'):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Étant donné un nombre de joueurs et une langue, le constructeur crée une partie de scrabble.

        Pour une nouvelle partie de scrabble:
        - Un nouvel objet Plateau est créé;
        - La liste des joueurs est créée et chaque joueur porte automatiquement le nom Joueur 1, Joueur 2, ... Joueur n,
          où n est le nombre de joueurs;
        - Le joueur_actif est None.

        Args:
            nb_joueurs (int): nombre de joueurs de la partie (au minimun 2 au maximum 4).
            langue (str): 'FR' pour la langue française et 'EN' pour la langue anglaise. Charge en mémoire les mots
                          contenus dans le fichier "dictionnaire_francais.txt" ou "dictionnaire_anglais.txt".
            La langue détermine aussi les jetons de départ.
            Voir https://fr.wikipedia.org/wiki/Lettres_du_Scrabble
            Note: Dans notre scrabble, nous n'utiliserons pas les jetons blancs (jokers) qui ne contiennent aucune lettre.

        Raises:
            AssertionError:
                - Si la langue n'est ni 'fr', 'FR', 'en', ou 'EN'.
                - Si le nombre de joueurs n'est pas compris entre 2 et 4 (2 et 4 étant inclus).
        """
        assert langue.upper() in ['FR', 'EN'], 'Langue non supportée.'
        assert 2 <= nb_joueurs <= 4, 'Il faut entre 2 et 4 personnes pour jouer.'

        self.plateau = Plateau()
        self.joueur_actif = None
        self.joueurs = [Joueur(f'Joueur {i + 1}') for i in range(nb_joueurs)]

        if langue.upper() == 'FR':
            # Infos disponibles sur https://fr.wikipedia.org/wiki/Lettres_du_Scrabble
            data = [('E', 15, 1), ('A', 9, 1), ('I', 8, 1), ('N', 6, 1), ('O', 6, 1),
                    ('R', 6, 1), ('S', 6, 1), ('T', 6, 1), ('U', 6, 1), ('L', 5, 1),
                    ('D', 3, 2), ('M', 3, 2), ('G', 2, 2), ('B', 2, 3), ('C', 2, 3),
                    ('P', 2, 3), ('F', 2, 4), ('H', 2, 4), ('V', 2, 4), ('J', 1, 8),
                    ('Q', 1, 8), ('K', 1, 10), ('W', 1, 10), ('X', 1, 10), ('Y', 1, 10),
                    ('Z', 1, 10)]
            chemin_fichier_dictionnaire = BASE_DIR / 'dictionnaire_francais.txt'
        elif langue.upper() == 'EN':
            # Infos disponibles sur https://fr.wikipedia.org/wiki/Lettres_du_Scrabble
            data = [('E', 12, 1), ('A', 9, 1), ('I', 9, 1), ('N', 6, 1), ('O', 8, 1),
                    ('R', 6, 1), ('S', 4, 1), ('T', 6, 1), ('U', 4, 1), ('L', 4, 1),
                    ('D', 4, 2), ('M', 2, 3), ('G', 3, 2), ('B', 2, 3), ('C', 2, 3),
                    ('P', 2, 3), ('F', 2, 4), ('H', 2, 4), ('V', 2, 4), ('J', 1, 8),
                    ('Q', 1, 10), ('K', 1, 5), ('W', 2, 4), ('X', 1, 8), ('Y', 2, 4),
                    ('Z', 1, 10)]
            chemin_fichier_dictionnaire = BASE_DIR / 'dictionnaire_anglais.txt'

        self.jetons_libres = [Jeton(lettre, valeur) for lettre, occurences, valeur in data]
        with open(chemin_fichier_dictionnaire, 'r') as f:
            self.dictionnaire = [x[:-1].upper() for x in f.readlines() if len(x[:-1]) > 1]

    def mot_permis(self, mot):
        """
        Permet de savoir si un mot est permis dans la partie ou pas 
        en vérifiant dans le dictionnaire.

        Args:
            mot (str): Mot à vérifier.

        Returns:
            bool: True si le mot est dans le dictionnaire, False sinon.
        """
        # TODO: À compléter
        # Mettre votre code ici

        # Idéalement, pour rechercher un mot dans une liste qui peut contenir des centaines de milliers de
        # mots, on ne voudrait pas faire une recherche en O(N). Si jamais on avait envie d'implémenter
        # un algorithme qui utilisait cette fonction ~N^2 fois, le temps d'exécution pourrait devenir ridicule.

        # C'est pourquoi on devrait utiliser une hashmap, par exemple, ou une représentation de donnée similaire pour
        # accèder aux mots. Ça permettrait de faire des opérations avec le dictionnaire en O(1).
        # Par contre, puisqu'on ne peut pas non-plus changer les attributs, ni en ajouter de nouveaux, l'utilisation
        # d'une hashmap n'est en fait pas une option dans le cadre du tp #3.

        # Pour une liste, la solution est donc de faire une recherche binaire (qui a une complexité
        # de O(log(N)) dans le pire des cas).

        # On commence par chercher au milieu de la liste, et on sépare la liste en deux sections différentes à
        # chercher. Si on est trop loin dans la liste, on cherche au milieu de la première moitié. Si on n'est pas
        # assez loin, on cherche dans la deuxième moitié. Ensuite, on sépare encore la moitié choisie en deux,
        # et on recommence ce procédé jusqu'à tomber sur une séparation d'un seul élément.

        # Si l'élément qu'on cherche correspond à cet élément, l'élément est présent dans la liste. Sinon,
        # il n'est pas présent.
        # Cet algorithme assume donc que la liste est ordonnée en ordre alphabétique (ce qui semble être le cas si on
        # jette un coup d'oeil aux fichiers des dictionnaires).
        mot_potentiel = ''
        diviseur = len(self.dictionnaire)
        index_liste = 0

        while diviseur > 0:
            diviseur /= 2
            if mot > mot_potentiel:
                index_liste += diviseur
            else:
                index_liste -= diviseur

            index_entier = int(index_liste)
            mot_potentiel = self.dictionnaire[index_entier]

            # Si on a assez cherché, ou si on a déjà trouvé le mot dans la liste, on sort de la boucle.
            if diviseur < 1 or mot == mot_potentiel:
                break

        return mot_potentiel == mot

    def determiner_gagnant(self):
        """
        Détermine le joueur gagnant.
        Le joueur gagnant doit avoir un pointage supérieur ou égal à celui des autres.

        Returns:
            Joueur: Le joueur gagnant. Si plusieurs sont à égalité, on en retourne un seul parmi ceux-ci.
        """
        # TODO: À compléter
        # Mettre votre code ici
        joueur_gagnant = self.joueurs[0]
        meilleurs_points = joueur_gagnant.points

        for joueur in self.joueurs:
            if joueur.points > meilleurs_points:
                joueur_gagnant = joueur
                meilleurs_points = joueur.points

        return joueur_gagnant

    def partie_terminee(self):
        """
        Vérifie si la partie est terminée. Une partie est terminée si il n'existe plus de jetons libres ou il reste
        moins de deux (2) joueurs. C'est la règle que nous avons choisi d'utiliser pour ce travail, donc essayez de
        négliger les autres que vous connaissez ou avez lu sur Internet.

        Returns:
            bool: True si la partie est terminée, et False autrement.
        """
        # TODO: À compléter
        # Mettre votre code ici
        if len(self.joueurs) < 2:
            return True
        if len(self.jetons_libres) == 0:
            return True
        return False

    def joueur_suivant(self):
        """
        Change le joueur actif.
        Le nouveau joueur actif est celui à l'index du (joueur courant + 1) % nb_joueurs.
        Si on n'a aucun joueur actif, on détermine au hasard le suivant.
        """
        # TODO: À compléter
        # Mettre votre code ici
        joueur_actif_n_est_pas_determine = self.joueur_actif is None

        if joueur_actif_n_est_pas_determine:
            index_joueur_max = len(self.joueurs)-1
            index_de_joueur_au_hasard = randint(0, index_joueur_max)
            self.joueur_actif = self.joueurs[index_de_joueur_au_hasard]
        else:
            nombre_de_joueurs = len(self.joueurs)
            ancien_index_de_joueur = self.joueurs.index(self.joueur_actif)
            nouvel_index_de_joueur = (ancien_index_de_joueur + 1) % nombre_de_joueurs
            self.joueur_actif = self.joueurs[nouvel_index_de_joueur]

    def tirer_jetons(self, n):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Simule le tirage de n jetons du sac à jetons et renvoie ceux-ci. Il s'agit de prendre au hasard des jetons dans
        self.jetons_libres et de les retourner.

        Args:
            n (int): Le nombre de jetons à tirer.

        Returns:
            list: La liste des jetons tirés (instances de la classe Jeton).

        Raises:
            AssertionError: Si n n'est pas compris dans l'intervalle [0, nombre total de jetons libres].
        """
        assert 0 <= n <= len(self.jetons_libres), 'n doit être compris entre 0 et le nombre total de jetons libres.'
        shuffle(self.jetons_libres)
        res = self.jetons_libres[:n]
        self.jetons_libres = self.jetons_libres[n:]
        return res

    def demander_positions(self):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Demande à l'utilisateur d'entrer les positions sur le chevalet et le plateau pour jouer son coup.
        Si les positions entrées sont valides, on retourne les listes de ces positions. On redemande tant que
        l'utilisateur ne donne pas des positions valides.

        Returns:
            list: Positions du chevalet. Plus précisement il s'agit des index (int) de ces positions.
            list: Positions codées du plateau.
        """    
        valide = False
        while not valide:
            input_pos_chevalet = input('Entrez les positions du chevalet à jouer séparées par un espace: ').upper().strip()
            pos_chevalet = [int(x) - 1 for x in input_pos_chevalet.split(' ')]
            valide = all([self.joueur_actif.position_est_valide(pos) for pos in pos_chevalet])

        valide = False
        while not valide:
            input_pos_plateau = input('Entrez les positions de chacune de ces lettres séparées par un espace: ').upper().strip()
            pos_plateau = input_pos_plateau.split(' ')
    
            if len(pos_chevalet) != len(pos_plateau):
                print('Les nombres de jetons et de positions ne sont pas les mêmes.')
                valide = False
            else:
                valide = self.plateau.valider_positions_avant_ajout(pos_plateau)

        return pos_chevalet, pos_plateau

    def jouer_un_tour(self):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Faire jouer à un des joueurs son tour entier, jusqu'à ce qu'il place un mot valide sur le plateau.

        Actions possibles:
        1 - Afficher le plateau puis le joueur;
        2 - Demander les positions à jouer;
        3 - Retirer les jetons du chevalet;
        4 - Valider si les positions sont valides pour un ajout sur le plateau;
        5 - Si oui, placer les jetons sur le plateau, sinon retourner en 1;
        6 - Si tous les mots formés sont dans le dictionnaire, alors ajouter les points au joueur actif;
        7 - Sinon retirer les jetons du plateau et les remettre sur le chevalet du joueur, puis repartir en 1;
        8 - Afficher le plateau.
        """
        print(self.plateau)
        print(self.joueur_actif)
        valide = False
        while not valide:
            pos_chevalet, pos_plateau = self.demander_positions()
            jetons = [self.joueur_actif.retirer_jeton(p) for p in pos_chevalet]

            mots, score = self.plateau.placer_mots(jetons, pos_plateau)
            if any([not self.mot_permis(m) for m in mots]):
                print("Au moins l'un des mots formés est absent du dictionnaire.")
                for pos in pos_plateau:
                    jeton = self.plateau.retirer_jeton(pos)
                    self.joueur_actif.ajouter_jeton(jeton)
                valide = False
            else:
                print('Mots formés:', mots)
                print('Score obtenu:', score)
                self.joueur_actif.ajouter_points(score)
                valide = True

        print(self.plateau)

    def changer_jetons(self):
        """
        Faire changer au joueur actif les jetons de son chevalet de son choix. La méthode doit demander au joueur de
        saisir les positions à changer les unes après les autres séparés par un espace.
        Si une position est invalide (utilisez self.joueur_actif.position_est_valide), alors redemander.
        Dès que toutes les positions valides les retirer du chevalet du joueur et lui en donner de nouveau.
        Enfin, on remet des jetons pris chez le joueur parmi les jetons libres.
        """
        # TODO: À compléter
        # Mettre votre code ici
        positions = []
        chaine_changement = input('Entrez la position des lettres de votre chevalet que vous voudriez changer.\n'
                                  '\x1B[3mNote: les positions doivent être comprises \033[4mentre 1 et 7\033[0m, '
                                  'et elles doivent être séparées par \033[4mdes espaces\033[0m\x1B[0m.\n'
                                  'Positions des lettres à changer: ')
        entree_valide = False
        while not entree_valide:
            # On assume que l'entrée est valide, et si on trouve qu'elle était en fait invalide, on met à jour la
            # variable 'entree_valide' à faux, et on demande à nouveau les positions au joueur.
            entree_valide = True
            try:
                positions_en_string = chaine_changement.split()
                for position_en_caractere in positions_en_string:
                    position = int(position_en_caractere) - 1
                    positions.append(position)
                    la_position_est_valide = self.joueur_actif.position_est_valide(position)
                    if not la_position_est_valide:
                        entree_valide = False
            except ValueError:
                entree_valide = False
            if not entree_valide:
                positions.clear()
                chaine_changement = input('\n'
                                          'Les positions entrées sont incorrectes.\n' 
                                          'Entrez les positions des lettres à changer: ')

        liste_de_jetons_retires = []
        for position_a_changer in positions:
            jeton_retire = self.joueur_actif.retirer_jeton(position_a_changer)
            liste_de_jetons_retires.append(jeton_retire)
            index_nouveau_jeton_max = len(self.jetons_libres)-1
            index_nouveau_jeton = randint(0, index_nouveau_jeton_max)
            nouveau_jeton = self.jetons_libres[index_nouveau_jeton]
            self.jetons_libres.remove(nouveau_jeton)
            self.joueur_actif.ajouter_jeton(nouveau_jeton)
        self.jetons_libres.extend(liste_de_jetons_retires)

    def jouer(self):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Cette fonction permet de jouer la partie.
        Tant que la partie n'est pas terminée, on joue un tour.
        
        À chaque tour :
            - On change le joueur actif et on lui affiche que c'est son tour. ex: Tour du joueur 2.
            - On lui affiche ses options pour qu'il choisisse quoi faire:
            "Entrez (j) pour jouer, (p) pour passer votre tour, (c) pour changer certains jetons, (s) pour sauvegarder
             ou (q) pour quitter"
            Notez que si le joueur fait juste sauvegarder on ne doit pas passer au joueur suivant mais dans tous les
            autres cas on doit passer au joueur suivant. S'il quitte la partie on l'enlève de la liste des joueurs.
        
        Une fois la partie terminée, on félicite le joueur gagnant!
        """
        abandon = False
        changer_joueur = True
        while not self.partie_terminee() and not abandon:
            debut = self.joueur_actif is None
            if changer_joueur:
                self.joueur_suivant()
            if debut:
                print(f'Le premier joueur sera: {self.joueur_actif.nom}.')

            for jeton in self.tirer_jetons(self.joueur_actif.nb_a_tirer()):
                self.joueur_actif.ajouter_jeton(jeton)

            print(f'Tour du {self.joueur_actif.nom}.')
            choix = input('Entrez (j) pour jouer, (p) pour passer votre tour,\n'
                          '(c) pour changer certains jetons, (s) pour sauvegarder\n'
                          'ou (q) pour quitter: ').strip().lower()
            if choix == 'j':
                self.jouer_un_tour()
                changer_joueur = True
            elif choix == 'p':
                changer_joueur = True
            elif choix == 'c':
                self.changer_jetons()
                changer_joueur = True
            elif choix == 'q':
                quitter = self.joueur_actif
                self.joueur_suivant()
                self.joueurs.remove(quitter)
                changer_joueur = False
            elif choix == 's':
                valide = False
                while not valide:
                    nom_fichier = input('Nom du fichier de sauvegarde: ')
                    valide = self.sauvegarder_partie(nom_fichier)
                changer_joueur = False
            else:
                raise Exception('Choix invalide.')

        if self.partie_terminee():
            print('Partie terminée.')
            print(f'{self.determiner_gagnant().nom} est le gagnant.')

    def sauvegarder_partie(self, nom_fichier):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Permet de sauvegarder l'objet courant dans le fichier portant le nom spécifié.
        La sauvegarde se fera grâce à la fonction dump du module pickle.

        Args:
            nom_fichier (str): Nom du fichier qui contient un objet scrabble.

        Returns:
            bool: True si la sauvegarde s'est bien déroulée,
                  False si une erreur est survenue durant la sauvegarde.
        """
        try:
            with open(nom_fichier, 'wb') as f:
                pickle.dump(self, f)
        except:
            return False
        return True


def charger_partie(nom_fichier):
    """ 
    *** Vous n'avez pas à coder cette fonction. ***
    
    Fonction permettant de créer un objet scrabble en lisant le fichier dans lequel l'objet avait été sauvegardé
    précédemment.

    Args:
        nom_fichier (str): Nom du fichier qui contient un objet scrabble.

    Returns
        Scrabble: L'objet chargé en mémoire.
    """
    with open(nom_fichier, 'rb') as f:
        return pickle.load(f)
