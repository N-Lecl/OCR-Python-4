class PlayerController:
    def __init__(self, player, player_view):
        self.player = player
        self.player_view = player_view

    def display_player_details(self):
        self.player_view.display_player_details(self.player)
