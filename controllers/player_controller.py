from controllers import menu_controller
from models import model_player
from view import main_view


class CreerJoueurControleur:
    """
    Crée un nouveau joueur et l'enregistre dans la BD joueur
    """

    def __init__(self):
        self.infos_joueur = []
        self.menu_principal_controleur = menu_controller.MenuPrincipalControleur()

    def __call__(self):
        # Initialisation du modèle joueur
        self.model_player = model_player.Joueur()
        # Saisie des informations sur le joueur
        self.infos_joueur.append(self.ajout_nom())
        self.infos_joueur.append(self.ajout_prenom())
        self.infos_joueur.append(self.ajout_chess_id())
        self.infos_joueur.append(self.ajout_anniversaire())
        self.infos_joueur.append(self.ajout_sexe())
        # Ajout du joueur à la base de données
        self.model_player.ajout_db(self.infos_joueur)
        # Réinitialisation de la liste d'informations du joueur
        self.infos_joueur.clear()
        # Retour au menu principal
        self.menu_principal_controleur()

    def ajout_nom(self):
        """
        Méthode pour saisir et valider le nom d'un joueur.

        Returns:
            str: Le nom du joueur.
        """
        nom_joueur = None
        nom_valide = False
        while not nom_valide:
            nom_joueur = input("Entrez le NOM du joueur: ")
            if nom_joueur != "" and nom_joueur.isalpha():
                nom_valide = True
            else:
                main_view.Print.nom_obligatoire()
        return nom_joueur

    def ajout_prenom(self):
        """
        Méthode pour saisir et valider le prénom d'un joueur.

        Returns:
            str: Le prénom du joueur.
        """
        prenom_joueur = None
        prenom_valide = False
        while not prenom_valide:
            prenom_joueur = input("Entrez le PRENOM du joueur: ")
            if prenom_joueur != "" and prenom_joueur.isalpha():
                prenom_valide = True
            else:
                main_view.Print.prenom_obligatoire()
        return prenom_joueur

    def ajout_anniversaire(self):
        """
        Méthode pour saisir et valider la date de naissance d'un joueur.

        Returns:
            str: La date de naissance du joueur au format JJ/MM/AAAA.
        """
        date = []

        jour_valide = False
        while not jour_valide:
            jour = input("Entrez le JOUR de naissance: ")
            if jour.isdigit() and (0 < int(jour) < 32):
                jour_valide = True
                date.append(jour)
            else:
                main_view.Print.jour_obligatoire()

        mois_valide = False
        while not mois_valide:
            mois = input("Entrez le MOIS de naissance: ")
            if mois.isdigit() and (0 < int(mois) < 13):
                mois_valide = True
                date.append(mois)
            else:
                main_view.Print.mois_obligatoire()

        annee_valide = False
        while not annee_valide:
            annee = input("Entrez l'ANNÉE de naissance: ")
            if annee.isdigit() and len(annee) == 4:
                annee_valide = True
                date.append(annee)
            else:
                main_view.Print.annee_obligatoire()

        return f"{date[0]}/{date[1]}/{date[2]}"

    def ajout_sexe(self):
        """
        Méthode pour saisir et valider le sexe d'un joueur.

        Returns:
            str: Le sexe du joueur (F pour féminin, M pour masculin).
        """
        while True:
            choix = input("Entrez les sexe: F ou M: ")
            if choix.upper() == "M":
                sexe = "M"
                break
            if choix.upper() == "F":
                sexe = "F"
                break
            else:
                main_view.Print.choix_hf()
        return sexe

    def ajout_chess_id(self):
        """
        Méthode pour saisir et valider le Chess ID d'un joueur.

        Returns:
            str: Le Chess ID du joueur.
        """
        while True:
            chess_id = input("Entrez le chess ID du joueur: ")
            if chess_id:
                return chess_id
            else:
                main_view.Print.choix_chess_id()


class JoueurRapport:
    """
    Affiche la liste des joueurs enregistrés.

    """

    def __call__(self):
        liste_joueurs = []
        self.menu_principal_controleur = menu_controller.MenuPrincipalControleur()
        self.joueur_db = model_player.JOUEUR_DB
        self.joueur = model_player.Joueur()
        if len(self.joueur_db) == 0:
            main_view.Print.aucun_joueurs()
            self.menu_principal_controleur()
        self.affiche_joueur = main_view.AfficheJoueurRapport()

        for joueur in self.joueur_db:
            liste_joueurs.append(self.joueur.creer_instance_joueur(joueur))

        # Affichage de la liste des joueurs
        self.affiche_joueur(liste_joueurs)

        # Boucle pour gérer les interactions avec l'utilisateur
        while True:
            entree = input("==> ")
            match entree:
                case ("X" | "x"):
                    self.menu_principal_controleur()
                case _:
                    main_view.Print.entree_non_valide()
