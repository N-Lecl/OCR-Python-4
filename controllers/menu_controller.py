

from controllers import tournament_controller, player_controller
from view import main_view
from models import model_player


def choix_menu():

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
                print("Entrée non valide")


class MenuPrincipalControleur:
    """
    Contrôleur du menu principal
    """

    def __init__(self):
        self.view = main_view.MenuPrincipal()
        self.model_player = model_player.Joueur()
        self.controleur_actuel = None

    def __call__(self):
        self.view.afficher_menu()
        entree = choix_menu()

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
        return self.controleur_actuel()

    def aller_vers_lancer_tournoi(self):
        return self.controleur_actuel()

    def aller_vers_reprendre_tournoi(self):
        return self.controleur_actuel.chargement_tournoi()

    def aller_vers_creer_joueur(self):
        return self.controleur_actuel()

    def aller_vers_rapport_joueur(self):
        return self.controleur_actuel()

    def aller_vers_fermer_application(self):
        return self.controleur_actuel()
