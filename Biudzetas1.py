from IslaiduIrasas1 import IslaiduIrasas
from PajamuIrasas1 import PajamuIrasas

class Biudzetas(PajamuIrasas,IslaiduIrasas):


    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        pajamos = PajamuIrasas("Pajamos", suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = IslaiduIrasas("Islaidos", suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            if irasas.tipas == "Islaidos":
                suma -= irasas.suma
        print(f'Balansas yra: {suma}')

    def parodyti_ataskaita(self):
        # for irasas1 in self.zurnalas:
        #     print(irasas1)
        for x in self.zurnalas:
            if isinstance(x, PajamuIrasas):
                # print(x, suma)
                print(f"Pajamos: {x.suma} {x.siuntejas} {x.papildoma_informacija}")
            elif isinstance(x, IslaiduIrasas):
                # print(x, suma)
                print(f"Išlaidos: {x.suma} {x.atsiskaitymo_budas} {x.isigyta_preke_paslauga}")

    def biudzeto_pvz(self):
        for x in self.zurnalas:
            if isinstance(x, PajamuIrasas):
                print(x, self.suma)
                print("cia pajamos")
            elif isinstance(x, IslaiduIrasas):
                print(x, self.suma)
                print("cia islaidos")