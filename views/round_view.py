class RoundView:
    def display_round_details(self, round):
        print(f"Round: {round.name}")
        print(f"Start Date and Time: {round.start_datetime}")
        print(f"End Date and Time: {round.end_datetime}")
        print("Matches:")
        for match in round.matches:
            print(f"- {match[0].first_name} vs {match[1].first_name}, Result: {match[0].result}")
