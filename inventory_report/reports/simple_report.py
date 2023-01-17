# from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        oldest_manufacture = "9999-99-99"
        for product in list:
            if oldest_manufacture > product["data_de_fabricacao"]:
                oldest_manufacture = product["data_de_fabricacao"]
                # print(oldest_manufacture)

        # now = datetime.today().strftime("%y-%m-%d")
        close_to_expire = "9999-99-99"
        for product in list:
            if close_to_expire > product["data_de_validade"]:
                close_to_expire = product["data_de_validade"]
                # print(close_to_expire)

        companies = [product["nome_da_empresa"] for product in list]
        company_with_more_products, _ = Counter(companies).most_common()[0]
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {close_to_expire}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
