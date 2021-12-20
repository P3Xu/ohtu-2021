from tuomari import Tuomari

class KPS:
    def pelaa(self):
        tuomari = Tuomari()


        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._tokan_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._tokan_siirto()

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_siirto(self):
        return 0
