class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality: str):
        players = [player for player in self.reader.get_players() if player.nationality == nationality]

        players.sort(key=lambda x: x.goals+x.assists, reverse=True)

        return players
