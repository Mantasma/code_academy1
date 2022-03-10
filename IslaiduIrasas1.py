from Irasas_1 import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, tipas, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(tipas, suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga