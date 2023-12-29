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
        print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        print("██████╗ ███████╗████████╗ █████╗ ██╗██╗     ███████╗    ██████╗ ██╗   ██╗    ████████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ ██████╗ ██╗")
        print("██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║     ██╔════╝    ██╔══██╗██║   ██║    ╚══██╔══╝██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔═══██╗██║")
        print("██║  ██║█████╗     ██║   ███████║██║██║     ███████╗    ██║  ██║██║   ██║       ██║   ██║   ██║██║   ██║██████╔╝██╔██╗ ██║██║   ██║██║")
        print("██║  ██║██╔══╝     ██║   ██╔══██║██║██║     ╚════██║    ██║  ██║██║   ██║       ██║   ██║   ██║██║   ██║██╔══██╗██║╚██╗██║██║   ██║██║")
        print("██████╔╝███████╗   ██║   ██║  ██║██║███████╗███████║    ██████╔╝╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝██║")
        print("╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝")
        print("")
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
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

    
    def display_add_player_to_tournament_menu(self, available_players, registered_players=None):
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

        # Filtrer les joueurs déjà inscrits
        available_players_filtered = [player for player in available_players if player not in registered_players]

        # Réinitialiser les numéros
        indexed_players = list(enumerate(available_players_filtered, start=1))

        for index, (first_name, last_name) in indexed_players:
            print(f"{index}. {first_name} {last_name}")

        # Afficher les joueurs déjà présents dans le tournoi
        if registered_players:
            print("\nJoueurs déjà présents dans le tournoi :")
            for player_info in registered_players:
                first_name, last_name = player_info
                print(f"{first_name} {last_name}")

    def get_selected_player(self, available_players, registered_players):
        while True:
            choice = input("\nChoisissez le numéro du joueur à ajouter au tournoi (0 pour terminer) : ")
            if choice == "0":
                break
            elif choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(available_players):
                    selected_player = available_players[index]
                    # Vérifier si le nom du joueur est déjà présent dans la liste des joueurs du tournoi
                    if f"{selected_player.first_name} {selected_player.last_name}" not in [f"{player.first_name} {player.last_name}" for player in registered_players]:
                        return selected_player
                    else:
                        print("Le joueur est déjà présent dans le tournoi. Veuillez choisir un autre joueur.")
                else:
                    print("Option invalide. Veuillez choisir un numéro valide.")
            else:
                print("Option invalide. Veuillez choisir un numéro valide.")
        return None




    def display_player_added_to_tournament(self, player_info):
        first_name, last_name = player_info
        print(f"Joueur ajouté au tournoi : {first_name} {last_name}")

    def display_players_added_successfully(self):
        print("Les joueurs ont été ajoutés avec succès au tournoi.")

    def display_players_file_not_found(self):
        print("\nLe fichier JSON des joueurs n'a pas été trouvé.")

    def display_current_round_matches(self, current_round):
        Utils.clear_terminal()
        print(f"\nAffichage des matchs pour le {current_round} tour :")
        for match in current_round.matches:
            player1, player2 = match.players
            print(f"{player1.full_name()} vs {player2.full_name()}")