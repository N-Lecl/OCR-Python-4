from models.player import Player
from views.player_view import PlayerView
import json

class PlayerController:
    def __init__(self, player, player_view):
        self.players = [] 
        self.player = player
        self.player_view = player_view if player_view else PlayerView()

    def add_player_menu(self):
        self.player_view.display_add_player_menu()
        first_name = self.player_view.get_player_data_input("le prénom")
        last_name = self.player_view.get_player_data_input("le nom de famille")
        birth_date = self.player_view.get_player_data_input("la date de naissance (YYYY-MM-DD)")
        chess_id = self.player_view.get_player_data_input("l'identifiant national d'échecs")

        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.add_player(new_player)

    def add_player(self, player):
        # Charge les joueurs depuis le fichier JSON
        self.load_players_from_json('players_infos.json') 
        self.players.append(player)
        # Sauvegarde les joueurs après l'ajout
        self.save_players_to_json('players_infos.json')  
        self.player_view.display_player_added(player)

    def display_all_players(self):
        while True:
            self.player_view.display_players_list_menu()
            # Charge les joueurs depuis le fichier JSON
            self.load_players_from_json('players_infos.json')  
            if not self.players:
                print("Aucun joueur enregistré.")
            else:
                for player in self.players:
                    self.player_view.display_player(player)

            print("\n1. Retour au menu Joueurs")

            choice = self.player_view.get_player_input("\nChoisissez une option : ")
            if choice == "1":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    def save_players_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([player.__dict__ for player in self.players], file)

    def load_players_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                player_data = json.load(file)
                self.players = [Player(**data) for data in player_data]
        except FileNotFoundError:
            print("\nLe fichier JSON n'a pas été trouvé.")
