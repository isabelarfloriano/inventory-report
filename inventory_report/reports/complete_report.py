from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)

        companies = [product["nome_da_empresa"] for product in list]
        company_products = Counter(companies).items()
        companies_amount = ""
        for company, amount in company_products:
            companies_amount += f"- {company}: {amount}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_amount}\n"
        )
