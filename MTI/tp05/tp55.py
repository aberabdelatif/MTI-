class DBPool:
    _instances = []
    _MAX = 3

    def __new__(cls, name):
        if len(cls._instances) < cls._MAX:
            inst = super(DBPool, cls).__new__(cls)
            inst.name = name
            inst.connected = True
            cls._instances.append(inst)
            print("Nouvelle connexion:", name)
            return inst
        else:
            raise Exception("Maximum database connections reached!")

    def close(self):
        print("Connexion fermée:", self.name)
        self.connected = False
        DBPool._instances.remove(self)


def main():
   
    c1 = DBPool("DB")
    c2 = DBPool("DB")
    c3 = DBPool("DB")

    # Tentative d'une 4e connexion
    try:
        c4 = DBPool("DB")
    except Exception as e:
        print("Erreur :", e)

    # Fermeture d’une connexion
    c1.close()

    # Maintenant une connexion est libre
    c4 = DBPool("DB")
    print("c4 créée après libération.")


# Lancer le programme
if __name__ == "__main__":
    main()
