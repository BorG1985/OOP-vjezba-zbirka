# Zadatak 1.2 Napraviti klasu Firma koja sadrži 5 polja, ime (string), vrstu poslovanja (string), adresu (string), grad (string),
# kontakt telefon (string). Neka polja predstavljaju prazne stringove.
# Instancirati jedan objekat I ispisati ime tog objekta. 

class Firma:
    def __init__(self,ime,vrsta_poslovanja,adresa,grad,kontakt_telefon):
        self.ime=ime
        self.vrsta_poslovanja=vrsta_poslovanja
        self.adresa=adresa
        self.grad=grad
        self.kontakt_telefon=kontakt_telefon

    def show(self):
        print(f"Firma : {self.ime}", f"\nPoslovanje: {self.vrsta_poslovanja}", f"\nGrad: {self.grad}", f"\nTelefon: {self.kontakt_telefon}")

subjekt=Firma("Hifa","Nafta","Krndija","Tešanj","032 655 422")
subjekt.show()