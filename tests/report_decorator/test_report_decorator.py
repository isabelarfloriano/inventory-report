from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


mock = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1"
    },
]


def test_decorar_relatorio():
    simple_colored_report = ColoredReport(SimpleReport).generate(mock)
    complete_colored_report = ColoredReport(CompleteReport).generate(mock)

    assert ("\033[36m" in simple_colored_report) is True
    assert ("\033[32m" in simple_colored_report) is True
    assert ("\033[31m" in simple_colored_report) is True
    assert ("\033[36m" in complete_colored_report) is True
    assert ("\033[32m" in complete_colored_report) is True
    assert ("\033[31m" in complete_colored_report) is True
