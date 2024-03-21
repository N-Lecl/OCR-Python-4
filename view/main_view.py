from datetime import datetime
from operator import attrgetter

from models import model_tournament, model_player, model_match
# from utils.utils import Utils
import sys


class MenuPrincipal:
    """
    Classe pour l'affichage des menus principaux
    """

    def afficher_menu(self):
        """
        Menu principal
        """
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage de l'en-tête
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
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage de l'en-tête
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
        """
        Menu de fermeture d'application
        """
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage de l'en-tête
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
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage de l'en-tête
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

        # Affichage des informations des joueurs
        for joueur in liste_joueurs:
            print(
                f"Nom --- Prénom --- Date de naissance\n"
                f"{joueur.nom_famille} {joueur.prenom} "
                f"{joueur.date_naissance}\n"
            )
        # Invite à appuyer sur X pour revenir
        print("Appuyer sur X pour revenir")


class AfficheTournoi:
    """
    Affiche les tournois existants non commencés de la DB
    :return True si un tournoi existe et n'est pas commencé
    :rtype: bool
    """

    def __call__(self, *args, **kwargs):
        # Initialisation du flag indiquant s'il y a des tournois non commencés
        tournoi_non_commence = False
        # Récupération de la base de données des tournois
        tournoi_db = model_tournament.TOURNOI_DB
        # Parcours de la base de données des tournois
        for tournoi in tournoi_db:
            # Vérification si le tournoi n'a pas de tours
            if not tournoi["Tours"]:
                # Affichage des informations du tournoi non commencé
                print(
                    f"ID Tournoi: {tournoi.doc_id}, Nom: "
                    f"{tournoi['Nom du tournoi']}, Lieu: {tournoi['Lieu']}"
                )
                # Mise à jour du flag indiquant qu'au moins un tournoi non commencé existe
                tournoi_non_commence = True
        # Retourne True si au moins un tournoi non commencé existe, sinon False
        return tournoi_non_commence


class AfficheChargementTournoi:
    """
    Affiche les tournois non terminés de la DB
    :return True si un tournoi existe et n'est pas terminé
    :rtype: bool
    """

    def __call__(self):
        # Initialisation du flag indiquant s'il y a des tournois non terminés
        tournoi_non_termine = False
        # Récupération de la base de données des tournois
        tournoi_db = model_tournament.TOURNOI_DB
        # Parcours de la base de données des tournois
        for tournoi in tournoi_db:
            # Vérification si le tournoi a des tours et n'est pas terminé
            if tournoi["Tours"]:
                if len(tournoi["Tours"]) < int(tournoi["Nombre de tours"]):
                    # Affichage des informations du tournoi non terminé
                    print(
                        f"ID Tournoi: {tournoi.doc_id}, Nom: "
                        f"{tournoi['Nom du tournoi']}, Lieu: {tournoi['Lieu']}"
                    )
                    # Mise à jour du flag indiquant qu'au moins un tournoi non terminé existe
                    tournoi_non_termine = True
        # Retourne True si au moins un tournoi non terminé existe, sinon False
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
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage du nom du tour
        print(f"-------------{tour_name}---------------\n")
        # Parcours et affichage des matchs du tour
        for match in liste_matchs:
            print(match)

    def affiche_date_heure_tour(self):
        """
        Affiche le signal pour débuter et terminer un tour.
        Enregistre l'heure de début et de fin du tour.
        """
        # Demande à l'utilisateur d'appuyer sur Y pour commencer le tour
        print("Appuyez sur Y pour commencer le tour")
        while True:
            entree = input("==> ")
            if entree.upper() == "Y":
                break
            else:
                print("Appuyez sur Y pour commencer le tour")
        # Enregistre l'heure de début du tour
        date_heure = datetime.now()
        debut = date_heure.strftime("%H:%M:%S - %d/%m/%Y")
        print(f"Début du tour : {debut}\n")

        # Demande à l'utilisateur d'appuyer sur Y pour indiquer que le tour est terminé
        print("Appuyez sur Y lorsque le tour est terminé")
        while True:
            entree = input("==> ")
            if entree.upper() == "Y":
                break
            else:
                print("Appuyez sur Y lorsque le tour est terminé")
        # Enregistre l'heure de fin du tour
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
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage de l'en-tête
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

        # Affichage des résultats des matchs
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

        # Affichage du classement des joueurs par points
        liste_joueurs_tournoi.sort(key=attrgetter("total_points_tournoi"), reverse=True)
        print("Classement des joueurs par points: ")
        for joueur in liste_joueurs_tournoi:
            print(
                f"{joueur.nom_famille} {joueur.prenom} - Score: "
                f"{joueur.total_points_tournoi}"
            )

        # Attente de l'entrée de l'utilisateur pour revenir au menu
        print("Appuyez sur X pour revenir au menu...")
        choix_valide = False
        while not choix_valide:
            choix = input("==> ")
            if choix.upper() == "X":
                choix_valide = True
            else:
                print("Entrée invalide, X pour revenir")


class Print:
    """
    Affiche les differents Prints dans le terminal
    """
    def afficher_message_sauvegarde():
        """
        Affiche : Tournoi sauvegardé, voulez-vous quitter?
        """
        print("Tournoi sauvegardé, voulez-vous quitter?\n")

    def id_tournoi_valide_yn():
        """
        Affiche : Entrée invalide (Y/N)
        """
        print("Entrée invalide (Y/N)")

    def id_tournoi_valide():
        """
        Affiche : Entrée invalide
        """
        print("Entrée invalide")

    def tournoi_non_termine():
        """
        Affiche : Pas de tournoi non terminé.
        """
        print("Pas de tournoi non terminé.")

    def tournoi_non_commence():
        """
        AFfiche : Pas de tournoi non terminé
        """
        print("Pas de tournoi non terminé.")

    def nom_obligatoire():
        """
        AFfiche : Un nom est obligatoire!
        """
        print("Un nom est obligatoire!")

    def prenom_obligatoire():
        """
        Affiche : Un prénom est obligatoire!
        """
        print("Un prénom est obligatoire!")

    def lieu_obligatoire():
        """
        Affiche : Un lieu est obligatoire!
        """
        print("Un lieu est obligatoire!")

    def jour_obligatoire():
        """
        Affiche : Entrez un chiffre entre 1 et 31!
        """
        print("Entrez un chiffre entre 1 et 31!")

    def mois_obligatoire():
        """
        Affiche : Entrez un chiffre entre 1 et 12!
        """
        print("Entrez un chiffre entre 1 et 12!")

    def annee_obligatoire():
        """
        Affiche : Entrez un nombre à 4 chiffres
        """
        print("Entrez un nombre à 4 chiffres!")

    def nombre_tours():
        """
        Affiche 4 tours par défaut.\n" "Voulez-vous modifier?
        """
        print("4 tours par défaut.\n" "Voulez-vous modifier?")

    def choix_tours():
        """
        Y pour changer / N pour garder 4 tours
        """
        print("Y pour changer / N pour garder 4 tours")

    def tour_erreur():
        """
        Affiche : Entrez un nombre entier supérieur à 0!
        """
        print("Entrez un nombre entier supérieur à 0!")

    def choix_yn():
        """
        Affiche : Veuillez choisir Y/N
        """
        print("Veuillez choisir Y/N")

    def description():
        """
        Affiche : Entrez la DESCRIPTION du tournoi:
        """
        print("Entrez la DESCRIPTION du tournoi: ")

    def nombre_pair_impair():
        """
        Affiche : Entrez un nombre pair et positif!
        """
        print("Entrez un nombre pair et positif!")

    def entree_non_valide():
        """
        Affiche : Entrée non valide
        """
        print("Entrée non valide")

    def choix_hf():
        """
        Affiche : Entrez un choix F ou M!
        """
        print("Entrez un choix F ou M!")

    def choix_chess_id():
        """
        Affiche : Entrez un Chess ID!
        """
        print("Entrez un Chess ID!")

    def aucun_joueurs():
        """
        Affiche : Aucun joueurs enregistrés !
        """
        print("Aucun joueurs enregistrés !")


class FermerApplication:
    """
    Affiche le message d'aurevoir dans le terminal
    """
    def __call__(self):
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Affichage de l'en-tête
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
