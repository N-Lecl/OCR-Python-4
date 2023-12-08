class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, players=None, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.players = players or []
        self.description = description
        self.rounds = []

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'num_rounds': self.num_rounds,
            'current_round': self.current_round,
            'players': [player.to_dict() for player in self.players],
            'description': self.description,
            'rounds': [round.to_dict() for round in self.rounds]
        }
