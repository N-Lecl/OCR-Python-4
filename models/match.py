class Match:
    """Class representing a model for a Match"""
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
