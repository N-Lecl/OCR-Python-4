class Match:
    """
    Représente un match d'échecs
    """

    NUMERO_MATCH = 1  # Numéro de match initialisé à 1, partagé par toutes les instances de Match

    def __init__(self, nom_match=None, joueur_1=None, joueur_2=None):
        """
        Initialise une instance de Match
        :param nom_match: nom du match
        :type nom_match: str
        :param joueur_1: L'objet joueur 1
        :type joueur_1: obj [Joueur]
        :param joueur_2: L'objet joueur 2
        :type joueur_2: obj [Joueur]
        """
        self.nom_match = nom_match  # Initialise le nom du match
        self.joueur_1 = joueur_1  # Initialise le joueur 1
        self.joueur_2 = joueur_2  # Initialise le joueur 2

    def __str__(self):
        """
        Méthode spéciale pour obtenir une représentation en chaîne d'un objet Match.

        Returns:
            str: Une chaîne représentant les détails du match à jouer, y compris les noms complets des deux joueurs.
        """
        return (
            f"Match à jouer: {self.joueur_1.nom_famille}"  # Affiche le nom de famille du joueur 1
            f" {self.joueur_1.prenom} "  # Affiche le prénom du joueur 1
            f"VS {self.joueur_2.nom_famille} {self.joueur_2.prenom}"  # Affiche le nom et le prénom du joueur 2
        )

    def __repr__(self):
        """
        Méthode spéciale pour obtenir une représentation en chaîne de l'objet Match.
        """
        return str(self)  # Renvoie la représentation en chaîne de l'objet Match
