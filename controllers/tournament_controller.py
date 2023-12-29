# controllers/tournament_controller.py
import json
from models.tournament import Tournament, Round, Match
from models.player import Player


class TournamentController:
    def __init__(self, tournament_model, tournament_view):
        self.tournament = None  # Initialisation à None, car le tournoi n'est pas encore créé
        self.tournament_model = tournament_model
        self.tournament_view = tournament_view

    def create_tournament(self):
        name = self.tournament_view.get_tournament_data_input("le nom du tournoi")
        location = self.tournament_view.get_tournament_data_input("le lieu du tournoi")
        start_date = self.tournament_view.get_tournament_data_input("la date de début du tournoi (YYYY-MM-DD)")
        end_date = self.tournament_view.get_tournament_data_input("la date de fin du tournoi (YYYY-MM-DD)")
        num_rounds = self.tournament_view.get_tournament_data_input("le nombre de tours (par défaut 4)", default=4)
        description = self.tournament_view.get_tournament_data_input("la description du tournoi (optionnelle)")
        # Initialisez registered_players avec une liste vide lors de la création d'un nouveau tournoi
        registered_players = []
        

        # Créer le tournoi
        self.tournament = Tournament(name, location, start_date, end_date, num_rounds, description=description, registered_players=registered_players)

        # Enregistrer le tournoi dans un fichier JSON
        self.save_tournament_to_json('tournament_info.json')

    def add_players_to_tournament(self):
        try:
            # Charger les joueurs depuis le fichier players_infos.json
            with open('players_infos.json', 'r') as file:
                player_data = json.load(file)
                available_players = [Player(**data) for data in player_data]

                # Vérifier si self.tournament est None et initialiser s'il l'est
                if self.tournament is None:
                    self.load_tournament_from_json('tournament_info.json')

                # Afficher la liste des joueurs disponibles dans la vue
                self.tournament_view.display_add_player_to_tournament_menu(
                [(player.first_name, player.last_name) for player in available_players],
                [(player.first_name, player.last_name) for player in self.tournament.registered_players]
            )

            # Demander à l'utilisateur de choisir des joueurs
            while True:
                selected_player = self.tournament_view.get_selected_player(available_players, self.tournament.registered_players)
                if selected_player is None:
                    break

                self.tournament.registered_players.append(selected_player)
                # Afficher le joueur ajouté dans la vue
                self.tournament_view.display_player_added_to_tournament((selected_player.first_name, selected_player.last_name))
                # Sauvegarder les modifications dans le fichier tournament_info.json
                self.save_tournament_to_json('tournament_info.json')
                # Afficher un message de succès dans la vue
                self.tournament_view.display_players_added_successfully()

        except FileNotFoundError:
            # Afficher un message d'erreur dans la vue
            self.tournament_view.display_players_file_not_found()


    
    #TODO: use load_tournament_from_json
    def display_tournament_details(self):
        try:
            with open('tournament_info.json', 'r') as file:
                tournament_data = json.load(file)
                self.tournament = Tournament(**tournament_data)
                self.tournament_view.display_tournament_details(self.tournament)

                while True:
                    print("\n1. Retour au menu principal")
                    choice = input("\nChoisissez une option (1) : ")
                    if choice == "1":
                        break
                    else:
                        print("Option invalide. Veuillez choisir une option valide.")
                        
        except FileNotFoundError:
            print("\nLe fichier JSON du tournoi n'a pas été trouvé.")

    def save_tournament_to_json(self, filename):
        with open(filename, 'w') as file:
            # Convertir l'objet Tournament en dictionnaire avant de le sauvegarder
            tournament_data = {
                'name': self.tournament.name,
                'location': self.tournament.location,
                'start_date': self.tournament.start_date,
                'end_date': self.tournament.end_date,
                'num_rounds': self.tournament.num_rounds,
                'current_round': self.tournament.current_round,
                'registered_players': [],
                'description': self.tournament.description
            }

            for player in self.tournament.registered_players:
                if isinstance(player, Player):
                    tournament_data['registered_players'].append(player.__dict__)
                elif isinstance(player, dict):
                    tournament_data['registered_players'].append(player)

            json.dump(tournament_data, file)

    def load_tournament_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                tournament_data = json.load(file)

                # Convertir les données des joueurs en objets Player
                player_data_list = tournament_data.get('registered_players', [])
                players = [Player(**player_data) if isinstance(player_data, dict) else player_data for player_data in player_data_list]

                # Mettre à jour le dictionnaire avec la liste d'objets Player
                tournament_data['registered_players'] = players

                self.tournament = Tournament(**tournament_data)
        except FileNotFoundError:
            print("\nLe fichier JSON du tournoi n'a pas été trouvé.")
            
    def start_tournament(self):
        if not self.tournament.is_ready():
            print("Le tournoi n'est pas prêt à démarrer. Assurez-vous d'avoir ajouté tous les joueurs.")
            return

        self.generate_pairs_for_round()
        self.tournament_view.display_current_round_matches(self.tournament.current_round)

    def generate_pairs_for_round(self):
        current_round = self.tournament.current_round

        if not current_round.is_completed:
            # Vérifiez si les paires ont déjà été générées pour ce tour
            if not current_round.matches:
                # Générez les paires en fonction des résultats des tours précédents
                sorted_players = self.tournament.get_sorted_players()
                pairings = self.create_pairings(sorted_players)

                # Enregistrez les paires générées dans le tour actuel
                current_round.matches = pairings

            self.tournament_view.display_current_round_matches(current_round)

        else:
            print("Le tour en cours est déjà terminé.")
            
    def create_pairings(self, players):
        # Assurez-vous que le nombre de joueurs est pair
        if len(players) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair pour créer des paires.")

        # Divisez les joueurs en deux groupes égaux
        half = len(players) // 2
        group1, group2 = players[:half], players[half:]

        # Générez toutes les combinaisons possibles des deux groupes
        pairings = list(itertools.product(group1, group2))

        # Mélangez les paires pour éviter des matchs prévisibles
        random.shuffle(pairings)

        # Vérifiez et évitez les matchs identiques par rapport aux tours précédents
        previous_matches = self.tournament.get_previous_rounds_matches()
        pairings = self.avoid_identical_matches(pairings, previous_matches)

        return pairings

    def avoid_identical_matches(self, pairings, previous_matches):
        # Vérifiez chaque paire pour éviter les matchs identiques
        filtered_pairings = []
        for pairing in pairings:
            reverse_pairing = (pairing[1], pairing[0])

            if pairing not in previous_matches and reverse_pairing not in previous_matches:
                filtered_pairings.append(pairing)

        return filtered_pairings

    def enter_match_results(self):
        if not self.tournament.is_ongoing():
            print("Le tournoi n'est pas en cours. Démarrez le tournoi d'abord.")
            return

        self.tournament_view.display_current_round_matches(self.tournament.current_round)
        self.enter_results_for_current_round()
        self.tournament.update_players_scores()

        if not self.tournament.is_finished():
            self.tournament.next_round()
            self.generate_pairs_for_round()
        else:
            print("Le tournoi est terminé.")

    def display_current_round_matches(self, current_round):
        Utils.clear_terminal()
        print(f"\nAffichage des matchs pour le {current_round} tour :")
        for match in current_round.matches:
            player1, player2 = match.players
            print(f"{player1.full_name()} vs {player2.full_name()}")

    def enter_results_for_current_round(self):
        print("\nEntrez les résultats pour chaque match (1 pour la victoire, 0 pour la défaite, 0.5 pour le match nul) :")
        for match in self.tournament.current_round.matches:
            result = input(f"Résultat pour {match.players[0].full_name()} vs {match.players[1].full_name()} : ").strip()
            while result not in ["0", "0.5", "1"]:
                print("Saisie invalide. Veuillez entrer 1 pour la victoire, 0 pour la défaite, ou 0.5 pour le match nul.")
                result = input(f"Résultat pour {match.players[0].full_name()} vs {match.players[1].full_name()} : ").strip()

            match.set_result(float(result))

        print("Résultats enregistrés avec succès.")