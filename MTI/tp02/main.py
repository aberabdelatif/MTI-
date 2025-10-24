# main.py
from moduleA import ConcreteModule
from unitA import UnitA
from ssemsterA import SemesterA

def main():
    print("=== GESTION DU MASTER 1 GSI - UNIVERSITÉ DE BOUIRA ===\n")

    # =============== SEMESTRE 1 ===============
    semestre1 = SemesterA("S1", "Premier Semestre - M1 GSI")

    # ----- UEF1 -----
    uef1 = UnitA("UEF1", "Unité Fondamentale 1")
    m1 = ConcreteModule("M1", "Méthodes et Technologies d’Implémentation", [14, 13, 15])
    m1.setCoef(3)
    m1.setCredit(6)
    m2 = ConcreteModule("M2", "Algorithmique avancée", [12, 13])
    m2.setCoef(2)
    m2.setCredit(4)
    uef1.add_module(m1)
    uef1.add_module(m2)

    # ----- UEF2 -----
    uef2 = UnitA("UEF2", "Unité Fondamentale 2")
    m3 = ConcreteModule("M3", "Système d’exploitation", [11, 13])
    m3.setCoef(2)
    m3.setCredit(4)
    m4 = ConcreteModule("M4", "Architecture Avancée des Systèmes Informatiques", [10, 14])
    m4.setCoef(2)
    m4.setCredit(4)
    uef2.add_module(m3)
    uef2.add_module(m4)

    # ----- UEF3 -----
    uef3 = UnitA("UEF3", "Unité Méthodologique")
    m5 = ConcreteModule("M5", "Programmation réseaux", [13, 15, 14])
    m5.setCoef(3)
    m5.setCredit(5)
    m6 = ConcreteModule("M6", "Les réseaux de la couche Physique", [12, 10])
    m6.setCoef(2)
    m6.setCredit(4)
    uef3.add_module(m5)
    uef3.add_module(m6)

    # ----- UED -----
    ued = UnitA("UED", "Unité Découverte")
    m7 = ConcreteModule("M7", "Systèmes de Communication Vocaux et Vidéos", [11, 12])
    m7.setCoef(2)
    m7.setCredit(2)
    ued.add_module(m7)

    # ----- UET -----
    uet = UnitA("UET", "Unité Transversale")
    m8 = ConcreteModule("M8", "Les technologies du Cloud Computing", [13])
    m8.setCoef(1)
    m8.setCredit(1)
    uet.add_module(m8)

    semestre1.add_unit(uef1)
    semestre1.add_unit(uef2)
    semestre1.add_unit(uef3)
    semestre1.add_unit(ued)
    semestre1.add_unit(uet)

    # =============== SEMESTRE 2 ===============
    semestre2 = SemesterA("S2", "Deuxième Semestre - M1 GSI")

    # ----- UEF1 -----
    uef1_s2 = UnitA("UEF1-S2", "Unité Fondamentale 1")
    m9 = ConcreteModule("M9", "Les Technologies du Middleware", [14, 15])
    m9.setCoef(3)
    m9.setCredit(6)
    m10 = ConcreteModule("M10", "Approches de spécification des Systèmes Informatiques", [13, 14])
    m10.setCoef(2)
    m10.setCredit(4)
    uef1_s2.add_module(m9)
    uef1_s2.add_module(m10)

    # ----- UEF2 -----
    uef2_s2 = UnitA("UEF2-S2", "Unité Fondamentale 2")
    m11 = ConcreteModule("M11", "Infographie", [15, 14])
    m11.setCoef(2)
    m11.setCredit(4)
    m12 = ConcreteModule("M12", "Gestion de Données Multimédia", [12, 13])
    m12.setCoef(2)
    m12.setCredit(4)
    uef2_s2.add_module(m11)
    uef2_s2.add_module(m12)

    # ----- UEM -----
    uem = UnitA("UEM", "Unité Méthodologique")
    m13 = ConcreteModule("M13", "Les réseaux IP", [14, 13, 15])
    m13.setCoef(3)
    m13.setCredit(6)
    m14 = ConcreteModule("M14", "Les réseaux de niveau liaison", [12, 11])
    m14.setCoef(2)
    m14.setCredit(3)
    m15 = ConcreteModule("M15", "Programmation pour le Big Data", [13, 14])
    m15.setCoef(2)
    m15.setCredit(2)
    uem.add_module(m13)
    uem.add_module(m14)
    uem.add_module(m15)

    # ----- UED -----
    ued_s2 = UnitA("UED-S2", "Unité Découverte")
    m16 = ConcreteModule("M16", "Sécurité des Systèmes Informatiques et de Communications", [15])
    m16.setCoef(1)
    m16.setCredit(1)
    ued_s2.add_module(m16)

    # ----- UET -----
    uet_s2 = UnitA("UET-S2", "Unité Transversale")
    m17 = ConcreteModule("M17", "Projet Professionnel", [14])
    m17.setCoef(1)
    m17.setCredit(1)
    uet_s2.add_module(m17)

    semestre2.add_unit(uef1_s2)
    semestre2.add_unit(uef2_s2)
    semestre2.add_unit(uem)
    semestre2.add_unit(ued_s2)
    semestre2.add_unit(uet_s2)

    # =================== AFFICHAGE ===================
    for semestre in [semestre1, semestre2]:
        print(f"\n=== {semestre.title} ===")
        print(f"Moyenne générale : {semestre.calculate_average()}")
        print(f"Crédits obtenus : {semestre.calculate_credits()}\n")
        for unit in semestre.units:
            print(f"--- {unit.title} ---")
            print(f"Moyenne de l’unité : {unit.calculate_average()}")
            print(f"Crédits obtenus : {unit.calculate_credits()}")
            print("Modules :")
            for mod in unit.modules:
                print(f"  - {mod.title}: Moyenne = {mod.calculate_average():.2f}, Crédit = {mod.calculate_credits()}")
            print("")

if __name__ == "__main__":
    main()
