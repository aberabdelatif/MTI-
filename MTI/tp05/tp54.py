class FileWriter:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super(FileWriter, cls).__new__(cls)
            cls._instance.file = open(filename, "w")
            print("Ouverture du fichier :", filename)
        return cls._instance

    def write(self, text):
        self.file.write(text + "\n")

    def close(self):
        print("Fermeture du fichier.")
        self.file.close()
        FileWriter._instance = None

def main():
    print("=== Test du FileWriter Singleton ===")

    f1 = FileWriter("output.txt")
    f2 = FileWriter("output.txt")

    
    assert f1 is f2
    print("f1 et f2 sont la même instance.")

    # Écriture dans le fichier
    f1.write("Hello")
    f2.write("World")

    # Fermeture
    f1.close()
    print("Programme terminé.")


if __name__ == "__main__":
    main()
