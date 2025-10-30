class Printable:
    def print_document(self, document):
        pass
class Scannable:
    def scan_document(self, document):
        pass
class Faxable:
    def fax_document(self, document):
        pass
class BasicPrinter(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")

class AdvancedPrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"Printing: {document}")
    def scan_document(self, document):
        print(f"Scanning: {document}")
    def fax_document(self, document):
        print(f"Faxing: {document}")

if __name__ == '__main__':
    prnters = AdvancedPrinter()
    prnters.print_document(["ddd","ddd"])
    prnters.scan_document("poo.tx")
    prnters.fax_document("eddv")