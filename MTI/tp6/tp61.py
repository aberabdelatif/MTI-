class DepartmentSite:
    def display_info(self):
        print("Affichage: Informations du site du département")

class InfoLearningPlatform:
    def display_info(self):
        print("Affichage: Cours et TD depuis Info-Learning")

class UniversityELearning:
    def display_info(self):
        print("Affichage: Cours, Examens, Devoirs de la plateforme E-learning")

class FacebookPages:
    def display_info(self):
        print("Affichage: Annonces Facebook (Université, Faculté, Département)")

class StudentGroups:
    def display_info(self):
        print("Affichage: Groupes étudiants (Documents, Résumés, Discussions)")

class StudentInfoFacade:
    def __init__(self):
        self.dep = DepartmentSite()
        self.info_learn = InfoLearningPlatform()
        self.elearning = UniversityELearning()
        self.facebook = FacebookPages()
        self.groups = StudentGroups()

    def display_all_sources(self):
        print("\n--- Tous les sources en un seul endroit ---")
        self.dep.display_info()
        self.info_learn.display_info()
        self.elearning.display_info()
        self.facebook.display_info()
        self.groups.display_info()


def main():
    facade = StudentInfoFacade()
    facade.display_all_sources()

if __name__ == "__main__":
    main()
