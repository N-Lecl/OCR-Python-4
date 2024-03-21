from datetime import datetime
from operator import attrgetter

from models import model_tournament, model_player, model_match
from utils.utils import Utils
import sys


class MenuPrincipal:
    """
    Classe pour l'affichage des menus principaux
    """

    def afficher_menu(self):
        """
        Menu principal
        """
        Utils.clear_terminal()
        print(
            "----------------------------------------------------------------------------------------\n"
            "   _____           _   _                   _        _______                           _ \n"
            "  / ____|         | | (_)                 | |      |__   __|                         (_)\n"
            " | |  __  ___  ___| |_ _  ___  _ __     __| | ___     | | ___  _   _ _ __ _ __   ___  _ \n"
            " | | |_ |/ _ \/ __| __| |/ _ \| '_ \   / _` |/ _ \    | |/ _ \| | | | '__| '_ \ / _ \| |\n"
            " | |__| |  __/\__ \ |_| | (_) | | | | | (_| |  __/    | | (_) | |_| | |  | | | | (_) | |\n"
            "  \_____|\___||___/\__|_|\___/|_| |_|  \__,_|\___|    |_|\___/ \__,_|_|  |_| |_|\___/|_|\n"
            "                                                                                        \n"
            "----------------------------------------------------------------------------------------\n"
            "\n"
            "-- Choisir une option:\n"
            "1) Créer nouveau tournoi \n"
            "2) Lancer un nouveau tournoi \n"
            "3) Reprendre un tournoi en cours \n"
            "\n"
            "4) Créer un joueur \n"
            "5) Liste des joueurs \n"
            "\n"
            "x) Quitter\n"
            "\n"
            ""
        )

    def menu_fin_tournoi(self):
        """
        Menu de fin de tournoi
        """
        Utils.clear_terminal()
        print(
            "------------------------------------------------------------------------------\n"
            "  _______                           _   _______                  _         __ \n"
            " |__   __|                         (_) |__   __|                (_)       /_/ \n"
            "    | | ___  _   _ _ __ _ __   ___  _     | | ___ _ __ _ __ ___  _ _ __   ___ \n"
            "    | |/ _ \| | | | '__| '_ \ / _ \| |    | |/ _ \ '__| '_ ` _ \| | '_ \ / _ \\n"
            "    | | (_) | |_| | |  | | | | (_) | |    | |  __/ |  | | | | | | | | | |  __/\n"
            "    |_|\___/ \__,_|_|  |_| |_|\___/|_|    |_|\___|_|  |_| |_| |_|_|_| |_|\___|\n"
            "                                                                              \n"
            "------------------------------------------------------------------------------\n"
            "\n"
            "-- Choisir une option:\n"
            "1) Voir résumé et vainqueur(s) du tournoi\n"
            "2) Voir le détail des joueurs \n"
            "\n"
            "x) Retour menu \n"
            "\n"
            ""
        )

    def fermer_application(self):
        Utils.clear_terminal()
        print("-----------------------------------------------------------------------------\n"
              "  __  __               _        _                                     _      \n"
              " |  \/  |             (_)      | |                                   (_)     \n"
              " | \  / | ___ _ __ ___ _    ___| |_    __ _ _   _ _ __ _____   _____  _ _ __ \n"
              " | |\/| |/ _ \ '__/ __| |  / _ \ __|  / _` | | | | '__/ _ \ \ / / _ \| | '__|\n"
              " | |  | |  __/ | | (__| | |  __/ |_  | (_| | |_| | | |  __/\ V / (_) | | |   \n"
              " |_|  |_|\___|_|  \___|_|  \___|\__|  \__,_|\__,_|_|  \___| \_/ \___/|_|_|   \n"
              "                                                                             \n"
              "-----------------------------------------------------------------------------\n")
        sys.exit()


class AfficheJoueurRapport:
    """
    Classe pour l'affichage des joueurs enregistrés
    """

    def __call__(self, liste_joueurs):
        Utils.clear_terminal()
        print(
            "-----------------------------------------------------------------\n"
            "  _____        __              _                                 \n"
            " |_   _|      / _|            (_)                                \n"
            "   | |  _ __ | |_ ___  ___     _  ___  _   _  ___ _   _ _ __ ___ \n"
            "   | | | '_ \|  _/ _ \/ __|   | |/ _ \| | | |/ _ \ | | | '__/ __|\n"
            "  _| |_| | | | || (_) \__ \   | | (_) | |_| |  __/ |_| | |  \__ \ \n"
            " |_____|_| |_|_| \___/|___/   | |\___/ \__,_|\___|\__,_|_|  |___/\n"
            "                             _/ |                                \n"
            "                            |__/                                 \n"
            "-----------------------------------------------------------------\n"
            "\n")
        for joueur in liste_joueurs:
            print(
                f"Nom --- Prénom --- Date de naissance\n"
                f"{joueur.nom_famille} {joueur.prenom} "
                f"{joueur.date_naissance}\n"
            )
        print("Appuyer sur X pour revenir")


class AfficheTournoi:
    """
    Affiche les tournois existants non commencés de la DB
    :return True si un tournoi existe et n'est pas commencé
    :rtype: bool
    """

    def __call__(self, *args, **kwargs):
        tournoi_non_commence = False
        tournoi_db = model_tournament.TOURNOI_DB
        for tournoi in tournoi_db:
            if not tournoi["Tours"]:
                print(
                    f"ID Tournoi: {tournoi.doc_id}, Nom: "
                    f"{tournoi['Nom du tournoi']}, Lieu: {tournoi['Lieu']}"
                )
                tournoi_non_commence = True
        return tournoi_non_commence


class AfficheChargementTournoi:
    """
    Affiche les tournois non terminés de la DB
    :return True si un tournoi existe et n'est pas terminé
    :rtype: bool
    """

    def __call__(self):
        tournoi_non_termine = False
        tournoi_db = model_tournament.TOURNOI_DB
        for tournoi in tournoi_db:
            if tournoi["Tours"]:
                if len(tournoi["Tours"]) < int(tournoi["Nombre de tours"]):
                    print(
                        f"ID Tournoi: {tournoi.doc_id}, Nom: "
                        f"{tournoi['Nom du tournoi']}, Lieu: {tournoi['Lieu']}"
                    )
                    tournoi_non_termine = True
        return tournoi_non_termine


class AfficheTour:
    """
    Affiche les informations pendant les tours
    """

    def __init__(self):
        self.match = model_match.Match()

    def affiche_tour(self, tour_name, liste_matchs):
        """
        Affiche le nom du tour et la liste des matchs du tour
        :param tour_name: un Tour
        :type tour_name: object Tour
        :param liste_matchs: liste d'objets Match
        :type liste_matchs: list
        """
        Utils.clear_terminal()
        print(f"-------------{tour_name}---------------\n")
        for match in liste_matchs:
            print(match)

    def affiche_date_heure_tour(self):
        """
        Affiche le signal pour débuter et terminer un tour.
        Enregistre l'heure de début et de fin du tour.
        """
        print("Appuyez sur Y pour commencer le tour")
        while True:
            entree = input("==> ")
            if entree.upper() == "Y":
                break
            else:
                print("Appuyez sur Y pour commencer le tour")
        date_heure = datetime.now()
        debut = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Début du tour : {debut}\n")

        print("Appuyez sur Y lorsque le tour est terminé")
        while True:
            entree = input("==> ")
            if entree.upper() == "Y":
                break
            else:
                print("Appuyez sur Y lorsque le tour est terminé")
        date_heure = datetime.now()
        fin = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Fin du tour : {fin}\n")
        return debut, fin


class ResultatsTournoi:
    """
    Affiche les résultats du tournoi et le classement des joueurs par points.
    """

    def __call__(self, tournoi_obj, liste_joueurs_tournoi):
        """
        :param tournoi_obj: un Tournoi
        :type tournoi_obj: object Tournoi
        :param liste_joueurs_tournoi: liste d'objets Joueur
        :type liste_joueurs_tournoi: list
        """
        Utils.clear_terminal()
        print(
            "-----------------------------------------------------------------------------\n"
            "  _____   __            _ _        _     _______                           _ \n"
            " |  __ \ /_/           | | |      | |   |__   __|                         (_)\n"
            " | |__) |___  ___ _   _| | |_ __ _| |_     | | ___  _   _ _ __ _ __   ___  _ \n"
            " |  _  // _ \/ __| | | | | __/ _` | __|    | |/ _ \| | | | '__| '_ \ / _ \| |\n"
            " | | \ \  __/\__ \ |_| | | || (_| | |_     | | (_) | |_| | |  | | | | (_) | |\n"
            " |_|  \_\___||___/\__,_|_|\__\__,_|\__|    |_|\___/ \__,_|_|  |_| |_|\___/|_|\n"
            "                                                                             \n"
            "-----------------------------------------------------------------------------\n"
        )
        for tour in tournoi_obj.liste_tours:
            print(tour)

            for match in tour.liste_matchs_termines:
                joueur_1 = model_player.JOUEUR_DB.get(doc_id=match[0][0])
                score_joueur_1 = match[0][1]
                joueur_2 = model_player.JOUEUR_DB.get(doc_id=match[1][0])
                score_joueur_2 = match[1][1]
                print(
                    f"{joueur_1['Nom']} {joueur_1['Prenom']} VS "
                    f"{joueur_2['Nom']} {joueur_2['Prenom']}\n"
                    f"RESULTAT: {score_joueur_1} VS {score_joueur_2}\n"
                )

        liste_joueurs_tournoi.sort(key=attrgetter("total_points_tournoi"), reverse=True)
        print("Classement des joueurs par points: ")
        for joueur in liste_joueurs_tournoi:
            print(
                f"{joueur.nom_famille} {joueur.prenom} - Score: "
                f"{joueur.total_points_tournoi}"
            )

        print("Appuyez sur X pour revenir au menu...")
        choix_valide = False
        while not choix_valide:
            choix = input("==> ")
            if choix.upper() == "X":
                choix_valide = True
            else:
                print("Entrée invalide, X pour revenir")


class Print:
    def afficher_message_sauvegarde():
        print("Tournoi sauvegardé, voulez-vous quitter?\n")

    def id_tournoi_valide():
        print("Entrée invalide (Y/N)")

    def tournoi_non_termine():
        print("Pas de tournoi non terminé.")

    def tournoi_non_commence():
        print("Pas de tournoi non terminé.")

    def nom_obligatoire():
        print("Un nom est obligatoire!")
        
    def prenom_obligatoire():
        print("Un prénom est obligatoire!")

    def lieu_obligatoire():
        print("Un lieu est obligatoire!")

    def jour_obligatoire():
        print("Entrez un chiffre entre 1 et 31!")

    def mois_obligatoire():
        print("Entrez un chiffre entre 1 et 12!")

    def annee_obligatoire():
        print("Entrez un nombre à 4 chiffres!")

    def nombre_tours():
        print("4 tours par défaut.\n" "Voulez-vous modifier?")

    def choix_tours():
        print("Y pour changer / N pour garder 4 tours")

    def tour_erreur():
        print("Entrez un nombre entier supérieur à 0!")

    def choix_yn():
        print("Veuillez choisir Y/N")

    def description():
        print("Entrez la DESCRIPTION du tournoi: ")

    def nombre_pair_impair():
        print("Entrez un nombre pair et positif!")

    def entree_non_valide():
        print("Entrée non valide")

    def choix_hf():
        print("Entrez un choix F ou M!")

    def choix_chess_id():
        print("Entrez un Chess ID!")

    def aucun_joueurs():
        print("Aucun joueurs enregistrés !")


class FermerApplication:
    def __call__(self):
        Utils.clear_terminal()
        print("-----------------------------------------------------------------------------\n"
              "  __  __               _        _                                     _      \n"
              " |  \/  |             (_)      | |                                   (_)     \n"
              " | \  / | ___ _ __ ___ _    ___| |_    __ _ _   _ _ __ _____   _____  _ _ __ \n"
              " | |\/| |/ _ \ '__/ __| |  / _ \ __|  / _` | | | | '__/ _ \ \ / / _ \| | '__|\n"
              " | |  | |  __/ | | (__| | |  __/ |_  | (_| | |_| | | |  __/\ V / (_) | | |   \n"
              " |_|  |_|\___|_|  \___|_|  \___|\__|  \__,_|\__,_|_|  \___| \_/ \___/|_|_|   \n"
              "                                                                             \n"
              "-----------------------------------------------------------------------------\n")
        sys.exit()
