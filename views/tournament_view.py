# views/tournament_view.py

class TournamentView:
    def get_tournament_data_input(self, field, default=None):
        prompt = f"Entrez {field} du tournoi : "
        user_input = input(prompt).strip()
        return user_input if user_input else default

    def display_tournament_details(self, tournament):
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("\    ___     _        _ _           _         _____                             _ ")
        print("\   /   \___| |_ __ _(_) |___    __| |_   _  /__   \___  _   _ _ __ _ __   ___ (_)")
        print("\  / /\ / _ \ __/ _` | | / __|  / _` | | | |   / /\/ _ \| | | | '__| '_ \ / _ \| |")
        print("\ / /_//  __/ || (_| | | \__ \ | (_| | |_| |  / / | (_) | |_| | |  | | | | (_) | |")
        print("\/___,' \___|\__\__,_|_|_|___/  \__,_|\__,_|  \/   \___/ \__,_|_|  |_| |_|\___/|_|")
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.location}")
        print(f"Date de début: {tournament.start_date}")
        print(f"Date de fin: {tournament.end_date}")
        print(f"Nombre de tours: {tournament.num_rounds}")
        print(f"Tour actuel: {tournament.current_round}")
        print("Joueurs inscrits:")

        for player_data in tournament.registered_players:
            if isinstance(player_data, dict):
                # Si le joueur est stocké sous forme de dictionnaire, afficher ses détails
                print(f"  - {player_data['first_name']} {player_data['last_name']}")
            else:
                # Sinon, supposer que le joueur est déjà un objet Player
                print(f"  - {player_data.first_name} {player_data.last_name}")

        print(f"Description: {tournament.description}")
        
    def display_add_player_to_tournament_menu(self, available_players):
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("   _    _             _         _ _               __                              ")
        print("  /_\  (_) ___  _   _| |_    __| ( _   _ _ __     \ \  ___  _   _  ___ _   _ _ __ ") 
        print(" //_\\ | |/ _ \| | | | __|  / _` || | | | '_ \     \ \/ _ \| | | |/ _ | | | | '__|")
        print("/  _  \| | (_) | |_| | |_  | (_| || |_| | | | | /\_/ | (_) | |_| |  __| |_| | |   ")
        print("\_/ \__/ |\___/ \__,_|\__|  \__,_| \__,_|_| |_| \___/ \___/ \__,_|\___|\__,_|_|   ")
        print("     |__/                                                                         ")
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("\nMenu d'ajout de joueur au tournoi:")
        print("Liste des joueurs disponibles :")
        for index, player in enumerate(available_players, start=1):
            print(f"{index}. {player.first_name} {player.last_name}")

        print("\n1. Ajouter un joueur au tournoi")
        print("2. Retour au menu principal")

        choice = input("\nChoisissez une option (1 ou 2) : ")
        return choice
    
    def display_add_player_to_tournament_menu(self, available_players):
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("   _    _             _         _ _               __                              ")
        print("  / /(_)___| |_ ___    __| | ___  ___    (_) ___  _   _  ___ _   _ _ __ ___ ")
        print(" / / | / __| __/ _ \  / _` |/ _ \/ __|   | |/ _ \| | | |/ _ \ | | | '__/ __|")
        print("/ /__| \__ \ ||  __/ | (_| |  __/\__ \   | | (_) | |_| |  __/ |_| | |  \__ \ ")
        print("\____/_|___/\__\___|  \__,_|\___||___/  _/ |\___/ \__,_|\___|\__,_|_|  |___/")
        print("                                       |__/                                 ")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("\nMenu d'ajout de joueur au tournoi:")
        print("Liste des joueurs disponibles dans la vue :")
        for index, (first_name, last_name) in enumerate(available_players, start=1):
            print(f"{index}. {first_name} {last_name}")

        print("\n1. Ajouter un joueur au tournoi")
        print("2. Retour au menu principal")

    def get_selected_player(self, available_players):
        choice = input("\nChoisissez le numéro du joueur à ajouter au tournoi (0 pour terminer) : ")
        return choice

    def display_player_added_to_tournament(self, player_info):
        first_name, last_name = player_info
        print(f"Joueur ajouté au tournoi : {first_name} {last_name}")

    def display_players_added_successfully(self):
        print("Les joueurs ont été ajoutés avec succès au tournoi.")

    def display_players_file_not_found(self):
        print("\nLe fichier JSON des joueurs n'a pas été trouvé.")
