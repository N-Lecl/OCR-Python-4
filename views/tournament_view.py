# views/tournament_view.py

class TournamentView:
    def get_tournament_data_input(self, field, default=None):
        prompt = f"Entrez {field} du tournoi : "
        user_input = input(prompt).strip()
        return user_input if user_input else default

    def display_tournament_details(self, tournament):
        print("\nDétails du Tournoi:")
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.location}")
        print(f"Date de début: {tournament.start_date}")
        print(f"Date de fin: {tournament.end_date}")
        print(f"Nombre de tours: {tournament.num_rounds}")
        print(f"Tour actuel: {tournament.current_round}")
        print("Joueurs inscrits:")
        for player in tournament.registered_players:
            print(f"  - {player.first_name} {player.last_name}")
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
