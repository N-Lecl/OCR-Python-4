from models.player import Player
from views.player_view import PlayerView
import json

class PlayerController:
    def __init__(self, player, player_view):
        self.players = [] 
        self.player = player
        self.player_view = player_view if player_view else PlayerView()

    def add_player_menu(self):
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("   _    _             _         _ _               __                              ")
        print("  /_\  (_) ___  _   _| |_    __| ( _   _ _ __     \ \  ___  _   _  ___ _   _ _ __ ")
        print(" //_\\ | |/ _ \| | | | __|  / _` || | | | '_ \     \ \/ _ \| | | |/ _ | | | | '__|")
        print("/  _  \| | (_) | |_| | |_  | (_| || |_| | | | | /\_/ | (_) | |_| |  __| |_| | |   ")
        print("\_/ \__/ |\___/ \__,_|\__|  \__,_| \__,_|_| |_| \___/ \___/ \__,_|\___|\__,_|_|   ")
        print("     |__/                                                                         ")
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        first_name = input("\nEntrez le prénom du joueur : ")
        last_name = input("Entrez le nom de famille du joueur : ")
        birth_date = input("Entrez la date de naissance du joueur (YYYY-MM-DD) : ")
        chess_id = input("Entrez l'identifiant national d'échecs du joueur : ")

        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.add_player(new_player)

    def add_player(self, player):
        self.players.append(player)
        self.save_players_to_json('players_infos.json') 
        print(f"Joueur ajouté : {player.first_name} {player.last_name}")

    def display_all_players(self):
        while True:
            print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("   __ _     _             _              _                                 ")
            print("  / /(_)___| |_ ___    __| | ___ ___    (_) ___  _   _  ___ _   _ _ __ ___ ")
            print(" / / | / __| __/ _ \  / _` |/ _ / __|   | |/ _ \| | | |/ _ | | | | '__/ __|")
            print("/ /__| \__ | ||  __/ | (_| |  __\__ \   | | (_) | |_| |  __| |_| | |  \__ \ ")
            print("\____|_|___/\__\___|  \__,_|\___|___/  _/ |\___/ \__,_|\___|\__,_|_|  |___/")
            print("                                      |__/                                 ")
            print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("")
            self.load_players_from_json('players_infos.json')
            if not self.players:
                print("Aucun joueur enregistré.")
            else:
                for player in self.players:
                    self.player_view.display_player(player)

            print("\n1. Retour au menu Joueurs")

            choice = input("\nChoisissez une option : ")
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

