from peli import Peli

def main():
    peli = Peli()

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = peli.aloita_kaksinpeli()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = peli.aloita_helppo_yksinpeli()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = peli.aloita_vaikea_yksinpeli()
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
