
class Student:
    def __init__(self, moyenne, credits, unites_valides):
        self.moyenne = moyenne
        self.credits = credits
        self.unites_valides = unites_valides



class TransitionStrategy:
    def verify(self, student: Student):
        pass



class L2toL3Strategy(TransitionStrategy):
    def verify(self, student: Student):
        if (student.moyenne >= 10 
            and student.credits >= 45 
            and "UE_fondamentale" in student.unites_valides):
            return "Passage accepté : L2 → L3"
        
        return "Refusé : Conditions insuffisantes pour passer de L2 à L3."



class L3toM1Strategy(TransitionStrategy):
    def verify(self, student: Student):
        if (student.moyenne >= 12 
            and student.credits >= 180 
            and "PFE" in student.unites_valides):
            return "Passage accepté : L3 → M1"
        
        return "Refusé : Conditions insuffisantes pour entrer en M1."



class M1toM2Strategy(TransitionStrategy):
    def verify(self, student: Student):
        if (student.moyenne >= 10 and student.credits >= 240):
            return "Passage accepté : M1 → M2"
        
        return "Refusé : Conditions insuffisantes pour entrer en M2."



class TransitionContext:
    def __init__(self, strategy: TransitionStrategy):
        self.strategy = strategy
    
    def check_transition(self, student: Student):
        return self.strategy.verify(student)



def main():
    
    etudiant = Student(
        moyenne=12.5, 
        credits=185, 
        unites_valides=["PFE", "UE_fondamentale"]
    )

    print("=== Vérification du passage L3 → M1 ===")
    strategy = L3toM1Strategy()
    context = TransitionContext(strategy)
    print(context.check_transition(etudiant))

    print("\n=== Vérification du passage L2 → L3 ===")
    strategy2 = L2toL3Strategy()
    context2 = TransitionContext(strategy2)
    print(context2.check_transition(etudiant))

    print("\n=== Vérification du passage M1 → M2 ===")
    strategy3 = M1toM2Strategy()
    context3 = TransitionContext(strategy3)
    print(context3.check_transition(etudiant))


if __name__ == "__main__":
    main()
