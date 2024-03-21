from collections import deque
from operator import attrgetter

from controllers import menu_controller
from models import model_player, model_tournament, model_round
from view import main_view
from utils.utils import Utils


class LancerTournoiControleur:
    """
    Lance un tournoi deja créé.
    """

    MATCHS_JOUES = []
    TOURS_JOUES = []

    def __init__(self):
        self.affiche_tournoi = None
        self.tournoi = None
        self.tour = model_round.Tour()
        self.liste_joueurs_trie = []
        self.menu_principal_controleur = menu_controller.MenuPrincipalControleur()
        self.vue_resultats = main_view.ResultatsTournoi()
        self.joueur = model_player.Joueur()

    def __call__(self):
        self.tournoi_obj = self.selection_tournoi()
        self.liste_joueurs_trie = self.triage_initial(self.tournoi_obj)

        self.tournoi_obj.liste_tours.append(
            self.tour.lancer_tour(self.liste_joueurs_trie.copy(), self.tournoi_obj)
        )
        self.sauvegarde_tournoi(self.tournoi_obj)

        for tour in range(int(self.tournoi_obj.nombre_tours) - 1):
            self.liste_joueurs_trie_suivant = self.triage_tours_suivants(
                self.liste_joueurs_trie.copy()
            )
            self.tournoi_obj.liste_tours.append(
                self.tour.lancer_tour(self.liste_joueurs_trie_suivant, self.tournoi_obj)
            )
            self.sauvegarde_tournoi(self.tournoi_obj)

        self.vue_resultats(self.tournoi_obj, self.liste_joueurs_trie)
        self.menu_principal_controleur()

    def sauvegarde_tournoi(self, tournoi_obj):
        """
        Méthode de sauvegarde de tournoi dans la DB tournoi
        :type tournoi_obj: object Tournoi
        """
        tournoi_db = model_tournament.TOURNOI_DB
        tournoi_choisi = model_tournament.TOURNOI_DB.get(doc_id=tournoi_obj.id_tournoi)
        dict_ids_scores_joueurs = tournoi_choisi["Liste joueurs"]

        for match in self.tour.liste_tours:
            id_joueur_1 = str(match.joueur_1.id_joueur)
            score_joueur_1 = match.joueur_1.total_points_tournoi
            dict_ids_scores_joueurs[id_joueur_1] = score_joueur_1

            id_joueur_2 = str(match.joueur_2.id_joueur)
            score_joueur_2 = match.joueur_2.total_points_tournoi
            dict_ids_scores_joueurs[id_joueur_2] = score_joueur_2

        tournoi_db.update(
            {"Liste joueurs": dict_ids_scores_joueurs}, doc_ids=[tournoi_obj.id_tournoi]
        )

        table_tours = tournoi_db.table("tours")

        tour_obj = tournoi_obj.liste_tours[-1]
        tour_serialise = tour_obj.serialise()
        tour_serialise["Liste matchs termines"] = tour_obj.liste_matchs_termines

        id_tour = table_tours.insert(tour_serialise)
        LancerTournoiControleur.TOURS_JOUES.append(id_tour)
        tournoi_db.update(
            {"Tours": LancerTournoiControleur.TOURS_JOUES},
            doc_ids=[tournoi_obj.id_tournoi],
        )

        main_view.MainView.afficher_message_sauvegarde()
        choix_valide = False
        while not choix_valide:
            choix = input("Y/N ==> ")
            if choix.upper() == "Y":
                choix_valide = True
                self.menu_principal_controleur()
            elif choix.upper() == "N":
                choix_valide = True
            else:
                main_view.Print.id_tournoi_valide()

    def chargement_tournoi(self):
        """
        Méthode de chargement de tournoi depuis la DB tournoi
        """
        self.affiche_tournoi = main_view.AfficheChargementTournoi()
        self.tournoi = model_tournament.Tournoi()
        self.model_player = model_player.Joueur()
        tournoi_db = model_tournament.TOURNOI_DB
        table_tours = tournoi_db.table("tours")
        instances_tours = []

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
            main_view.Print.tournoi_non_termine()
            self.menu_principal_controleur()

        for tour in range(int(tournoi_obj.nombre_tours) - len(tournoi_obj.liste_tours)):
            print(tournoi_obj)
            joueurs_tries = self.triage_tours_suivants(liste_obj_joueurs.copy())
            tournoi_obj.liste_tours.append(
                self.tour.lancer_tour(joueurs_tries, tournoi_obj)
            )
            self.sauvegarde_tournoi(tournoi_obj)

        self.vue_resultats(tournoi_obj, liste_obj_joueurs)
        self.menu_principal_controleur()

    def selection_tournoi(self):
        """
        Méthode pour sélectionner un tournoi non démarré.
        :rtype: object Tournoi
        """
        self.affiche_tournoi = main_view.AfficheTournoi()
        self.tournoi = model_tournament.Tournoi()

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

            tournoi_choisi = model_tournament.TOURNOI_DB.get(doc_id=int(choix))
            tournoi_obj = self.tournoi.creer_instance_tournoi(tournoi_choisi)
            return tournoi_obj
        else:
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
        ids_joueurs = tournoi.ids_scores_joueurs
        instances_joueurs = []
        liste_joueurs_tri = []

        for id_joueur in ids_joueurs:
            joueur = model_player.JOUEUR_DB.get(doc_id=int(id_joueur))
            joueur_obj = self.joueur.creer_instance_joueur(joueur)
            instances_joueurs.append(joueur_obj)

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
        test_match = set()
        liste_joueurs_par_score = []

        instances_joueurs_a_trier.sort(
            key=attrgetter("total_points_tournoi"), reverse=True
        )

        queue = deque(instances_joueurs_a_trier)
        while len(queue) > 1:
            joueur_1 = queue.popleft()
            joueur_2 = None
            for i in range(0, len(queue)):
                joueur_2_tmp = queue[i]

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
        self.infos_tournoi.append(self.ajout_nom())
        self.infos_tournoi.append(self.ajout_lieu())
        self.infos_tournoi.append(self.ajout_date())
        self.infos_tournoi.append(self.ajout_description())
        self.infos_tournoi.append(self.ajout_nombre_tours())
        self.infos_tournoi.append(self.ajout_nombre_joueurs())
        self.ajout_joueurs()
        dict_id_score_joueurs = dict.fromkeys(self.liste_id_joueurs, 0)

        self.infos_tournoi.append(dict_id_score_joueurs)
        self.tournoi.ajout_db(self.infos_tournoi)
        self.menu_principal_controleur()

    def ajout_nom(self):
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
        date = []

        jour_valide = False
        while not jour_valide:
            jour = input("Entrer le jour du Tournoi: ")
            if jour.isdigit() and (0 < int(jour) < 32):
                jour_valide = True
                date.append(jour)
            else:
                main_view.Print.jour_obligatoire()

        mois_valide = False
        while not mois_valide:
            mois = input("Entrer le mois du Tournoi: ")
            if mois.isdigit() and (0 < int(mois) < 13):
                mois_valide = True
                date.append(mois)
            else:
                main_view.Print.mois_obligatoire()

        annee_valide = False
        while not annee_valide:
            annee = input("Entrer l'année du Tournoi: ")
            if annee.isdigit() and len(annee) == 4:
                annee_valide = True
                date.append(annee)
            else:
                main_view.Print.annee_obligatoire()

        return f"{date[0]}/{date[1]}/{date[2]}"

    def ajout_nombre_tours(self):
        nombre_tours = 4
        main_view.Print.nombre_tours()
        entree_valide = False
        while not entree_valide:
            main_view.Print.choix_tours()
            choix = input("==> ")
            if choix.upper() == "Y":
                nombre_tours = input("Entrer un nombre de tours: ")
                if nombre_tours.isdigit() and int(nombre_tours) > 0:
                    entree_valide = True
                else:
                    main_view.Print.tour_erreur()
            if choix.upper() == "N":
                entree_valide = True
            if choix == "":
                main_view.Print.choix_yn()
        return int(nombre_tours)

    def ajout_description(self):
        main_view.Print.description()
        description = input("==> ")
        return description

    def ajout_nombre_joueurs(self):
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
        Utils.clear_terminal()
        id_choisi = None
        choix_valide = False
        while not choix_valide:
            choix = input("Ajouter un joueur au tournoi? Y/N ==> ")
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")
            if choix.upper() == "Y":
                choix_valide = True
            elif choix.upper() == "N":
                return

        for player in self.joueur_db:
            print(
                f"Joueur ID: {player.doc_id} - {player['Nom']} "
                f"{player['Prenom']}"
            )

        id_valide = False
        while not id_valide:
            id_choisi = input("Entrer l'ID du joueur à ajouter au tournoi: ")
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")
            if (
                id_choisi.isdigit() and int(id_choisi) > 0 and int(id_choisi) <= len(self.joueur_db)
            ):
                id_valide = True
            else:
                print("Entrez une ID de joueur existant")
        id_choisi = int(id_choisi)
        if id_choisi in self.liste_id_joueurs:
            print(
                f"Le joueur {id_choisi} est deja dans le tournoi !\n"
                f"Joueurs inscrits: {self.liste_id_joueurs}\n"
            )
            id_choisi = None
            self.ajout_joueurs()

        if id_choisi is not None:
            self.liste_id_joueurs.append(id_choisi)
            print(f"Joueurs inscrits: {self.liste_id_joueurs}\n")
            self.ajout_joueurs()
