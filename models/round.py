class Round:
    def __init__(self, name, start_datetime=None, end_datetime=None, matches=None):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = matches or []

    def serialize(self):
        return {
            'name': self.name,
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime,
            'matches': self.matches
        }
