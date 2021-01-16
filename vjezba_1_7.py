# Zadatak 1.7 Napraviti klasu Racun koja ima metode za uplatu, isplatu novca i proveru stanja rаčuna korisnika.
# Klasa treba da sadrži konstruktor koji definiše stanje računa na 0. 
# Otvoriti račun.
# Uplatiti 500e I ispisati stanje računa, isplatiti 250e, proveriti stanje računa.
# Ako ima para skinuti 350e, ispisati stanje računa.

class Racun:
    def __init__(self):
        self.stanje=0

    def uplata(self,amount):
        self.stanje=self.stanje + amount
        

    def isplata(self,amount):
        if(self.stanje<amount):
            print("Nema dovoljno novca na racunu")
        else:
            self.stanje=self.stanje-amount
       
    def stanjeRacuna(self):
        print(f"Stanje racuna je {self.stanje}")

racun= Racun()
racun.uplata(500)
racun.stanjeRacuna()
racun.isplata(250)
racun.stanjeRacuna()
racun.isplata(350)
racun.stanjeRacuna()


