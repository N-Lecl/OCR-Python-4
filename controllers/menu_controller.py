

from controllers import tournament_controller, player_controller
from view import main_view
from models import model_player


def choix_menu():
    """
    Fonction permettant de capturer l'entrée de l'utilisateur dans un menu.

    Returns:
        str: La chaîne correspondant à l'option choisie par l'utilisateur.
    """
    while True:
        entree = input("==>")
        match entree:
            case "1":
                return "1"
            case "2":
                return "2"
            case "3":
                return "3"
            case "4":
                return "4"
            case "5":
                return "5"
            case ("X" | "x"):
                return "x"
            case _:
                main_view.Print.entree_non_valide()


class MenuPrincipalControleur:
    """
    Contrôleur du menu principal
    """

    def __init__(self):
        self.view = main_view.MenuPrincipal()  # instance de la vue
        self.model_player = model_player.Joueur()  # instance du modele joueurs
        self.controleur_actuel = None

    def __call__(self):
        self.view.afficher_menu()
        entree = choix_menu()

        # Gérer les différentes options du menu principal
        if entree == "1":
            self.controleur_actuel = tournament_controller.CreerTournoiControleur()
            self.aller_vers_creer_tournoi()
        if entree == "2":
            self.controleur_actuel = tournament_controller.LancerTournoiControleur()
            self.aller_vers_lancer_tournoi()
        if entree == "3":
            self.controleur_actuel = tournament_controller.LancerTournoiControleur()
            self.aller_vers_reprendre_tournoi()
        if entree == "4":
            self.controleur_actuel = player_controller.CreerJoueurControleur()
            self.aller_vers_creer_joueur()
        if entree == "5":
            self.controleur_actuel = player_controller.JoueurRapport()
            self.aller_vers_rapport_joueur()
        if entree == "x":
            self.controleur_actuel = main_view.FermerApplication()
            self.aller_vers_fermer_application()

    def aller_vers_creer_tournoi(self):
        """
        Méthode permettant de naviguer vers l'écran de création d'un nouveau tournoi.
        """
        return self.controleur_actuel()

    def aller_vers_lancer_tournoi(self):
        """
        Méthode permettant de naviguer vers l'écran de lancement d'un tournoi déjà créé.
        """
        return self.controleur_actuel()

    def aller_vers_reprendre_tournoi(self):
        """
        Méthode permettant de naviguer vers l'écran de reprise d'un tournoi en cours.
        """
        return self.controleur_actuel.chargement_tournoi()

    def aller_vers_creer_joueur(self):
        """
        Méthode permettant de naviguer vers l'écran de création d'un nouveau joueur.
        """
        return self.controleur_actuel()

    def aller_vers_rapport_joueur(self):
        """
        Méthode permettant de naviguer vers l'écran de rapport sur un joueur.
        """
        return self.controleur_actuel()

    def aller_vers_fermer_application(self):
        """
        Méthode permettant de naviguer vers l'écran de fermeture de l'application.
        """
        return self.controleur_actuel()
