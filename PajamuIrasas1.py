from Irasas_1 import Irasas

class PajamuIrasas(Irasas):
    def __init__(self, tipas, suma, siuntejas, papildoma_informacija):
        super().__init__(tipas, suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija