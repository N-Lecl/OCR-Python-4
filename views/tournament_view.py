class TournamentView:
    def display_tournament_details(self, tournament):
        print(f"Tournament: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Start Date: {tournament.start_date}")
        print(f"End Date: {tournament.end_date}")
        print(f"Current Round: {tournament.current_round}")
        print("Players:")
        for player in tournament.players:
            print(f"- {player.first_name} {player.last_name}")

    def display_round_details(self, round):
        print(f"Round: {round.name}")
        print(f"Start Date and Time: {round.start_datetime}")
        print(f"End Date and Time: {round.end_datetime}")
        print("Matches:")
        for match in round.matches:
            print(f"- {match[0].first_name} vs {match[1].first_name}, Result: {match[0].result}")

    def display_tournament_report(self, tournament):
        print("Tournament Report:")
