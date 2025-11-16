class model:

    def __init__(self):
        self.directory = [
            {"firstname": 'Ahmed', "familyname": 'Mahdi', 'tel': '0778787887'},
            {"firstname": 'Mohamed', "familyname": 'Mahdi', 'tel': '0778787887'},
            {"firstname": 'Mounir', "familyname": 'Katibi', 'tel': '0778787887'},
            {"firstname": 'Noui', "familyname": 'Brahimi', 'tel': '0778787887'},
        ]

    def search(self, nom):
        persons = []
        for persn in self.directory:
            if persn["familyname"].lower() == nom.lower():  
                persons.append(persn)
        return persons  

    def get_all(self):
        return self.directory  

class view:
    def __init__(self):
        pass

    def input(self):
        print("Finding a phone")
        name = input("Give a family name: ")
        return name

    def output(self, persons):
        print("List of found names")
        print(" %d found people " % len(persons))
        for pers in persons:
            print(pers["familyname"], pers["firstname"], pers['tel'])


def controller():
    data_model = model()
    myviewer = view()

    name = myviewer.input()         
    persons = data_model.search(name) 
    myviewer.output(persons)     


if __name__ == '__main__':
    controller()
