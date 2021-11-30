import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

        self.maito = Tuote("Maito", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteella(self):
        self.kori.lisaa_tuote(self.maito)

        hinta = self.kori.hinta()

        self.assertEqual(hinta, self.maito.hinta())

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteiden_summa(self):
        leipa = Tuote("Leipä", 2)

        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
