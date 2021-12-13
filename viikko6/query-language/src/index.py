from statistics import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .playsIn("EDM")
        .hasAtLeast(40, "points")
        .build()
    )

    m3 = (
        query
            .playsIn("NYR")
            .hasAtLeast(5, "goals")
            .hasFewerThan(10, "goals")
            .build()
    )

    m4 = (
        query
            .playsIn("ANA")
            .build()
    )

    #matcher = query.oneOf(m1, m2, m3, m4).build()

    matcher = (
        query
            .oneOf(
            query.playsIn("PHI")
                .hasAtLeast(10, "assists")
                .hasFewerThan(5, "goals")
                .build(),
            query.playsIn("EDM")
                .hasAtLeast(40, "points")
                .build(),
            query.playsIn("NYR")
                .hasAtLeast(5, "goals")
                .hasFewerThan(10, "goals")
                .build(),
            query.playsIn("ANA")
                .build()
            )
            .build()
        )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
