from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.simples = SimpleReport
        self.completo = CompleteReport
        self.importer = importer
        self.data = []

    def import_data(self, file, type):
        self.data.extend(self.importer.import_data(file))
        if type == "simples":
            return self.simples.generate(self.data)
        elif type == "completo":
            return self.completo.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
