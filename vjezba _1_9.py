# Zadatak 1.9 Napraviti klasu Stan koja treba da sadrži konstruktor koji unosi podatke koji
# predstavljaju broj stana I sifru alarma. Napraviti metod ispisi_broj_stana koji ispisuje
#  koji je broj stana I napraviti privatnu metodu ispisi_sifru_alarma koja ispisuje šifru alarma.
# Instancirati objekat I pozvati obe metode na objektom.

class Stan:
    def __init__(self,broj_stana,sifra_alarma):
        self.broj_stana=broj_stana
        self.sifra_alarma=sifra_alarma

    def brojStana(self):
        print("Broj stana je:",self.broj_stana)

    def __ispisi_sifru_alarma(self):
        print("Sifra alarma je : ",self.sifra_alarma)

    def __sifraAlarma(self):
        print("Sifra alarma je:",self.sifra_alarma)

stan=Stan(22,3625)
stan.brojStana()
stan.sifraAlarma()
