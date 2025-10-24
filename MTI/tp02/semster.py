class semster:
    def __init__(self,name,title,model=[]):
        self.name= name
        self.title= title
        self.model=model

    def add_model(self, model):
        """Add a module to the unit."""
        self.models.append(model)    

    def calculate_average(self):
        """
        Calculate the weighted average of all modules in the unit
        using their coefficients.
        """
        if not self.models:
            return 0

        total_weighted = 0
        total_coef = 0

        for m in self.models:
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
        for m in self.models:
            avg = m.calculate_average()
            if avg is not None and avg >= 10:
                total_credits += m.credit
        return total_credits
