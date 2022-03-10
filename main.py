from Biudzetas1 import  Biudzetas

biudzetas= Biudzetas()

while True:
    pasirinkimas = int(input("\n1 - Ivesti pajamas\n2 - Ivesti islaidas\n3 - parodyti biudžeto ataskaitą"
                             "\n4 - parodyti balansa\n5 - pasiziureti islaidas ir pajamas\n6 - iseiti is programos\n * Iveskite skaiciu: "))
    if pasirinkimas == 1:
        suma = int(input("iveskite suma: "))
        siuntejas = input("iveskite siunteja: ")
        papildoma_informacija = input("iveskite papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)

    if pasirinkimas == 2:
        suma = int(input("iveskite suma: "))
        atsiskaitymo_budas = input("atsiskaitymo budas: ")
        isigyta_preke_paslauga = input("isigyta_preke_paslauga: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
#pakeisti

    if pasirinkimas == 3:
        biudzetas.parodyti_ataskaita()

    if pasirinkimas == 4:
        biudzetas.gauti_balansą()

    if pasirinkimas == 5:
        biudzetas.biudzeto_pvz()

    if pasirinkimas == 6:
        print("Viso gero")
        break
