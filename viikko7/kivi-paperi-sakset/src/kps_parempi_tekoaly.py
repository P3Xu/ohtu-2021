from KPS import KPS
from tekoaly import Tekoaly
from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self._tekoaly = Tekoaly()
        self._ekan_siirto = None

    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")
            tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")

        self._ekan_siirto = ekan_siirto

        return ekan_siirto

    def _tokan_siirto(self):
        if self._ekan_siirto:
            tokan_siirto = self._tekoaly.anna_siirto(self._ekan_siirto)
        else:
            tokan_siirto = self._tekoaly.anna_siirto()
        
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
