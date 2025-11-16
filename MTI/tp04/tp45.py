import json
import os

class model:
    def __init__(self):
        self.filename = "directory.json"
        self.directory = self.load_data()

    def load_data(self):
        """Load data from JSON file, or create default data if not found"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        else:
            # Default initial data
            data = [
                {"firstname": "Ahmed", "familyname": "Mahdi", "tel": "0778787887"},
                {"firstname": "Mohamed", "familyname": "Mahdi", "tel": "0778787887"},
                {"firstname": "Mounir", "familyname": "Katibi", "tel": "0778787887"},
                {"firstname": "Noui", "familyname": "Brahimi", "tel": "0778787887"},
            ]
            self.save_data(data)
            return data

    def save_data(self, data=None):
        """Save current directory to JSON file"""
        if data is None:
            data = self.directory
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def search(self, nom):
        persons = []
        for persn in self.directory:
            if persn["familyname"].lower() == nom.lower():
                persons.append(persn)
        return persons

    def add(self, name, firstname, tel):
        person = {"familyname": name, "firstname": firstname, "tel": tel}
        self.directory.append(person)
        self.save_data()  # Save immediately when adding


class view:
    def input(self):
        print("\nFinding a phone")
        return input("Give a family name: ")

    def output(self, persons):
        print("\nList of found names:")
        print(f"{len(persons)} found people")
        for pers in persons:
            print(pers["familyname"], pers["firstname"], pers["tel"])

    def input_add(self):
        print("\nAdd a person")
        name = input("Give a family name: ")
        firstname = input("Give a firstname: ")
        tel = input("Give a phone number: ")
        return name, firstname, tel


class controller:
    def __init__(self):
        self.data_model = model()
        self.viewer = view()

    def search(self):
        name = self.viewer.input()
        persons = self.data_model.search(name)
        self.viewer.output(persons)

    def add(self):
        name, firstname, tel = self.viewer.input_add()
        self.data_model.add(name, firstname, tel)
        print("\n✅ Person added successfully!")
        persons = self.data_model.directory
        self.viewer.output(persons)


if __name__ == '__main__':
    contro = controller()

    while True:
        print("\n--- Phone Directory Menu ---")
        print("1. Search for a person")
        print("2. Add a new person")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            contro.search()
        elif choice == '2':
            contro.add()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
