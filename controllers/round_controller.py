class RoundController:
    def __init__(self, round, round_view):
        self.round = round
        self.round_view = round_view

    def display_round_details(self):
        self.round_view.display_round_details(self.round)
