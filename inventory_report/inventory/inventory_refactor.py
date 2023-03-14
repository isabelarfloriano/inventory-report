from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        products_file = self.importer.import_data(path)
        self.data += products_file

        return InventoryRefactor.generate_report_by_type(
            report_type, products_file)

    @staticmethod
    def generate_report_by_type(report_type, products_file):
        if report_type == "simples":
            return SimpleReport.generate(products_file)
        elif report_type == "completo":
            return CompleteReport.generate(products_file)

    def __iter__(self):
        return InventoryIterator(self.data)
