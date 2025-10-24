# unitA.py
from AcademicElement import AcademicElement

class UnitA(AcademicElement):
    """
    Represents an academic unit (UE) that groups several modules.
    """

    def __init__(self, name, title, modules=None):
        super().__init__(name, title)
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
                total_weighted += avg * m.getCoef()
                total_coef += m.getCoef()

        return round(total_weighted / total_coef, 2) if total_coef > 0 else 0

    def calculate_credits(self):
        """
        Calculate the total credits obtained in the unit (only for passed modules).
        """
        total_credits = 0
        for m in self.modules:
            total_credits += m.calculate_credits()
        return total_credits
