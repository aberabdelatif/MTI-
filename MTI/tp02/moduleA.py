from AcademicElement import AcademicElement

class Module(AcademicElement):
    """
    Represents a module that inherits from AcademicElement.
    """

    def __init__(self, name, title, coef=1, credit=1, hours_lecture=1.5, hours_tp=0, hours_td=0):
        super().__init__(name, title)
        self.coef = coef
        self.credit = credit
        self.hours_lecture = hours_lecture
        self.hours_tp = hours_tp
        self.hours_td = hours_td

    # ====== Setters ======
    def setCoef(self, coef):
        self.coef = coef

    def setCredit(self, credit):
        self.credit = credit

    # ====== Getters ======
    def getCoef(self):
        return self.coef

    def getCredit(self):
        return self.credit


class ConcreteModule(Module):
    def __init__(self, name, title, grades):
        super().__init__(name, title)
        self.grades = grades

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def calculate_credits(self):
        avg = self.calculate_average()
        # ✅ Utiliser le vrai crédit du module
        if avg >= 10:
            return self.getCredit()
        else:
            return 0
