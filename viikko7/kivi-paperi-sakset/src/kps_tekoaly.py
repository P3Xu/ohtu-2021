from KPS import KPS
from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self._tekoaly = Tekoaly()

    def _tokan_siirto(self):
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
