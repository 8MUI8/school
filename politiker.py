class Politiker:
    def __init__(self, navn, parti, fylke, f_dato, kjonn):
        self._navn = navn
        self._parti = parti
        self._fylke = fylke
        self._f_dato = f_dato
        self._kjonn = kjonn

    def __str__(self):
        return f"{self._navn} ({self._parti})"
        

if __name__ == "__main__":
    print("test_politiker")
    jonas = Politiker("Jonas Gahr Støre", "AP", "Oslo", "1.1.1958", "Mann")
    print(jonas)
