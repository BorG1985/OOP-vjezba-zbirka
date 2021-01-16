# Zadatak 1.5
# Napraviti klasu Zivotinja koja kao podatak sadrži ime I metodu stampaj_ime, koji štampa podatak ime.
# Napravitu klasu Pas I Macka koje nasleđuju klasu Zivotinja.
# Klase Pas I Macka sadrže matode Oglasavam_se koja ispisuje oglašavanje te životinje.
# Instancirati 2 objekta, psa I mačku.

class Zivotinja:
    def __init__(self,ime):
        self.ime=ime
    
    def stampaj_ime(self):
        print(f"ime zivotinje: {self.ime}")

class Pas(Zivotinja):
    def oglasavam_se(self,sound):
        self.sound=sound
        print(f"ja sam, {self.ime} , oglašavam se sa : {self.sound}")

class Macka(Zivotinja):
    def oglasavam_se(self,sound):
        self.sound=sound
        print(f"ja sam, {self.ime} , oglašavam se sa : {self.sound}")

pas1=Pas("Cuko")
pas1.stampaj_ime()
pas1.oglasavam_se("vau vau")

maca=Macka("Mačak")
maca.stampaj_ime()
maca.oglasavam_se("mjau mjau")
