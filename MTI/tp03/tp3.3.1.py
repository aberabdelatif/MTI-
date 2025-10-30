
class AfficherPourResearcher:
    def print_information(self, info):
        pass

class AfficherPourTeacher:
    def print_information(self, info):
        pass

class AfficherPourHospital:
    def print_information(self, info):
        pass



class ProfessorResearcher(AfficherPourResearcher, AfficherPourTeacher):
    def print_information(self, info):
        print(f"[ProfessorResearcher] {info}")



class FullTimeResearcher(AfficherPourResearcher):
    def print_information(self, info):
        print(f"[FullTimeResearcher] {info}")



class ProfessorHospitalResearcher(AfficherPourResearcher, AfficherPourTeacher, AfficherPourHospital):
    def print_information(self, info):
        print(f"[ProfessorHospitalResearcher] {info}")


if __name__ == "__main__":
    prof_researcher = ProfessorResearcher()
    prof_researcher.print_information("Teaches and conducts research")

    full_researcher = FullTimeResearcher()
    full_researcher.print_information("Conducts research only")

    hospital_prof = ProfessorHospitalResearcher()
    hospital_prof.print_information("Teaches, conducts research, and practices medicine")
