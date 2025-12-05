class ServiceAcces:
   
    def entrer(self):
        print("ServiceAcces : Bienvenue ! Vous pouvez entrer dans le stade.")


class ProxyPassSanitaire:
  
    def __init__(self, service_acces, possede_pass_sanitaire):
        self._service = service_acces
        self._possede_pass = possede_pass_sanitaire

    def entrer(self):
        if self.verifier_pass_sanitaire():
            self._service.entrer()
        else:
            print("Accès refusé : Pass Sanitaire Covid-19 invalide ou absent.")

    def verifier_pass_sanitaire(self):
        print("Proxy : Vérification du Pass Sanitaire Covid-19...")
        return self._possede_pass




def client_code(subject):
    subject.entrer()




if __name__ == "__main__":
    print("Cas 1 : Visiteur SANS Pass Sanitaire")
    visiteur1 = ProxyPassSanitaire(ServiceAcces(), possede_pass_sanitaire=False)
    client_code(visiteur1)

    print("\nCas 2 : Visiteur AVEC Pass Sanitaire")
    visiteur2 = ProxyPassSanitaire(ServiceAcces(), possede_pass_sanitaire=True)
    client_code(visiteur2)
