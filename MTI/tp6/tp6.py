class Person:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
class personne:
    def __init__ (self, nomcomplet):
        self.nom = nomcomplet
class adapter(personne):
    def __init__(self, person):
        self.nom = person.nom +"-"+ person.prenom
def main():
# personne
    personOne = Person("Akli", "Mohand")
    per = adapter(personOne)
    print(per.nom)
    return 0
if __name__ == '__main__':
    main()
