class PlayerView:
    def get_player_input(self, prompt):
        return input(prompt)

    def display_player(self, player):
        print(f"Nom: {player.last_name}, Prénom: {player.first_name}, Date de naissance: {player.birth_date}, ID d'échecs: {player.chess_id}")

    def display_add_player_menu(self):
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("   _    _             _         _ _               __                              ")
        print("  /_\  (_) ___  _   _| |_    __| ( _   _ _ __     \ \  ___  _   _  ___ _   _ _ __ ") 
        print(" //_\\ | |/ _ \| | | | __|  / _` || | | | '_ \     \ \/ _ \| | | |/ _ | | | | '__|")
        print("/  _  \| | (_) | |_| | |_  | (_| || |_| | | | | /\_/ | (_) | |_| |  __| |_| | |   ")
        print("\_/ \__/ |\___/ \__,_|\__|  \__,_| \__,_|_| |_| \___/ \___/ \__,_|\___|\__,_|_|   ")
        print("     |__/                                                                         ")
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    def display_players_list_menu(self):
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("   __ _     _             _              _                                 ")
        print("  / /(_)___| |_ ___    __| | ___ ___    (_) ___  _   _  ___ _   _ _ __ ___ ")
        print(" / / | / __| __/ _ \  / _` |/ _ / __|   | |/ _ \| | | |/ _ | | | | '__/ __|")
        print("/ /__| \__ | ||  __/ | (_| |  __\__ \   | | (_) | |_| |  __| |_| | |  \__ \ ")
        print("\____|_|___/\__\___|  \__,_|\___|___/  _/ |\___/ \__,_|\___|\__,_|_|  |___/")
        print("                                      |__/                                 ")
        print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    def get_player_data_input(self, field):
        return self.get_player_input(f"Entrez {field} du joueur : ")

    def display_player_added(self, player):
        print(f"Joueur ajouté : {player.first_name} {player.last_name}")
