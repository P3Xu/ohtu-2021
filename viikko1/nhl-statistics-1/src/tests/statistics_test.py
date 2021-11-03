import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_is_not_none(self):
        self.assertIsNotNone(self.statistics.search("Semenko"))
    
    def test_search_is_none(self):
        self.assertIsNone(self.statistics.search("Selänne"))

    def test_team_returns_list(self):
        self.assertIsInstance(self.statistics.team("EDM"), list)
    
    def test_team_returns_empty_list(self):
        self.assertEqual(len(self.statistics.team("PHI")), 0)

    def test_top_scorers(self):
        self.assertEqual(len(self.statistics.top_scorers(5)), 5)
