import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipä", 2)

    # case 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # case 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # case 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteella(self):
        self.kori.lisaa_tuote(self.maito)

        hinta = self.kori.hinta()

        self.assertEqual(hinta, self.maito.hinta())

    # case 4
    def test_kaksi_eri_tuotetta_koriin_ja_korissa_tällöin_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)


        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # case 5
    def test_lisaa_kaksi_eri_tuotetta_ja_tarkista_korin_hinta_samaksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.hinta(), self.maito.hinta()+self.leipa.hinta())

    # case 6
    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # case 7
    def test_kahden_saman_tuotteen_jalkeen_ostoskorin_hinta_tasmaa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 6)

    # case 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    # case 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_ostoksella_validit_parametrit(self):
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

        self.kori.lisaa_tuote(self.maito)

    # case 10
    def test_kahden_eri_ostoksen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    # case 11
    def test_kahden_saman_ostoksen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    # case 12
    def test_kahden_saman_ostoksen_jalkeen_korissa_ostos_jolla_parametrit_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[-1]

        self.assertEqual(self.maito.nimi(), ostos.tuotteen_nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    # case 13
    def test_korissa_kaksi_samaa_tuotetta_poiston_jalkeen_yksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # case 14
    def test_korin_ainoa_tuote_poistettaessa_kori_on_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
