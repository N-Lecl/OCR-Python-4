from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.round_view import RoundView
from models.tournament import Tournament
from models.player import Player
from models.round import Round

class MainController:
    def __init__(self):
        self.tournament = Tournament("Chess Masters", "City Hall", "2023-01-01", "2023-01-07")
        self.tournament_view = TournamentView()
        self.tournament_controller = TournamentController(self.tournament, self.tournament_view)

        # For simplicity, let's create a player and a round for testing
        player = Player("John", "Doe", "1990-01-01", "AB12345")
        player_view = PlayerView()
        player_controller = PlayerController(player, player_view)

        round_1 = Round("Round 1")
        round_view = RoundView()
        round_controller = RoundController(round_1, round_view)

    def run(self):
        # Simulate user actions
        self.tournament_controller.display_tournament_details()
        print("\n=== Simulating Player Details ===")
        self.tournament_controller.display_round_details(1)

        print("\n=== Simulating Round Details ===")
        round_controller.display_round_details()

if __name__ == "__main__":
    main_controller = MainController()
    main_controller.run()
