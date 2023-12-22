from utils.utils import Utils

class TournamentView:
    def get_tournament_data_input(self, field, default=None):
        Utils.clear_terminal()
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print(" ██████╗██████╗ ███████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗    ████████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ ██████╗ ██╗")
        print("██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║    ╚══██╔══╝██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔═══██╗██║")
        print("██║     ██████╔╝█████╗  ███████║   ██║   ██║██║   ██║██╔██╗ ██║       ██║   ██║   ██║██║   ██║██████╔╝██╔██╗ ██║██║   ██║██║")
        print("██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║       ██║   ██║   ██║██║   ██║██╔══██╗██║╚██╗██║██║   ██║██║")
        print("╚██████╗██║  ██║███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝██║")
        print(" ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝")
        print("")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("")
        prompt = f"Entrez {field} du tournoi : "
        user_input = input(prompt).strip()
        return user_input if user_input else default

    def display_tournament_details(self, tournament):
        Utils.clear_terminal()
        print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("██████╗ ███████╗████████╗ █████╗ ██╗██╗     ███████╗    ██████╗ ██╗   ██╗    ████████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ ██████╗ ██╗")
        print("██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║     ██╔════╝    ██╔══██╗██║   ██║    ╚══██╔══╝██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔═══██╗██║")
        print("██║  ██║█████╗     ██║   ███████║██║██║     ███████╗    ██║  ██║██║   ██║       ██║   ██║   ██║██║   ██║██████╔╝██╔██╗ ██║██║   ██║██║")
        print("██║  ██║██╔══╝     ██║   ██╔══██║██║██║     ╚════██║    ██║  ██║██║   ██║       ██║   ██║   ██║██║   ██║██╔══██╗██║╚██╗██║██║   ██║██║")
        print("██████╔╝███████╗   ██║   ██║  ██║██║███████╗███████║    ██████╔╝╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝██║")
        print("╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝")
        print("")
        print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
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
        Utils.clear_terminal()
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print(" █████╗      ██╗ ██████╗ ██╗   ██╗████████╗    ██████╗ ██╗   ██╗███╗   ██╗         ██╗ ██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ ")
        print("██╔══██╗     ██║██╔═══██╗██║   ██║╚══██╔══╝    ██╔══██╗██║   ██║████╗  ██║         ██║██╔═══██╗██║   ██║██╔════╝██║   ██║██╔══██╗") 
        print("███████║     ██║██║   ██║██║   ██║   ██║       ██║  ██║██║   ██║██╔██╗ ██║         ██║██║   ██║██║   ██║█████╗  ██║   ██║██████╔╝")
        print("██╔══██║██   ██║██║   ██║██║   ██║   ██║       ██║  ██║██║   ██║██║╚██╗██║    ██   ██║██║   ██║██║   ██║██╔══╝  ██║   ██║██╔══██╗")
        print("██║  ██║╚█████╔╝╚██████╔╝╚██████╔╝   ██║       ██████╔╝╚██████╔╝██║ ╚████║    ╚█████╔╝╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║  ██║")
        print("╚═╝  ╚═╝ ╚════╝  ╚═════╝  ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝     ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝")
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("")
        print("Liste des joueurs disponibles :")
        for index, player in enumerate(available_players, start=1):
            print(f"{index}. {player.first_name} {player.last_name}")

        print("\n1. Ajouter un joueur au tournoi")
        print("2. Retour au menu principal")

        choice = input("\nChoisissez une option (1 ou 2) : ")
        return choice
    
    def display_add_player_to_tournament_menu(self, available_players):
        Utils.clear_terminal()
        print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("██╗     ██╗███████╗████████╗███████╗    ██████╗ ███████╗███████╗         ██╗ ██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ ███████╗")
        print("██║     ██║██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝██╔════╝         ██║██╔═══██╗██║   ██║██╔════╝██║   ██║██╔══██╗██╔════╝")
        print("██║     ██║███████╗   ██║   █████╗      ██║  ██║█████╗  ███████╗         ██║██║   ██║██║   ██║█████╗  ██║   ██║██████╔╝███████╗")
        print("██║     ██║╚════██║   ██║   ██╔══╝      ██║  ██║██╔══╝  ╚════██║    ██   ██║██║   ██║██║   ██║██╔══╝  ██║   ██║██╔══██╗╚════██║")
        print("███████╗██║███████║   ██║   ███████╗    ██████╔╝███████╗███████║    ╚█████╔╝╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║  ██║███████║")
        print("╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝╚══════╝     ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝")
        print("")
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("")
        print("Liste des joueurs disponibles :")
        for index, (first_name, last_name) in enumerate(available_players, start=1):
            print(f"{index}. {first_name} {last_name}")

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
