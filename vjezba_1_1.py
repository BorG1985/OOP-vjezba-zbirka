# Zadatak 1.1 Napraviti praznu klasu Serija I I instancirati jedan objekat.

class Serija:
    def __init__(self,naziv):
        self.naziv=naziv

    def show(self):
        print(f"naziv serije je: {self.naziv}")

dead=Serija("Dead like me")
dead.show()
