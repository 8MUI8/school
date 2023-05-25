class Parti:
    def __init__(self, navn, retning):
        self._navn = navn
        self._retning = retning
        self._leder = None
        self._politikere = []
    
    def __str__(self):
        return f"{self._navn}, {self._leder}"
    
    def sett_leder(self, leder):
        for politiker in self._politikere:
            if leder == politiker:
                self._leder = leder
                return f"{leder} er ny leder av {self._navn}"
        return "FEIl"

    def legg_til_politiker(self, politiker):
        self._politikere.append(politiker)



if __name__ == "__main__":
    from politiker import Politiker
    jonas = Politiker("Jonas Gahr Støre", "Arbeiderpartiet", "Oslo", "1.1.1958", "Mann")
    erna = Politiker("Erna Solberg", "Høyre", "Oslo", "1.1.1958", "Kvinne")
    ap = Parti("Arbeiderpartiet", "sentrum-venstre")
    ap.legg_til_politiker(jonas)
    ap.sett_leder(jonas)
    assert ap.sett_leder(erna) == "FEIL" #Forsikrer meg om at det ikke skal være mulig å legge til Erna som leder i AP.
    print(ap)
    