from AcademicElement import AcademicElement

class SemesterA(AcademicElement):
    """
    Represents a semester that contains multiple academic units (UE).
    """

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self.units = units if units is not None else []

    def add_unit(self, unit):
        """Add an academic unit (UE) to the semester."""
        self.units.append(unit)

    def calculate_credits(self):
        """Sum of all credits from all units."""
        total = 0
        for u in self.units:
            total += u.calculate_credits()
        return total

    def calculate_average(self):
        """Weighted average of all units in the semester."""
        if not self.units:
            return 0

        total_weighted = 0
        total_coef = 0
        for u in self.units:
            avg = u.calculate_average()
            if avg is not None:
                total_weighted += avg * len(u.modules)
                total_coef += len(u.modules)

        return round(total_weighted / total_coef, 2) if total_coef > 0 else 0
