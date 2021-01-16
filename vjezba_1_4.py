#Zadatak 1.4 Napraviti klasu Brojevi, koja sadrži 2 polja koja polja koja predstavljaju  cele brojeve.
# Koristiti konstruktor klase. Napraviti metode sabiranje, oduzimanje, množenje I deljenje(celobrojno)
# koje vraćaju rezultat svake od operacija. Instancirati jedan objekat I pozvati metode nad njim. Iskoristiti 

class Brojevi:
    def __init__(self,broj1,broj2):
        self.broj1=broj1
        self.broj2=broj2
    
    def add(self):
        a = self.broj1 + self.broj2
        return a
        print(a)

    def sub(self):
        a = self.broj1 - self.broj2
        return a
        print(a)

    def mul(self):
        a = self.broj1 * self.broj2
        return a
        print(a)

    def div(self):
        a = self.broj1 / self.broj2
        return a
        print(a)

a1=Brojevi(10,5)
print("Zbir je:" , a1.add())
print("Razlika je:" , a1.sub())
print("Umnožak je:" , a1.mul())
print("količnik je:" , a1.div())
