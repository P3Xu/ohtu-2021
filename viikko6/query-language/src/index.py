from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, PlaysIn, Not

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    """matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )"""

    """matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )"""

    #matcher = Not(HasAtLeast(1, "goals"))

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    #t1 = reader.get_players()
    #t2 = stats.matches(matcher)

    for player in stats.matches(matcher):
        #    pass
        print(player)

    #for player in reader.get_players():
    #    print(player)

    #print(matcher.matches(reader.get_players()[0]))

    #print(len(t1))
    #print(len(t2))

if __name__ == "__main__":
    main()
