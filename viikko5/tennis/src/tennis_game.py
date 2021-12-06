from entities.scores import Scores

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def won_point(self, player):
        player.score = player.score + 1

    def get_score(self):
        scores = Scores().get_scores()

        return scores[str(f"{self.player1.score}-{self.player2.score}")]
