from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "pessego",
        "Bryant",
        "29/11/2022",
        "29/11/2023",
        1234,
        "Guardar em local gelado",
    )

    assert produto.nome_da_empresa == 'Bryant'
    assert produto.id == 1
    assert produto.nome_do_produto == 'pessego'
    assert produto.data_de_fabricacao == '29/11/2022'
    assert produto.data_de_validade == '29/11/2023'
    assert produto.numero_de_serie == 1234
    assert produto.instrucoes_de_armazenamento == 'Guardar em local gelado'
