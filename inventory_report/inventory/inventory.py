from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as csv_file:
                file = csv.DictReader(csv_file)
                products_file = [line for line in file]

        if path.endswith(".json"):
            with open(path, encoding="utf-8") as json_file:
                products_file = json.load(json_file)

        if path.endswith(".xml"):
            with open(path) as xml_file:
                file = xmltodict.parse(xml_file.read())
                products_file = file["dataset"]["record"]

        if report_type == "simples":
            return SimpleReport.generate(products_file)
        elif report_type == "completo":
            return CompleteReport.generate(products_file)
