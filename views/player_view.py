class PlayerView:
    def display_player(self, player):
        print(f"Nom: {player.last_name}, Prénom: {player.first_name}, Date de naissance: {player.birth_date}, ID d'échecs: {player.chess_id}")
