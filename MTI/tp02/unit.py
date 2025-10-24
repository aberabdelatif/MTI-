
from Module import Module  

class Unit:
    """
    Represents an academic unit that groups several modules.
    """

    def __init__(self, name, title, modules=None):
        self.name = name
        self.title = title
        self.modules = modules if modules is not None else []

    def add_module(self, module):
        """Add a module to the unit."""
        self.modules.append(module)

    def calculate_average(self):
        """
        Calculate the weighted average of all modules in the unit
        using their coefficients.
        """
        if not self.modules:
            return 0

        total_weighted = 0
        total_coef = 0

        for m in self.modules:
            avg = m.calculate_average()
            if avg is not None:
                total_weighted += avg * m.coef
                total_coef += m.coef

        return round(total_weighted / total_coef, 2) if total_coef > 0 else 0

    def calculate_credits(self):
        """
        Calculate the total number of credits obtained (only for passed modules).
        """
        total_credits = 0
        for m in self.modules:
            avg = m.calculate_average()
            if avg is not None and avg >= 10:
                total_credits += m.credit
        return total_credits


# ---------- Classe Module (si tu n’as pas encore module.py) ----------
class Module:
    """
    Represents a module with grades, coefficient, and credit.
    """
    def __init__(self, name, coef, credit, grades):
        self.name = name
        self.coef = coef
        self.credit = credit
        self.grades = grades  # list of grades (exam, tp, etc.)

    def calculate_average(self):
        """Calculate the simple average of grades."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)


# ---------- Fonction principale (main) ----------
def main():
    print("=== Test du système d’unités ===\n")

    # Création de quelques modules
    m1 = Module("Sécurité", coef=3, credit=6, grades=[12, 14, 13])
    m2 = Module("Réseaux", coef=2, credit=4, grades=[9, 11])
    m3 = Module("Base de données", coef=2, credit=5, grades=[15, 16])

    # Création d'une unité et ajout des modules
    unit = Unit("UEF1", "Sécurité Informatique")
    unit.add_module(m1)
    unit.add_module(m2)
    unit.add_module(m3)

    # Calculs
    avg = unit.calculate_average()
    credits = unit.calculate_credits()

    # Affichage des résultats
    print(f"--- Résultats de l'unité {unit.title} ---")
    print(f"Moyenne de l'unité : {avg}")
    print(f"Crédits obtenus : {credits}")
    print("\nDétails des modules :")
    for m in unit.modules:
        print(f" - {m.name}: Moyenne {m.calculate_average():.2f}, Coef {m.coef}, Crédit {m.credit}")


# ---------- Point d’entrée du programme ----------
if __name__ == "__main__":
    main()
