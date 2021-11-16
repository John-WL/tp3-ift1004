from tp3.case import Case
from tp3.jeton import Jeton


class Plateau:
    """
    Cette classe représente un plateau de scrabble.
    Une partie de la logique du jeu sera implémentée ici donc lisez bien les spécifications de chaque méthode.
    
    Exemple:
             1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        A |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | A
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        B |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | B
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        C |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | C
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        D |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | D
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        E |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | E
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        F |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | F
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        G |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | G
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        H |    |    |    |    |    |    |    | ★  |    |    |    |    |    |    |    | H
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        I |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | I
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        J |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | J
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        K |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | K
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        L |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | L
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        M |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | M
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        N |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | N
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
        O |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | O
          +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
             1    2    3    4    5    6    7    8    9   10   11   12   13   14   15

    Attributes:
        dimension (int): La dimension (nombre de lignes et de colonnes) pour le plateau de scrabble. Dans notre cas, la
                         dimension sera toujours égale à 15.
        cases (list): Liste de liste de cases.
            Le programmeur peut avoir accès et manipuler les cases du plateau avec des index i et j, tels que
            0 <= i < Plateau.dimension et 0 <= i < Plateau.dimension.
            Pour vous aider un peu:
                * cases[i] vous retourne la i+1 ème ligne du plateau
                  (l'index i == 0 correspond donc à la première ligne, et ainsi de suite).
                * cases[i][j] vous donne la case au croisement de la i+1 ème ligne et de la j+1 ème colonne du plateau
                  (l'index j == 0 correspond donc à la première colonne, et ainsi de suite).

            L'utilisateur de la classe, désignera les cases grâce à un code au format « XY » où X représente une lettre
            comprise entre 'A' et 'O', et Y un nombre compris entre 1 et 15. Ex: K9, E15.
            - La lettre désigne une ligne: 'A' pour la 1ère ligne, B pour la seconde ligne, etc.
            - Le nombre désigne une colonne: 5 correspond à la 5ème colonne.
            Par exemple:
            - K9 permet de désigner la case à l'intersection de la 11ème ligne et de la 9ème colonne.
            - E15 permet de désigner la case à l'intersection de la 5ème ligne et 15ème colonne.
            Note: Vous pouvez vour servir du graphe ASCII plus haut pour une meilleure compréhension.
    """
    def __init__(self):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Constructeur d'un plateau.
        Pour compléter cette méthode vous devez vous référer à la configuration réelle d'un plateau de scrabble.
        Vous pouvez commencer par créer l'attribut cases en considérant qu'aucune case n'est spéciale.
        Regardez ensuite sur un vrai plateau de scrabble, quelles positions sont spéciales, créer ces cases spéciales et
        remplacez les anciennes cases.
        """
        self.dimension = 15

        self.cases = []
        for _ in range(self.dimension):
            ligne = []
            for _ in range(self.dimension):
                ligne.append(Case())
            self.cases.append(ligne)

        for (i, j) in [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]:
            self.cases[i][j] = Case(3, 'M')

        for (i, j) in [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13),
                       (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]:
            self.cases[i][j] = Case(3, 'L')

        for i in [1, 2, 3, 4]:
            self.cases[i][i] = Case(2, 'M')
            self.cases[i][self.dimension - i - 1] = Case(2, 'M')
            self.cases[self.dimension - i - 1][self.dimension - i - 1] = Case(2, 'M')
            self.cases[self.dimension - i - 1][i] = Case(2, 'M')

        for i, j in [(1, 1), (4, 0), (0, 4), (5, 1), (1, 5), (7, 4)]:
            self.cases[7 - i][7 - j] = Case(2, 'L')
            self.cases[7 + i][7 - j] = Case(2, 'L')
            self.cases[7 - i][7 + j] = Case(2, 'L')
            self.cases[7 + i][7 + j] = Case(2, 'L')
        self.cases[7][7] = Case(2, 'M')

    def code_position_est_valide(self, code):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Méthode permettant de valider si un code de positionnement sur le tableau est valide ou pas.

        Args:
            code (str): Chaîne au format « XY » ou « xy » représentant un 
            code de positionnement.

        Returns:
            bool: True si le code passé en argument est un code de positionnement au format « XY » ou « xy » valide,
                  False sinon.
        """
        code = code.upper()
        valide = 2 <= len(code) <= 3 and code[0].isalpha() and code[1:].isdigit()
        if valide:
            index_ligne = ord(code[0]) - ord('A')
            index_colonne = int(code[1:]) - 1
            return 0 <= index_ligne < self.dimension and 0 <= index_colonne < self.dimension
        return False

    def decode_position(self, code):
        """
        Méthode servant à transformer un code de positionnement sur
        le plateau en index d'accès de ligne et de colonne sur le plateau.

        Args:
            code (str): Chaîne au format « XY » ou « xy » représentant un 
            code de positionnement.

        Returns:
            int: Index de la ligne
            int: Index de la colonne

        Raises:
            AssertionError: Si le code de la position est invalide.
        """
        assert self.code_position_est_valide(code), 'Code position invalide.'
        code = code.upper()
        index_ligne = ord(code[0]) - ord('A')
        index_colonne = int(code[1:]) - 1
        return index_ligne, index_colonne

    def case_est_vide(self, position_code):
        """
        Permet de déterminer si une case est vide, c'est-à-dire qu'elle ne
        contient pas de jeton.

        Args:
            position_code (str): code de positionnement de la case sur le plateau (au format « XY » ou « xy »). Pensez à
                                réutiliser Plateau.decode_position.

        Returns:
            bool: True si la case est vide, False sinon.
                  Rappelez-vous qu'il existe une méthode est_vide disponible pour les objets de type Case.
        """
        # TODO: À compléter
        # Mettre votre code ici
        position_en_2d = self.decode_position(position_code)
        index_ligne = position_en_2d[0]
        index_colonne = position_en_2d[1]
        case = self.cases[index_ligne][index_colonne]
        return case.est_vide()

    def est_vide(self):
        """
        Permet de déterminer si le plateau est vide, c'est à dire que toutes les cases sont vides.

        Returns:
            bool: True si le plateau est vide, False sinon.
        """
        # TODO: À compléter
        # Mettre votre code ici
        return all([case.est_vide() for ligne in self.cases for case in ligne])

    def ajouter_jeton(self, jeton, position_code):
        """
        Permet d'ajouter un jeton dans une case vide du plateau.
        La case est indiquée grâce à son code de positionnement.

        Args:
            jeton (Jeton): Le jeton à ajouter sur le plateau.
            position_code (str): La position où ajouter (au format « XY » ou « xy »)


        Returns:
            bool: True si le jeton a été placé avec succès;
                False sinon (si la case est déjà occupée).
        """
        # TODO: À compléter
        # Mettre votre code ici
        position_en_2d = self.decode_position(position_code)
        index_ligne = position_en_2d[0]
        index_colonne = position_en_2d[1]
        case = self.cases[index_ligne][index_colonne]
        return case.placer_jeton(jeton)

    def retirer_jeton(self, position_code):
        """
        Permet d'enlever le jeton dans une case du plateau.
        La case est indiquée grâce à son code de positionnement.

        Args:
            position_code (str): La position où enlever le jeton (au format « XY » ou « xy »).

        Returns:
             Jeton: Le jeton retiré du plateau, ou None si la case est vide.
                    Rappelez-vous qu'il existe une méthode retirer_jeton disponible 
                    pour les objets de type Case.
        """
        # TODO: À compléter
        # Mettre votre code ici
        position_en_2d = self.decode_position(position_code)
        index_ligne = position_en_2d[0]
        index_colonne = position_en_2d[1]
        case = self.cases[index_ligne][index_colonne]
        return case.retirer_jeton()

    def cases_adjacentes_occupees(self, position_code):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Étant donné une position, cette méthode permet de voir si au moins 
        l'une de ses positions voisines est occupée.
        Les cases voisines sont les cases juste en haut, en bas, à gauche 
        et à droite de la case concernée.
        NB: Les cases voisines diagonales ne comptent pas.

        Args:
            position_code (str): La position d'intérêt.

        Returns:
            bool: True si au moins l'une des cases voisines est occupée,
                  False si aucune case voisine n'est occupée.
        """
        index_ligne, index_colonne = self.decode_position(position_code)
        voisins = [(index_ligne, index_colonne - 1), (index_ligne, index_colonne + 1),
                   (index_ligne + 1, index_colonne), (index_ligne - 1, index_colonne)]
        voisins = [(i, j) for i, j in voisins if (0 <= i < self.dimension) and (0 <= j < self.dimension)]
        return any([not self.cases[i][j].est_vide() for (i, j) in voisins])

    def valider_positions_avant_ajout(self, positions_codes):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Cette méthode implémente certaines règles du jeu donc soyez attentifs au texte ci-dessous.
        Étant donné des positions_codes où un utilisateur veut placer ses jetons, cette méthode permet de valider s'il
        peut réelement ajouter les jetons à ces positions.
        
        Les positions sont valides si:
         - elles sont toutes vides;
         - elles sont toutes sur la même ligne ou la même colonne;
         - une fois qu'elles seront placées sur une même ligne ou une même colonne, elles formeront un mot et pas plus
           sur cette même ligne ou colonne. Ici, le mot formé n'est pas important du tout donc on n'essaie pas de le
           valider. Par exemple, si toutes les positions sont sur la ligne 5, le code s'assure simplememt
           qu'entre les positions où l'on doit ajouter des jetons, des cases ne sont vides.
         - si le plateau est vide, le centre du plateau doit être dans les positions;
         - sinon, au moins une des positions doit être adjacente à une des cases occupées du plateau.

        Args:
            positions_codes (list): liste de chaînes de caractères (str) représentant les positions où on veut ajouter
                                    des jetons.

        Returns:
            bool: True si les positions sont valides, False sinon.
        """
        positions_decodees = [self.decode_position(p) for p in positions_codes]
        lignes, cols = zip(*positions_decodees)
        lignes, cols = list(set(lignes)), list(set(cols))
        meme_ligne, meme_col = len(lignes) == 1, len(cols) == 1
        valide = meme_ligne or meme_col
        valide = valide and all([self.case_est_vide(p) for p in positions_codes])
        if valide:
            if self.est_vide():
                valide = (7, 7) in positions_decodees
            else:
                valide = any([self.cases_adjacentes_occupees(pos) for pos in positions_codes])

            if valide and meme_ligne:
                ligne, n, m = lignes[0], min(cols), max(cols)
                valide = all([(not self.cases[ligne][i].est_vide()) for i in range(n, m + 1) if i not in cols])
            elif valide and meme_col:
                col, n, m = cols[0], min(lignes), max(lignes)
                valide = all([(not self.cases[i][col].est_vide()) for i in range(n, m + 1) if i not in lignes])

        return valide

    def placer_mots(self, jetons_a_ajouter, position_codes):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Permet de placer plusieurs jetons sur le plateau afin de former un 
        ou plusieurs mots.
        Pensez à réutiliser valider_positions_avant_ajout.

        Args:
            jetons_a_ajouter (list): Jetons à ajouter pour placer nos mots (instances de la classe Jeton).
            position_codes (list): Liste de chaînes de caractères (str) représentant les positions où placer les jetons.

        Returns:
            list: Liste des mots (str) formés avec les jetons si l'ajout a été fait, liste vide sinon.
            int: Points obtenus si l'ajout a été fait, 0 sinon.

        Raises:
            AssertionError:
                - Si le nombre de jetons à ajouter est différent du nombre de positions fournies.
                - Si les positions sont invalides.
        """
        assert len(jetons_a_ajouter) == len(position_codes), 'Le nombre de jetons est différent du nombre de positions.'
        assert self.valider_positions_avant_ajout(position_codes), "Les positions pour l'ajout sont invalides."

        for i in range(len(jetons_a_ajouter)):
            self.ajouter_jeton(jetons_a_ajouter[i], position_codes[i])

        mots, score = self.mots_score_obtenus(position_codes)
        return mots, score

    def mots_score_obtenus(self, nouvelles_positions):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Trouver les mots ajoutés et le score total obtenu lorsque le joueur 
        vient juste d'ajouter des jetons aux positions de la liste en argument.

        Args:
            nouvelles_positions (list): Liste de chaînes de caractères (str) représentant les dernières positions où des
                                        jetons ont été ajoutés.
        Returns
            list: Liste de tous les mots (str) formés par l'ajout de jetons aux nouvelles positions.
            int: Somme des points obtenus par l'ajout de ces mots.
        """
        positions_decodees = [self.decode_position(p) for p in nouvelles_positions]
        score_total = 0
        lignes, cols = zip(*positions_decodees)
        mots = []
        for ligne in set(lignes):
            lmots, score = self.mots_et_score_sur_ligne_ou_colonne(nouvelles_positions, ligne=ligne)
            mots += lmots
            score_total += score
        for col in set(cols):
            lmots, score = self.mots_et_score_sur_ligne_ou_colonne(nouvelles_positions, colonne=col)
            mots += lmots
            score_total += score
        return mots, score_total

    def mots_et_score_sur_ligne_ou_colonne(self, nouvelles_positions, ligne=None, colonne=None):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Permet de trouver les mots sur une ligne ou une colonne et le score associé.

        Args:
            nouvelles_positions (list): Liste de chaînes de caractères (str) représentant les dernières positions où des
                                        jetons ont été ajoutés.

            ligne (int, optionnel): Index de la ligne d'intérêt
            colonne: (int, optionnel): Index de la colonne d'intérêt

        Returns:
            list: La liste des mots (str) trouvés sur la ligne ou la colonne.
            int: Score total. 

            Plus précisément la liste devra contenir au maximum un élément car un tout nouvel ajout de jetons ne peut
            pas créer plus d'un mot sur la même ligne ou colonne.

        Raises:
            AssertionError: Si la ligne et la colonne sont spécifiées ou aucun des deux ne l'est. Pour les curieux(ses),
                            il s'agit d'un OU Exclusif (XOR): https://fr.wikipedia.org/wiki/Fonction_OU_exclusif).
        """
        assert (ligne is None) ^ (colonne is None), 'Précisez seulement la ligne ou la colonne, pas les deux.'

        positions_decodees = [self.decode_position(p) for p in nouvelles_positions]
        mots, score_total = [], 0
        mot, score_mot, multiplicateur, pos_mot = '', 0, 1, []
        for i in range(self.dimension):
            pos = (ligne, i) if ligne is not None else (i, colonne)
            case = self.cases[pos[0]][pos[1]]
            if case.est_vide():
                if len(mot) > 1 and any([p in pos_mot for p in positions_decodees]):
                    mots.append(mot)
                    score_total += score_mot * multiplicateur
                mot, score_mot, multiplicateur, pos_mot = '', 0, 1, []
            else:
                mot += case.lettre_jeton()
                pos_mot.append(pos)
                if pos in positions_decodees and case.effet == 'L':
                    score_mot += case.valeur_jeton() * case.multiplicateur
                else:
                    score_mot += case.valeur_jeton()
                if pos in positions_decodees and case.effet == 'M':
                    multiplicateur *= case.multiplicateur
        if len(mot) > 1 and any([p in pos_mot for p in positions_decodees]):
            mots.append(mot)
            score_total += score_mot * multiplicateur

        return mots, score_total

    def __str__(self):
        """
        *** Vous n'avez pas à coder cette méthode. ***
        
        Formatage du plateau pour l'affichage.
        Utilise des codes Unicode, ce qui pourrait causer des problèmes avec le système d'exploitation utilisé par
        certains. Écrivez-nous sur le forum si cela vous arrive!

        Returns:
            str: Chaîne de caractères représentant un tableau.
        """
        ligne_separation = '  +' + '----+' * self.dimension + '\n'
        chaine = '   '
        for colonne in range(self.dimension):
            chaine += "{:^5d}".format(colonne+1)
        chaine += '\n'
        chaine += ligne_separation
        for rangee in range(self.dimension):
            chaine += '{} |'.format(chr(ord('A')+rangee))
            for colonne in range(self.dimension):
                if rangee == colonne and rangee == 7 and self.cases[rangee][colonne].est_vide():
                    s = '\x1b[0;30;{}m{:^4s}\x1b[0m'.format(self.cases[rangee][colonne].code_couleur(), '\u2605')
                else:
                    s = '{:^4s}'.format(str(self.cases[rangee][colonne]))
                chaine += s + '|'
            chaine += ' {}\n'.format(chr(ord('A') + rangee))
            chaine += ligne_separation
        chaine += '   '
        for colonne in range(self.dimension):
            chaine += "{:^5d}".format(colonne+1)
        chaine += '\n'
        return chaine


if __name__ == '__main__':
    # À titre indicatif, vous pouvez exécuter ce fichier pour afficher 
    # un plateau vide dans la console.
    # Vous pouvez aussi écrire du code pour tester vos méthodes ici.
    plateau = Plateau()
    print(plateau)
