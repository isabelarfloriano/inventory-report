from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


import csv


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as csv_file:
            file = csv.DictReader(csv_file)
            products_file = [line for line in file]

            if report_type == "simples":
                return SimpleReport.generate(products_file)
            elif report_type == "completo":
                return CompleteReport.generate(products_file)
