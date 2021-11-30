from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteet = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        count = 0

        for ostos in self.tuotteet:
            count += ostos.lukumaara()

        return count
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0

        for tuote in self.tuotteet:
            hinta += tuote.hinta()
        
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        maara = len(self.tuotteet)

        if maara == 0:
            self.tuotteet.append(Ostos(lisattava))
        else:
            for i in range(maara):
                ostos = self.tuotteet[i]

                if i < maara-1 and ostos.tuote == lisattava:
                    ostos.muuta_lukumaaraa(1)
                if i == maara-1:
                    if ostos.tuote == lisattava:
                        ostos.muuta_lukumaaraa(1)
                    else:
                        self.tuotteet.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.tuotteet:
            if ostos.tuote == poistettava:
                if ostos.lukumaara == 1:
                    self.tuotteet.remove(ostos)
                else:
                    ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self.tuotteet.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.tuotteet
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
