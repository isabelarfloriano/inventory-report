from inventory_report.inventory.product import Product


def test_relatorio_produto():

    product = Product(
        1,
        "Produto Teste",
        "Testers S.A",
        "01/01/1001",
        "01/01/9999",
        "0123456789",
        "Mantenha fora do alcance de crianças",
    )

    assert Product.__repr__(product) == str(
        "O produto Produto Teste fabricado em 01/01/1001 "
        "por Testers S.A com validade até 01/01/9999 "
        "precisa ser armazenado Mantenha fora do alcance de crianças."
    )
