# controllers/tournament_controller.py
import json
from models.tournament import Tournament, Round, Match
from models.player import Player


class TournamentController:
    def __init__(self, tournament, tournament_view):
        self.tournament = tournament
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
                self.tournament_view.display_add_player_to_tournament_menu([(player.first_name, player.last_name) for player in available_players])

                # Demander à l'utilisateur de choisir des joueurs
                while True:
                    choice = self.tournament_view.get_selected_player(available_players)
                    if choice == "0":
                        break
                    else:
                        index = int(choice) - 1
                        if 0 <= index < len(available_players):
                            selected_player = available_players.pop(index)
                            self.tournament.registered_players.append(selected_player)
                            # Afficher le joueur ajouté dans la vue
                            self.tournament_view.display_player_added_to_tournament((selected_player.first_name, selected_player.last_name))
                        else:
                            # Afficher un message d'erreur dans la vue
                            self.tournament_view.display_players_added_successfully()

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
                'registered_players': [player.__dict__ for player in self.tournament.registered_players],
                'description': self.tournament.description
            }
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