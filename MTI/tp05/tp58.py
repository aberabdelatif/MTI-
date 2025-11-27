
class Voiture:
    def __init__(self):
        self.pieces = []

    def ajouter(self, piece):
        self.pieces.append(piece)

    def afficher(self):
        print("Configuration de la voiture :", self.pieces)


class ConstructeurVoiture:
    def __init__(self):
        self.voiture = Voiture()

    def construire_moteur(self):
        pass

    def construire_roues(self):
        pass

    def construire_clim(self):
        pass

    def construire_gps(self):
        pass

    def construire_capteurs(self):
        pass


class ConstructeurBasique(ConstructeurVoiture):
    def construire_moteur(self):
        self.voiture.ajouter("Moteur basique")

    def construire_roues(self):
        self.voiture.ajouter("Roues standard")

    def construire_clim(self):
        pass  # pas de climatisation

    def construire_gps(self):
        pass  # pas de GPS

    def construire_capteurs(self):
        pass  # pas de capteurs


class ConstructeurComplet(ConstructeurVoiture):
    def construire_moteur(self):
        self.voiture.ajouter("Moteur V8")

    def construire_roues(self):
        self.voiture.ajouter("Roues sport")

    def construire_clim(self):
        self.voiture.ajouter("Climatisation")

    def construire_gps(self):
        self.voiture.ajouter("Système GPS")

    def construire_capteurs(self):
        self.voiture.ajouter("Capteurs de stationnement")


class ConstructeurPersonnalise(ConstructeurVoiture):
    """L'utilisateur choisit les options spécifiques"""
    def construire_moteur(self):
        self.voiture.ajouter("Moteur V6")

    def construire_roues(self):
        self.voiture.ajouter("Roues en alliage")

    def construire_clim(self):
        self.voiture.ajouter("Climatisation")

    def construire_gps(self):
        pass  # pas de GPS

    def construire_capteurs(self):
        self.voiture.ajouter("Capteurs")


class DirecteurVoiture:
    def construire(self, constructeur: ConstructeurVoiture):
        constructeur.construire_moteur()
        constructeur.construire_roues()
        constructeur.construire_clim()
        constructeur.construire_gps()
        constructeur.construire_capteurs()


def main():
    directeur = DirecteurVoiture()

   
    basique = ConstructeurBasique()
    directeur.construire(basique)
    basique.voiture.afficher()

   
    complet = ConstructeurComplet()
    directeur.construire(complet)
    complet.voiture.afficher()

    
    perso = ConstructeurPersonnalise()
    directeur.construire(perso)
    perso.voiture.afficher()


if __name__ == "__main__":
    main()
