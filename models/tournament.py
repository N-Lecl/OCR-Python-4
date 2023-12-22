# models/tournament.py

class Match:
    def __init__(self, player1, player2, result=None):
        self.player1 = player1
        self.player2 = player2
        self.result = result

    def to_dict(self):
        return {
            'player1': self.player1.to_dict(),
            'player2': self.player2.to_dict(),
            'result': self.result
        }

class Round:
    def __init__(self, name, start_datetime=None, end_datetime=None, matches=None):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = matches or []

    def to_dict(self):
        return {
            'name': self.name,
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime,
            'matches': [match.to_dict() for match in self.matches]
        }

class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, rounds=None,
                 registered_players=None, description=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds or []
        self.registered_players = registered_players or []
        self.description = description

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'num_rounds': self.num_rounds,
            'current_round': self.current_round,
            'rounds': [round.to_dict() for round in self.rounds],
            'registered_players': [player.to_dict() for player in self.registered_players],
            'description': self.description
        }
