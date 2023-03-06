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

