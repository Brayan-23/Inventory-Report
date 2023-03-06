from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "pessego",
        "Bryant",
        "29/11/2022",
        "29/11/2023",
        1234,
        "guardar em local gelado",
    )

    assert str(produto) == (
        f"O produto {produto.nome_do_produto}"
        f" fabricado em {produto.data_de_fabricacao}"
        f" por {produto.nome_da_empresa} com validade"
        f" até {produto.data_de_validade}"
        f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
    )
