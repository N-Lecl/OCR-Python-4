from collections import deque
from operator import attrgetter

from controllers import menu_controller
from models import model_player, model_tournament, model_round
from view import main_view
# from utils.utils import Utils


class LancerTournoiControleur:
    """
    Lance un tournoi deja créé.
    """

    MATCHS_JOUES = []  # Liste des matchs joués
    TOURS_JOUES = []   # Liste des tours joués

    def __init__(self):
        self.affiche_tournoi = None
        self.tournoi = None
        self.tour = model_round.Tour()
        self.liste_joueurs_trie = []
        self.menu_principal_controleur = menu_controller.MenuPrincipalControleur()
        self.vue_resultats = main_view.ResultatsTournoi()
        self.joueur = model_player.Joueur()

    def __call__(self):
        # Sélection du tournoi à lancer
        self.tournoi_obj = self.selection_tournoi()
        # Tri initial des joueurs pour le premier tour
        self.liste_joueurs_trie = self.triage_initial(self.tournoi_obj)

        # Lancement du premier tour
        self.tournoi_obj.liste_tours.append(
            self.tour.lancer_tour(self.liste_joueurs_trie.copy(), self.tournoi_obj)
        )
        self.sauvegarde_tournoi(self.tournoi_obj)

        # Lancement des tours suivants
        for tour in range(int(self.tournoi_obj.nombre_tours) - 1):
            self.liste_joueurs_trie_suivant = self.triage_tours_suivants(
                self.liste_joueurs_trie.copy()
            )
            self.tournoi_obj.liste_tours.append(
                self.tour.lancer_tour(self.liste_joueurs_trie_suivant, self.tournoi_obj)
            )
            self.sauvegarde_tournoi(self.tournoi_obj)

        # Affichage des résultats du tournoi
        self.vue_resultats(self.tournoi_obj, self.liste_joueurs_trie)
        self.menu_principal_controleur()

    def sauvegarde_tournoi(self, tournoi_obj):
        """
        Méthode de sauvegarde de tournoi dans la DB tournoi
        :param tournoi_obj: Objet Tournoi à sauvegarder
        """
        # Récupération de la base de données des tournois
        tournoi_db = model_tournament.TOURNOI_DB

        # Récupération du tournoi choisi dans la base de données
        tournoi_choisi = model_tournament.TOURNOI_DB.get(doc_id=tournoi_obj.id_tournoi)
        # Récupération du dictionnaire des IDs des joueurs et de leurs scores
        dict_ids_scores_joueurs = tournoi_choisi["Liste joueurs"]

        # Mise à jour des scores des joueurs pour chaque match du dernier tour
        for match in self.tour.liste_tours:
            id_joueur_1 = str(match.joueur_1.id_joueur)
            score_joueur_1 = match.joueur_1.total_points_tournoi
            dict_ids_scores_joueurs[id_joueur_1] = score_joueur_1

            id_joueur_2 = str(match.joueur_2.id_joueur)
            score_joueur_2 = match.joueur_2.total_points_tournoi
            dict_ids_scores_joueurs[id_joueur_2] = score_joueur_2

        # Mise à jour de la base de données avec les nouveaux scores des joueurs
        tournoi_db.update(
            {"Liste joueurs": dict_ids_scores_joueurs}, doc_ids=[tournoi_obj.id_tournoi]
        )

        # Récupération de la table des tours dans la base de données
        table_tours = tournoi_db.table("tours")

        # Sérialisation du dernier tour et ajout dans la table des tours
        tour_obj = tournoi_obj.liste_tours[-1]
        tour_serialise = tour_obj.serialise()
        tour_serialise["Liste matchs termines"] = tour_obj.liste_matchs_termines

        id_tour = table_tours.insert(tour_serialise)

        # Ajout de l'ID du dernier tour dans la liste des tours joués du tournoi
        LancerTournoiControleur.TOURS_JOUES.append(id_tour)
        tournoi_db.update(
            {"Tours": LancerTournoiControleur.TOURS_JOUES},
            doc_ids=[tournoi_obj.id_tournoi],
        )

        # Affichage du message de sauvegarde et gestion des choix de l'utilisateur
        main_view.Print.afficher_message_sauvegarde()
        choix_valide = False
        while not choix_valide:
            choix = input("Y/N ==> ")
            if choix.upper() == "Y":
                choix_valide = True
                self.menu_principal_controleur()
            elif choix.upper() == "N":
                choix_valide = True
            else:
                main_view.Print.id_tournoi_valide_yn()

    def chargement_tournoi(self):
        """
        Méthode de chargement de tournoi depuis la DB tournoi
        """
        # Création des instances nécessaires
        self.affiche_tournoi = main_view.AfficheChargementTournoi()
        self.tournoi = model_tournament.Tournoi()
        self.model_player = model_player.Joueur()
        tournoi_db = model_tournament.TOURNOI_DB
        table_tours = tournoi_db.table("tours")
        instances_tours = []

        # Vérification de l'existence de tournois
        if self.affiche_tournoi():

            choix = None
            id_valide = False
            while not id_valide:
                choix = input("Choisir ID du tournoi ==> ")
                if (
                    choix.isdigit() and int(choix) > 0 and int(choix) <= len(model_tournament.TOURNOI_DB)
                ):
                    id_valide = True
                else:
                    main_view.Print.id_tournoi_valide()

            # Récupération des données du tournoi choisi
            tournoi_choisi = model_tournament.TOURNOI_DB.get(doc_id=int(choix))
            for tour in tournoi_choisi["Tours"]:
                tour_serialise = table_tours.get(doc_id=tour)
                tour_obj = self.tour.creer_instance_tour(tour_serialise)
                instances_tours.append(tour_obj)
            tournoi_choisi["Tours"] = instances_tours
            tournoi_obj = self.tournoi.creer_instance_tournoi(tournoi_choisi)
            dict_ids_scores_joueurs = tournoi_choisi["Liste joueurs"]

            liste_obj_joueurs = []
            for id_joueur in tournoi_obj.ids_scores_joueurs:
                joueur = model_player.JOUEUR_DB.get(doc_id=int(id_joueur))
                joueur_obj = self.model_player.creer_instance_joueur(joueur)
                joueur_obj.total_points_tournoi = dict_ids_scores_joueurs[id_joueur]
                liste_obj_joueurs.append(joueur_obj)
        else:
            # Aucun tournoi trouvé
            main_view.Print.tournoi_non_termine()
            self.menu_principal_controleur()

        # Pour chaque tour restant, lancer un tour et sauvegarder le tournoi
        for tour in range(int(tournoi_obj.nombre_tours) - len(tournoi_obj.liste_tours)):
            print(tournoi_obj)
            joueurs_tries = self.triage_tours_suivants(liste_obj_joueurs.copy())
            tournoi_obj.liste_tours.append(
                self.tour.lancer_tour(joueurs_tries, tournoi_obj)
            )
            self.sauvegarde_tournoi(tournoi_obj)
            
        # Afficher les résultats du tournoi et retourner au menu principal
        self.vue_resultats(tournoi_obj, liste_obj_joueurs)
        self.menu_principal_controleur()

    def selection_tournoi(self):
        """
        Méthode pour sélectionner un tournoi non démarré.
        :rtype: object Tournoi
        """
        # Affichage des tournois disponibles
        self.affiche_tournoi = main_view.AfficheTournoi()
        self.tournoi = model_tournament.Tournoi()

        # Vérification de l'existence de tournois
        if self.affiche_tournoi():
            choix = None
            id_valide = False
            while not id_valide:
                # Sélection de l'ID du tournoi
                choix = input("Choisir ID du tournoi ==> ")
                if (
                    choix.isdigit() and int(choix) > 0 and int(choix) <= len(model_tournament.TOURNOI_DB)
                ):
                    id_valide = True
                else:
                    main_view.Print.id_tournoi_valide()

            # Création de l'instance Tournoi choisie
            tournoi_choisi = model_tournament.TOURNOI_DB.get(doc_id=int(choix))
            tournoi_obj = self.tournoi.creer_instance_tournoi(tournoi_choisi)
            return tournoi_obj
        else:
            # Aucun tournoi trouvé
            main_view.Print.tournoi_non_commence()
            self.menu_principal_controleur()

    def triage_initial(self, tournoi):
        """
        Méthode pour générer les paires (matchs) du premier tour
        :param tournoi: un tournoi
        :type tournoi: object Tournoi
        :return: liste d'objets Joueur
        :rtype: list
        """
        # Récupération des IDs des joueurs du tournoi
        ids_joueurs = tournoi.ids_scores_joueurs
        instances_joueurs = []
        liste_joueurs_tri = []

        # Création des instances des joueurs à partir de leurs IDs
        for id_joueur in ids_joueurs:
            joueur = model_player.JOUEUR_DB.get(doc_id=int(id_joueur))
            joueur_obj = self.joueur.creer_instance_joueur(joueur)
            instances_joueurs.append(joueur_obj)

        # Création des paires de joueurs pour le premier tour
        for joueur in instances_joueurs:
            joueur_1 = joueur
            index_joueur_1 = instances_joueurs.index(joueur)

            if index_joueur_1 + len(ids_joueurs) / 2 < len(ids_joueurs):
                index_joueur_2 = index_joueur_1 + int(len(ids_joueurs) / 2)
                joueur_2 = instances_joueurs[index_joueur_2]

                print(f"Ajout du match {joueur_1} VS {joueur_2}\n")
                liste_joueurs_tri.append(joueur_1)
                liste_joueurs_tri.append(joueur_2)
                self.MATCHS_JOUES.append({joueur_1.id_joueur, joueur_2.id_joueur})
            else:
                pass

        return liste_joueurs_tri

    def triage_tours_suivants(self, instances_joueurs_a_trier):
        """
        Méthode pour générer les paires (matchs) des tours suivants
        :param instances_joueurs_a_trier: liste d'objets Joueur
        :type instances_joueurs_a_trier: list
        :return: liste d'objets Joueur
        :rtype: list
        """
        # Initialisation d'un ensemble pour tester les paires de matchs
        test_match = set()
        liste_joueurs_par_score = []

        # Tri des joueurs selon leur score total dans le tournoi
        instances_joueurs_a_trier.sort(
            key=attrgetter("total_points_tournoi"), reverse=True
        )

        # Utilisation d'une file pour gérer les paires de joueurs
        queue = deque(instances_joueurs_a_trier)
        while len(queue) > 1:
            joueur_1 = queue.popleft()
            joueur_2 = None
            for i in range(0, len(queue)):
                joueur_2_tmp = queue[i]

                # Vérification de la possibilité de créer un nouveau match
                test_match.add(joueur_1.id_joueur)
                test_match.add(joueur_2_tmp.id_joueur)

                if test_match not in self.MATCHS_JOUES:
                    joueur_2 = joueur_2_tmp
                    queue.remove(joueur_2_tmp)
                    break
                else:
                    if i == (len(queue) - 1):
                        joueur_2 = queue.popleft()
                    else:
                        continue

            # Affichage du match ajouté
            print(f"Ajout du match {joueur_1} VS {joueur_2}\n")
            liste_joueurs_par_score.append(joueur_1)
            liste_joueurs_par_score.append(joueur_2)
            instances_joueurs_a_trier.pop(instances_joueurs_a_trier.index(joueur_2))
            self.MATCHS_JOUES.append({joueur_1.id_joueur, joueur_2.id_joueur})
            test_match.clear()

        return liste_joueurs_par_score


class CreerTournoiControleur:
    """
    Crée un nouveau tournoi et l'enregistre dans la DB tournoi
    """

    def __init__(self):
        self.menu_principal_controleur = menu_controller.MenuPrincipalControleur()
        self.infos_tournoi = []
        self.liste_joueurs_serial = []
        self.liste_id_joueurs = []
        self.objet_tournoi = None
        self.joueur_db = model_player.JOUEUR_DB
        self.tournoi = model_tournament.Tournoi()

    def __call__(self):
        # Saisie des informations sur le tournoi
        self.infos_tournoi.append(self.ajout_nom())
        self.infos_tournoi.append(self.ajout_lieu())
        self.infos_tournoi.append(self.ajout_date())
        self.infos_tournoi.append(self.ajout_description())
        self.infos_tournoi.append(self.ajout_nombre_tours())
        self.infos_tournoi.append(self.ajout_nombre_joueurs())
        self.ajout_joueurs()
        dict_id_score_joueurs = dict.fromkeys(self.liste_id_joueurs, 0)

        # Ajout du tournoi dans la base de données
        self.infos_tournoi.append(dict_id_score_joueurs)
        self.tournoi.ajout_db(self.infos_tournoi)
        self.menu_principal_controleur()

    def ajout_nom(self):
        """
        Méthode pour saisir le nom du tournoi.

        Returns:
            str: Le nom du tournoi saisi par l'utilisateur.
        """
        # Saisie du nom du tournoi
        nom_tournoi = None
        nom_valide = False
        while not nom_valide:
            nom_tournoi = input("Entrez le NOM du Tournoi: ")
            if nom_tournoi != "":
                nom_valide = True
            else:
                main_view.Print.nom_obligatoire()
        return nom_tournoi

    def ajout_lieu(self):
        """
        Méthode pour saisir le lieu du tournoi.

        Returns:
            str: Le lieu du tournoi saisi par l'utilisateur.
        """
        # Saisie du lieu du tournoi
        lieu_tournoi = None
        lieu_valide = False
        while not lieu_valide:
            lieu_tournoi = input("Entrer le lieu du Tournoi: ")
            if lieu_tournoi != "":
                lieu_valide = True
            else:
                main_view.Print.lieu_obligatoire()

        return lieu_tournoi

    def ajout_date(self):
        """
        Méthode pour saisir la date du tournoi.

        Returns:
            str: La date du tournoi au format JJ/MM/AAAA saisie par l'utilisateur.
        """
        date = []  # Initialisation d'une liste pour stocker la date

        # Saisie du jour du tournoi
        jour_valide = False
        while not jour_valide:
            jour = input("Entrer le jour du Tournoi: ")
            if jour.isdigit() and (0 < int(jour) < 32):  # Vérification de la validité du jour
                jour_valide = True
                date.append(jour)  # Ajout du jour à la liste de la date
            else:
                main_view.Print.jour_obligatoire()  # Affichage du message d'erreur

        # Saisie du mois du tournoi
        mois_valide = False
        while not mois_valide:
            mois = input("Entrer le mois du Tournoi: ")
            if mois.isdigit() and (0 < int(mois) < 13):  # Vérification de la validité du mois
                mois_valide = True
                date.append(mois)  # Ajout du mois à la liste de la date
            else:
                main_view.Print.mois_obligatoire()  # Affichage du message d'erreur

        # Saisie de l'année du tournoi
        annee_valide = False
        while not annee_valide:
            annee = input("Entrer l'année du Tournoi: ")
            if annee.isdigit() and len(annee) == 4:  # Vérification de la validité de l'année
                annee_valide = True
                date.append(annee)  # Ajout de l'année à la liste de la date
            else:
                main_view.Print.annee_obligatoire()  # Affichage du message d'erreur

        # Construction de la date au format JJ/MM/AAAA et retour
        return f"{date[0]}/{date[1]}/{date[2]}"

    def ajout_nombre_tours(self):
        """
        Méthode pour saisir le nombre de tours du tournoi.

        Returns:
            int: Le nombre de tours du tournoi saisi par l'utilisateur.
        """
        nombre_tours = 4  # Nombre de tours par défaut
        main_view.Print.nombre_tours()  # Affichage du message pour entrer le nombre de tours
        entree_valide = False
        while not entree_valide:
            main_view.Print.choix_tours()  # Affichage de la demande de choix Y/N
            choix = input("==> ")
            if choix.upper() == "Y":
                nombre_tours = input("Entrer un nombre de tours: ")
                if nombre_tours.isdigit() and int(nombre_tours) > 0:  # Vérification de la validité de l'entrée
                    entree_valide = True
                else:
                    main_view.Print.tour_erreur()  # Affichage du message d'erreur
            if choix.upper() == "N":
                entree_valide = True
            if choix == "":
                main_view.Print.choix_yn()  # Affichage du message d'erreur si aucune option n'est choisie
        return int(nombre_tours)  # Retourne le nombre de tours saisi par l'utilisateur

    def ajout_description(self):
        """
        Méthode pour saisir la description du tournoi.

        Returns:
            str: La description du tournoi saisie par l'utilisateur.
        """
        # Saisie de la description du tournoi
        main_view.Print.description()
        description = input("==> ")
        return description

    def ajout_nombre_joueurs(self):
        """
        Méthode pour saisir le nombre de joueurs participants au tournoi.

        Returns:
            int: Le nombre de joueurs participants au tournoi saisi par l'utilisateur.
        """
        # Ajout des joueurs au tournoi
        nombre_joueurs = None
        entree_valide = False
        while not entree_valide:
            nombre_joueurs = input("Entrez le nombre de participants au tournoi: ")
            if (
                nombre_joueurs.isdigit() and int(nombre_joueurs) > 1 and (int(nombre_joueurs) % 2) == 0
            ):
                entree_valide = True
            else:
                main_view.Print.nombre_pair_impair()
        return int(nombre_joueurs)

    def ajout_joueurs(self):
        """
        Choix des joueurs depuis la DB et les ajoute à self.liste_id_joueurs
        """
        # Efface le terminal pour une meilleure lisibilité
        # Utils.clear_terminal()
        # Initialise la variable pour stocker l'ID du joueur choisi et pour vérifier si le choix est valide
        id_choisi = None
        choix_valide = False

        # Demande à l'utilisateur s'il veut ajouter un joueur
        while not choix_valide:
            choix = input("Ajouter un joueur au tournoi? Y/N ==> ")
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")  # Affiche la liste des joueurs inscrits
            if choix.upper() == "Y":
                choix_valide = True
            elif choix.upper() == "N":
                return  # Sort de la méthode si l'utilisateur choisit de ne pas ajouter de joueur

        # Affiche les joueurs disponibles dans la base de données
        for player in self.joueur_db:
            print(
                f"Joueur ID: {player.doc_id} - {player['Nom']} "
                f"{player['Prenom']}"
            )

        id_valide = False
        while not id_valide:
            # Demande à l'utilisateur l'ID du joueur à ajouter
            id_choisi = input("Entrer l'ID du joueur à ajouter au tournoi: ")
            # Affiche la liste des joueurs inscrits
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")
            if (
                id_choisi.isdigit() and int(id_choisi) > 0 and int(id_choisi) <= len(self.joueur_db)
            ):
                id_valide = True  # Vérifie si l'ID entré est valide
            else:
                print("Entrez une ID de joueur existant")  # Message d'erreur si l'ID entré n'est pas valide
        id_choisi = int(id_choisi)
        if id_choisi in self.liste_id_joueurs:
            print(
                f"Le joueur {id_choisi} est deja dans le tournoi !\n"
                f"Joueurs inscrits: {self.liste_id_joueurs}\n"
            )
            id_choisi = None
            self.ajout_joueurs()  # Appel récursif pour ajouter un autre joueur si celui-ci est déjà inscrit

        if id_choisi is not None:
            self.liste_id_joueurs.append(id_choisi)  # Ajoute l'ID du joueur à la liste des joueurs inscrits
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")  # Affiche la liste des joueurs inscrits
            self.ajout_joueurs()  # Appel récursif pour ajouter un autre joueur
