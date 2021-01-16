# Zadatak 1.6  Napisati klasu Automobil koja kreira podatke o automobilu.
# Informacije o automobilu su naziv proizvođača, modela I maksimalna brzina kojom se automobil kreće.
# Klasa treba sadržati metod ispis koji će odštampati podatke kao I metode koje služe za upis podataka.
# Instancirati jedan objekat.

class Automobil:
    proizvodjac="Nije unijet"
    model="Nije unijet"
    max_brzina=0

    def postavi_proizvodjaca(self,x):
        self.proizvodjac=x

    def postavi_model(self,x):
        self.model=x

    def postavi_max_brzina(self,x):
        self.max_brzina=x

    def ispis(self):
        print("Proizvodjač: ",self.proizvodjac, "\nModel: ", self.model,"\nMaximalna brzina: ",self.max_brzina)
    
auto1=Automobil()
auto1.postavi_proizvodjaca("BMW")
auto1.postavi_model("E90")
auto1.postavi_max_brzina(220)
auto1.ispis()
