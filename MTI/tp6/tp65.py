
class CreditStrategy:
    def calculer_credit(self, montant, duree):
        pass



class CreditAvecInteret(CreditStrategy):
    def __init__(self, taux_interet):
        self.taux = taux_interet  # exemple : 0.05 = 5%

    def calculer_credit(self, montant, duree):
        """
        Formule simple :
        montant_final = montant + (montant * taux * durée)
        """
        montant_total = montant + (montant * self.taux * duree)
        return f"Crédit avec intérêt : montant final = {montant_total:.2f} DA"


# ------ Concrete Strategy : Crédit sans intérêt ------
class CreditSansInteret(CreditStrategy):
    def calculer_credit(self, montant, duree):
        return f"Crédit sans intérêt : montant final = {montant:.2f} DA"



class Banque:
    def __init__(self, strategy: CreditStrategy):
        self.strategy = strategy

    def traiter_credit(self, montant, duree):
        return self.strategy.calculer_credit(montant, duree)



def main():
    montant = 100000  # 100k DA
    duree = 3  # 3 ans

    print("=== Crédit avec intérêt ===")
    strategy1 = CreditAvecInteret(taux_interet=0.04)  # 4% d'intérêt
    banque1 = Banque(strategy1)
    print(banque1.traiter_credit(montant, duree))

    print("\n=== Crédit sans intérêt ===")
    strategy2 = CreditSansInteret()
    banque2 = Banque(strategy2)
    print(banque2.traiter_credit(montant, duree))


if __name__ == "__main__":
    main()
