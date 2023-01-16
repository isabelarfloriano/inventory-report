from inventory_report.inventory.product import Product


def test_cria_produto():
    
    product = Product(
        1,
        "Produto Teste",
        "Testers S.A",
        "01/01/1001",
        "01/01/9999",
        "0123456789",
        "Mantenha fora do alcance de crianças",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Produto Teste"
    assert product.nome_da_empresa == "Testers S.A"
    assert product.data_de_fabricacao == "01/01/1001"
    assert product.data_de_validade == "01/01/9999"
    assert product.numero_de_serie == "0123456789"
    assert product.instrucoes_de_armazenamento == "Mantenha fora do alcance de crianças"
