from tinydb import TinyDB

# Création de la base de données des joueurs
JOUEUR_DB = TinyDB("models/joueur_db.json")


class Joueur:
    """
    Représente un joueur d'échecs
    """

    def __init__(
        self,
        nom_famille=None,
        prenom=None,
        chess_id=None,
        date_naissance=None,
        sexe=None,
        total_points_tournoi=0,
        id_joueur=0,
    ):
        """
        Initialise une instance de Joueur.
        :param nom_famille: nom du joueur
        :type nom_famille: str
        :param prenom: prenom du joueur
        :type prenom: str
        :param date_naissance: date de naissance du joueur
        :type date_naissance: str
        :param sexe: M ou F
        :type sexe: str
        :param chess_id: nombre positif
        :type chess_id: str
        :param total_points_tournoi: score total du joueur
        :type total_points_tournoi: int
        :param id_joueur: ID du joueur
        :type id_joueur: int
        """
        self.nom_famille = nom_famille  # Initialise le nom de famille du joueur
        self.prenom = prenom  # Initialise le prénom du joueur
        self.date_naissance = date_naissance  # Initialise la date de naissance du joueur
        self.sexe = sexe  # Initialise le sexe du joueur
        self.chess_id = chess_id  # Initialise l'identifiant du joueur
        self.total_points_tournoi = total_points_tournoi  # Initialise le score total du joueur
        self.id_joueur = id_joueur  # Initialise l'ID du joueur

    def __str__(self):
        """
        Méthode spéciale pour obtenir une représentation en chaîne d'un objet Joueur.

        Returns:
            str: Le nom complet du joueur.
        """
        return f"{self.nom_famille} {self.prenom}"

    def __repr__(self):
        """
        Méthode spéciale pour obtenir une représentation en chaîne de l'objet Joueur.
        """
        return f"{self.nom_famille} {self.prenom}, Chess ID : {self.chess_id}"

    def creer_instance_joueur(self, joueur_sauve):
        """
        Méthode d'instanciation de joueur à partir de données texte
        :param joueur_sauve: dictionnaire contenant les informations d'un joueur
        :type joueur_sauve: dict
        :return: un Joueur
        :rtype: object Joueur
        """
        # Création d'une nouvelle instance de joueur avec les informations sauvegardées
        nom_famille = joueur_sauve["Nom"]
        prenom = joueur_sauve["Prenom"]
        date_naissance = joueur_sauve["Date de naissance"]
        sexe = joueur_sauve["Sexe"]
        chess_id = joueur_sauve["chess_id"]
        total_points_tournoi = joueur_sauve["Score"]
        id_joueur = joueur_sauve["ID joueur"]
        return Joueur(
            nom_famille,
            prenom,
            chess_id,
            date_naissance,
            sexe,
            total_points_tournoi,
            id_joueur,
        )

    def serialise(self):
        """
        Méthode de sérialisation du modèle joueur
        :return: dictionnaire contenant les informations d'un joueur
        :rtype: dict
        """
        # Sérialisation des informations du joueur
        joueur_sauve = {
            "Nom": self.nom_famille,
            "Prenom": self.prenom,
            "Date de naissance": self.date_naissance,
            "Sexe": self.sexe,
            "chess_id": self.chess_id,
            "Score": self.total_points_tournoi,
            "ID joueur": self.id_joueur,
        }
        return joueur_sauve

    def ajout_db(self, infos_joueur):
        """
        Méthode d'ajout d'un joueur à la DB joueur
        :param infos_joueur: liste des informations du joueur
        :type infos_joueur: list
        """
        # Création d'une instance de joueur avec les informations fournies et ajout à la base de données
        joueur = Joueur(
            infos_joueur[0],
            infos_joueur[1],
            infos_joueur[2],
            infos_joueur[3],
            infos_joueur[4],
        )
        id_joueur = JOUEUR_DB.insert(joueur.serialise())  # Insère le joueur dans la base de données
        JOUEUR_DB.update({"ID joueur": id_joueur}, doc_ids=[id_joueur])  # Met à jour l'ID du joueur
