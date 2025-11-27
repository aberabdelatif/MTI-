from abc import ABC, abstractmethod

# Classe abstraite
class Compte(ABC):
    @abstractmethod
    def stock(self):
        pass
    
    @abstractmethod
    def achat(self):
        pass
    
    @abstractmethod
    def commande(self):
        pass

# Visiteur
class Visiteur(Compte):
    def stock(self):
        print("Les produits disponibles pour le visiteur")

    def achat(self):
        print("Créer un compte pour pouvoir acheter")

    def commande(self):
        print("Le visiteur n'a pas de commandes")

# Vendeur
class Vendeur(Compte):
    def stock(self):
        print("Votre stock (vendeur) est affiché")

    def achat(self):
        print("Le vendeur ne peut pas acheter, seulement vendre")

    def commande(self):
        print("Les commandes reçues par le vendeur")

# Gestionnaire
class Gestionnaire(Compte):
    def stock(self):
        print("Gestionnaire : consultation globale du stock")

    def achat(self):
        print("Gestionnaire : aucune fonction d'achat")

    def commande(self):
        print("Gestionnaire : gestion de toutes les commandes")

# Factory simple
class CompteFactory:
    def create_compte(self, type_compte):
        compte = type_compte()
        compte.stock()
        compte.achat()
        compte.commande()

# Factory avec string
class CreateCompteFactory(CompteFactory):
    def create(self, literal_type):
        literal_type = literal_type.lower()

        if literal_type == "visiteur":
            return Visiteur()
        elif literal_type == "vendeur":
            return Vendeur()
        elif literal_type == "gestionnaire":
            return Gestionnaire()
        else:
            print("Type inconnu !")
            return None


def main():
    factory = CreateCompteFactory()

    print("=== Choisissez un type de compte ===")
    print("1 - Visiteur")
    print("2 - Vendeur")
    print("3 - Gestionnaire")

    choix = input("Votre choix : ")

    if choix == "1":
        compte = factory.create("visiteur")
    elif choix == "2":
        compte = factory.create("vendeur")
    elif choix == "3":
        compte = factory.create("gestionnaire")
    else:
        print("Choix invalide !")
        return

    print("\n=== Résultat ===")
    compte.stock()
    compte.achat()
    compte.commande()

# Lancement du programme
if __name__ == "__main__":
    main()
