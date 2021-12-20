from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


class Peli:

    @staticmethod
    def aloita_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def aloita_helppo_yksinpeli():
        return KPSTekoaly()

    @staticmethod
    def aloita_vaikea_yksinpeli():
        return KPSParempiTekoaly()
