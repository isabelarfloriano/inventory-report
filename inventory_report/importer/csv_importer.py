from inventory_report.importer.importer import Importer


import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as csv_file:
                file = csv.DictReader(csv_file)
                products_file = [line for line in file]
                return products_file
        raise ValueError("Arquivo inválido")
