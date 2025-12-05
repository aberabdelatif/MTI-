
class DepartementSite:
    
    def __init__(self):
        self._observers = set()
        self._latest_post = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._latest_post)

    def publier_post(self, post):
        """نشر خبر أو مقال جديد"""
        self._latest_post = post
        print(f"\n[Site] Nouveau post publié : {post}")
        self._notify()



class EtudiantObserver:
    def __init__(self, nom):
        self._subject = None
        self.nom = nom
        self.notifications = []

    def update(self, post):
        self.notifications.append(post)
        print(f"[Notification] {self.nom} a reçu : {post}")

    def afficher_notifications(self):
        print(f"\n=== Notifications pour {self.nom} ===")
        for n in self.notifications:
            print(f"- {n}")


# ------ MAIN ------
def main():
    # إنشاء الموقع الرسمي للقسم
    site = DepartementSite()

    # إنشاء الطلاب
    ahmed = EtudiantObserver("Ahmed")
    salem = EtudiantObserver("Salem")
    leila = EtudiantObserver("Leila")

    
    site.attach(ahmed)
    site.attach(salem)

    
    site.publier_post("Publication des résultats du semestre 1")

    
    site.attach(leila)

    
    site.publier_post("Annonce du concours de projet final")

    
    site.detach(salem)

   
    site.publier_post("Mise à jour du planning des TD")

   
    ahmed.afficher_notifications()
    salem.afficher_notifications()
    leila.afficher_notifications()


if __name__ == "__main__":
    main()
