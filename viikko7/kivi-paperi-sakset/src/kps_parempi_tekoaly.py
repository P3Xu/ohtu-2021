from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)
        self._ekan_siirto = None

    def _tokan_siirto(self):
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

    def _onko_ok_siirto(self, siirto):
        if self._ekan_siirto:
            self._tekoaly.aseta_siirto(self._ekan_siirto)

        return super()._onko_ok_siirto(siirto)
