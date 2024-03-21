from view import main_view
from models import model_match


class Tour:
    """
    Représente un tour de tournoi
    """

    def __init__(
        self, nom_tour=None, date_debut=None, date_fin=None, liste_matchs_termines=None
    ):
        """
        Initialise une instance de Tour.
        :param nom_tour: nom du tour
        :type nom_tour: str
        :param date_debut: date et heure de début du tour
        :type date_debut: str
        :param date_fin: date et heure de fin du tour
        :type date_fin: str
        :param liste_matchs_termines: liste des matchs terminés du tour
        :type liste_matchs_termines: list
        """
        self.nom_tour = nom_tour  # Initialise le nom du tour
        self.date_debut = date_debut  # Initialise la date de début du tour
        self.date_fin = date_fin  # Initialise la date de fin du tour
        self.liste_matchs_termines = liste_matchs_termines  # Initialise la liste des matchs terminés du tour
        self.liste_tours = []  # Initialise la liste des tours

    def __str__(self):
        """
        Méthode spéciale pour obtenir une représentation en chaîne d'un objet Tour.

        Returns:
            str: Une chaîne représentant les détails du tour.
        """
        return (
            f"----Tour: {self.nom_tour}----,\n"
            f"Date de début: {self.date_debut},\n"
            f"Date de fin: {self.date_fin}\n"
        )

    def __repr__(self):
        """
        Méthode spéciale pour obtenir une représentation en chaîne de l'objet Tour.
        """
        return str(self)

    def creer_instance_tour(self, tour_sauve):
        """
        Méthode d'instanciation de tour à partir de données texte
        :param tour_sauve: dictionnaire contenant les informations d'un tour
        :type tour_sauve: dict
        :return: un Tour
        :rtype: object Tour
        """
        # Crée une nouvelle instance de Tour avec les informations sauvegardées
        nom = tour_sauve["Nom"]
        date_debut = tour_sauve["Debut"]
        date_fin = tour_sauve["Fin"]
        liste_matchs_termines = tour_sauve["Liste matchs termines"]
        return Tour(nom, date_debut, date_fin, liste_matchs_termines)

    def serialise(self):
        """
        Méthode de sérialisation du modèle tour
        :return dictionnaire contenant les informations d'un tour
        :rtype: dict
        """
        # Sérialise les informations du tour
        tour_serialise = {
            "Nom": self.nom_tour,
            "Debut": self.date_debut,
            "Fin": self.date_fin,
            "Liste matchs termines": self.liste_matchs_termines,
        }
        return tour_serialise

    def lancer_tour(self, liste_joueurs_trie, tournoi_obj):
        """
        Méthode de contrôle du tour avec entrée des résultats de matchs
        :param tournoi_obj: objet Tournoi
        :type tournoi_obj: Tournoi
        :param liste_joueurs_trie: liste d'objets joueur
        :type liste_joueurs_trie: list
        :return: un Tour
        :rtype: object Tour
        """
        # Initialise et lance le tour
        self.nom_tour = f"Tour {len(tournoi_obj.liste_tours) + 1}"  # Nomme le tour
        self.vue = main_view.AfficheTour()  # Initialise la vue du tour
        self.liste_tours = []  # Initialise la liste des matchs du tour
        self.liste_matchs_termines = []  # Initialise la liste des matchs terminés du tour

        # Crée les matchs pour le tour en cours
        while len(liste_joueurs_trie) > 0:
            match = model_match.Match(
                self.nom_tour, liste_joueurs_trie[0], liste_joueurs_trie[1]
            )  # Crée un nouveau match
            model_match.Match.NUMERO_MATCH += 1  # Incrémente le numéro de match
            self.liste_tours.append(match)  # Ajoute le match à la liste des matchs du tour
            del liste_joueurs_trie[0:2]  # Supprime les joueurs concernés de la liste

        # Affiche les détails du tour
        self.vue.affiche_tour(self.nom_tour, self.liste_tours)

        # Récupère les dates de début et de fin du tour
        self.date_debut, self.date_fin = self.vue.affiche_date_heure_tour()

        # Gère les résultats des matchs
        for match in self.liste_tours:
            resultat_valide = False
            while not resultat_valide:
                resultat_joueur_1 = input(
                    f"Entrez le résultat de {match.joueur_1.nom_famille}"
                    f" {match.joueur_1.prenom}\n"
                    f"1: Victoire | 0: Défaire | N: Match nul "
                    f"==> "
                )
                resultat_joueur_2 = None
                if resultat_joueur_1 in ("0", "1", "n", "N"):
                    resultat_valide = True
                    # Définit les résultats des joueurs en fonction de l'entrée de l'utilisateur
                    match.resultat_joueur_1 = resultat_joueur_1
                    match.joueur_1.total_points_tournoi += resultat_joueur_1
                    match.resultat_joueur_2 = resultat_joueur_2
                    match.joueur_2.total_points_tournoi += resultat_joueur_2
                else:
                    continue
            # Ajoute les résultats des matchs à la liste des matchs terminés du tour
            self.liste_matchs_termines.append(
                (
                    [match.joueur_1.id_joueur, match.resultat_joueur_1],
                    [match.joueur_2.id_joueur, match.resultat_joueur_2],
                )
            )

        # Retourne une nouvelle instance de Tour avec les résultats
        return Tour(
            self.nom_tour, self.date_debut, self.date_fin, self.liste_matchs_termines
        )
