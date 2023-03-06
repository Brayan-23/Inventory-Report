from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        return f"""{super().generate(lista)}
Produtos estocados por empresa:
{cls.name_emprises(lista)}"""

    @classmethod
    def name_emprises(cls, lista):
        total_string = ''
        tuplas_emprises = super().empresa_mais_produtos(lista)
        for obj in tuplas_emprises:
            total_string += f'- {obj[0]}: {obj[1]}\n'
        return total_string


print(CompleteReport.generate([
  {
    "id": 1,
    "nome_do_produto": "MESA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  },
  {
    "id": 2,
    "nome_do_produto": "CADEIRA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo SOL"
  },
  {
    "id": 2,
    "nome_do_produto": "FONE",
    "nome_da_empresa": "Bryant",
    "data_de_fabricacao": "2022-07-04",
    "data_de_validade": "2023-05-09",
    "numero_de_serie": "FR45",
    "instrucoes_de_armazenamento": "Conservar ao abrigo agua"
  }
]))
